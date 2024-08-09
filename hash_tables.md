# Hash Tables
(Source: Grokking Algorithms - Aditya Y. Bhargava; Chapter 5)

As a reminder, there’s a big difference between O(n) and O(log n) time!

You already know that binary search is darn fast.

What
you really need is a buddy who has all the names and prices memorized.
Then you don’t need to look up anything: you ask her, and she tells you
the answer instantly.

Your buddy Maggie can give you the price in O(1) time for any item, no
matter how big the book is. She’s even faster than binary search.

What a wonderful person! How do you get a “Maggie”?

You know two data structures so far: 
*arrays* and *lists* (I won’t talk about stacks because you can’t really “search” for something in a *stack*).

Each item in the *array* is really **two items**: one is the *name* of a kind of
produce and the other is the *price*. 

If you sort this *array* by *name*, you can run binary search on it to find the price of an item. So you can find items in **O(log n) time**. 

But you want to find items in **O(1) time**. That is,
you want to make a “Maggie.” That’s where *hash functions* come in.

## Hash functions

A *hash function* is a function where you put in a *string* and you get
back a *number*.
(String here means any kind of data—a sequence of bytes.)

Hash function “maps strings to numbers.” 

There are some requirements for a hash function:

- It needs to be consistent.

For example, suppose you put in “apple” and get back “4”. Every time you put in “apple”, 
you should get “4” back. Without this, your hash table won’t work.

- It should map different words to different numbers.

For example, a hash function is no good if it always returns “1” for any word you put
in. In the best case, every different word should map to a different number.

So a hash function maps strings to numbers. What is that good for?
Well, you can use it to make your “Maggie”!

Now you ask, “Hey, what’s the price of an avocado?” You don’t need to
search for it in the array. Just feed “avocado” into the hash function.

It tells you that the price is stored at *index* 4. And sure enough,
there it is.

The hash function tells you exactly where the price is stored, so you
don’t have to search at all! This works because:

- The hash function consistently maps a name to the same index. Every
time you put in “avocado”, you’ll get the same number back. 

So you can use it the first time to find where to store the price of an avocado,
and then you can use it to find where you stored that price.

- The hash function maps different strings to different indexes.

“Avocado” maps to index 4. “Milk” maps to index 0. Everything maps
to a different slot in the array where you can store its price.

- The hash function knows how big your array is and only returns valid
indexes.

So if your array is 5 items, the hash function doesn’t return 100… 
that wouldn’t be a valid index in the array.

You just built a “Maggie”! Put a **hash function** and an **array** together,
and you get a *data structure* called a **hash table**.

A hash table is the *first data structure you’ll learn that has some extra logic behind it*.

*Arrays* and *lists* **map straight to memory, but hash tables are smarter**. 
They *use a hash function to intelligently figure out where to store elements*.

Hash tables are probably the most useful complex data structure you’ll learn. 
They’re also known as *hash maps, maps, **dictionaries** and associative arrays*.

And hash tables are fast! 
You can get an item from an array instantly. 
And hash tables use an array to store the data, so they’re equally fast.

You’ll probably never have to implement hash tables yourself. 
Any good language will have an implementation for hash tables. 
Python has hash tables; they’re called **dictionaries**. 

You can make a new hash table using the *dict function*.

A **hash table** has **keys** and **values**. In the book hash, the names of
produce are the keys, and their prices are the values. 
*A hash table maps keys to values*.

## Use cases

### Preventing duplicate entries

Each time someone new comes in to vote, you have to scan this giant
list to see if they’ve already voted. But there’s a better way: use a hash!

First, make a hash to keep track of the people who have voted:

    voted = {}

When someone new comes in to vote, check if they’re already in the hash:

    value = voted.get(“tom”)

The get function returns the value if “tom” is in the hash table.
Otherwise, it returns None. You can use this to check if someone has already voted!

Here’s the code:

    voted = {}

    def check_voter(name):
        if voted.get(name):
            print “kick them out"
        else:
            voted[name] = True
            print “let them vote!”

Remember, if you were storing these names in a *list of people* who have
voted, this function would eventually become *really slow*, because 
**it would have to run a simple search over the entire list**.

But *you’re storing their names in a hash table instead*, and a **hash table instantly tells you whether this person’s name is in the hash table or not**. Checking for duplicates is very fast with a hash table.

### Using hash tables as a cache

One final use case: *caching*.

If you work on a website, you may have heard of caching before as a good thing to do.

Here’s the idea. Suppose you visit facebook.com:

1. You make a request to Facebook’s server.
2. The server thinks for a second and comes up with
the web page to send to you.
3. You get a web page.

This is how caching works: websites remember the data instead of recalculating it.

This is called caching. It has two advantages:

- You get the web page a lot faster, just like when you memorized the
distance from Earth to the Moon. The next time your niece asks you,
you won’t have to Google it. You can answer instantly.

- Facebook has to do less work.

Caching is a common way to make things faster. All big websites use
caching. And **that data is cached in a hash**!

Facebook isn’t just caching the home page. It’s also caching the About
page, the Contact page, the Terms and Conditions page, and a lot more.
So it needs a mapping from page URL to page data.

When you visit a page on Facebook, it first checks whether the page is
stored in the hash.

Here it is in code:
 
    cache = {}

    def get_page(url):
        if cache.get(url):
            return cache[url] Returns cached data
        else:
            data = get_data_from_server(url)
            cache[url] = data Saves this data in your cache first
            return data

Here, you make the server do work only if the URL isn’t in the cache.
Before you return the data, though, you save it in the cache. The next
time someone requests this URL, you can send the data from the cache
instead of making the server do the work.

## Recap

To recap, hashes are good for:

- Modeling relationships from one thing to another thing
- Filtering out duplicates
- Caching/memorizing data instead of making your server do work

## Collisions

To understand the performance of hash tables, you first need to understand what
collisions are. The next two sections cover *collisions* and *performance*.

First, I’ve been telling you a *white lie*. I told you that a hash function
always maps different keys to different slots in the array.

In reality, *it’s almost impossible to write a hash function that does this*.

This is called a *collision*: **two keys have been assigned the same slot**. This is a problem.

If you store the price of avocados at that slot, you’ll overwrite the price
of apples. Then the next time someone asks for the price of apples, they will get the price of avocados instead! Collisions are bad, and you need to work around them. 

There are many different ways to deal with collisions. 
The simplest one is this: **if multiple keys map to the same slot, start a linked list at that slot**.

There are two lessons here:

- Your hash function is really important. 

Your hash function mapped all the keys to a single slot. 
Ideally, your hash function would map keys evenly all over the hash.

- If those linked lists get long, it slows down your hash table a lot. 
But they won’t get long if you use a good hash function!

Hash functions are important. A good hash function will give you very
few collisions. So how do you pick a good hash function? That’s coming
up in the next section!

## Performance

You wanted to build something that would give you the prices for produce instantly. 
Well, hash tables are really fast.

In the average case, **hash tables take O(1) for everything**. 

**O(1) is called constant time**. 

You haven’t seen constant time before. **It doesn’t mean instant**.

It means the time taken will stay the same, regardless of how
big the hash table is. 

- For example, you know that **simple search takes linear time**.
- Binary search is faster — **it takes log time**.
- **Looking something up in a hash table takes constant time**.

See how it’s a flat line? That means it doesn’t matter whether your hash
table has 1 element or 1 billion elements—getting something out of a hash table
will take the same amount of time.

Actually, you’ve seenconstant time before. 
Getting an item out of an array takes constant time. 
It doesn’t matter how big your array is; it takes the same amount of time to get an element. 

In the average case, hash tables are really fast.
In the worst case, a hash table takes O(n)—linear time—for everything,
which is really slow. 

Let’s compare hash tables to arrays and lists.

Look at the average case for hash tables. Hash tables are as fast as arrays
at searching (getting a value at an index). And they’re as fast as linked
lists at inserts and deletes. It’s the best of both worlds! 

But in the worst case, hash tables are slow at all of those. 
So it’s important that you don’t hit worst-case performance with hash tables. 

And to do that, you need to *avoid collisions*. To avoid collisions, you need:

- A low load factor
- A good hash function

Before you start this next section, know that this isn’t required reading. I’m
going to talk about how to implement a hash table, but you’ll never have
to do that yourself. Whatever programming language you use will have an
implementation of hash tables built in. You can use the built-in hash table
and assume it will have good performance. The next section gives you a
peek under the hood.

### Load factor

Load factor measures how many empty slots remain in your hash table.

Suppose you need to store the price of 100 produce items in your hash
table, and your hash table has 100 slots. In the best case, each item will
get its own slot.

This hash table has a load factor of 1. What if your hash table has only
50 slots? Then it has a load factor of 2.

Having a load factor greater than 1 means you have more items than slots in your array.

Once the load factor starts to grow, you need to add more slots to your
hash table. This is called *resizing*.

With a lower load factor, you’ll have fewer collisions, and your table will perform better. A
good rule of thumb is, resize when your load factor is greater than 0.7.

Resizing is expensive, and you don’t want to resize too
often. But averaged out, hash tables take O(1) even with resizing.

### A good hash function

A good hash function distributes values in the array evenly.

A bad hash function groups values together and produces a lot of
collisions.

## Recap

You’ll almost never have to implement a hash table yourself. The
programming language you use should provide an implementation for
you. You can use Python’s hash tables and assume that you’ll get the
average case performance: constant time.

Hash tables are a powerful data structure because they’re so fast and
they let you model data in a different way. 

You might soon find that you’re using them all the time:

- You can make a hash table by combining a hash function with an array.
- Collisions are bad. You need a hash function that minimizes collisions.
- Hash tables have really fast search, insert, and delete.
- Hash tables are good for modeling relationships from one item to another item.
- Once your load factor is greater than .07, it’s time to resize your hash table.
- Hash tables are used for caching data (for example, with a web server).
- Hash tables are great for catching duplicates.






