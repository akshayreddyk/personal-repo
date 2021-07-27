T = input()
temp = float(T[:-1])
category = T.replace(str(temp),"")
if category  == 'C':
  F = (9/5)*temp+32
  K = temp+273
  print(str(temp)+'C')
  print(str(F)+'F')
  print(str(K)+'K')
elif category == 'F':
  C = (temp-32)*(5/9)
  K = C + 273
  print(str(C)+'C')
  print(str(temp)+'F')
  print(str(K)+'K')
elif category == 'K':
  C = int(temp)+273
  F = (9/5)*C+32
  print(str(C)+'C')
  print(str(F)+'F')
  print(str(temp)+'K')
