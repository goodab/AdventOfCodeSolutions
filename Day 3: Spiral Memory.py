#This is not an elegant solution
from math import floor, sqrt
from collections import Counter

def base(n):
  rootBelow = floor(sqrt(n))
  if rootBelow % 2 == 0 :
    return evenSquareUlamCoord(rootBelow)
  else:
    return oddSquareUlamCoord(rootBelow)
    
def offset(n):
  rootBelow = floor(sqrt(n))
  distToSquareBelow = n - rootBelow ** 2
  if distToSquareBelow == 0:
    return (0,0)
  if distToSquareBelow <= rootBelow:
    return (((-1) ** (rootBelow % 2 + 1)),((-1) ** (rootBelow % 2 + 1)) * (distToSquareBelow - 1))
  else:
    return ((rootBelow + 2 - distToSquareBelow)*((-1) ** (rootBelow % 2 + 1)), ((-1) ** (rootBelow % 2 + 1)) * rootBelow)

def findUlamCoord(n):
  return add(base(n), offset(n))
  
def distToOrigin(n):
  return sum([abs(x) for x in list(findUlamCoord(n))])

def evenSquareUlamCoord(n):
  return (-1*(n/2 - 1), n/2)
  
def add(a, b):
  return (a[0]+b[0], a[1]+b[1])
  
def oddSquareUlamCoord(n):
  return ((n - 1)/2, -1* (n - 1)/2)
  
def initSpiral():
  c = Counter({(0,0) : 1})
  return c

def computeNewSpiral(c,n):
  c[n] = sum([c[(a,b)] for a in [n[0] + x for x in range(-1, 2)] for b in [n[1] + y for y in range(-1, 2)]])
  
def stressTest(toBeat):
  spiral = initSpiral()
  n = 1
  while spiral[findUlamCoord(n)] < toBeat:
    n += 1
    computeNewSpiral(spiral, findUlamCoord(n))
  return (spiral[findUlamCoord(n)], n, findUlamCoord(n))
  
def iterativeStress(end):
  spiral = initSpiral()
  n = 1
  while n<end:
    n += 1
    computeNewSpiral(spiral, findUlamCoord(n))
    print((spiral[findUlamCoord(n)], n, findUlamCoord(n)))
  
