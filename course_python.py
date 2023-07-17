#I/O with Basic file in Python

myfile = open('C:/Users/magda/udemy_course/Python exercises/test.txt')
myfile.read()
myfile.seek(0) #wraca kursor do początku

contents = myfile.read()

myfile.readlines()

with open('C:/Users/magda/udemy_course/Python exercises/test.txt') as my_new_file:
    contents = my_new_file.read()


#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for sentence in st.split():
    if sentence.startswith('s') or sentence.startswith('S'):
        print(sentence)

#Use range() to print all the even numbers from 0 to 10.
for num in range(0,11):
    if (num % 2) == 0 and num != 0:
        print(num)

#Lub
for num in range(0,11,2):
    print(num)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
list = [numb for numb in range(0,51) if numb%3 == 0]
print(list)

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for sentence in st.split():
    if len(sentence) % 2 == 0:
        print(sentence + ' is even')

#Write a program that prints the integers from 1 to 100. But for multiples of three print 
# "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples 
# of both three and five print "FizzBuzz".

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

mylist = [sentence[0] for sentence in st.split()]
mylist
mylist[0]
mylist[1]

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return (min(a,b))
    else:
        return (max(a,b))
    

# Check
lesser_of_two_evens(2,4)
# Check
lesser_of_two_evens(2,7)


#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    my_list = [t[0] for t in text.split()]
    if my_list[0] == my_list[1]:
        return True
    return False


# Check
animal_crackers('Levelheaded Llama')
# Check
animal_crackers('Crazy Kangaroo')

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

def makes_twenty(n1:int ,n2: int):
    suma = n1 + n2
    if suma == 20 or n1 == 20 or n2 == 20:
        return True
    return False

# Check
makes_twenty(20,10)
# Check
makes_twenty(2,3)


#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#old_macdonald('macdonald') --> MacDonald

#Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    #first_half = name [:3]
    #second_half = name[3:]
    #return first_half.capitalize() + second_half.capitalize()
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

# Check
old_macdonald('macdonald')


#MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

#Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

#>>> "--".join(['a','b','c'])
#>>> 'a--b--c'

#This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

#>>> " ".join(['Hello','world'])
#>>> "Hello world"

def master_yoda(text):
    my_list = [t for t in text.split()]
    my_list.reverse()
    #my_list[0]= my_list[0].capitalize()
    #my_list[-1] = my_list[-1].lower()
    return " ".join(my_list)


# Check
master_yoda('I am home')
# Check
master_yoda('We are ready')

#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


# Check
has_33([1, 3, 3])
# Check
has_33([1, 3, 1, 3])
# Check
has_33([3, 1, 3])

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    for t in text:
        print(t*3, end ='')

# Check
paper_doll('Hello')
# Check
paper_doll('Mississippi')

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    pass
# Check
blackjack(5,6,7)
# Check
blackjack(9,9,9)
# Check
blackjack(9,9,11)
    