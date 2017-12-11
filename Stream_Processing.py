

pstate = {
  'inc':0,
  'summation':0,
  'garbageFlag':False,
  'pointer':0
}

def initializePState():
  global pstate
  pstate = {
    'inc':0,
    'summation':0,
    'garbageFlag':False,
    'pointer':0
  }

def entergroup(state):
  if state['garbageFlag']:
    return
  state['inc'] += 1
  state['summation'] += state['inc']

def exitgroup(state):
  if state['garbageFlag']:
    return
  state['inc'] -= 1
  
def entergarbage(state):
  if state['garbageFlag']:
    return
  state['garbageFlag'] = True
  
def exitgarbage(state):
  state['garbageFlag'] = False
  
def ignore(state):
  state['pointer'] += 1

def parseStream(l):
  initializePState()
  while(pstate['pointer'] < len(l) ):
    
    if l[pstate['pointer']] in specialcharacters.keys():
      specialcharacters[l[pstate['pointer']]](pstate)
    pstate['pointer'] += 1
  
  return pstate['summation']
  
specialcharacters = {
  '{':entergroup,
  '}':exitgroup,
  '<':entergarbage,
  '>':exitgarbage,
  '!':ignore
}
  
print(parseStream('{}'))
print(parseStream('{{{}}}'))
print(parseStream('{{},{}}'))
print(parseStream('{{{},{},{{}}}}'))
print(parseStream('{{<a!>},{<a!>},{<a!>},{<ab>}}'))

      
