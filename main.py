def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = len(file_contents.split())
    print(words, "words found in the document")

def count_characters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    letter_dict = {}
    for x in file_contents:
        if x.isalpha():
            x = x.lower()
            if x in letter_dict:
                letter_dict[x] += 1
            else:
                letter_dict[x] = 1
    return(letter_dict)

def letter_reporter(letter_dict):
    # print(letter_dict)
    # print(type(letter_dict))
    # this prints the scentences we're after, but I need to sort these into a list from the function below.
    for x in letter_dict:
        print(f"The '{x['letter']}' character was found {x['num']} times")


def sort_em(pre_dict):
    # print(type(pre_dict))
    list_of_dicts = [{"letter": k, "num": v} for k, v in pre_dict.items()]

    list_of_dicts.sort(reverse=True, key=sort_nums)

    return(list_of_dicts)

def sort_nums(dict):
    return dict["num"]

print("--- Begin report of books/frankenstein.txt ---")
# main() # main will print the file contents
word_count() # word count will print the wordcount to the console.
print()
# count_characters() #this returns a dictionary with all the letters added up {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504,}
letter_reporter(sort_em(count_characters())) #prints a list of letters and amount they appear in decending order
# sort_em(count_characters()) # count_characters() is a dictonary
print("--- End report ---")