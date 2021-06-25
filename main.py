from wordCount import wordcount
from lineCount import linecount
from meanWordLength import meanwordlen
import argparse


def main(doc, calctype):
    try:
        if calctype == "wordcount":
            wc = wordcount(doc=doc)
            print("Word Count:", wc, "\n")
        elif calctype == "linecount":
            lc = linecount(doc=doc)
            print("Line Count:", lc, "\n")
        elif calctype == "meanwordlength":
            mwl = meanwordlen(doc=doc)
            print("Mean Word Count:", mwl, "\n")
        else:
            wc = wordcount(doc=doc)
            lc = linecount(doc=doc)
            mwl = meanwordlen(doc=doc)
            print("Word Count:", wc, "\nLine Count:", lc, "\nMean Word Count:", mwl)

    except TypeError as e:
        print(e, "\nPlease enter only a file with extensions of .txt or .md")
    except FileNotFoundError as e:
        print(e, "\nPlease check the file path and try again")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Word Count, Line Count and Mean Word Length calculator"
    )
    parser.add_argument(
        "-d",
        "--document",
        help="For the text document"
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=["wordcount", "linecount", "meanwordcount", "all"],
        default=["all"],
        help="Choice of which calculation to do. Accepted args include 'wordcount', "
             "'linecount', 'meanwordlength' and 'all'"
    )
    args = parser.parse_args()
    main(args.document, args.type)
