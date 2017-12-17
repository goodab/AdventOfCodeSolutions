from collections import Counter
  
def parseBlock(s):
  registers = Counter()
  coresp = {'inc':1 ,'dec':-1}
  largest = 0
  for row in s.split('\n'):
    pieces = row.split(' ')
    if eval(str(registers[pieces[4]])+''.join(pieces[5:])):
      registers[pieces[0]] += coresp[pieces[1]]*int(pieces[2])
      if registers[pieces[0]] > largest:
        largest = registers[pieces[0]]
  
  return (largest, registers[max(registers, key=registers.get)])
