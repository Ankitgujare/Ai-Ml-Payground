"""
 Lamda functions are aslo knowns as one Liner function
 or annonymous fun

Syntax
lamda    a,b:  Expression
Keyword  para   a+b
Example

lamda a,b=a+b/2

lamda fun returns an Expression which we can store in variables
Like

x=lamda a,b=a+b/2

we use lamda functions for handling simple tasks
and pass it to higher Order functions that we will see
In future


Lets practice few Questions On Lamda fun
🟢 Easy Level

Q1. Create a lambda function that takes a number and returns the number plus 5.

Q2. Create a lambda function that takes two numbers and returns their sum.

Q3. Create a lambda function that takes a number and returns its square.

Q4. Create a lambda function that checks whether a number is even or odd.

Q5. Create a lambda function that takes a number and returns its cube.

Q6. Create a lambda function that takes a string and returns its length.

Q7. Create a lambda function that takes two numbers and returns the larger number.

🟡 Medium Level

Q8. Use a lambda function with map() to add 2 to each element in a list.

Q9. Use a lambda function with map() to convert a list of numbers into their squares.

Q10. Use a lambda function with filter() to extract even numbers from a list.

Q11. Use a lambda function with filter() to extract numbers greater than 50 from a list.

Q12. Use a lambda function with sorted() to sort a list of numbers in ascending order.

Q13. Use a lambda function with sorted() to sort a list of tuples based on the second element.

Q14. Use a lambda function with map() to convert all strings in a list to uppercase.

Q15. Use a lambda function with filter() to extract strings whose length is greater than 5.

 """

xbyFive = lambda a: a + 5

# let's pass the value to the lamda function
ans = xbyFive(100)
print("Answer is", ans)



addTwo=lambda a,b:a+b
print("Add two is", ans)


ans=addTwo(10,20)

calsqrt=lambda x:(x*x)
ans=calsqrt(4)
print("Square of n is ", ans)


evenOdd=lambda n:"Even" if n%2==0 else "Odd"




cube=lambda n:(n*n*n)
ans=cube(2)
print("Cube of n is ", ans)

callength=lambda str:len(str)
ans=callength("Hellow")



