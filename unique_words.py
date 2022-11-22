
import os


def unique_words(path, name):

    words_set = set(())

    words_dict = {}
    most_freq_words = {}

    with open(path + '\\' + name, 'r', encoding='utf-8') as file:
        # Get the lines of the file
        lines = file.readlines()

        # Assign each line/word to the set.
        for word in lines:
            word = word.strip('\n')
            words_set.add(word)
            if len(word) > 4:
                # If the word is not in the dict, add the word
                # as the key, and add it's value to 1
                if word not in words_dict.keys():
                    words_dict[word] = 1

                else:
                    # Otherwise, increase the word's value by 1.
                    words_dict[word] += 1

        # Got the sorted function from freecodecamp.com
        # Sort the dict by it's value in reverse
        sorted_list = sorted(words_dict.items(),
                             key=lambda x: x[1], reverse=True)

        # Get the firt 10 key-value pairs from the list
        for i in range(10):
            k = sorted_list[i][0]
            v = sorted_list[i][1]
            # Assign the key and the value to the most_freq_words dict.
            most_freq_words[k] = v

        return len(words_set), most_freq_words


path = os.getcwd()

# lIFE OF BRIAN
print("Results for Life of Brian file:\n")
unique_words_count, most_freq_words = unique_words(
    path, 'brian_13375_words.txt')

print(f'There are {unique_words_count} unique words.')
print("Top 10 most frequented words: \n")
for key, value in most_freq_words.items():
    print(f"{key}: {value}")

# SWEDISH NEWS
print("Results for Swedish News:\n")
unique_words_count, most_freq_words = unique_words(
    path, 'swe_news_15103923_words.txt')
print(f'There are {unique_words_count} unique words.')

print("Top 10 most frequented words: \n")
for key, value in most_freq_words.items():
    print(f"{key}: {value}")

# It takes around 15 seconds to process Swedish News!!
