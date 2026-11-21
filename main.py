def square(number):
   return number*number

result=square(4)
print((square(4)))



# def sum(num1,num2):
#     return num1+num2

# print(sum(2,4))


# def multiply(p1,p2):
#     return p1*p2

# print(multiply(5,5))
# print(multiply('a',5))
# import math

# def circle(r):
#     area=math.pi*r**2
#     circumference=2*math.pi*r
#     return area,circumference


# a,c=circle(3)
# print("area",a,"circumference:",c)


# def greet(name='user'):
#     return"hello, "+name+"!"

# print(greet('shraddha'))

# cube=lambda x: x **3

# print(cube(3))


# def sum_all(*args):
#     print(args)
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5,))

# def printmul(num):
#      for i in range(1,11):
#           print(num*i)

# printmul(3)

# def sum(n):
#     sum=0
#     for i in range (1,n):
#       sum=sum+i
#       i+=1
#       print(sum)
      
# sum(11)
     
# def swap():
#     temp=None
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     temp=a
#     a=b
#     b=temp
#     print(a,b)


# swap()

# def reverse_num():
#     num=int(input("enter tye number:"))
#     rev_num=0

#     while num!=0:
#         digit=num%10
#         rev_num=rev_num*10+digit
#         num=num//10

#     print("reverse num:",rev_num)

# reverse_num()   
     
       
# def profitloss():
#     cost_price=int(input("enter cost price:"))
#     selling_price=int(input("enter selling price:"))

#     if(cost_price-selling_price>0):
#         print("loss")

#     elif(selling_price-cost_price>0):
#         print("profit")

#     else:
#         print("no profit no loss")

# profitloss()

