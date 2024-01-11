#addition
def addition(x,y):
    return x+y

#Subtraction
def subtraction(x,y):
    return x-y

#Multiplication
def multiplication(x,y):
    return x*y
3
#division. Take care of 0

def division(x,y):
    if y != 0:
        return x/y
    else:
        return ("BSDK")

#input
a=float(input("Enter first number:\n"))
o=input("Operator +/-/*//\n")
b=float(input("Enter secondnumber:\n"))

#Function by operator
if o == '+':
    result= addition(a,b)
elif o == '-':
    result=subtraction(a,b)
elif o == '*':
    result=multiplication(a,b)
elif o == '/':
    result=division(a,b)
else:
    result= "TMKC"

#RESULT
print(f"Result={result}\n")

print("Desired outputs here could have been:")
Sumab = a+b;
subab= a-b;
mulab= a*b;
divab= a/b;
print("HELLO WORLD")
print(f"Sum is {a}+{b}={Sumab}\nDifference is {a}-{b}={subab}\nMultiplication is {a}*{b}={mulab}\nDivision is {a}/{b}={divab}\n")