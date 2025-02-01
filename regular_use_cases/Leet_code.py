def largest_unique_substring(input_string):
    char_index_map = {}
    start = 0
    max_length = 0
    max_substring = ""

    for end in range(len(input_string)):
        current_char = input_string[end]

        # If the character is already in the substring, move the start pointer
        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1

        # Update the last seen index of the character
        char_index_map[current_char] = end
        
        # Update max substring if current length is greater
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = input_string[start:end + 1]

    return max_substring

# Test cases
print(largest_unique_substring('ccccc'))        # Output: 'c'
print(largest_unique_substring('ccabcccc'))     # Output: 'cab' or 'abc'
print(largest_unique_substring(' abacdabaceabacefabacfegabacfghabcdefghijklabcdemnoabcdepqrst'))  # Check your input
