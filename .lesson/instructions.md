# Instructions  

  ** use termcolor **
  
_this is a package that lets you colour text_

You install the package (done for you) see packager  files

In your code you import the package 

`from termcolor import colored`

use the function `colored()` to change the colours of text 

`print(colored('some text','blue'))`

[termcolor package documentation](https://pypi.org/project/termcolor/)

_Note_ because I am used to the Canadian spelling I will often import as below so that I can use `coloured()`
instead of `colored()`

`from termcolor import colored as coloured`

## Challenge
Write and test a function  `snazzy_name()` that asks the user to input  a firstname, then a last name.  Then displays them both with a color and 2 attributes.

Look here for documentation https://pypi.org/project/termcolor/   (the example shows how to use attributes and below it is a list of colours, highligts and attributes (note they won't all work, you will have to experiment) )

choose a colour and two attributes to display the first name, and a different color and attributes for the second set
