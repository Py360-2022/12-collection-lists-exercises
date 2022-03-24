'''
examples and exercises using termcolor
'''
from termcolor import colored

print(colored('some text','magenta'))

word = 'abc'
colours = ['blue', 'green', 'red']
ix = 0
for letter in word:
  print(colored(letter,colours[ix]))
  ix += 1  
'''print on one line'''
ix = 0
'''
the default for print is to have a carriage return & line feed \n
so if you want to change it you use ,end=
but you need the extra print after so the next one doesn't start
on the same line  
'''
for letter in word:
  print(colored(letter,colours[ix]), end=' ')
  ix += 1 
  
print() 

coloured_word = ''
ix = 0
for letter in word:
  coloured_word += colored(letter, colours[ix])
  ix += 1
print(coloured_word)
'''
the below code gets an error, how would you fix it ?
'''
ix = 0
for letter in "python":
  coloured_word += colored(letter, colours[ix])
  ix += 1
print(coloured_word)
