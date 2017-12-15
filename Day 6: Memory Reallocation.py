from collections import Counter

def redistribute(banks, index):
  value = banks[index]
  banks[index] = 0
  for i in range(1, value + 1):
    banks[(index + i) % len(banks)] += 1
  return banks

def findRepeat(banks):
  states = Counter()
  timestep = 1
  
  
  while states[hashable(banks)] == 0:
    index = banks.index(max(banks))
    states.update({hashable(banks): timestep})
    banks = redistribute(banks,index)
    timestep += 1
    
  return (states[hashable(banks)], timestep - 1)

def hashable(s):
  return ','.join(list(map(str, s)))
