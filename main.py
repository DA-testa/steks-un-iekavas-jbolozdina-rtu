# python3

from collections import namedtuple
from os.path import exists


Bracket = namedtuple("Bracket", ["char", "position"])


RESPONSE_TYPE_SUCCESS = "Success"


OPENING_BRACKETS = "([{"
CLOSING_BRACKETS = ")]}"


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, char in enumerate(text):
        if char in OPENING_BRACKETS:
            opening_brackets_stack.append(Bracket(char, i))

        if char in CLOSING_BRACKETS and (not opening_brackets_stack or not are_matching(opening_brackets_stack.pop().char, char)):
            return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1

    return False


def get_text():
    while True:
        user_choice = input("F for file OR I for input OR Q to quit: ").strip().lower()
        if user_choice ==  "f":
            file_path = input("Input file path: ")
            if not exists(file_path):
                print("Incorrect file path")

            with open(file_path, "r", encoding="UTF-8") as file:
                return file.read()
        elif user_choice == 'i':
            return input("Input text: ")
        elif user_choice == 'q':
            print("Exiting")

            break
        else:
            print("No such option exists")


def handle_mismatch(text):
    mismatch_found = find_mismatch(text)
    if mismatch_found:
        print(mismatch_found)
    else:
        print(RESPONSE_TYPE_SUCCESS)


def main():
    text = get_text()
    if not text:
        return

    handle_mismatch(text)


if __name__ == "__main__":
    main()
