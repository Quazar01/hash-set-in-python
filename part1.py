
import os


def unique_words(path, name):
    # Declare an empty set
    words = set(())

    with open(path + '\\data\\' + name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Assign each word in the file to the words set.
        for word in lines:
            words.add(word)

    return len(words)


path = os.getcwd()

# Get how many unique words for Life of Brian.
unique_words_count = unique_words(path, 'brian_13375_words.txt')
print(f'Life of Brian has {unique_words_count} unique words!')

# Get unique words count for Swedish News
unique_words_count = unique_words(path, 'swe_news_15103923_words.txt')
print(f'Swedish News has {unique_words_count} unique words!')
