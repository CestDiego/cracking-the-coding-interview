def urlify(le_string):
    a = ""
    for char in le_string:
        if char == " ":
            a += "%20"
        else:
            a += char
    return a


def is_palyndrome(le_string):
    # check if it has an even length
    length  = len(le_string)
    le_dict = {}
    for char in le_string:
        try:
            le_dict[char]
        except KeyError:
            le_dict[char] = 0
        le_dict[char] += 1

    count = 0
    for key, value in le_dict.iteritems():
        if value % 2:
            count += 1

    if length % 2:
        ## if odd length, only one odd repetition of letter is allowed. 1, 3, 5, etc
        if count % 2:
            return False
        else:
            return True
    else:
        ## if so, no odd repetitions of each letter are allowed.
        if count == 0:
            return True
        else:
            return False


class HashTable:

    def __init__(self):
        pass


#1.6

def string_comprehension(string):
    buf_char = ""
    # lets say we count upper case and lower case letters differently.
