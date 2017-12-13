def collideValue(k):
  l,d = k
  if l % (2*d - 2) == 0:
    return l*d
  return 0

def parseFirewalls(s):
  return [(int(row.split(':')[0].strip()),int(row.split(':')[1].strip())) for row in s.split('\n')]
  
def getSeverity(l):
  return sum(map(collideValue, l))
  
def solvePuzzle(s):
  return getSeverity(parseFirewalls(s))
