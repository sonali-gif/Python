words = {
    "paani": "water",
    "kitaab": "book",
    "ghar": "house",
    "khana": "food"
}

word = input("Enter Hindi word: ")

print(words.get(word, "Word not found"))