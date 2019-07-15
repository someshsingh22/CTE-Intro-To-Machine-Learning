%precision 2    #To set floating point precision(places after decimal)
import csv
import numpy as np
import time

with open('numberlist1.csv') as csvfile:
    number_list = list(csv.DictReader(csvfile))

##Part 1
###Here you write your function to check if a given no. is prime or not:

def findtype(inputnumber): 
    '''Here you write the code(for loop) for checking if inputnumber which is taken as argument to 
       this function is prime or composite or not 
                                                '''
    #if inputnumber is prime return 'prime'

    #else if inputnumber is return 'composite'

    #else return 'NA'

    
'''Instructions:
   a.Now that you have written your function, iterate through the number_list list that is read from the csv file and use your function to return a list with
     name numtype_list and it should contain the number type('prime','composite','nan') of the corresponding numbers in number_list
     For example: 
     number_list = [2,3,4,5,6,'a','',5.3,6.7]
     numtype_list = ['prime','prime','composite','prime','composite','NA','NA','NA','NA']
   b.You might have to check if the number is an integer (Hint: Google a built-in function or write your own)
   c.numtype_list will be a python list rather than storing output in text file numpy offers .npy format to store numpy arrays
     reading .npy in python is blazing fast compared to .txt and .csv. So convert numtype_list to numpy array and store it in disk
     in .npy format with the name ''submit_assign_1_0.npy''.
   d.Measure time of execution of your loop with time module(Already imported)[Read documentation online how to use it].See the time
     of exececution for yourself. Could you be faster? Any solution with correct output is accepted as correct.
   e.The code that is fastest gets a treat.
   f.The code that is shortest(more Pythonic) also gets a treat.
'''

'''Lists can be so large that they cant be stored in the memory, suppose the list goes as [2,3,4,5,6....,a_very_large_number]. 
   Suppose this is a very large list to be stored on disk and so we cant loop through it in python.
   In our software program we need to find the sum of all the primes such that.
   We want prime numbers depending on number of customer logging into our website.
   Customer logins can end up being very large(big website). No way to estimate very_large_number.
   And every time a user logs in we need to get the next sum of prime.
   Because we need to record sum of primes at the end of the year.
   Here is the trick we dont want to store a very very big list whose size we cant estimate, what a wastage of memory.
   So why dont add primes as a customer logs in ie, "On the Fly". Meaning lets not store the primes at all, rather generate 
   numbers as a new customer logs in, and add them to existing sum.
   But how do we do it?
   Whats the minimum requirement to get an incremental number? The previous number.
   Whats the minimum requirement to get an incremental sum? The previous some.
   So. We just need to store two things in-order to get the next two things.
   So we virtually store nothing. And do exactly the number of operations required no more no less.
   But how do we implement it?
   A function, probably? No, a function is loses all its memory(I mean english language memory not computer memory) once it hits return statement, all its variables are lost.
   But what if function had some (english language memory), what if we could call the function over and over again and it remembers
   what happened in the previous call? Oh yeah. This should do it.
   Someone sitting late night sipping coffee surely came up with this idea, which is generally called coroutines
   Python has it implemented for you called "yield" statement.
   An yield statement makes a function generators. [Read more on Generators and Iterators]
   
   Below are some implementations which make you familiar with yield statement, iterators, generators.
'''
#First is range()
k_range = range(0, 10, 2)
print(type(k)) 
for elems in k:
    print(elems) #Now k is not a list, it generates the numbers only when queried.
#Range is an iterable not an iterator.
#But
k_iterator = iter(k) 
print(type(range(k)))
#Iterator is just a class with some methods(Read Docs),an iterator has the most useful is the next() function.[Thats the only thing we use]
next(k_range) #error
next(k_iter)
next(k_iter)
next(k_iter) 
#Iterators get exhausted. They are of one-time use. But Iterables are reusable to make iterators again.
#Lists also are iterables. Calling iter([1,2,3]) makes it an iterator
#A for loop implicitly converts [1,2,3] or range(0,10,2) to an interator by calling iter() on it.
#So all Iterators are Lazy, they give out numbers only when called next() on them
#But Iterables such as range(0,10,2) are lazy iterables. These dont store anything before hand. But Iterables such as lists are not
#Lazy iterables they consume space in memory.


#Now all generators are iterators but not vice-versa. Iterators have more flexibility than generators.
#But mostly in ML we probably dont need that distinction. You can look up on the web if interested.

generator1 = (x*x for x in range(10)) #This a generator expression.To do simple things.
type(generator1)
next(generator1)
next(generator1)
next(generator1)
next(generator1)
next(generator1) #Also get exhausted. And also are lazy.
list1 = [x*x for x in range(10)]   #List comprehension style list
#So lets get back to yield statement
def yield_me_even_sums(): #To get more complex generators we can use generator functions.
    sum = 0
    for i in range(30):
        if i%2 == 0:
            sum = sum + i
            yield sum
        else:
            yield sum
generator2 = yield_me_evens()
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
'''Note that we are not calling a function anymore, yield statement converts the function into generator
   a.Visualizing the flow.
     We first make a generator object by calling the function yield_me_evens() and assigning it to generator2
     When we call next on it. for loop is entered, until yield statement is hit, and corresponding is returned value is returned.
     And we are out of the function. Next time we call next(), the process is continued from yield statement and stops when loop 
     Again hits the yield statement and the value next to yield is put out. And On and on.'''

'''So here is your task. Write a function that returns sum of primes in imaginary list [2,3,4,5,6,7...,infinite], only as an when a customer logs in.
   Calling next() on customer_prime_sum for the first time must return 2
   Calling next() on customer_prime_sum for the second time must return 5
   Calling next() on customer_prime_sum for the third time must return 5
   Calling next() on customer_prime_sum for the infinite(th) time must return sum of all primes until inifinte+1.'''
def customer_login_func(*args, **kwargs):
    '''Your code here , Hint: you can call a function inside a function, 
        ie you can use previous prime checking function'''

    
customer_prime_sum = customer_login_func() #Add arguments if any.
    



#Part 3-Basic Matrix manipulations
"""
NumPy is one of the best ways to manipulate and do matrix operations in python.
Now in this part you'll be given an array of 10 3x3 arrays and then when given a new 3x3 array
you'd need to the find one of those 10 previous which is closest to this new array.
Images can be represented as arrays with each pixel having an element value in array.
For example in grayscale images let 0 be black pixel, 1 be a white pixel and any value between will be gray.
(0.3 would be darker than 0.6 likewise)
"""
import numpy as np#importing NumPy module with name as np

#Initialising an array :

blackarray=np.array([[0,0,0],
	                 [0,0,0],
	                 [0,0,0]])
#this would reperesent an all black image.
print(blackarray)
#we are only representing images as arrays for undeerstanding purposes only,
# numpy doesn't show these arrays as images. There are other image libraries for that purpose.

whitedotarray=np.array([[0,0,0],
	                    [0,1,0],
	                    [0,0,0]])
#Now this would be an image with a single white dot in centre of other 8 black pixels around it.

whitedotarray=np.array([[0,0,0],
	                    [0,0.9,0],
	                    [0,0,0]])
#This would similarly be a slightly faint white dot than before.


whitelinearray=np.array([[0,0,0],
	                     [1,1,1],
	                     [0,0,0]])
#Similarly this would represent a single white horizontal line on black background.

imgs_array=np.array([[0,0,0],
	                 [0,0,0],
	                 [0,0,0]],

	                [[1,1,1],
	                 [1,1,1],
	                 [1,1,1]],

	                [[0,0,0],
	                 [0,1,0],
	                 [0,0,0]],

	                [[1,1,1],
	                 [1,0,1],
	                 [1,1,1]],

	                [[0,1,0],
	                 [0,1,0],
	                 [0,1,0]],

	                [[0,0,0],
	                 [1,1,1],
	                 [0,0,0]],

	                [[1,0,0],
	                 [0,1,0],
	                 [0,0,1]],

	                [[1,1,1],
	                 [0,0,0],
	                 [1,1,1]],

	                [[1,0,1],
	                 [1,0,1],
	                 [1,0,1]],

	                [[0,0,1],
	                 [0,1,0],
	                 [1,0,0]])

#This is the data you've been provided with. These are 10 different arrays, make sure they are iterable in a
#for loop, coz you would need to compare every new array with each one of these 10 arrays.

query_arrays=np.array([[0.03,0.06,0.1],
	                    [0.1,0.98,0.2],
	                    [0.04,0.1,0.02]],

	                   [[0.96,0.03,0.2],
	                    [0.06,0.91,0.02],
	                    [0.03,0.3,0.8]],

	                   [[0.67,0.15,0.93],
	                    [0.76,0.12,0.89],
	                    [0.68,0.03,0.83]],

	                   [[0.92,0.1,0.92],
	                    [0.12,0.95,0.12],
	                    [0.99,0.06,0.99]])
#These are your query arrays which you need to compare with your data to classify them as either of the 10 given to you.
"""
for example let's have a look at the first query array
[[0.03,0.06,0.1],                                       [[0,0,0],
 [0.1,0.98,0.2],       --> looks very similar to -->     [0,1,0],
 [0.04,0.1,0.02]]                                        [0,0,0]]

 But how would you compare 2 arrays, to find if they are similar?
 You could find an error or difference between those arrays and then the one with the least error is the most similar.
 So lets subtract the arrays to find difference_array :

[[0.03,0.06,0.1],                          
 [0.1,-0.02,0.2],       
 [0.04,0.1,0.02]]

 But while comparing, + or - shouldn't affect, so to find error you can add all the Absolute values of elements.
 Absolute error = 0.03+0.06+0.1+0.1+0.02+0.2+0.04+0.1+0.02
 Now you can find error with each pair in a for loop,
 and classify as the one with least error. 
 Another way instead of taking absolute of elements of the difference array, you could just square them and add them, to find squared error.
"""
query_errors=[0,0,0,0,0,0,0,0,0,0]
for i in 4:
	for j in 10:
		#find error between query_arrays[i] and imgs_array[j]
		#query_errors[j]= error
    #argmin will give you the the argument of the least one of 10 errors for a particular query_array 'i'
    #search more about argmax and argmin	
    #print argmin value, ie. which one of the 10 img arrays is most similar to i'th query array.

"""
Machine learning is about learning the underlying structure in data, recognising patterns in your data.
This algorithm is an called k-nearest neighbours algorithm, as you are finding nearest neighbours or similar arrays by just comparing them
"""
#COMPLETE the above assignment
