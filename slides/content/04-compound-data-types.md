# Compound data types
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### Overview
- Data types that are compound of smaller pieces, example: a string is made up from smaller strings
 containing  a single character.
- Support similar methods, although each type has it's own unique qualities and will be effective in
 certain use cases (and not others).
- Types included are: string, tuple, list, dictionary, set.

---

# More fun with Strings!
<!-- .slide: data-background="img/string.jpg" -->

--
### Slicing
- Similar to `range` parameters
- Index with square brackets: `s[1]`
- Negative indexing gets elements from the end of list: `s[-1]`
- Slices:
  - Basic syntax is `s[start:end]`: `s[1:4]`
  - Slicing from the beginning of the string: `s[:5]`
  - Slicing until the end of the string: `s[3:]`
  - Negative indexes can also be used in slices: `s[-3:-1]`

--
### Examples

    s = 'hello world'

    # slicing (inclusive start, exclusive end)
    s[1:4]  # -> 'ell'

    # from start to index
    s[:4]  # -> 'hell'

    # from index to end
    s[3:]  # -> 'lo world'

--

    # can use negative indexes as well
    s[2:-2]  # -> 'llo wor'

    # jumps
    s[::2]  # -> 'hlowrd'
    s[1::2]  # -> 'el ol'

    # negative jumps
    s[::-1]  # -> 'dlrow olleh'

--
### + and *

    'hello ' + 'world'  # -> 'hello world'

    'hello ' * 3  # -> 'hello hello hello '

---

# Lists
<!-- .slide: data-background="img/list.jpg" -->
--
### Basics
- An ordered collection of values
- Create an empty list:

        >>> l = list()
        >>> type(l)
        list
        >>> l = []
        >>> type(l)
        list

--
### Modilfying

-   Appending values to the list:

        >>> l.append('apple')
        >>> l
        ['apple']
        >>> l.append('orange')
        >>> l
        ['apple', 'orange']

-   Creating a populated list:

        >>> l = ["orange", "apple", "strawberry", "banana", "apricot"]
        >>> l
        ['orange', 'apple', 'strawberry', 'banana', 'apricot']

--

-   Adding on a specific index:

        >>> l.insert(3, 'melon')
        >>> l
        ['orange', 'apple', 'strawberry', 'melon', 'banana', 'apricot', 'grapes']

-   Deleting an item on a specific index:

        >>> del l[0]
        >>> l
        ['apple', 'strawberry', 'melon', 'banana', 'apricot', 'grapes']

--

-   Popping an element (remove it and return it's value):

        >>> l.pop() # last element by default
        'grapes'
        >>> l
        ['apple', 'strawberry', 'melon', 'banana', 'apricot']
        >>>l.pop(0) # by index
        'apple'
        >>> l
        ['strawberry', 'melon', 'banana', 'apricot']

--
### More actions

- `lst[i] = v`: Change an element or slice by assigning to it
- `lst.extend(l)`: Add an iterable
- `lst.remove(v)`:remove a specific value

--

### Sequence operations on lists

-   All sequence operations are valid on lists:

        >>> l = ['orange', 'apple', 'strawberry', 'melon', 'banana', 'apricot', 'grapes']
        >>> len(l)
        7

-   For loops through the list:

        >>> for x in l:
        ...     print(x)
        ...
        orange
        apple
        strawberry
        banana
        apricot

--

-   Retrieving elements by index, negative index, and slicing:

        >>> l[0]
        'apple'
        >>> l[8]
        ...
        IndexError: list index out of range
        >>> l[-1]
        'grapes'
        >>> l[2:4]
        ['strawberry', 'melon']
        >>> [10,20,30,40][::-1]
        [40, 30, 20, 10]

--

-   The `in` operator scans through all elements and return `True` or `False`:

        >>> 'apple' in l
        True
        >>> 'basketball' in l
        False

-   Lists can be concatenated with `+` and multiplied by `*`:

        >>> [25,3,14] + [5,4] + [101, 2]
        [25, 3, 14, 5, 4, 101, 2]
        >>> ["foo", "bar"] * 4
        ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar']

--

### In-place list operations

-   The `.reverse()` method changes a list in-place, and returns `None`:

        >>> fruit = ["orange", "apple", "strawberry", "banana", "apricot"]
        >>> fruit.reverse()  # changes the list fruit!
        >>> fruit
        ['apricot', 'banana', 'strawberry', 'apple', 'orange']

--

-   The `.sort()` method sorts elements in-place, and returns `None`:

        >>> fruit = ["orange", "apple", "strawberry", "banana", "apricot"]
        >>> fruit.sort()  # changes the list fruit!
        >>> fruit
        ['apple', 'apricot', 'banana', 'orange', 'strawberry']
        >>> fruit.sort(reverse=True)
        >>> fruit
        ['strawberry', 'orange', 'banana', 'apricot', 'apple']

--

### Lists and Refereneces

When using the assignment operator (`=`) on a list, a reference is created to the original list:

    >>> l = [10,5,25,100,250,1,8]
    >>> l
    [10, 5, 25, 100, 250, 1, 8]
    >>> l2 = l
    >>> l2
    [10, 5, 25, 100, 250, 1, 8]
    >>> l.append("BOOM!")
    >>> l
    [10, 5, 25, 100, 250, 1, 8, 'BOOM!']
    >>> l2
    [10, 5, 25, 100, 250, 1, 8, 'BOOM!']

--

As demonstrated above, `l2` is not a copy of `l`, but a reference to the same list in python's memory.
To create a copy of the list, use the slicing operator (`[:]`) :

    >>> l3 = l[:]
    >>> l3.append(9876)
    >>> l3
    [10, 5, 25, 100, 250, 1, 8, 'BOOM!', 9876]
    l
    >>> [10, 5, 25, 100, 250, 1, 8, 'BOOM!']

--

Keep in mind this is a SHALLOW copy of l:

    >>> numbers = [10,20,30]
    >>> l = [numbers, "x", "y"]
    >>> l
    [[10, 20, 30], 'x', 'y']
    >>> l2 = l[:]
    >>> l2
    [[10, 20, 30], 'x', 'y']
    >>> l2.append("z")
    >>> l2
    [[10, 20, 30], 'x', 'y', 'z']
    >>> l
    [[10, 20, 30], 'x', 'y']
    >>> # BUT:
    >>> numbers.append(9999)
    >>> l
    [[10, 20, 30, 9999], 'x', 'y']
    >>> l2
    [[10, 20, 30, 9999], 'x', 'y', 'z']


(`copy.deepcopy` should be used to create a deep copy of lists)

--
###### Excercise #1
### Calculate Median

Create a program that accepts numbers from the user, until a blank line is entered,
and then prints the number of items, minimum, maximum, average and median of the numbers entered.
(The median is the value of the middle number after sorting them. In case of even items, return the average of the two middle items).

See example on the next slide ->

--
Example:

    > 10
    > 15
    > 20
    > -40
    > 90
    >

    Items: 5
    Min: -40
    Max: 90
    Avg: 19
    Median: 15

---

# Tuple
<!-- .slide: data-background="img/tulips.jpg" -->

--
### Overview
- **Immutable**
- Tuples are used for grouping ordered data
- Support indexing and slicing syntax
- Powerful assignment feature (packing/unpacking)
- Creation is faster than a list
- Can be hashed! (we'll talk about that soon)

--
### Creating a tuple
    >>> t = tuple()
    >>> type(t)
    tuple

    >>> t = (1, 2, 'hi')
    >>> type(t)
    tuple

    >>> t = 1, 2, 'hi' # be careful
    >>> type(t)
    tuple

    >>> t = tuple([1,2,'yo'])
    >>> t
    (1, 2, 'yo')

--

### Powerful assigments

    def f():
        x, y = 'hi', 'man'
        x, y = y, x # Awsome!
        return x,y

---

# Dictionary
<!-- .slide: data-background="img/dictionary.jpg" -->

--
### Basics
- A dictionary is a hash map:
  - It hashes the keys to lookup values
  - Keys must be immutable so that the hash doesn't change
- `dict()` and `{}` are empty dictionaries
- `d[k]` accesses the value mapped to `k`
- `d[k] = v` updates the value mapped to `k`

--
### Methods
- `len()`, `in`, and `del` work like lists
- `d.keys()` and `d.values()` return corresponding lists of the dict keys and values.
- `d.items()` produces a list of tuples `(k,v)`
- `d.get(k,x)` looks up the value of `k`. Returns `x` if `k not in d`
- `d[k] = x` creates a key or changes that existing key value
- `d.pop(k,x)` return and remove value at `k`. Returns `x` as default

--
### Switch Statement Replacement
- Python doesnt have a `switch(x)`, dictionaries do the job
- Replace long `if x = a: elif x = b: elif...` with a dictionary lookup

--
###### Excercise #2
### Letter Counter

Count the number of letters in a sentence.
Implement `letter_counter` and print its return value - each letter on a separate line
(see code on next slide).

--
Boilerplate code:

    def letter_counter(s):
        """Returns the count of letters in s.
        """
        # --- WRITE YOUR CODE HERE --- #

        # ---------------------------- #


    result = letter_counter("Hello world!!! HELLO!")
    print("First result:", result)
    expected = {'e': 2, 'd': 1, 'h': 2, 'l': 5, 'o': 3, 'r': 1, 'w': 1}
    assert result == expected


---

# Set
<!-- .slide: data-background="img/set.png" -->

--
### Basics
- No order, no duplicates
- Hash Set: elements must be immutable
- Empty set: `set()` not `{}` (empty dict)
- `{1, 'blah', 5, -1}`
- Can de-duplicate a list: `list(set(lst))`

--
### Methods
- `s.add(v)`: adds a value to set
- `s.remove(v)`: removes v. will raise an error if v not in s
- `s.discard(v)`: removes v. will not raise error
- `s.difference(s2)` or `s - s2`: elements in s but not s2
- `s.union(s2)` or `s | s2`: elements in s or s2
- `s.intersection(s2)` or `s & s2`: elements in s and s2
- `s.update(s2)` or `s = s | s2`: updates s with s2 values

--
###### Excercise #3
### Sets vs Lists

-   Create a program that Adds 10,000 distinct random numbers between 1 and 1,000,000 to a list
-   Generates 10,000 more random numbers between 1 and 1,000,000 and counts how many of them exists in the list.
-   Do the same thing with a set instead of a list. Which method is faster? Why?

--

-   To generate a random number use:

        import random
        print(random.randint(1, 1000))

-   Use `time.time()` to measure how much time this takes:

        import time
        print(time.time())


---

# More On Sequences
<!-- .slide: data-background="img/sequences.jpg" -->

--
## Builtins
- `len(x)`: gives the number of elements
- `sum(x)`: adds up elements
- `a in x`: checks presence
- `all(x)/any(x)`: return True is any/all in lst are True
- `max(x)/min(x)`: biggest/smallest element
- `reversed(x)`: iterator of elements in reverse order (doesn't work for sets, why?)
- `zip(x,x)`: list of tuples with one element from each list
- `sorted(x)`: returns new sorted list

--
### List Comprehensions
- Compile a list with a one-liner.
- `[expr for v in iter]`
- `[expr for v in iter if cond]`
- This:
```python
res = []
for v1, v2 in lst:
    if v1 > v2:
        res.append(v1 * v2)
```
- Becomes that:
```python
res = [v1 * v2 for v1, v2 in lst if v1 > v2]
```

--
### Nested List Comprehensions
- This:
```python
res = []
for y in lst2:
    inter = []
    for x in lst1:
        inter.append(x)
```
- Becomes that:
```python
[[x for x in lst1] for y in lst2]
```

--
### Dictionary Comprehensions
- Like lists but swap `[]` for `{}`
- This:
```python
d = dict()
for k, v in lst:
    d[k] = v
```
- Becomes that:
```python
{k: v for k,v in lst}
```

--
### Set Comprehensions
-   Like dictionaries but no `:`
-   This:

        s = set()
        for x in lst:
            s.add(x)

- Becomes that:

        {x for x in lst}


--
### Tuple Comprehensions?
```python
tup = (x for x in lst)
type(tup)
<class 'generator'>
```
- We'll cover generators later

--
###### Excercise #4
### Funny Reverse

Using list comprehension, `join()` and `split()`, create a function that does this:

    def funny(s):
        # === YOUR CODE HERE! ===

        # =======================
        pass


    assert funny("Foo bar") == "Oof Rab"
    assert funny("The quick brown fox") == "Eht Kciuq Nworb Xof"

Tips -->

--

`.split()` and `.join()` examples:

    'hello world'.split()  # -> ['hello', 'world']
    ' '.join(['hello', 'world'])  # -> 'hello world'
    '<br >'.join(['first line', 'second line'])  # -> 'first line<br >second line'

--
###### Excercise #5
### Sentence Statistics

Create a function that returns a list with the number of letters in each word in the provided sentence:

    def word_lengths(s):
        # ==== YOUR CODE HERE ===

        # =======================


    result = word_lengths("Contrary to popular belief Lorem Ipsum is not simply random text")
    print("Result:", result)
    assert result == [8, 2, 7, 6, 5, 5, 2, 3, 6, 6, 4]
    print("OK")


Continue >>

--

Now create a function that returns the length of the longest word in the provided sentence:

    def max_word_length(s):
        # ==== YOUR CODE HERE ===

        # =======================

    result = max_word_length("Contrary to popular belief Lorem Ipsum is not simply random text")
    print("Result:", result)
    assert result == 8
    print("OK")


