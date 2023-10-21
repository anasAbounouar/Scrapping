import itertools
import random 

# Sample list of 10 elements
elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K"]
s=0
r=2
while r<7:

    # Generating combinations of 2 elements
    combinations = list(itertools.combinations(elements, r))
    print(len(combinations))
    s+=len(combinations)
    r+=1
print("total possibilités est : ")
print(s)
list=["pile","face"]
print(random.choice(list))