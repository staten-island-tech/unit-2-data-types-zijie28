import math
""" a=input("Please type a sentence.")
answer=a.split( )
print(f"This sentence has {len(answer)} words.") """

""" l=[]
d={0:"Verb",1:"Another Verb",2:"Another verb", 3:"Noun",4:"A Number",5:"A Celebrity Guest", 6:"A Adjective", 7:"Another Adjective"}
n=len(d)

a=input("Provide a Verb: ")
b=input("Provide a Another Verb: ")
c=input("Provide a Another Verb: ")
d=input("Provide a Noun: ")
e=input("Provide a Number: ")
f=input("Provide a Celebrity Guest: ")
g=input("Provide a Adjective: ")
h=input("Provide a Another Adjective: ")
print(f"It was {g} day at school, and {f} was super {b} for lunch. But when she went outside to eat, a {d} stole her food! {f} chased the {d} all over school. She {a}, {b}, and {c} through the playground. Then she tripped on her {d} and the {d} escaped! Luckily, {f}’s friends were willing to share their food with her.") """

""" x=input("Input a number")

if int(x)%2 == 0:
    print("Number is even")
else:
    print("Number is odd") """
""" def get_response():
    res=input("Was the service bad, okay, good, or great? ")
    res_1=res.lower()
    bill_calculator(res_1)
def bill_calculator(response):
    if response == "bad":
        a=input("Would you like to tip 0%?")
        a_1=a.lower()
        if a_1 == "no":
            get_response()
        elif a == "yes":
            print("You have tipped 0%")
    elif response == "okay":
        a=input("Would you like to tip 15%?")
        a_1=a.lower()
        if a_1 == "no":
            get_response()
        elif a == "yes":
            print("You have tipped 15%")
    elif response == "good":
        a=input("Would you like to tip 20%?")
        a_1=a.lower()
        if a_1 == "no":
            get_response()
        elif a == "yes":
            print("You have tipped 20%")
    elif response == "great":
        a=input("Would you like to tip 25%?")
        a_1=a.lower()
        if a_1 == "no":
            get_response()
        elif a == "yes":
            print("You have tipped 25%")
    else:
        print("Not a vaild response!")
        get_response()
def tip():
    res_2=input("What was your bill?")
    get_response()
tip() """



""" def numb(x):
    range_num=int(x) + 1
    for i in range(1, range_num):
        if int(x)%i == 0:
            l.append(i)
    print(f"The factors of {y} are:")
    for i in l:
        print(i)
l=[]
y=input("Input a number: ")
numb(y)
 """
""" def numb(x,y):
    range_num=int(x) + 1
    for i in range(1, range_num):
        if int(x)%i == 0:
            l.append(i)
    range_num2=int(y) + 1
    for i in range(1, range_num2):
        if int(y)%i == 0:
            l_2.append(i)
    gcf_dict=set(l).intersection(l_2)
    gcf_list=list(gcf_dict)
    print(f"The greatest common factor between the 2 numbers is: {gcf_list[-1]}")
l=[]
l_2=[]
x=input("Input a number: ")
y=input("Input another number: ")
numb(x,y) """