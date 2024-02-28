n1=0
n2=0
op=""
resultado=0
n1=float(input("ingrese un numero:"))
n2=float(input("ingrese otro numero:"))

op=input("que operacio desea realizar?:")
if op=="+":
    print(n1+n2)
if op=="-":
    print(n1-n2)
if op=="*":
    print(n1*n2)
if op=="/":
    print(n1/n2)