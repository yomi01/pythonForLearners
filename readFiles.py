
# this is how you tell python which file you want it to open or read
# opening it will not show the contents of the file
'''handle = open('rand.txt')'''

#instanciating a variable 
count = 0

# This is a for loop that counts how many lines of text there are in a file
# Then prints out the answer using the format method/function

'''for email in handle:
  count = count + 1
print('there are {} lines in this file'.format(count))'''

# print how many characters in the file
'''imp = handle.read()
print(imp)
print(len(imp))'''

#this loop removes every line that starts with a j
'''for email in handle:
    email = email.rstrip()
    if not email.startswith('j'):
        print(email)'''

#this loop removes every line that starts with a j
'''for email in handle:
    email = email.rstrip()
    if email.startswith('j'):
        print(email)'''

#skip all lines containing 'j' with the continue keyword
'''for email in handle:
    email = email.rstrip()
    if email.startswith('j'):
        continue
    print(email)'''

# Prompts the user to enter file name and passes user input into fname
'''fname = input('please enter the file name you want opened:' )
handle = open(fname)'''

#find all the users with a @yahoo email account and print to console
'''for email in handle:
    email = email.rstrip()
    if '@yahoo' in email:
        print(email)'''

#Prompts the user to enter file name and catch bad inputs and print msg to console
'''fname = input('please enter the file name you want opened:' )'''
'''try:
    handle = open(fname)
except:
    print('file is not found in this folder, please check file name', handle)
    quit

for email in handle:
    email = email.rstrip()
    if '@yahoo' in email:
        print(email)'''

#Make a brandNew list with nothing in it
stuff = list()

#add elements to list 
'''stuff.append('book')
stuff.append('key')
stuff.append('table')
stuff.append('bag')
print(stuff)'''
# checking what's in a list
'''6 in stuff
9 in stuff
print(stuff)'''
#sort in alphabetical order using .sort()
'''stuff.sort()
print(stuff)'''

#turn a stirng into a list
'''sentence = 'this is a string'
nSent = sentence.split()
print(nSent)'''

#Dictionarys have key-value pairs. this instanciates a Dictionary
bags = dict()
    #pass key-value piars into dictionary
bags['rxp'] = 2
bags['btc'] = 9000
bags['eth'] = 200
bags['ltc'] = 70
bags['link'] = 4
bags['zch'] = 50
print(bags)

#Dictionaries are mutable
bags['rxp'] = bags['rxp'] + 2
print(bags)

#counting elements in a Dict
counts = dict()
names = ['chen', 'len', 'ben', 'glen', 'chen', 'chen','glen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#method for getting the keys
print(counts.keys())

#method for getting just values
print(counts.values())

#method the get back a list of key-value pairs
print(counts.items())

#two iteration key value 

for key,value in counts.items():    
    print(key,value) 