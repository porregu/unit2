name= input("what is your name")
print("nice to meet you", name,"my name is bot")
location=input("where are you from")
print(location,"is a really cool place","I'm from spain")
number=float(input("what's your favorite number"))
my_number=3000/number
print(number,"is a incredible number","my favorite number is",my_number,"times bigger than yours")
car=input("what's your dream car")
print(car,"wow i know that car is soo cool","my dream car is a porche")
price=float(input("how much that car cost?"))
print(price,"gee, that is spendy")
rate=float(input("what will be a normal yearly interest for the car"+"%"))
print(rate, "well that's okay")
loan=float(input("how many years will take you for get out of the loan"+"years"))
print(loan,"well it's reasonable")
loan=loan*12# make the loan times 12 months
rate=rate/100/12#make the rate percent in 12 months
mpymt=(rate*price)/(1-(1+rate)**-(loan))#monthly payment
print("so", mpymt, "is your monthly payment")
print("thanks a lot appreciate this, goodbye")