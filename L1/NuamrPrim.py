n = int(input("Introduceti un numar intreg: "))
este_div=False
if n <= 1:
    print("Numarul ",n," NU este prim")

else:
   for i in range(2, n):
       if n%i==0:
           este_div=True
           break

if este_div:
    print("Numarul ",n," NU este prim")
else:
    print("Numarul ",n," este prim")

