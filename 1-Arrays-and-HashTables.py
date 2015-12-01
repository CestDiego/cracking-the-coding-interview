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
    # for key, value in le_dict.iteritems(): if value % 2: count += 1

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

    le_string = ""
    new_string = []
    new_count  = []
    # lets say we count upper case and lower case letters differently.
    for char in string:
        if len(new_string) == 0 and len(new_count) == 0:
            new_string.append(char)
            new_count.append(1)
        else:
            if char == new_string[-1]:
                new_count[-1] += 1
            else:
                new_count.append(1)
                new_string.append(char)

    if max(new_count) == 2:
        return string

    for c, n in zip(new_string, new_count):
        le_string += c + str(n)

    return le_string



coords = [(1,3), (1,2), (3,4)]
#1.7
def rotate_indices(coord, size):
    i, j = coord
    return j, size - 1 - i

def get_all_rotated_indices(coord, size):
    "Sorry not sorry."
    first  = coord
    second = rotate_indices(first, size)
    third  = rotate_indices(second, size)
    fourth = rotate_indices(third, size)

    return [first, second, third, fourth]


def switch_points(mat, coord1, coord2):
    i1, j1 = coord1
    i2, j2 = coord2

    mat[i1][j1] , mat[i2][j2] = mat[i2][j2], mat[i1][j1]


def rotate_points(mat, coords, size):
    "Coords is an array of four indices that are rotation of the previous one"
    val = [mat[i][j] for (i,j) in coords]

    switch_points(mat, coords[0], coords[3])
    switch_points(mat, coords[1], coords[3])
    switch_points(mat, coords[2], coords[3])

def doIt(mat, N):
    for i in xrange(0, N/2):
        for j in xrange(i, N - i - 1):
            coords = get_all_rotated_indices((i,j), N)
            rotate_points(mat, coords, N)
    return mat

def test():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    expected_mat = [[7,4,1],[8,5,2],[9,6,3]]
    return expected_mat == doIt(mat, 3)

def test2():
    mat = [[1]]
    expected_mat = [[1]]
    return expected_mat == doIt(mat, 1)

def test3():
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    expected_mat = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
    return expected_mat == doIt(mat, 4)
