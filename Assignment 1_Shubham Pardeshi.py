#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators

*      : It is an expression.Basically it is an Arithmetic opertor named as Multiplication Operator.

'hello': It is a string value.
-87.8  : It is a value having numeric data type float .
-      : It is an expression.One of the Arithmetic operator named as Subtraction Operator.
/      : It is expression.It also comes under an Arithmetic operator named as Division Operator.
+	   : An expression which is an Arithmetic operator named as Addition Operator.
6      : It is a value having numeric data type int.
2. What is the difference between string and variable?

-Variables are containers for storing data values. They are created the moment you first assign a value to it.
-Strings in python are surrounded by either a single quotation marks,or double quotation marks.

A string value is just a literal text.For eg. 'Hello'.And a variable is something that stores data i.e it can store string,float,int etc.3. Describe three different data types.

Data type is one of the important concept in programming.A variable can store data of diiferent types,and these data types can do different different things.Python has several data types built-in by default.Three data types are catagorised as follows:
 - Numeric Types :int, float, complex
 - Text Type      :str
 - Boolean Type   :bool4. What is an expression made up of? What do all expressions do?

--An expression is a combination of operators and operands that is interpreted to produce some other value. In any programming language, an expression is evaluated as per the precedence of its operators. So that if there is more than one operator in an expression, their precedence decides which operation will be performed first. We have many different types of expressions in Python.
 1. Constant Expressions: These are the expressions that have constant values only.
 eg. x= 20+26.3
     print(x)
 output: 46.3
 
 2. Arithmetic Expressions: An arithmetic expression is a combination of numeric values, operators, and sometimes parenthesis. The result of this type of expression is also a numeric value. The operators used in these expressions are arithmetic operators like addition, subtraction, etc. Here are some arithmetic operators in Python:
 
 -Addition +
 -Subtraction -
 -Multiplication *
 -Division /
 -Power **
 -Modulus %
 -Floor division //
 
For eg:
 x, y = 10, 5
 print("Addition=",x+y)
 print("Subtraction=",x-y)
 print("Multiplication=",x*y)
 print("Division=",x/y)
 print("Power=",x**y)
 print("Modulus=",x%y)
 print("Floor division=",x//y)

output:
 Addition= 15
 Subtraction= 5
 Multiplication= 50
 Division= 2.0
 Power= 100000
 Modulus= 0
 Floor division= 2

3. Integral Expressions: These are the kind of expressions that produce only integer results after all computations and type conversions.

eg:
 a = 43
 b = 22.0

 c = a + int(b)
 print(c)

output: 65

4. Floating Expressions: These are the kind of expressions which produce floating point numbers as result after all computations and type conversions.

eg:
a = 13
b = 5

c = a / b
print(c)

output: 2.6

5. Relational Expressions: In these types of expressions, arithmetic expressions are written on both sides of relational operator (> , < , >= , <=). Those arithmetic expressions are evaluated first, and then compared as per relational operator and produce a boolean output in the end. These expressions are also called Boolean expressions.

eg:

x= 21
y = 13
z = 40
w = 37

p = (x - y) >= (z + w)
print(p)

output: False

6. Logical Expressions: These are kinds of expressions that result in either True or False. It basically specifies one or more conditions

Operator	   Syntax	 Functioning
 and	       P and Q	 It returns true if both P and Q are true otherwise returns false
 or	           P or Q	 It returns true if at least one of P and Q is true
 not           not P	 It returns true if condition P is false


for eg:

P = (10 == 9)
Q = (7 > 5)


R = P and Q
S = P or Q
T = not P

print(R)
print(S)
print(T)

output:
False
True
True6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

-- After running the above code the value of bacon will not change unless and until we will write it in proper manner.
if we go like this:
bacon=22
bacon=bacon + 1

output= 23

The value of bacon will be 23.

7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3

-- The value of 'spam' + 'spamspam' will be 'spamspamspam'
   The value of 'spam' * 3 will be 'spamspamspam'8. Why is eggs a valid variable name while 100 is invalid?

--Variable name:
 A variable name must start with a letter or the underscore character
 A variable name cannot start with a number
 A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
 Variable names are case-sensitive (age, Age and AGE are three different variables)
 
 According to the defination of how to define a variable in python 
eggs is a valid name since it is written in the way a variable has to be in python and 100 is invalid becase a variable name cannot start with a number.9. What three functions can be used to get the integer, floating-point number, or string version of a value?

---This can be done with type casting:
    int():constructs an integer number from an integer literal, a float literal, or a string literal.
    eg:
    x = int(1)   # x will be 1
    y = int(2.8) # y will be 2
    z = int("3") # z will be 3
    
    float():constructs a float number from an integer literal, a float literal or a string literal.
    eg:
    x = float(1)     # x will be 1.0
    y = float(2.8)   # y will be 2.8
    z = float("3")   # z will be 3.0
    w = float("4.2") # w will be 4.2
   
    str():constructs a string from a wide variety of data types, including strings, integer literals and float literals.
    eg:
    x = str("s1") # x will be 's1'
    y = str(2)    # y will be '2'
    z = str(3.0)  # z will be '3.0'10. Why does this expression cause an error? How can you fix it?
     'I have eaten ' + 99 + ' burritos.'

--The above expression will cause an error because one can do concatnation on string to string not on string to integer.
 This can be fixed by using a str() funtion.
 'I have eaten ' + str(99) + ' burritos.'
