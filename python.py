#Create a program that takes two sortedarrays as input and merges them into a single sorted array
def merge_array(arr1,arr2):
    arr3= sorted(arr1) + sorted(arr2)
    print(arr3)


arr1=[1,2,3]
arr2=[4,5,6]


#A program that takes a string as input and output the string reversed
def reversed(name):
    name=list(name)
    name.reverse()
    name="".join(name)
    print(name)
name="Daisy"
#A program that takes a string as input and removes duplicate characters
def word(numbr):
    number=set(numbr)
    number=list(numbr)
    print(number)
number=(1,2,2,3,3,4,4,5)
#a program that takes a list of intergersas input and output the list sorted in descending order
def number(list):
    list.sort().reverse()
    print(list)
interger=[1,2,3,4,5,5]
#write a program that takes a list of integers as input and removes all duplicate numbers
def unique_integers(integers):
    numbers=set(intergers)
    numbers=list(integers)
    print(number)
integers=[1,2,3,3,5,6,8]
#Write a program that takes a sentence as input and reverses the order of words in it
sentence="I am always happy"
mySentence=sentence.split("")
print(mySentence)
mySentence.reverse()
mySentence.join()
print(mySentence)
#create a program that takes a base and exponent as input and calculates the exponential value.
a=(base,exponent)
base=3
exponent=2
b=base**exponent
print(b)
#anagram
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")         
         
  
s1 ="listen"
s2 ="silent"r4







