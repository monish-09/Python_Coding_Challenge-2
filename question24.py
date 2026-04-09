text = input("Enter string: ")
char = input("Enter character: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("Count:", count)