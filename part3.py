import HashSet as hset
import BstMap as bst
import os


def implement(path, name):

    with open(path + '\\' + name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip('\n')
            # Add the word to the hash set.
            hash_lst.add(line)

    print("***Hash Set Implementation***")
    print('Unique words: ', hash_lst.get_size())
    print('Top-10 most frequently used words: \n')

    # for i in range(10):
    #     print(f'{sorted_map_lst[i][0]}: {sorted_map_lst[i][1]}')

    print('\nBucket List Size: ', hash_lst.bucket_list_size())
    print('Max Bucket Size: ', hash_lst.max_bucket_size())
    print('Zero Bucket Ration: ', hash_lst.zero_bucket_ratio())


hash_lst = hset.HashSet()
# Initialize HastSet.
hash_lst.init()
# Declare the binary search map.

path = os.getcwd()
life_of_brian = 'brian_13375_words.txt'
swedish_news = 'swe_news_15103923_words.txt'

print("Results for Life of Brian file:\n")

implement(path, life_of_brian)


hash_lst.init()
# map = bst.BstMap()
print('\n\nResults for Swedish News file: ')
# It takes around 2.5 minutes in order to process Swedish News!!
implement(path, swedish_news)
