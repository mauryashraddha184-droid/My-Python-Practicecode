# n=int(input("enter the number:"))
# for i in range(1,11):
# #     print(f"{n}={n*i}")


# def sum_even_num(number):
#     sum=0 
#     for num in number:
#         if num%2==0:
#             sum+=num

#     return sum
#method of cincatination
# s1=input("enter the first string:")
# s2=input("enter the second string")
# s3=s1+""+s2
# print(s3) 

# s1=input("enter the first string:")
# s3=f"hello my name is {s1}"
# print(s3)

# def celcuis_to_far(celcuis):
#     F=(celcuis*1.8)+32
#     print(f"{celcuis} to {F}")

# celcuis_to_far(200)

    
def traingle():
    n1=int(input("enter the angle"))
    n2=int(input("enter the angle"))
    n3=int(input("enter the angle"))
    if(n1+n2+n3==180): 
     print("this is a traingle")
    else:
       print("not a traingle")
traingle()
