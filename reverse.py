def reverse(s) :
  if len(s) == 0:
    return s
  else :
    return reverse(s[1 :]) + s[0]
s = "Edoya"
print("input:", end = "")
print(s)   
print("output :" , end="")
print(reverse(s))            