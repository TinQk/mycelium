

import numpy as np
import scipy.linalg as lng
import matplotlib.pyplot as plt
import numpy.random as rd
import time
from scipy.integrate import odeint, quad, simps
import scipy.optimize as opt
import matplotlib.animation as animation

from numba import njit, jit

# Mesh ploting :
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



start_time = time.time()

n = 100
t = 5000

structure = - np.ones((n,n))
structure[1:-1,1:-1] = np.zeros((n-2,n-2))
# structure[10:15,10:15] = -np.ones((5,5))
#
# for k in range(15):
#     nb1 = rd.randint(n-15)
#     nb2 = rd.randint(n)
#     nb3 = rd.randint(n)
#     nb4 = rd.randint(n-15)
#     structure[nb1:nb1+15,nb2:nb2+1] = -np.ones((15,1))
#     structure[nb3:nb3+1,nb4:nb4+15] = -np.ones((1,15))


Universe = np.zeros((t,n,n))

def init_structure(t, n, structure):
    Universe = np.zeros((t,n,n))
    for k in range(t):
        Universe[k,:,:] = structure
    return Universe

Universe = init_structure(t, n, structure)

origin = structure.copy()


Cells = []

for i in range(n) :
    for j in range(n) :
        if structure[i,j] != -1 :
            nb = rd.rand()
            if nb < 0.05 :
                origin[i,j] = 1
                Cells.append([1,(i,j),5,1,1,1])
            elif 0.99 < nb :
                origin[i,j] = 3
                Cells.append([3,(i,j),300,1,1,1])
            elif  0.05 < nb < 0.06 :
                Cells.append([2,(i,j),5,1,1,1])

origin[2,2] = 3
Cells.append([3,(2,2),300,1,1,1])

Universe[0,:,:] = origin

# print(Cells)

def reproduce(k, cell):
    type = cell[0]
    i, j = cell[1]
    nb = rd.randint(4)
    if np.sum(np.abs(Universe[k,i-1:i+2,j-1:j+2])) == 1 and np.sum(np.abs(Universe[k+1,i-1:i+2,j-1:j+2])) == 1 :
        if nb == 0:
            Universe[k+1,i+1,j] = type
            Cells.append( [type, (i+1,j), 5, 1, 1, 1] )
            # print("0")
        elif nb == 1 :
            Universe[k+1,i-1,j] = type
            Cells.append( [type, (i-1,j), 5, 1, 1, 1] )
            # print("1")
        elif nb == 2 :
            Universe[k+1,i,j+1] = type
            Cells.append( [type, (i,j+1), 5, 1, 1, 1] )
            # print("2")
        elif nb == 3 :
            Universe[k+1,i,j-1] = type
            Cells.append( [type, (i,j-1), 5, 1, 1, 1] )
            # print("3")
    return None

def type_1(k, cell) :
    i, j = cell[1]
    nb = rd.randint(4)
    # print("k=",k,"et i=",i,"et j=",j, "et nb=",nb)
    if nb == 0 and Universe[k+1,i+1,j] == 0 and Universe[k,i+1,j] == 0:
        Universe[k+1,i+1,j] = 1
        cell[1] = (i+1,j)
        # print("0")
    elif nb == 1 and Universe[k+1,i-1,j] == 0 and Universe[k,i-1,j]== 0 :
        Universe[k+1,i-1,j] = 1
        cell[1] = (i-1,j)
        # print("1")
    elif nb == 2 and Universe[k+1,i,j+1] == 0 and Universe[k,i,j+1]== 0 :
        Universe[k+1,i,j+1] = 1
        cell[1] = (i,j+1)
        # print("2")
    elif nb == 3 and Universe[k+1,i,j-1] == 0 and Universe[k,i,j-1] == 0 :
        Universe[k+1,i,j-1] = 1
        cell[1] = (i,j-1)
        # print("3")
    else :
        Universe[k+1,i,j] = 1
        cell[1] = (i,j)
        # print("4")
    return cell


def type_2_move(k, cell) :
    i, j = cell[1]
    nb = rd.randint(4)
    # print("k=",k,"et i=",i,"et j=",j, "et nb=",nb)
    if nb == 0 and Universe[k+1,i+1,j] == 0 and Universe[k,i+1,j] == 0:
        Universe[k+1,i+1,j] = 2
        cell[1] = (i+1,j)
        # print("0")
    elif nb == 1 and Universe[k+1,i-1,j] == 0 and Universe[k,i-1,j]== 0 :
        Universe[k+1,i-1,j] = 2
        cell[1] = (i-1,j)
        # print("1")
    elif nb == 2 and Universe[k+1,i,j+1] == 0 and Universe[k,i,j+1]== 0 :
        Universe[k+1,i,j+1] = 2
        cell[1] = (i,j+1)
        # print("2")
    elif nb == 3 and Universe[k+1,i,j-1] == 0 and Universe[k,i,j-1] == 0 :
        Universe[k+1,i,j-1] = 2
        cell[1] = (i,j-1)
        # print("3")
    else :
        Universe[k+1,i,j] = 2
        cell[1] = (i,j)
        # print("4")
    return cell

def type_2_eat(k,cell,kill_list) :
    i, j = cell[1]
    nb = rd.randint(4)
    # print("k=",k,"et i=",i,"et j=",j, "et nb=",nb)
    if nb == 0 and Universe[k+1,i+1,j] == 1 :
        Universe[k+1,i+1,j] = 0
        cell[2] += 5
        kill_list.append((i+1,j))
        # print("0")
    elif nb == 1 and Universe[k+1,i-1,j] == 1 :
        Universe[k+1,i-1,j] = 0
        cell[2] += 5
        kill_list.append((i-1,j))
        # print("1")
    elif nb == 2 and Universe[k+1,i,j+1] == 1 :
        Universe[k+1,i,j+1] = 0
        cell[2] += 5
        kill_list.append((i,j+1))
        # print("2")
    elif nb == 3 and Universe[k+1,i,j-1] == 1 :
        Universe[k+1,i,j-1] = 0
        cell[2] += 5
        kill_list.append((i,j-1))
        # print("3")
    Universe[k+1,i,j] = 2
    # cell[2] -= 1
        # print("4")
    # if len(kill_list)!=0:
        # print("kill kill kill",kill_list)
    return cell, kill_list


def type_3(k, cell, kill_list) :
    i, j = cell[1]
    nb = rd.randint(4)
    # print("k=",k,"et i=",i,"et j=",j, "et nb=",nb)
    if nb == 0 and Universe[k+1,i+1,j] == 1 :
        Universe[k+1,i+1,j] = 3
        Cells.append([3,(i+1,j),300,1,1,1])
        cell[2] += 100
        kill_list.append((i+1,j))
        # print("0")
    elif nb == 1 and Universe[k+1,i-1,j] == 1 :
        Universe[k+1,i-1,j] = 3
        Cells.append([3,(i-1,j),300,1,1,1])
        cell[2] += 100
        kill_list.append((i-1,j))
        # print("1")
    elif nb == 2 and Universe[k+1,i,j+1] == 1 :
        Universe[k+1,i,j+1] = 3
        Cells.append([3,(i,j+1),300,1,1,1])
        cell[2] += 100
        kill_list.append((i,j+1))
        # print("2")
    elif nb == 3 and Universe[k+1,i,j-1] == 1 :
        Universe[k+1,i,j-1] = 3
        Cells.append([3,(i,j-1),300,1,1,1])
        cell[2] += 100
        kill_list.append((i,j-1))
        # print("3")
    Universe[k+1,i,j] = 3
    cell[2] -= 1
        # print("4")
    # if len(kill_list)!=0:
        # print("kill kill kill",kill_list)
    return cell, kill_list


def faucheuse(kill_list, Cells) :
    for cell in Cells :
        if (cell[1] in kill_list and cell[0] == 1) or cell[2] <= 0 :
            Cells.remove(cell)


def evolution_time(Universe) :
    for k in range(t-1) :
        if k%100 == 0:
            print("k =",k)
        # print("Cells at beginning of step",k," :")
        # print(Cells)
        kill_list = []
        for cell in Cells:
            if cell[0] == 1 :
                cell = type_1(k, cell)
                if rd.randint(5) == 4:
                    cell[2] += 1
            elif cell[0] == 2 :
                cell = type_2_move(k, cell)
                cell, kill_list = type_2_eat(k, cell, kill_list)
            elif cell[0] == 3 :
                cell, kill_list = type_3(k, cell, kill_list)
        # print("Cell_size before", len(Cells))
        # print("kill list length", len(kill_list))
        faucheuse(kill_list, Cells)
        for cell in Cells :
            if cell[0] ==1 and cell[2] >= 10 :
                    cell[2] -= 5
                    reproduce(k, cell)
        # print("Cell_size after", len(Cells))
    return Universe

Universe = evolution_time(Universe)

# def the_whole_story(Universe) :

if __name__ == "__main__" :

    fig = plt.figure()

    im = plt.imshow(Universe[0])
    im.set_cmap("turbo")
    #seismic, jet or turbo

    def init():
        im.set_data(Universe[0])

    def animate(i):
        im.set_data(Universe[10*i])
        im.set_clim( vmin=np.min(Universe[0]), vmax=np.max(Universe[0]) )
        return im

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(t/10), repeat = False)

    fig.show()

    # return None
#
#
# the_whole_story(Universe)



## Computation time

end_time = time.time()

if __name__ == "__main__" :
    print("Execution time : ",end_time-start_time)



