import re
"""
Python library for regular expressions (aka regex)
(sequences of characters that define a search pattern)
"""


def string_match(s) -> bool:
    """
    Regex Breakdown:

    ?: indicates a non-capturing group, it doesn't save captured matched text

    \\. indicates an escaped backslash and dot operator, to match their string literals

    | indicates an alternation operator, matching either the left or right expression

    [^"\\] indicates a negated character class, matching any character except a single quote
    or backslash
    """
    # Regex pattern to match Python string literals
    pattern = re.compile(r"""
        (?:                         # Non-capturing group
            ' (?: \\. | [^'\\] )* '   # Single quoted string
        |
            " (?: \\. | [^"\\] )* "   # Double quoted string
        |
            ''' (?: \\. | [^'\\] )* '''  # Triple single quoted string
        |
            \"\"\" (?: \\. | [^"\\] )* \"\"\"  # Triple double quoted string
        )
    """, re.VERBOSE)

    # Casts and returns a boolean from the fullmatch() function
    # (that attempts to match the regex pattern to the entire string)
    return bool(pattern.fullmatch(s))


# Test the function with some examples
examples = [
    "'hello'",
    '"world"',
    "'''hello world'''",
    '"""hello world"""',
    "'hello\nworld'",
    "'hello\\'",
    "'hello\\nworld'",
    "'hello world",
    "hello world'",
    "hello world"
]


def main() -> None:
    for example in examples:
        print(f'{example}: {string_match(example)}')


if __name__ == "__main__":
    main()
