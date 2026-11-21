n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the third number:"))
n4=int(input("enter the fourth number:"))
if(n1>n2 and n1>n3 and n1>n4):
   print("n1 is greatest")
elif(n2>n1 and n2>n3 and n2>n4):
    print("n2 is greatest")
elif(n3>n1 and n3>n2 and n3>n4):
    print("n3 is greatest")
else:
    print("n4 is greatest")

sub1=int(input("sub1 marks:"))
sub2=int(input("sub2 marks:"))
sub3=int(input("sub3 marks:"))
percent=(sub1+sub2+sub3/300)*100

if(percent>=40 and sub1>33 and sub2>33 and sub3>33):
   print("passed")
else:
   print("failed")


# #name=input("enter your name:")
# #if(len(name)<10):
#     #print("less than 10 character")
# li=["harry","shraddha","naman"]
# print(li.count("harry"))


# year=int(input("enter the yaer:"))

# if year%100==0:
#      print(year//10)
# else:
#    print((year//100)+1)


# age=int(input("enter the age:"))
# if age<5:
#     print("price=0")
# elif age<=5 and age<=12:
#     print("price=100")
# elif age<=13 and age<=60:
#     print("price=200")
# else:
#     print("price=150")

# ang1,ang2,ang3=int(input("enter the first angle:")),int(input("enter the second angle:")),int(input("enter the third angle:"))
# if(ang1+ang2+ang3==180) :
#     print("its a avalid traingle")

# mon=1
# tues=2
# wed=3
# thrus=4
# fri=5
# sat=6
# sun=7
# day=int(input("enter the day number:"))
# if(day==1):
#     print("monday")
# elif(day==2):
#     print("tuesday")
# elif(day==3):
#     print("wednesday")
# elif(day==4):
#     print("thursday")
# elif(day==5):
#     print("friday")
# elif(day==6):
#     print("saturday")
# else:
#     print("sunday")

