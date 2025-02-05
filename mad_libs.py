""" a=input("Please type a sentence.")
answer=a.split( )
print(f"This sentence has {len(answer)} words.") """

l=[]
d={0:"Verb",1:"Another Verb",2:"Noun",3:"A Number",4:"A Celebrity Guest"}
def mad_lib():
    for i in d:
        a= input(f"Provide a {d[i]}")

mad_lib()
