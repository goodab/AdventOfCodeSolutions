from collections import deque

def parseNeighborlist(s):
  
  return {int(row[:row.index('<')].strip()):map(int,row[row.index('>')+1:].strip().split(',')) for row in s.split('\n')}

def graphtraversal(neighborlist):
  
  nodeSet = set()
  toVisit = deque()
  
  #neighborlist is ordered -> node 0 is the first element
  toVisit.append(neighborlist[0])
  nodeSet.add(0)
  while len(toVisit) > 0:
    
    toTrav = toVisit.popleft()
    for i in toTrav:
     
      if i not in nodeSet:
        nodeSet.add(i)
        toVisit.append(neighborlist[i])
  
  return len(nodeSet)
