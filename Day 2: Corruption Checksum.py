def checkSum(l):
  return sum([max(k) - min(k) for k in l])
  
def wholeQuotientSum(l):
  return sum([getWholeQuotient(row) for row in l])

def getWholeQuotient(row):
  s = sorted(row)
  for divisorIndex in range(0,len(s)):
    for dividendIndex in range(divisorIndex+1, len(s)):
      quotient = s[dividendIndex]/s[divisorIndex]
      if quotient == int(quotient):
        return int(quotient)

def formatList(s):
  return [[int(k) for k in row.split('\t')] for row in s.split('\n')]
  
def test(s):
  print(checkSum(formatList(s)))
  print(wholeQuotientSum(formatList(s)))
