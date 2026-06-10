# letters never back to back
seen = set()
doubled = set()
with open("sowpods.txt", "r") as file:
    for line in file:
        word = line.strip().lower()
        seen.update(word)
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                doubled.add(word[i])
result = sorted(seen - doubled)
print("Letters that never appear back-to-back:")
print(result)