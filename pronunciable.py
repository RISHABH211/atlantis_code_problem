# function to list out all the pronounceable words from a string

def pronounceable_words():
    """
    Take string input from user and return the expected pronounceable words
    :return: list
    """
    pro_word = input("Enter the string : ")
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    word_list = []
    unpronounceable_word_list = []
    j = 1
    l = 1

    for k in range(len(pro_word)):
        for i in range(l, len(pro_word)):
            word_list.append(pro_word[:j] + pro_word[i])
        j += 1
        l += 1
    for i, word in enumerate(word_list):
        consonant_counter = 0
        vowel_counter = 0
        for alphabet in word:
            if alphabet not in vowel:
                consonant_counter += 1
            else:
                vowel_counter += 1
            if vowel_counter == 0 and consonant_counter > 2:
                unpronounceable_word_list.append(word)
                break
        if vowel_counter == 0:
            unpronounceable_word_list.append(word)
    pronounceble_word_list = [word for word in word_list if word not in unpronounceable_word_list]
    print(pronounceble_word_list)


# execute the function after file is run
if __name__ == "__main__":
    pronounceable_words()
