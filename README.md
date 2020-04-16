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
  - ` def my_function(): print("Hello from a function")`

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
- Arbitrary Arguments, *args
  - If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
  - This way the function will receive a tuple of arguments, and can access the items accordingly:
  - If the number of arguments is unknown, add a * before the parameter name: 
    - `def my_function(*kids): print("The youngest child is " + kids[2])`

- Keyword Arguments
  - You can also send arguments with the key = value syntax.
  - This way the order of the arguments does not matter.

- Arbitrary Keyword Arguments, **kwargs
  - If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
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




