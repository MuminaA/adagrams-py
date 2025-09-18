from random import randint
# create a dictionary to represent the letter pool
pool_of_letters = {
        'A':9, 'B':2, 'C':2, 'D':4,
        'E':12, 'F':2, 'G':3, 'H':2,
        'I':9, 'J':1, 'K':1, 'L':4,
        'M':2, 'N':6, 'O':8, 'P':2,
        'Q':1, 'R':6, 'S':4, 'T':6,
        'U':4, 'V':2, 'W':2, 'X':1,
        'Y':2, 'Z':1
}

def draw_letters():
    # output: ['A','T','U','D','X','S','J','N','M','P']

    letter_bank = []
    pool_dict_copy = pool_of_letters.copy()

    while len(letter_bank) < 10:
        available_letters = []
        # check what letters are avaliable (count > 0)
        for letter, count in pool_dict_copy.items():
            if count > 0:
                available_letters.append(letter)
        # pick one avaliable letter randomly
        random_index = randint(0, len(available_letters) - 1)
        random_letter = available_letters[random_index]
        #print(random_letter)
        # add the random avaliable letter to the hand
        letter_bank.append(random_letter)
        # decrement the count of the letter in pool copy
        pool_dict_copy[random_letter] -= 1

    return letter_bank

def uses_available_letters(word, letter_bank):
    # make a copy of letter_bank
    letter_bank_copy = letter_bank.copy()
    #capatalize all words
    upper_word = word.upper()
    # check if letter is in letter_bank
    for letter in upper_word:
        if letter in letter_bank_copy:
        # if word in bank remove so dosent effect future checks
            letter_bank_copy.remove(letter)
            #print(f'{letter} in {letter_bank}')
        else:
            #if not in bank then return false
            return False
    return True


def score_word(word):
    upper_word = word.upper()
    # print(upper_word)

    # points counter
    num_of_points = 0

    point_value = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10:['Q', 'Z']
    }

    for num, alpha in point_value.items():
        #print(num, alpha)
        for i in alpha:
            #print(i)
            for letter in upper_word:
                # compare letter to dict value
                if letter == i:
                    # print(f"{word} and {i} are the same letters")
                    # add the key(point)to the num of points
                    #print(num)
                    num_of_points += num

    if 6 < len(word) < 11:
        # word gets an additional 8 points
        # print(f"{word} is longer than 6 words")
        num_of_points += 8
    #else:
        # word points dosent get additional points
        #print(f"{word} is NOT longer than 6 words")

    #print(num_of_points)
    return num_of_points


def get_highest_word_score(word_list):
    pass
