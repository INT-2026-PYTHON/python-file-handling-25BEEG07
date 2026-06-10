# palindrome words
def is_palindrome(word):
    return word == word[::-1]
count = 0
with open("sowpods.txt", "r") as file:
    for line in file:
        word = line.strip().lower()
        if is_palindrome(word):
            print(word)
            count += 1
print(f"Total palindromes: {count}")