if 2>4:
    print("high")
elif 10>2:
    print("low")
else:
    print("hehe")

#accept 2 num n print greater num
a=int(input("enter num1: "))
b=int(input("enter num2: "))
if a>b:
    print(a)
else:
    print(b)


#leap year
year=int(input("enter year: "))
if year/400==0 and year/100==0:
    print("leap")
elif year/4==0:
    print("leap")
else:
    print("nope")