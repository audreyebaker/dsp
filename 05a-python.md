# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are both sequences of values of any type that can be indexed, sliced, and iterated over. The main difference between the two is that lists are mutable whereas tuples are immutable. 

Tuples work well as keys in dictionaries because they are immutable and therefore do not risk creating complications with hash values in the same way that a list might if changed after assigned as the keys in a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets both contain sequences of values of any type. Lists can be indexed, sliced, and iterated over, whereas sets cannot. Lists are also ordered whereas sets are not. Sets, on the other hand, include only unique values while lists may include duplicates.

Sets are better for finding an element because you do not have to iterate over each element, as you do in a list. Instead, sets use the hash value to check if an element is included.


---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is an anonymous function that can be used only where it is called/defined.

Example: sorted(x, key = lambda x:x\[0])

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a substitute for lambda, map, and filter functions that use a syntax that mimics the mathematical notation for working with sets. 

Examples below using the following list
numbers = \[1, 1, 2, 3]

### Doubles
[Map]
doubles = map(lambda x: x \times 2, numbers)
print(doubles)
\[2, 2, 4, 6]

[List Comprehension]
doubles = \[(x \times 2) for x in numbers]
print(doubles)
\[2, 2, 4, 6]

[Set Comprehension]
doubles = {(x \times 2) for x in numbers}
print(doubles)
{2, 2, 4, 6}

### Evens 

[Filter]
evens = filter(lambda x: x%2==0, numbers)
print(evens)
\[2]

[Set Comprehension]
evens = \[x in numbers if (x%2==0)]
print(evens)
\[2]

[List Comprehension]
evens = {x in numbers if (x%2==0)}
print(evens)
{2}

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





