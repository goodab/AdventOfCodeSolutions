def sumConsecDigits(l):
  return sum([l[i] for i in range(0,len(l)) if l[i] == l[(i+1) % len(l)]])  

def sumHalfwayDigits(l):
  length = len(l)
  halfLength = int(len(l)/2)
  return sum([2*l[i] for i in range(0, halfLength) if l[i] == l[(i + halfLength) % length]])

def test(s):
  print(sumConsecDigits(list(map(int,list(s)))))
  print(sumHalfwayDigits(list(map(int, list(s)))))
