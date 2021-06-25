# Counting the total number of lines in a file


def linecount(doc):
    total = 0
    with open(doc, 'r') as line:
        for lines in line.readlines():
            filledlines = lines.rstrip()
            if filledlines:
                total += 1
    # print(total)
    return total


if __name__ == "__main__":
    document = "test.md"
    linecount(doc=document)
