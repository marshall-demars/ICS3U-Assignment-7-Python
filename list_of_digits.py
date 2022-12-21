#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program sees if you guess the right number using while true

def new_list(int_list):
    # this function return list of its digits
    lst = int_list[0]
    # process
    process = list(map(int, str(lst)))
    # return
    return process


def main():
    # this function prints the output
    List_of_numbers = []

    # input & output
    try:
        input_from_user = int(input("The original number is: "))
        List_of_numbers.append(input_from_user)

        print_list = new_list(List_of_numbers)

        print(
            "\n\nThe list from number is : {0}"
            .format(print_list))
    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()