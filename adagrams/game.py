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

# Wave 1
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

# Wave 2
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

# Wave 3
def score_word(word):
    upper_word = word.upper()
    # print(upper_word)

    # points counter
    num_of_points = 0

    point_value = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    for letter in upper_word:
        if letter in point_value:
            num_of_points += point_value[letter]

    if 6 < len(word) < 11:
        # word gets an additional 8 points
        # print(f"{word} is longer than 6 words")
        num_of_points += 8

    #print(num_of_points)
    return num_of_points

# Wave 4
def get_highest_word_score(word_list):
    # keep track of the best word and its score
    best_word = None
    best_score = 0
    # iterate through word list
    for word in word_list:
        # print(word)
        # score the words
        score = score_word(word)
        # find higher score then update winner
        if score > best_score:
            best_word = word
            best_score = score
        # if score is tie apply tie-breaker
        elif score == best_score:
            # prefer the 10 letter word
            if len(best_word) != 10 and len(word) == 10:
                best_word = word
                best_score = score
            # otherwise, perfer the shorter word
            elif len(best_word) != 10 and len(word) < len(best_word):
                best_word = word
                best_score = score

    return(best_word, best_score)
