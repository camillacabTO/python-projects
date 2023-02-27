text = input("Enter a text to be analyzed: \n").lower().strip()
letters = input("Enter 3 random letters: \n").lower().split()

for letter in letters:
    print(f"'{letter}' appears {text.count(letter)} times")

print(f'There are {len(text.split())} words in the text')
print(f"The first letter in the text is '{text[0]}' and the last letter is '{text[-1]}'")
print(f'The inverted text looks like this:\n{(" ".join(text.split()[::-1]))}')
print(f'Python inside the text is {"python" in text}')

