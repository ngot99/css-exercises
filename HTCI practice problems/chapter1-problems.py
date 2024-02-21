#1.1 checking if a problem is a permutation
def is_perm(x,y):
   if len(x) != len(y):
        return False
   letters = [0]*128
   for i in x:
        letters[ord(i)] += 1
   for i in y:
        if letters[ord(i)] > 0:
            letters[ord(i)] -= 1
        else:
            return False
   return True
'''
def URLify(s,t):
    #go in reverse identify first index

    index = 0
    for i in range(len(s), 0, -1):
        if s[i] != " ":
            index = i
            break
    for 
'''

def palindrome_permutation(s):
    # Case insenstive
    s = s.lower()
    # Create a dict of all letters
    charCount = {}
    # Add all letters and values to dict
    for i in s:
        if charCount.get(i) is None:
            charCount[i] = 1
        else:
            charCount[i] += 1
    # Eliminate space from the dict. In this use case we are not considering spaces as letters
    charCount.pop(" ")
    occurences = charCount.values()
    # Allow for 1 odd value
    oneOdd = True
    for i in occurences:
        if i%2 != 0:
            if(oneOdd):
                oneOdd = False
            else:
                return False
    return True

# Compare two strings and determine if they are 1 or 0 edits away from each other.
# Assuming that only letters are use, all lowerecase
# Check if 1 removal away
# Check if 1 replace away
# Check if 1 insertion away
def one_away(s,t):
    distance = 0
    if len(s) != len(t):
        return one_insert_or_remove_away(s,t)
    else:
        return one_replace_away(s,t) 

def one_insert_or_remove_away(s,t):
    distance = 0
    indexS = len(s)- 1
    indexT = len(t)- 1

    while distance <2 and (indexS > -1 and indexT -1):
        if s[indexS] == t[indexT]:
            indexS -= 1
            indexT -= 1
        if s[indexS] != t[indexT]:
            
            distance += 1
            if indexS > indexT:
                indexS -= 1
            elif indexS < indexT:
                indexT -= 1
            else:
                indexS -= 1
                indexT -= 1
    return distance <= 1

def one_replace_away(s,t):
    distance = 0
    index = 0
    while distance <2 and index < len(s):
        if s[index] != t[index]:
            distance += 1
        index += 1
    return distance <= 1

# String Compression
def string_compression(s):
# iterate through the string with a counter and current character. increment if same letter and reset when needed
    counter = 0
    letter = s[0]
    compressed = ''
    for c in s:
        if letter == c:
            counter += 1
        else:
            compressed += letter + str(counter)
            counter = 1
            letter = c
    compressed += letter + str(counter) 
    return compressed if len(compressed) < len(s) else s

'''
Rotate a matrix by 90degrees
This is a 2 step process. First we rotate the matrix by turning the rows to colums. The swap the rows (front and back, then move inward)
This uses 2 nested functions fo O(2n^2) -> O(n^2).
''' 

def rotate_matrix(m):
    #itterate through matrix, if we spot a 0, flag it.
    temp = 0
    for j in range(len(m)):
        for i in range(j,len(m)):
            temp = m[j][i]
            m[j][i] = m[i][j]
            m[i][j] = temp
    for r in range(len(m)):
        for c in range(len(m)//2):
            temp = m[r][c]
            m[r][c] = m[r][len(m)- 1 - c]
            m[r][len(m)- 1 - c] = temp
    return m

'''
Notes for zero matrix
Iteraate through matrix and indentify 0s. Have 2 seperate arrays that store the row and col flags

Second forloop that goes over 2 other arrays, if a 0 is identified, m array values are set 0 appropriate 0.

Run time = 2 nested forloops = O(2n^2) -> O(n^2)
Space complexity. We have 2 arrays of length n and m
'''

def zero_matrix(m):
    rowM = [1] * len(m)
    colM = [1] * len(m[0])
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 0:
                rowM[r] = 0
                colM[c] = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if rowM[r] == 0 or colM[c] == 0:
                m[r][c] =0

    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 0:
                m[[0]]
    print(m)

def string_rotation(s,t):
    j = s+s
    print("hello")
    if t in j:
        return True
    else:return False




if __name__ == "__main__":
    #print(is_perm("aaabbb", "abaabb"))'
    #print(URLify("Mr John Smith   "))
    #print(palindrome_permutation("tact Coa"))   
    '''
    test = ["pale", "pales", "pale", "pale"]
    test2 = ["ple", "pale", "bale", "bake"]
    
    for i in range(4):
        print(one_away(test[i], test2[i]))
    '''
    #print(string_compression("ab"))
    '''
    m = [[1,2,3,4], [5,6,7,8], [9,1,2,3],[4,5,6,7]]
    m2 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

    '''

    '''
    m = [[1,1,1], [1,0,1], [1,1,1]]
    m2 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    zero_matrix(m)
    '''
    string_rotation("waterbottle", "erbottlewat")
