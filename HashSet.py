from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0
    num_of_elements = 0

    def init(self):
        self.size = 8
        self.num_of_elements = 0
        self.buckets = [[] for i in range(8)]

    def get_hash(self, word):

        # djb2 is faster than multiplying the letter
        # with the constant to the power of the letter's index.
        # g = 31
        hash = 5381  # 5381 is found the best prime number for this algorithm.
        # hash_value = 0
        for letter in word:
            # djb2 hash function.
            # Found on: https://python.algorithms-library.com/hashes/djb2
            hash = ((hash * (2**5)) + hash) + ord(letter)

            # Some hash function i found on youtube from
            # Dr. Rob Edwards from San Diego State University.

            # index = word.index(letter)
            # hash_value += ord(letter) * (g ** index)

            # Basic hash function.
            # hash_value += ord(letter)

        return hash

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

    # Adds a word to set if not already added

    def add(self, word):

        hash_value = self.get_hash(word)
        # Get which bucket the word would be put in.
        bucket_num = hash_value % self.size

        if word not in self.buckets[bucket_num]:
            self.buckets[bucket_num].append(word)
            self.num_of_elements += 1

        if self.num_of_elements == self.size:
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):

        s = ''
        for bucket in self.buckets:
            for element in bucket:
                s += element + ' '
        return s
        return self.buckets

    # Returns current number of elements in set
    def get_size(self):
        num_of_elements = 0
        for bucket in self.buckets:
            num_of_elements += len(bucket)

        return num_of_elements

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hash_value = self.get_hash(word)
        bucket_num = hash_value % self.size
        if word in self.buckets[bucket_num]:
            return True
        else:
            return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        pass    # Placeholder code ==> to be replaced

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        pass    # Placeholder code ==> to be replaced

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        maximus = 0
        for bucket in self.buckets:
            if len(bucket) > maximus:
                maximus = len(bucket)

        return maximus

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        pass    # Placeholder code ==> to be replaced
