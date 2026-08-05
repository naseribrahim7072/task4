temp=float(input("enter the tempreture in celsius "))
fahrenheit= temp* 9/5+32
print ("the tempreture is",fahrenheit)
if fahrenheit>30:
    print("its hot day ")
elif fahrenheit<=30 :
    print("its normal")
elif fahrenheit<15 :
    print("it cold")