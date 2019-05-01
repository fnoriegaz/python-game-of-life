#the Game Of Life
#Rules:
#   1.Any live cell with fewer than two live neighbours dies, as if by
#   underpopulation
#   2.Any live cell with two or three live neighbours lives on to  the next
#   generation
#   3.Any live cell with more than three neighbours dies, as if by
#   overpopulation
#   4.Any dead cell with exactly three live neighbours becomes a live cell, as
#   if by reproduction


import gameFunctions as gameF
from  matplotlib import pyplot as plt
from  gameFunctions import np

#Define matrixIn dimensions. the bigger the matrix, the slower the process. 
cols=127
rows=127

#Create and manually modify the input (matrixIn).
matrixIn=np.zeros((rows,cols))
for j in range(1,rows-1):
    for i in range(1,cols-1):
        # if(i==j):
        #     matrixIn[j][i]=1.0
        # if((cols-i)==j):
        #     matrixIn[j][i]=1.0
        # if(10<=j<=13 and 32<=i<=96):
        #     matrixIn[j][i]=1.0
        # if(53<=j<=55 and 32<=i<=96):
        #     matrixIn[j][i]=1.0
        # if(105<=j<=107 and 32<=i<=96):
        #     matrixIn[j][i]=1.0
        # if(31<=i<=33 and 32<=j<=96):
        #     matrixIn[j][i]=1.0
        # if(83<=i<=85 and 32<=j<=96):
        #     matrixIn[j][i]=1.0
        # if(95<=i<=97 and 32<=j<=96):
        #     matrixIn[j][i]=1.0
        if(i==61):
            matrixIn[j][i]=1.0
        if(i==63):
            matrixIn[j][i]=1.0
        if(i==65):
            matrixIn[j][i]=1.0

        if(j==61):
            matrixIn[j][i]=1.0
        if(j==63):
            matrixIn[j][i]=1.0
        if(j==65):
            matrixIn[j][i]=1.0





#Create context to plot matrixIn every t step
fig=plt.gcf()
fig.show()
fig.canvas.draw()
for t in range(1000):
    plt.imshow(matrixIn)
    matrixIn=gameF.rules(matrixIn,cols,rows)
    plt.pause(.001)
    fig.canvas.draw()
    plt.clf()
