def countWords(S):
    # Initialize word count to 0
    word_count = 0
    # Initialize a variable to track if the previous character was a whitespace
    prev_whitespace = True

    # Iterate over each character in the string
    for char in S:
        # Check if the current character is a whitespace
        if char == ' ' or char == '\t' or char == '\n':
            # If the previous character was not a whitespace, increment word count
            if not prev_whitespace:
                word_count += 1
                prev_whitespace = True
        else:
            # If the current character is not a whitespace, set prev_whitespace to False
            prev_whitespace = False

    # Increment word count if the last character is not a whitespace
    if not prev_whitespace:
        word_count += 1

    return word_count


# Example 1
S1 = "abc def"
print(countWords(S1))  # Output: 2

# Example 2
S2 = "a\nyo\n"
print(countWords(S2))  # Output: 2
