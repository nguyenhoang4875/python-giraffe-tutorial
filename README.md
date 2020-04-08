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
