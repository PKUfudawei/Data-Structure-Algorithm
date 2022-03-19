#!/usr/bin/env python
# coding=utf-8
def arroundSearch(matrix,i,j,):
    m=len(matrix)
    n=len(matrix[0])
    

def getMaxLen(matrix):
    coordinate={
        matrix[i][j]: [i,j] for i in range(len(matrix)) for j in range(len(matrix[0]))
    }
    
    sortedHeights=[]
    for i in range(len(matrix)):
        sortedHeights+=matrix[i]
    sortedHeights.sort()
    
    Max=1
    maxLen=[[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(sortedHeights)):
        h=sortedHeights[i]
        x,y=coordinate[h]
        nearMax=0
        if x>0 and matrix[x-1][y]<h and matrix[x-1][y]>nearMax:
            nearMax=matrix[x-1][y]
        if x<len(matrix)-1 and matrix[x+1][y]<h and matrix[x+1][y]>nearMax:
            nearMax=matrix[x+1][y]
        if y>0 and matrix[x][y-1]<h and matrix[x][y-1]>nearMax:
            nearMax=matrix[x][y-1]
        if y<len(matrix[0])-1 and matrix[x][y+1]<h and matrix[x][y+1]>nearMax:
            nearMax=matrix[x][y+1]
        
        if nearMax!=0:
            m,n=coordinate[nearMax]
            maxLen[x][y]=maxLen[m][n]+1
        if maxLen[x][y]>Max:
            Max=maxLen[x][y]
        
    return Max

def driver():
    R,C=map(int,input().split())
    heights=[]
    for i in range(R):
        heights.append(list(map(int,input().split())))
        
    print(getMaxLen(heights))
    
driver()
