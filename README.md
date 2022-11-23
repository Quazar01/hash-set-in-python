# Mini-project report

Members: Sami Alabed
Program: Software Technology  
Course: 1DV501  
Date of submission: 2022-11-24

## Introduction

This mini-project deals with implementing hash-set and binary search trees data structers.
It is formed of three main tasks:

First, getting the count of unique words of two text files using python's sets, and getting the most 10 frequent words in the file using dictionaries.

Second, creating the hash set structure and its functions to put and distribute the words in it, and creating the binary search tree map with its functions to distribute the words in a way that makes it easier to search, fetch, add or remove a word.

Third, Implementing those those data structuers the previousely mentioned two text files and compare the results with the results of the first part.

## Part 1: Count unique words 1

The two text files in question here are `life_of_brian` and `swedish_news_2020`

- For `life_of_brian` the result was `2004` unique words out of `10761` total count of words.
- For `swedish_news_2020` the result was `412587` unique words out of `15103923` total count of words.

```python:
		# Sort the dict by it's value in reverse
	sorted_list = sorted(words_dict.items(),
							key=lambda x: x[1], reverse=True)

	# Get the firt 10 key-value pairs from the list
	for i in range(10):
		k = sorted_list[i][0]
		v = sorted_list[i][1]

		# Assign the key and the value to the most_freq_words dict.
		most_freq_words[k] = v
```

- While iterating through the words list the program adds each word as the key into the dictionary, and the value of that key is (1), but if the word already exists in the dictionary, then it increases its value by one.
  In this way we got each word and its frequency in the dictionary. That dictionary is sorted in post-order by its values and inserted the top 10 words and their values into another dictionary.

  - Top 10 most frequented words for `life of brian`:
    _ brian: 368
    _ crowd: 161
    _ centurion: 121
    _ mother: 104
    _ right: 99
    _ crucifixion: 78
    _ pilate: 68
    _ pontius: 64
    _ don't: 59
    _ rogers: 52

  - Top 10 most frequented words for `swedish news 2020`:
    - under: 54018
    - säger: 47539
    - efter: 44058
    - kommer: 42839
    - eller: 32064
    - också: 30472
    - sedan: 30375
    - andra: 28043
    - finns: 27576
    - många: 26810

## Part 2: Implementing data structures

- The BST is a linked nodes and the Hash Set consists of buckets where each bucket consists of lists.
  Basically part 2 consists of building the functions of those two data structures.

- For the `add` function to work we need first to build the `hash` and the `rehash` functions first.
  So.. for the `hash` fucntion, we get the index of each letter in the word, and raise a prime number `31` to the power of that index, then multiply the result by the ASCII value of the letter. The hash value is the sum of results of all the letters in the word.

```python
        # djb2 is faster than multiplying the letter
        # with the constant to the power of the letter's index.
        # 5381 is found the best prime number for this algorithm.
        hash_djb2 = 5381
        # hash_value = 0
        for letter in word:
            # djb2 hash function.
            # Found on: https://python.algorithms-library.com/hashes/djb2
            hash_djb2 = ((hash_djb2 * (2**5)) + hash_djb2) + ord(letter)

        return hash_djb2

```

- The `rehash` gets the size of the set doubled then makes a copy of the existing set to empty it, then it creates empty buckets according to the new size. Now it takes each element in the buckets of the copied set and run it through the `hash` function to determine in wich bucket the element is gonna be put in.

```python
    def rehash(self):
        # Doubles size of bucket list
        self.size *= 2
        copy_set = self.buckets.copy()
        self.buckets.clear()
        self.buckets = [[] for i in range(self.size)]
        # Filling the enlarged set with the elements from
        # the copied list.
        for bucket in copy_set:
            for element in bucket:
                # self.add(element)
                hash_value = self.get_hash(element)
                bucket_num = hash_value % self.size

                if element not in self.buckets[bucket_num]:
                    self.buckets[bucket_num].append(element)
```

- Now the `add` request the hash value of the word from `hash` and take the modulus of it by the size of the bucket set to determine the bucket number to put the word in, then simply appending the word to the specified bucket/list if the word doesn't already exist in it. Then it increases the total number of elements/words added by one.

```python
      def add(self, word):

        hash_value = self.get_hash(word)
        # Get which bucket the word would be put in.
        bucket_num = hash_value % self.size

        if word not in self.buckets[bucket_num]:
            self.buckets[bucket_num].append(word)
            self.num_of_elements += 1

        if self.num_of_elements == self.size:
            self.rehash()
```

\*\* By runing the `hash_main.py` two results appear to be different from the inteded output:

- The order of the names in 'to_string()' and the 'zero bucket ratio: ', I think the difference is due to a different hashing functions applied.
- The program got 'zero bucket ratio: 0.31' which is 0.07 less than the intended result, which indicates that the hash function applied here is slightly better in terms of distributing the elements.

* The `put` function in BstMap() takes a key and value,

- it first checks if the node is empty and insert the key and the value if so,
- then it checks if the node's key/word is the same as the passed key and override its value if so,
- then, it checks if the passed key is less than the node's key
  - it checks on the existens of the left node and add the passed values into that node if so,
  - otherwise it access left node and call for the put function to insert the passed values hence
    recursion.
- Repeat for the right side of the tree.

```python
    def put(self, key, value):

        if self.key is None:
            self.key = key
            self.value = value

        # Override existing key.
        if self.key == key:
            self.value += 1

        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value, None, None)

            else:

                self.left.put(key, value)

        else:
            if self.right is None:
                self.right = Node(key, value, None, None)

            else:
                self.right.put(key, value)
```

- The `max_depth` function starts by decalring assigning the depth of the right side and the left side as 1,we'll get to why 1 shortly.

* First, it checks if the root node is empty and return 0 depth if so.
* Otherwise, it checks if the left node is not empty, if so,
  - it calls the `max_depth` function on that node add the result to the existing depth of the left side, so that's why `left_depth` is assigned to one, because on its first call there's already one node to count. Then it recurse until there are no left nodes left.
  - then it checks if a right node exist, if so,
    - it calls `max_depth` on this node and recurse until there are no right nodes left and keep adding count of the nodes.
* Then checks which side has more nodes and return as the max depth of the tree.

```python

    def max_depth(self):

        left_depth = 1
        right_depth = 1
        if self is None:
            return 0
        else:

            if self.left:
                left_depth += self.left.max_depth()
            if self.right:
                right_depth += self.right.max_depth()

        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth
```

- `bst_main.py` got no different results from the inteded ones.

## Part 3: Count unique words 2

- First I got the of the file in a list, then iterate through the list and add each word into the bst map using `put` method passing the key as word and the value initially as `1`.
  Then convert the map to a list by calling `as_list` function. Sorted that list in decending order by the values and got the first 10 elements of that sorted list.

```python
        lines = file.readlines()

        for line in lines:
            line = line.strip('\n')
            # Add the word to the BST
            map.put(line, 1)

    # Returns a list of tuples for the words that are longer than 4
    # with thier frequency.
    map_lst = map.as_list()

    sorted_map_lst = sorted(map_lst, key=lambda x: x[1], reverse=True)


    for i in range(10):
        print(f'{sorted_map_lst[i][0]}: {sorted_map_lst[i][1]}')
```

- Unique words count:

  - `life of brian` got `2004` unique words of the total `10761` words.

    - Those words are:
      - brian: 368
      - crowd: 161
      - centurion: 121
      - mother: 104
      - right: 99
      - crucifixion: 78
      - pilate: 68
      - pontius: 64
      - don't: 59
      - rogers: 52

  - `swedish_news_2020` got `412587` unique words of the total `15103923` words.
    - Those words are:
      - under: 54018
      - säger: 47539
      - efter: 44058
      - kommer: 42839
      - eller: 32064
      - också: 30472
      - sedan: 30375
      - andra: 28043
      - finns: 27576
      - många: 26810

* Bucket list size is:
  - For `life of brian`: `2048`
  - For `swedish_news_2020`:
* Max bucket size is:
  - For `life of brian`: `7`
  - For `swedish_news_2020`:
* Zero bucket ratio:
  - For `life of brian`: `0.38`
  - For `swedish_news_2020`:

- Total node count:
  - For `life of brian`: `2004`
  - For `swedish_news_2020`: `412587`

* Max depth:
  - For `life of brian`: `27`
  - For `swedish_news_2020`: `134`
* Leaf count:
  - For `life of brian`: `647`
  - For `swedish_news_2020`: `136302`

- If the max bucket size is high that means the elements aren't distributed through the set in a good way, which depends on the hashing function, so the lower the better. And if zero bucket ratio is closer to 1 that means as well the hash function isn't good, on the other hand,
  if size of the set is much almost double the number of elements, then zero bucket ratio is certainly gonna be high. For example, in our mini-project, if there are 9 elements then the set's size is gonna be 16 wich will guarantee a high zero bucket ratio number, so we have to take that into considiration when evaluating the hash set.

* The optimal case of MBZ is (1) element in each bucket, while 5-8 elements is pretty reasonable but it is poor result if it's higher than 8.
* For the ZBR an optimal result would be (0), but if it's between 0.4 and 0.6 it would be reasonable. A poor result would be higher that 0.7.

- Bst map can be evaluated by looking the it's max depth, if it is high then it would take longer time to access an element.

* Leaf count, indicate much the tree is balanced.
* Unfortunately I don't have a good idea of what results would be optimal or reasonable or poor.

## Project conclusions and lessons learned

We separate technical issues from project related issues.

### Technical issues

- Well, conceptualizing the binary search tree was pretty hard for me, so I had to go through trial and error many times to get the grasp of it. So Bst was consuming most of the time workin on this project.

- Divide and conquer is the way to go in solving a programming problem. In the beginning I trying to get the full picture before I get to know the pixels of it, so in the future I would slice the problem into many smaller bits and I would go through them one by one.

- How could the results be improved if you were given a bit more time to complete the task.
- I think taking more time looking for/creating a better hashing function would give better results, but hey, time is not the one to blame here.

### Project issues

The project was carried on by one person, me here,
so it took around 6 full working days to finish it.
