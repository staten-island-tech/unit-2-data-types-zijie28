""" a=input("Please type a sentence.")
answer=a.split( )
print(f"This sentence has {len(answer)} words.") """

l=[]
d={0:"Verb",1:"Another Verb",2:"Another verb", 3:"Noun",4:"A Number",5:"A Celebrity Guest", 6:"A Adjective", 7:"Another Adjective"}
def mad_lib():
    for i in d:
        a= input(f"Provide a {d[i]}")
        l.append(a)

mad_lib()
        print(f"It was {l[0]} day at school, and {l[5]} was super {l[1]}for lunch. But when she went outside to eat, a {l[3]} stole her food! {l[5]}chased the {l[3]} all over school. She {l[0]}, {l[1]}, and {1[2]} through the playground. Then she tripped on her {l[3]} and the {l[3]} escaped! Luckily, {l[5]}’s friends were willing to share their food with her.")
        print(len(l))

