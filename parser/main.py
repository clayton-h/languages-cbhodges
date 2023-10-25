import re
"""
Python library for regular expressions (aka regex)
(sequences of characters that define a search pattern)
"""


def string_match(s) -> bool:
    """
    [^"\\] indicates a negated character class, matching any character except a single quote
    or backslash
    """

    # Regex pattern to match Python string literals
    pattern = re.compile(r"""
        (?: # Non-capturing group (doesn't save captured matched text)
            ' (?: # Single quoted string
                \\.                 # Escaped backslash and dot operator
                | [abfnrtv"']       # Match common escape characters
                | x[0-9A-Fa-f]{2}   # Match hexadecimal escape (\xhh)
                | [0-7]{1,3}        # Match octal escape (\ooo)
                | N\{[^}]+\}        # Match Unicode character by name (\N{name})
                | u[0-9A-Fa-f]{4}   # Match Unicode character by 4-digit hexadecimal
                | U[0-9A-Fa-f]{8}   # Match Unicode character by 8-digit hexadecimal
                | r|
                | [^'\\]            # Don't match a single quote or backslash
            )* '
        |
            " (?: # Double quoted string
                \\. 
                | [abfnrtv"']
                | x[0-9A-Fa-f]{2}
                | [0-7]{1,3}
                | N\{[^}]+\}
                | u[0-9A-Fa-f]{4}
                | U[0-9A-Fa-f]{8}
                | r|
                | [^"\\] 
            )* " 
        )
    """, re.VERBOSE)

    # Casts and returns a True/False from the fullmatch() function
    # (that attempts to match the regex pattern to the entire string)
    return bool(pattern.fullmatch(s))


# Test the function with some examples
examples = [
    "'hello'",          # Single quoted string
    '"hello world"',    # Double quoted string
    "'\a'",             # Bell character
    r'r'\n'             # Raw string with newline
]


def main() -> None:
    for example in examples:
        print(f'{example}: {string_match(example)}')


if __name__ == "__main__":
    main()
