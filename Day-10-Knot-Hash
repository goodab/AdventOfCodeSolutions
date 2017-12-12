from collections import deque

def knot(string, start, length, skip):
  string = revList(string, start, length)
  start = (start + length + skip) % len(string)
  skip += 1
  return (string, start, skip)
  
def revList(string, start, length):
  
  string = rotate(string, start)
  toRev = string[0:length]
  rest = string[length:]
  
  toRev.reverse()
  toRev.extend(rest)
  
  toRev = rotate(toRev, -1*start)
  return toRev
  
#left rotate
def rotate(string, amount):
  return string[amount:] + string[:amount]
  
def knotIterate(startingString, knots):
  knots = deque(knots)
  start = 0
  skip = 0
  while len(knots) > 0:
    startingString, start, skip = knot(startingString, start, knots.popleft(), skip)
    print(startingString)
    print(start)
  return startingString
