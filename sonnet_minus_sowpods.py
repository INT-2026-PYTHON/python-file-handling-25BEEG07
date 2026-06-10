# sonnet minus sowpods
with open("sowpods.txt", "r") as file:
    sowpods = {line.strip().lower() for line in file}
with open("sonnet_words.txt", "r") as file:
    sonnet = {line.strip().lower() for line in file}
unique_words = sorted(sonnet - sowpods)
print("Words in sonnet but not in sowpods:")
print(unique_words)
print(f"Total: {len(unique_words)}")