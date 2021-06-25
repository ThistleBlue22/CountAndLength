from wordCount import wordcount
from lineCount import linecount
from meanWordLength import meanwordlen
import argparse


def main(doc, calctype):
    try:
        # the below code checks the
        if calctype == "wordcount":
            wc = wordcount(doc=doc)
            print("Word Count:", wc, "\n")
        elif calctype == "linecount":
            lc = linecount(doc=doc)
            print("Line Count:", lc, "\n")
        elif calctype == "meanwordlength":
            mwl = meanwordlen(doc=doc)
            print("Mean Word Length:", mwl, "\n")
        # the above checks the passed type argument and runs the equivalent code snippet
        else:
            wc = wordcount(doc=doc)
            lc = linecount(doc=doc)
            mwl = meanwordlen(doc=doc)
            print("Word Count:", wc, "\nLine Count:", lc, "\nMean Word Length:", mwl)
            # simply runs all the individual components at once, printing the results to the console

    except TypeError as e:  # ensures that an error is thrown when passing a wrong extension value
        print("Please enter only a file with extensions of .txt or .md")
    except FileNotFoundError as e:  # ensures that the error is caught if a incorrect path name is run on the file
        print("Please check the file path and try again")
    except UnicodeDecodeError as e:
        print("Please only supply text based documents. Note: Some Microsoft Word documents, including .docx extensions"
              " have issues running through the program, please try pasting the contents of the document into a .txt"
              " file and trying again")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Word Count, Line Count and Mean Word Length calculator"
    )
    parser.add_argument(  # picks up on the file passed and helps enter it into the program
        "-d",
        "--document",
        help="For the text document"
    )
    parser.add_argument(  # intended to give the user options of one of the three, or all of them by default
        "-m",
        "--mode",
        choices=["wordcount", "linecount", "meanwordcount", "all"],
        default=["all"],
        help="Choice of which calculation to do. Accepted args include 'wordcount', "
             "'linecount', 'meanwordlength' and 'all'"
    )
    args = parser.parse_args()
    main(args.document, args.mode)  # passes the arguments given to main, to run the program(s)
