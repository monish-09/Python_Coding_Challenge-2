text = input("Enter string: ")

result = ""

for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print(result)