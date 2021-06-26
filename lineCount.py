# Counting the total number of lines in a file


def linecount(doc):
    total = 0  # initialising the "total" value for use in the program
    with open(doc, 'r') as line:
        for lines in line.readlines():  # increments through each line of the document
            filledlines = lines.rstrip()  # cuts out the blank lines
            if filledlines:
                total += 1  # increments the value stored in "words" for each loop

    return total
