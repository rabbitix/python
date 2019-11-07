
'''
+ 	Addition 	x + y 	
- 	Subtraction 	x - y 	
* 	Multiplication 	x * y 	
/ 	Division 	x / y 	
% 	Modulus 	x % y 	
** 	Exponentiation 	x ** y 	
// 	Floor division 	x // y 	
'''

'''
== 	Equal 	x == y 	
!= 	Not equal 	x != y 	
> 	Greater than 	x > y 	
< 	Less than 	x < y 	
>= 	Greater than or equal to 	x >= y 	
<= 	Less than or equal to 	x <= y 	
'''

x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True


'''
and  	Returns True if both statements are true 	x < 5 and  x < 10 	
or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10) 	
'''
print(not False)  # Prints out True
print((not False) == (False))  # Prints out False

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


'''
is  	Returns true if both variables are the same object 	x is y 	
is not 	Returns true if both variables are not the same object 	x is not y 	
'''

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do another thing
    pass


'''
in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y 	

'''

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
else:
    pass

elif True:
    pass

# if - if elif else


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# range(start,stop,step)
range(1,30,3)
range(10,0,-1)
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"


# else block runs when loop over successfully
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))


# in this example else block will not run because for loop had been breaked!!

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
