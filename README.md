# Python for Beginners

<h2>Print hello world</h2>

<h2>Variable & Data Types</h2>

> Python has five standard data types:

- Numbers
- String
- List
- Tuple
- Dictionary
- Text Type: str
- Numeric Types: int, float, complex
- Sequence Types: list, tuple, range
- Mapping Type: dict
- Set Types: set, frozenset
- Boolean Type: bool
- Binary Types: bytes, bytearray, memoryview

<h2>Working With String</h2>

> Some method of String:

- upper()
- lower()
- isupper()
- islower()
- len(str)
- [] , index(str)
- replace(src,des)
- RegEx Functions:
  - findall()
  - search()
  - split()
  - sub()

<h2>Working With Number</h2>

> Some method of Number:

- str(num) : convert number to string
- abs()
- pow(num,pow)
- max(array_numbers)
- min(array_numbers)
- round(num)
- form math:
  - floor(num)
  - ceil(num)
  - sqrt(num)

<h2>Getting Input From Users</h2>

> use input() example: `name = input("Enter your name: ")`

<h2>Building a Basic Calculator</h2>

> Some method for Basic Calculator:

- int(str) convert to int
- float(str) convert to float

<h2>Mad Libs Game</h2>

<h2>Lists and List Function</h2>

> Some method for Basic Calculator:

- Access Item: [] example `list[1]`

  - Negative indexing : `list[-1]` return last item and so on

- Range of Indexes

  - You can specify a range of indexes by specifying where to start and where to end the range.<br>
    When specifying a range, the return value will be a new list with the specified items.
  - Example: `list[2:5]` return the second, third and forth item
  - By leaving out the start value, the range will start at the first item: example `list[:4]`
  - By leaving out the end value, the range will go on to the end of the list: example `list[2:]`

- Range of Negative Indexes

  - Specify negative indexes if you want to start the search from the end of the list:<br>
    This example returns the items from index -4 (included) to index -1 (excluded): `list[-4:-1]`

- Change Item Value

  - To change the value of a specific item, refer to the index number: `list[1]="change"`

- Loop Through a List

  - You can loop through the list items by using a for loop: `for x in list: print(x)`

- Check if Item Exists

  - To determine if a specified item is present in a list use the in keyword:<br>
    `if "apple" in list: print("yes, 'apple' is in the fruits list)`

- List Length

  - To determine how many items a list has, use the len() function: `print(len(list))`

- Add Items

  - To add an item to the end of the list, use the append() method: `list.append("orange")`
  - To add an item at the specified index, use the insert() method: `list.insert(1,"orange")`

- Remove Item

  - There are several methods to remove items from a list:<br>
    - The remove() method removes the specified item: `list.remove("banana")`
    - The pop() method removes the specified index, (or the last item if index is not specified): `list.pop()`
    - The del keyword removes the specified index: `del list[0]`
    - The del keyword can also delete the list completely: `del list`
    - The clear() method empties the list: `list.clear()`

- Copy a List

  - You cannot copy a list simply by typing list2 = list1, because: <br>
    list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
  - There are ways to make a copy, one way is to use the built-in List method copy().
    - Make a copy of a list with the copy() method: `copy_list = list.copy()`
  - Another way to make a copy is to use the built-in method list().
    - Make a copy of a list with the list() method: `copy_list = list(this_list)`

- Join Two Lists

  - There are several ways to join, or concatenate, two or more lists in Python.<br>
  - One of the easiest ways are by using the + operator: `list3 = list1 + list2`
  - Another way to join two lists are by appending all the items from list2 into list1, one by one:<br>
    - `for x in list2: list1.append(x)`
  - Or you can use the extend() method, which purpose is to add elements from one list to another list:
    - `list1.extend(list2)`

- The list() Constructor

  - It is also possible to use the list() constructor to make a new list.
    - Using the list() constructor to make a List: `this_list = list(("apple", "banana", "cherry"))`

- List Methods
  |Method | Description|
  |----------|-------------|
  |append() | Adds an element at the end of the list|
  |clear() | Removes all the elements from the list|
  |copy() | Returns a copy of the list|
  |count() | Returns the number of elements with the specified value|
  |extend() | Add the elements of a list (or any iterable), to the end of the current list|
  |index() | Returns the index of the first element with the specified value|
  |insert() | Adds an element at the specified position|
  |pop() | Removes the element at the specified position|
  |remove() | Removes the item with the specified value|
  |reverse() | Reverses the order of the list|
  |sort() | Sorts the list|

<h2>Tuples</h2>

- Tuple
  - A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
  - Create a Tuple: `this_tuple = ("apple", "banana", "cherry")`
- Access Tuple Items

  - You can access tuple items by referring to the index number, inside square brackets:
  - Print the second item in the tuple: `print(this_tuple[1])`
  - Negative Indexing
  - Range of Indexes
  - Range of Negative Indexes

- Change Tuple Values

  - Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
  - But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

- Loop Through a Tuple
- Check if Item Exists
- Tuple Length
- Add Items
- Join Two Tuples
  - To join two or more tuples you can use the + operator: `tuple3 = tuple1 + tuple2`
- The tuple() Constructor: It is also possible to use the `tuple()` constructor to make a tuple.

  - `this_tuple = tuple(("apple", "banana", "cherry"))`

- Tuple Methods
  |Method | Description|
  |----------|-------------|
  |count() |Returns the number of times a specified value occurs in a tuple|
  |index() | Searches the tuple for a specified value and returns the position of where it was found|

<h2>Functions</h2>

- Creating a Function: In Python a function is defined using the `def` keyword

  - `def my_function(): print("Hello from a function")`

- Calling a Function: To call a function, use the function name followed by parenthesis

  - `my_function()`

- Arguments

  - Information can be passed into functions as arguments.

- Parameters or Arguments?

  - The terms parameter and argument can be used for the same thing: information that are passed into a function.
  - From a function's perspective:
    - A parameter is the variable listed inside the parentheses in the function definition.
    - An argument is the value that is sent to the function when it is called.

- Number of Arguments
- Arbitrary Arguments, \*args

  - If you do not know how many arguments that will be passed into your function, add a \* before the parameter name in the function definition.
  - This way the function will receive a tuple of arguments, and can access the items accordingly:
  - If the number of arguments is unknown, add a \* before the parameter name:
    - `def my_function(*kids): print("The youngest child is " + kids[2])`

- Keyword Arguments

  - You can also send arguments with the key = value syntax.
  - This way the order of the arguments does not matter.

- Arbitrary Keyword Arguments, \*\*kwargs

  - If you do not know how many keyword arguments that will be passed into your function, add two asterisk: \*\* before the parameter name in the function definition.
  - This way the function will receive a dictionary of arguments, and can access the items accordingly

- Default Parameter Value

  - If we call the function without argument, it uses the default value:
    - `def my_function(country = "Norway"): print("I am from " + country)`

- Passing a List as an Argument

  - You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

- Return Values

  - To let a function return a value, use the return statement:

- The pass Statement

  - function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
    - `def my_function(): pass`

- Recursion
  - Python also accepts function recursion, which means a defined function can call itself.
  - Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

<h2>If ... Else</h2>

- Python Conditions and If statements
- Indentation
  - Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
- Elif
  - The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
- Else
  - The else keyword catches anything which isn't caught by the preceding conditions.
  - You can also have an else without the `elif`:
- And
  - The `and` keyword is a logical operator, and is used to combine conditional statements:
- Or
  - The `or` keyword is a logical operator, and is used to combine conditional statements:
- Nested If
  - You can have `if` statements inside `if` statements, this is called nested `if` statements.
- The pass Statement
  - `if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

<h2>Building a better Calculator</h2>

<h2>Dictionaries</h2>

- Dictionary
  - A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
- Accessing Items
  - You can access the items of a dictionary by referring to its key name, inside square brackets: `x = this_dict["model"]`
  - There is also a method called get() that will give you the same result: `this_dict.get("model")`
- Change Values
  - You can change the value of a specific item by referring to its key name:
- Loop Through a Dictionary
  - You can loop through a dictionary by using a for loop.
  - When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
  - Print all key names in the dictionary, one by one: `for x in this_dict: print(this_dict[x])`
  - You can also use the values() function to return values of a dictionary: `for x in this_dict.values(): print(this_dict[x])`
  - Loop through both keys and values, by using the items() function: `for x, y in this_dict.item(): print(x, y)`
- Check if Key Exists
  - To determine if a specified key is present in a dictionary use the in keyword: `if "model" in this_dict:`
- Dictionary Length
  - To determine how many items (key-value pairs) a dictionary has, use the `len()` method: `print(len(this_dict))`
- Adding Items
  - Adding an item to the dictionary is done by using a new index key and assigning a value to it: `this_dict["color"] = "red"`
- Removing Items
  - There are several methods to remove items from a dictionary:
    - The `pop()` method removes the item with the specified key name: `this_dict.pop(key)`
    - The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):`this_dict.popitem()`
    - The del keyword removes the item with the specified key name: `del this_dict[key]`
    - The clear() method empties the dictionary: `this_dict.clear()`
- Copy a Dictionary
  - You cannot copy a dictionary simply by typing `dict2 = dict1`, because: `dict2` will only be a reference to `dict1`, and changes made in `dict1` will automatically also be made in `dict2`.
  - There are ways to make a copy, one way is to use the built-in Dictionary method `copy()`: `my_dict = this_dict.copy()`
  - Another way to make a copy is to use the built-in method `dict()`: `my_dict = dict(this_dict)`
- Nested Dictionaries
  - A dictionary can also contain many dictionaries, this is called nested dictionaries.
  - Or, if you want to nest three dictionaries that already exists as dictionaries:
- The dict() Constructor
  - It is also possible to use the `dict()` constructor to make a new dictionary
- Dictionary Methods

| Method       | Description                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| clear()      | Removes all the elements from the dictionary                                                                |
| copy()       | Returns a copy of the dictionary                                                                            |
| fromkeys()   | Returns a dictionary with the specified keys and value                                                      |
| get()        | Returns the value of the specified key                                                                      |
| items()      | Returns a list containing a tuple for each key value pair                                                   |
| keys()       | Returns a list containing the dictionary's keys                                                             |
| pop()        | Removes the element with the specified key                                                                  |
| popitem()    | Removes the last inserted key-value pair                                                                    |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| update()     | Updates the dictionary with the specified key-value pairs                                                   |
| values()     | Returns a list of all the values in the dictionary                                                          |

<h2>While Loops</h2>

- Loops
  - `while` loops
  - `for` loops
- The while Loop
  - With the `while` loop we can execute a set of statements as long as a condition is true.
  - The `while` loop requires relevant variables to be ready
- The break Statement
  - With the `break` statement we can stop the loop even if the while condition is true
- The continue Statement
  - With the `continue` statement we can stop the current iteration, and continue with the next
- The else Statement
  - With the `else` statement we can run a block of code once when the condition no longer is true

<h2>Building a Guessing Game</h2>

<h2>For Loop</h2>

- For Loops
  - A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
  - This is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
  - With the `for` loop we can execute a set of statements, once for each item in a list, tuple, set etc.
  - The `for` loop does not require an indexing variable to set beforehand.
- Looping Through a String
  - Even strings are iterable objects, they contain a sequence of characters: `for x in "banana": print(x)`
- The break Statement
  - With the `break` statement we can stop the loop before it has looped through all the items
- The continue Statement
  - With the `continue` statement we can stop the current iteration of the loop, and continue with the next
- The range() Function
  - To loop through a set of code a specified number of times, we can use the `range()` function
  - The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
  - The `range()` function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`
- Else in For Loop
  - The `else` keyword in a `for` loop specifies a block of code to be executed when the loop is finished
- Nested Loops
  - A nested loop is a loop inside a loop.
  - The "inner loop" will be executed one time for each iteration of the "outer loop": `for x in adj: for y in fruits: print(x, y)`
- The pass Statement
  - `for` loops cannot be empty, but if you for some reason have a `for` loop with no content, put in the `pass` statement to avoid getting an error.

  <h2>Exponent Function</h2>

  <h2>2D Lists & Nested Loops</h2>

  <h2>Build a Translator</h2>

  <h2>Comments</h2>

  - Creating a Comment
    - Comments starts with a `#`, and Python will ignore them
  - Multi Line Comments
    - Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it.
      - `""" comment multi line in python """`
      - `''' comment multi line in python '''`

<h2>Try Except</h2>

- The `try` block lets you test a block of code for errors.
- The `except` block lets you handle the error.
- The `finally` block lets you execute code, regardless of the result of the try- and except blocks.
- Exception Handling
  - When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
  - These exceptions can be handled using the `try` statement
  - Since the try block raises an error, the except block will be executed.
  - Without the try block, the program will crash and raise an error
- Many Exceptions


  


