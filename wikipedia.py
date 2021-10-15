from bs4 import BeautifulSoup
import requests
import re


def wikipedia():
    three_letter_words_per_para = []
    four_letter_words_per_para = []
    five_letter_words_per_para = []
    three_letter_words = []
    four_letter_words = []
    five_letter_words = []
    regex = re.compile('[.@_!#$%^&*()<>?,;"/\|}{~:]')
    search_url = input("Enter the url : ")
    html_text = requests.get(search_url).text
    soup = BeautifulSoup(html_text, "lxml")
    all_paragraphs = soup.find_all("p")
    for para in all_paragraphs:
        three_word_counter = 0
        four_word_counter = 0
        five_word_counter = 0

        all_words_list = para.text.split()
        for each_word in all_words_list:

            # condition to check and remove all special characters before and after the words if they exist

            if (regex.search(each_word[0]) != None) and (regex.search(each_word[-1]) != None):
                each_word = each_word[1:-1]
            elif (regex.search(each_word[-1]) != None):
                each_word = each_word[:-1]
            elif (regex.search(each_word[0]) != None):
                each_word = each_word[1:]

            # condition check to sort out all 3,4,5 letters words

            if len(each_word) == 3 and each_word.isalpha():
                three_word_counter += 1
                three_letter_words.append(each_word)
            elif len(each_word) == 4 and each_word.isalpha():
                four_word_counter += 1
                four_letter_words.append(each_word)
            elif len(each_word) == 5 and each_word.isalpha():
                five_letter_words.append(each_word)
                five_word_counter += 1
        three_letter_words_per_para.append(three_word_counter)
        four_letter_words_per_para.append(four_word_counter)
        five_letter_words_per_para.append(five_word_counter)
    total_three_letter_word = 0
    total_four_letter_word = 0
    total_five_letter_word = 0
    for i in range(len(three_letter_words_per_para)):
        total_three_letter_word = total_three_letter_word + three_letter_words_per_para[i]
    for i in range(len(four_letter_words_per_para)):
        total_four_letter_word = total_four_letter_word + four_letter_words_per_para[i]
    for i in range(len(five_letter_words_per_para)):
        total_five_letter_word = total_five_letter_word + five_letter_words_per_para[i]

    print(total_three_letter_word, total_four_letter_word, total_five_letter_word)
    print(len(three_letter_words_per_para), len(four_letter_words_per_para), len(five_letter_words_per_para),)
    print(f"3-letter words: {round(total_three_letter_word / len(three_letter_words_per_para))}/paragraph",
          f"4-letter words: {round(total_four_letter_word / len(four_letter_words_per_para))}/paragraph",
          f"4-letter words: {round(total_five_letter_word / len(five_letter_words_per_para))}/paragraph"
          )


if __name__ == "__main__":
    wikipedia()
