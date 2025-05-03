# Hindi-English Dictionary
hindi_dict = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "खुश": "Happy",
    "पढ़ाई": "Study"
}

# User lookup option
word = input("Enter a Hindi word to look up its English translation: ")
translation = hindi_dict.get(word, "Word not found")
print("Translation:", translation)
