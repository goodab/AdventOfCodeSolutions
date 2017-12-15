def doMaze(instructions):
  i = 0
  count = 0
  while i < len(instructions):
    nexti = (instructions[i] + i) 
    if instructions[i] >= 3:
      instructions[i] -= 1
    else:
      instructions[i] += 1
    count += 1
    i = nexti
  return count

def test(s):
  s = list(map(int, s.split('\n')))
  print(doMaze(s))
