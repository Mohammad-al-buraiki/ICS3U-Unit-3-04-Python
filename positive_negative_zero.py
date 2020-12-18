# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is Positive / Negative / 0


def main():
    # this function shows the sign of the number
    # that user entered

    # input
    number = int(input("Enter the number: "))
    print("")

    # process
    if number > 0:
        print("It is a positive (+)")
    elif number < 0:
        print("It is a negative (-)")
    else:
        print("0")


if __name__ == "__main__":
    main()
