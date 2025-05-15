def remove_and_strip(word_list, word_to_remove):
    return [item.strip() for item in word_list if item.strip() not in word_to_remove]

# Example usage
words = [" apple ", "banana ", "    orange ", " grape ", "apple "]
word_to_remove = ["apple", "grape"]
result = remove_and_strip(words, word_to_remove)
print(result)
