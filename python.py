# class number:
#     def checkevenodd(a):
#       if(a%2==0):
#          print("a is even")
#       else:
#          print("a is odd")
#     def checknumber(n):
#        if(n>0):
#           print("n is negative")
#        elif(n<0):
#            print("n is positive")
#        else:
#           print("n is equals to zero")


# b=number()
# number.checkevenodd(4)
# number.checknumber(0)

s=input("enter the string:")
vowels="aeiou"
count=0
for char in s:
    if char in vowels:
        count+=1
print("number of vowels:",count)



