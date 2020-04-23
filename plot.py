import math
function = input("Enter a function f(x):\n")


#def ypos(func,xvalue):
   #for i in range(len(func)):
      #if func[i]=='x':
         #func.replace("x",str(xvalue))
   #return eval(func)

def v(x):
   i = eval(function)
   return i

for y in range(-10,11):
   for x in range (-10,11):
      if -round(v(x))==y:
         print("*",end="")
      elif y==0  and x==0:
         print("+",end="")      
      elif y==0:
         print("-",end='')
      elif  x==0:
         print("|",end="")
      else: 
         print(" ", end='')
   print()
           
           