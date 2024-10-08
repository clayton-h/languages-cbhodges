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
        (?:                         # Non-capturing group (doesn't save captured matched text)
            r?                      # Raw strings
            '(?:                    # Single-quoted strings
                \\.                 # Escaped backslash and dot operator
                | [abfnrtv"']       # Match common escape characters
                | x[0-9A-Fa-f]{2}   # Match hexadecimal escape (\xhh)
                | [0-7]{1,3}        # Match octal escape (\ooo)
                | N\{[^}]+\}        # Match Unicode character by name (\N{name})
                | u[0-9A-Fa-f]{4}   # Match Unicode character by 4-digit hexadecimal
                | U[0-9A-Fa-f]{8}   # Match Unicode character by 8-digit hexadecimal
                | [^'\\]            # Don't match a single quote or backslash
            )*'
            |
            r?                      # Raw strings
            "(?:                    # Double-quoted strings
                \\.                 # Escaped backslash and dot operator
                | [abfnrtv"']       # Match common escape characters
                | x[0-9A-Fa-f]{2}   # Match hexadecimal escape (\xhh)
                | [0-7]{1,3}        # Match octal escape (\ooo)
                | N\{[^}]+\}        # Match Unicode character by name (\N{name})
                | u[0-9A-Fa-f]{4}   # Match Unicode character by 4-digit hexadecimal
                | U[0-9A-Fa-f]{8}   # Match Unicode character by 8-digit hexadecimal
                | [^'\\]            # Don't match a single quote or backslash
            )*"
        )
    """, re.VERBOSE)

    # Casts and returns a True/False from the fullmatch() function
    # (that attempts to match the regex pattern to the entire string)
    return bool(pattern.fullmatch(s))


# Test the function with some examples
examples = [
    R'r"\n"'    # raw string with capital 'R' - exp: True
    '"hello"',  # double quoted string - exp: True
    "'world'",  # single quoted string - exp: True


    "'\a'",    # bell escape character - exp: True
    "'\\'",    # escaped backslash - exp: False
    "\'",      # escaped single quote - exp: False

    '"\x41"',  # Hexadecimal escape (\xhh) - exp: True
    '"\101"',  # Octal escape (\ooo) - exp: True

    # Unicode by name (\N{name}) - exp: True
    '"\N{LATIN CAPITAL LETTER A}"',
    # Unicode by 4-digit hexadecimal (\u) - exp: True
    '"\u0041"',
    # Unicode by 8-digit hexadecimal (\U) - exp: True
    '"\U00000041"',
]


def main() -> None:
    for example in examples:
        print(f'{example}: {string_match(example)}')


if __name__ == "__main__":
    main()
