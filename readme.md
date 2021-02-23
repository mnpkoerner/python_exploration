# Notes on Installing Python

I used homebrew to install what I needed for Python, then I started reading https://python.land/ and used the interative terminal in VS Code as a sandbox to see how Python worked. I got an overview with some pretty broad strokes, but was able to approach some interesting whiteboard problems with my group:

Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.

Examples

check_square_and_cube([4, 8]) ➞ True
check_square_and_cube([16, 48]) ➞ False
check_square_and_cube([9, 27]) ➞ True

Notes
Remember to return either True or False.
All lists contain two positive numbers.


def checkNums(list) :
	If list[0] ** (1/2)  == round(list[1] ** (1/3)):
		Return true
	Else :
		Return false


I like that Python allows for the user to to do more complex math more simply than JavaScript. I think post-Prime that I'll dig into machine learning a little bit with Python and JS to see how the two compare.
