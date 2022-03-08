# Instructions  

  ** manipulate lists **

  _ write functions to solve the following _

  ## Specifications
  1. Write a function `count_multiples` that takes two parameters, a list of positive integers and a positive number. It will count the number of items in the list which are multiples of the number.
For example: `count_multiple([3,4,5,6,7,8] , 3)` should return 2 since 3 and 6 are multiples of 3
  2. Write a function `is_sorted` that takes a list of integers as a parameter. It will return True if the list is in sorted order (each item is smaller than or equal to the next item), False if not.
    * For example: `is_sorted([4,4,5,7,8])` should return True
    * Hint: Like exercise 1, as soon as you find a case where the next item is not bigger, you can return False
  
    * Question: will your function work with lists of strings?
  3. Write a function `is_palindrome` that takes a string as parameter and return True is the string is a palindrome, False if not

  A palindrome is a string that reads the same way in both directions (e.g., 'madam')
    * Hints: use a for in range, where the iterator is the index, starting at 0 and going to len (optional: for greater efficiency, stop half way)
    * Check the letter in the front and in the back if they are equal (how do you know the index at the end? use negative numbers?)
    * As soon as two are unequal, you can return False
    * If you get to the end of the loop, it means all were equal so you can return True
4. The value of π can be approximated by the following infinite series (Nilakantha's Series):  ![nilakatha series](assets/nilakatha.jpg)
  Write a function `approx_pi` that takes a parameter that indicates the number of approximations to be calculated. For example, if the parameter is 0 return 3, if the parameter is 1, return 3 + the first term, if the parameter is 2, return 3 plus the first, minus the second. Hints:
    * You need a way to alternate between adding and subtracting the next term. Consider using (-1)**n where n is changing between even and odd
    * Look at the pattern in the denominators – is there a way you can use your range variable to help figure the first number of each denominator expression?
    * Ref https://en.wikipedia.org/wiki/Pi 


    ![test2](assets/nilakatha.jpg)