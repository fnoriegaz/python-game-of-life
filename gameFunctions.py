#functions for "game of life" game
import numpy as np

#check how many neighbours are alive
def chkNeighb(data,iy,ix):
    accum=0

    if(data[iy-1][ix-1]==1):
        accum+=1
    if(data[iy-1][ix]==1):
        accum+=1
    if(data[iy-1][ix+1]==1):
        accum+=1

    if(data[iy][ix-1]==1):
        accum+=1
    if(data[iy][ix+1]==1):
        accum+=1

    if(data[iy+1][ix-1]==1):
        accum+=1
    if(data[iy+1][ix]==1):
        accum+=1
    if(data[iy+1][ix+1]==1):
        accum+=1


    return accum

#Rules to decide whether a cell lives or dies
def rules(input,cols,rows):
    output=np.zeros((rows,cols))
    for ix in range(1,cols-1):
        for iy in range(1,rows-1):
            neighbours=chkNeighb(input,iy,ix)
            #   1.Any live cell with fewer than two live neighbours dies, as if
            #   by underpopulation
            if(input[iy][ix]==1.0 and neighbours<2):
                output[iy][ix]=0.0

            #   2.Any live cell with two or three live neighbours lives on to
            #   the next generation
            elif(input[iy][ix]==1.0 and 2<=neighbours<=3):
                output[iy][ix]=1.0

            #   3.Any live cell with more than three neighbours dies, as if by
            #   overpopulation
            elif(input[iy][ix]==1.0 and neighbours>3):
                output[iy][ix]=0.0

            #   4.Any dead cell with exactly three live neighbours becomes a
            #   live cell, as if by reproduction
            elif(input[iy][ix]==0 and neighbours==3):
                output[iy][ix]=1.0

    return output
    # plt.matshow(matrix)
