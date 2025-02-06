def is_palindrome(text):
    """
    Checks if a given string is a palindrome (reads the same forwards and backwards).

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    processed_text = ''.join(char.lower() for char in text if char.isalnum())  # Remove non-alphanumeric chars and lowercase
    return processed_text == processed_text[::-1]


def main():
    """
    A simple program to demonstrate palindrome checking.  Asks the user for input
    and then reports whether or not the input is a palindrome.
    """
    while True:
        user_input = input("Enter a string (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome!")
        else:
            print(f"'{user_input}' is not a palindrome.")


if __name__ == "__main__":
    main()
