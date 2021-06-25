# Counts the words in a specified document

def wordcount(doc):
    words = 0  # simple list initialisation ready for appending
    with open(doc, 'r') as word:
        for w in word.readlines():  # iterating through the file assigning each line to w
            for x in w.split():  # iterating through the words on each line and splitting at the next space character
                words += 1  # increments the value stored in "words" for each loop

    # print(words)
    return words  # returning the 'words' list


#if __name__ == "__main__":
#    document = "test.md"
#    wordcount(doc=document)
