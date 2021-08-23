"""Reversing a string

x = input("Input a string: ")

y = [x[a] for a in range(len(x)-1,0,-1)]
y.append(x[0])

print("".join(y))
"""
#---------------------------------------#

"""Count Vowels 
#Get Input
x = input("Enter a word: ")

#Initialize variables
vowels = ['a', 'e','i','o','u']
vowelTrack = {}

#find vowels from input
answer = [temp for temp in x if temp in vowels]

#generate count of vowels from input
    vowelTrack[vowel] = x.count(vowel)

print("Number of vowels: ", len(answer))
print("Frequency of vowels:")

for vowel,count in vowelTrack.items():
    print(vowel,count)
"""
#---------------------------------------#

"""Count words in a string 

with open('someText.txt', "r") as f:
    count = 1
    for word in f.read():
        if word == " ":
            count += 1

    print(count)
"""
#---------------------------------------#

"""Letter Sum """

def lettersum(string):
    """Takes in a string and returns the sum of the values """

    #Set values
    letterValues = {'':0, ' ':0}
    value = 1
    output = 0

    for p in range(97, 123):
        letterValues[chr(p)] = value
        value += 1
    
    if string == ' ' or string == '':
        print(output)
    
    else:
        for letter in string:
            output += letterValues[letter.lower()]
    
    return output

""" This code creates a dictionary and assignes a word and its respective value. Used in conjunction with the code below it
enableWC = {}

with open("enable1.txt", "r") as f:
    temp = f.read().splitlines()
    for word in temp:
        enableWC[word] = lettersum(word)
"""

""" This code writes the list of words and their values to a document, only needs to be ran once 
with open('test.txt', 'w') as f:
    for x,y in enableWC.items():
            a = x + ' '+ str(y) + '\n'
            f.write(a)
"""


def findSum319():
    with open("test.txt",'r') as f:
        for line in f:
            a = line.split(' ')
            b = int(a[1].rstrip('\n'))
            if b == 319:
                print(a)

def countOddSum():
    with open("test.txt",'r') as f:
        count = 0
        for line in f:
            a = line.split(' ')
            b = int(a[1].rstrip('\n'))
            if b%2 == 1:
                count += 1
    
    print(count)

def mostCommonSum():
    with open("test.txt",'r') as f:
        output = {}
        for line in f:
            a = line.split(' ')
            b = int(a[1].rstrip('\n'))

            if b in output:
                output[b] += 1
            else:
                output[b] = 1
        
    sortedOut = sorted(output.items(), key=lambda x:x[1], reverse=True)

    for i in sortedOut:
        count = 0
        if count ==5:
            break
        else:
            count = 0
            print(i[0], i[1])
            count += 1
        
