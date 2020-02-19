import re

#extracting data with regular expressions
x = 'this string contains a 2 that is a number, a 9 and 12'
y= re.findall('[0-9]+', x) 
print(y)

#Greedy regular expressions push outwards in both directions and returns the biggest value(s)
x = 'this string contains; a 2 that is a number; a 9 and 12'
y= re.findall('^t.+;', x) 
print(y)

#Non-greedy "?" regular expressions push outwards in both directions and returns the nearest value(s). 
x = 'this string contains; a 2 that is a number; a 9 and 12'
y= re.findall('^t.+?;', x) 
print(y)
