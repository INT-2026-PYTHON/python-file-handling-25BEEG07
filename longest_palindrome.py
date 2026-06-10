# longest palindrome
def is_palindrome(word):
    return word == word[::-1]
longest_length = 0
longest_palindromes = []
with open("sowpods.txt", "r") as file:
    for line in file:
        word = line.strip().lower()
        if is_palindrome(word):
            length = len(word)
            if length > longest_length:
                longest_length = length
                longest_palindromes = [word]
            elif length == longest_length:
                longest_palindromes.append(word)
print(f"Longest palindrome length: {longest_length}")
for word in longest_palindromes:
    print(word)