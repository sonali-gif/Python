#for loop
# a= range(1,20,1)
# for i in a:
#     print(i)

for i in range(1,20,1):# stop point is imp to give  strt value=0 default and skip default is 1
    print(i)


#reverse
for i in range(20, 0,-1):
    print(i)

#table 5
for i in range(5,51,5):
    print(i)


#take n from user n print its table
n=int(input("enter number"))
for i in range(n,n*10+1,n):
    print(i)
