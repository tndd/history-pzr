ld={'A':4, 'E':3, 'G':6, 'I':1, 'O':0, 'S':5, 'Z':2}
for s in input():
  if s in ld: print(ld[s],end='')
  else: print(s,end='')
print()