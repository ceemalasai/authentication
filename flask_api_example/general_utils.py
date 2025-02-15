def to_uppercase(s: str) -> str:
    """Convert a string to uppercase."""
    return s.upper()

def to_lowercase(s: str) -> str:
    """Convert a string to lowercase."""
    return s.lower()

def capitalize_first_letter(s: str) -> str:
    """Capitalize the first letter of a string."""
    return s.capitalize()

def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]

def remove_whitespace(s: str) -> str:
    """Remove leading and trailing whitespace from a string."""
    return s.strip()

def replace_substring(s: str, old: str, new: str) -> str:
    """Replace occurrences of a substring with another substring."""
    return s.replace(old, new)

def split_string(s: str, delimiter: str = " ") -> list:
    """Split a string into a list using a specified delimiter."""
    return s.split(delimiter)

def join_strings(strings: list, delimiter: str = " ") -> str:
    """Join a list of strings into a single string using a specified delimiter."""
    return delimiter.join(strings)

def count_occurrences(s: str, substring: str) -> int:
    """Count the number of occurrences of a substring in a string."""
    return s.count(substring)

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = remove_whitespace(s).lower()
    return cleaned == cleaned[::-1]

# Example usage
if __name__ == "__main__":
    test_string = "  Hello World!  "
    print(to_uppercase(test_string))  # "  HELLO WORLD!  "
    print(to_lowercase(test_string))  # "  hello world!  "
    print(capitalize_first_letter(test_string))  # "  Hello world!  "
    print(reverse_string(test_string))  # "  !dlroW olleH  "
    print(remove_whitespace(test_string))  # "Hello World!"
    print(replace_substring(test_string, "World", "Python"))  # "  Hello Python!  "
    print(split_string(test_string))  # ["", "", "Hello", "World!", "", ""]
    print(join_strings(["Hello", "World!"]))  # "Hello World!"
    print(count_occurrences(test_string, "o"))  # 2
    print(is_palindrome("A man a plan a canal Panama"))  # True
