# sum of numbers in the list
# def sum_of_list():
#     number=[8,2,3,0,7]
#     total=sum(number)
#     print("sum of the list is:",total);

# sum_of_list()

#reverse  string
# def reverse_string():
#     str="hello world"
#     print("reversed string:",str[::-1])

# reverse_string()


# count lowercase and uppercase letters in a string
def count_upper_lower():
    str="hello world"
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper=upper+1
        elif i.islower():
            lower=lower+1
            print("number of uppercase letters:",upper)
            print("number of lowercase letters:",lower)
count_upper_lower()



