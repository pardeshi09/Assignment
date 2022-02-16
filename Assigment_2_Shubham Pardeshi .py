#!/usr/bin/env python
# coding: utf-8
1.What are the two values of the Boolean data type? How do you write them?


0 and 1 are the two values of the Boolean data type.
For 0 we have False and for True we have 1.2. What are the three different types of Boolean operators?

Bollean operations are simple arithmetic of True and False values.These values can be manipulated by the use of Boolean operators which include AND,OR,and NOT.
3. Make a list of each Boolean operator's truth tables .

    A     B   A and B   A or C  Not A
  True  True   True      True   False
  True  False  False     True   True
  False True   False     True
  False False  False     False4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
output: False

not (5 > 4)
output:False

(5 > 4) or (3 == 5)
output:True

not ((5 > 4) or (3 == 5))
output:False

(True and True) and (True == False)
output:False

(not False) or (not True)
output:True
5. What are the six comparison operators?

Operator	Name	                  Example	
 ==	       Equal	                  x == y	
 !=	       Not equal	              x != y	
 >	       Greater than               x > y	
 <	       Less than	              x < y	
 >=	       Greater than or equal to	  x >= y	
 <=	       Less than or equal to	  x <= y6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

=,is an Assignment operator and is used to assign the value on the right to the variable on the left.

for eg.
a = 10;
b = 20;
ch = 'y';

==,is an relation/comparison operator used to compare value of both left and right operants.

for eg:
5==5

This will return true.


7.Identify the three blocks in this code:

spam = 0
if spam == 10:   #block number 1 
print('eggs')  
if spam > 5:     #block number 2
print('bacon')  
else:            #block number 3
print('ham')    
print('spam')
print('spam')
##code with proper intendation

spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')

output:
ham
spam
spam8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam=int(input())

if spam==1:
    print('Hello')
    
elif spam==2:
    print('Howdy')
    
else:
    print('Greetings!')

output:
3
Greetings!9.If your programme is stuck in an endless loop, what keys you’ll press?

I will press the 'intrrupt the kernel' key exactly next to 'run' key in jupyter notebook. 
10. How can you tell the difference between break and continue?

break statement:
The break statement is used to terminate the loop or statement in which it is present. After that, the control will pass to the statements that are present after the break statement, if available. If the break statement is present in the nested loop, then it terminates only those loops which contains break statement.

for eg:

list = ['Shubham', 'Ajinkya', 'Manthan', 'Yadhu', 'Aatish', 'Kunal']
i = 0

while True:
    print(list[i])
    if list[i] == 'Kunal':
        print('Found the name Kunal')
        break
        print('After break statement')
    i += 1

print('Exit while loop')

output:
Shubham
Ajinkya
Manthan
Yadhu
Aatish
Kunal
Found the name Kunal
Exit while loop



continue statement:
When the continue statement is executed in the loop structure, it does not exit the loop structure, but immediately ends the current loop and starts the next loop again, that is, it skips all statements in the loop body after the continue statement and continues the next loop.

eg:
i = 0
while i <= 10:    
    if i == 7:
        i += 1
        continue  
    print("The Number is  :" , i)
    i += 1
    
output:
The Number is  : 0
The Number is  : 1
The Number is  : 2
The Number is  : 3
The Number is  : 4
The Number is  : 5
The Number is  : 6
The Number is  : 8
The Number is  : 9
The Number is  : 10

The coclusion is that the main difference between continue and break statement is that continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop. As the name suggests the continue statement forces the loop to continue or execute the next iteration.



11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
There is no key difference between  range(10), range(0, 10), and range(0, 10, 1).
All of these commands throws same output i.e:
for i in range(10):
    print(i)
   
output:
0
1
2
3
4
5
6
7
8
9
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print(i)
    
output:
1
2
3
4
5
6
7
8
9
10


i=1
while i<11:
    print(i)
    i=i+1
    
output:
1
2
3
4
5
6
7
8
9
10
13.If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

This function can be called with spam.bacon().  as folows:
    import spam
    spam.bacon()