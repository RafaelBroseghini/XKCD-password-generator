import random

number_subs = {"e":"3","s":"5","b":"8","o":"0","i":"!"}

easy_typing = {'a': -1, 'b': 1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': 0, 'h': 1, 'i': 1, 'j': 1, 'k': 1,
               'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': -1, 'r': -1, 's': -1, 't': 0, 'u': 1, 'v': -1,
               'w': -1,'x': -1, 'y': 1, 'z': -1, "1":-1, "2":-1 ,"3":-1, "4":-1, "5":-1, "6":1, "7":1, "8":1,
               "9":1, "0":1, "!":-1}

def read_file(filename):
    words_dict = {}
    with open(filename, "r") as filein:
        all_words = list(filein)
    random.shuffle(all_words) 

    for word in all_words:
        word = word.strip("\n")
        if word not in words_dict:
            words_dict[word] = {"len":len(word),"easy":"no"}
            sum_of_easiness = 0
            for letter in word:
                if letter in easy_typing:
                    sum_of_easiness += easy_typing[letter]

            if sum_of_easiness >= -1 and sum_of_easiness <= 1:
                words_dict[word]["easy"] = "yes"

    return words_dict

def type_easy(not_easy_dict):
    easy_dict = {}
    for word in not_easy_dict:
        if not_easy_dict[word]["easy"] == "yes" and word not in easy_dict:
            easy_dict[word] = {"len": not_easy_dict[word]["len"]}

    return easy_dict

def generate_possible_words(words, maxwl, minwl):
    possible_words = {}
    for word in words:
        if words[word]["len"] >= minwl and words[word]["len"] <= maxwl:
            possible_words[word] = len(word)
    return possible_words

def generate_pswds(words, minl, maxl, minwl, maxwl, words_p_pwd):
    possible_words = generate_possible_words(words, maxwl, minwl)
    used_words = {}
    all_pswd = []

    number_of_passwords = 0
    tries = 0
    while number_of_passwords < 10 and tries < 50:
        pswd = ""
        a_pswd = []
        current_word_size = maxl
        for word in possible_words:
            if len(pswd)+possible_words[word] < minl and word not in used_words and len(a_pswd) < words_p_pwd:
                used_words[word] = "USED"
                pswd += word
                a_pswd.append(word.lower())
                current_word_size = current_word_size - possible_words[word]
            else:
                if possible_words[word] < current_word_size and word not in used_words and len(a_pswd) < words_p_pwd:
                    used_words[word] = "USED"
                    pswd += word
                    a_pswd.append(word.lower())
                    current_word_size = current_word_size - possible_words[word]

        if len(a_pswd) == 4 and len("".join(a_pswd)) >= minl and len("".join(a_pswd)) <= maxl:
            all_pswd.append(a_pswd)
            pswd = ""
            current_word_size = maxl
            number_of_passwords += 1
        tries += 1

    print("Generated 10 passwords in: {} tries.".format(tries))
    return all_pswd



def number_substitution(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = list(lst[i][j])
            for l in range(len(lst[i][j])):
                if lst[i][j][l] in number_subs:
                    lst[i][j][l] = number_subs[lst[i][j][l]]
            lst[i][j] = "".join(lst[i][j])

    return lst
