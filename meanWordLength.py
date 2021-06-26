# A script to count the total number of characters in a block of text and return the mean

def meanwordlen(doc):
    words = []  # simple list initialisation ready for appending
    length = 0  # initialising the "length" value for use in the program

    with open(doc, 'r') as word:
        for w in word.readlines():  # iterating through the file assigning each line to w
            for x in w.split():  # iterating through the words on each line and splitting at the next space character
                x = x.strip(",.")  # strips the characters "," and "." to get the true word length
                words.append(x)  # appends the variable "x" to the "words" list

    for count in words:
        num = len(count)
        length += num

    meanwordlength = (length / len(words))  # sets the meanwordlength equal to the length
    return meanwordlength
