#1
password = "parol7698"
new_password = ""
i = 0
while i < len(password):
    if not password[i].isdigit():
        new_password += password[i]
    i += 1
print(new_password)
#2
text = "man nurislom man."
new_text = ""
i = 0
while i < len(text) and i < 10:
    new_text += text[i]
    i += 1
print(new_text)
#3
name = "nurislom1234"
cleaned_name = ""
i = 0
while i < len(name):
    if not name[i].isdigit():
        cleaned_name += name[i]
    i += 1
print(cleaned_name)
#4
text = "man nurislom man."
modified_text = ""
i = 0
while i < len(text):
    if text[i] != ' ':
        modified_text += text[i].lower()
    i += 1
print(modified_text)
#5
text = "man nurislom man."
vowels = "aaueoiAAUEOI"
unli_harflar = ""
i = 0
while i < len(text):
    if text[i] in vowels:
        unli_harflar += text[i]
    i += 1
print(unli_harflar)
#6
word = "sobr kachok"
modified_word = ""
i = 0
while i < len(word):
    if i < len(word) - 1 and word[i] == 'a' and word[i + 1] == 'b':
        modified_word += '#'
        i += 2
    else:
        modified_word += word[i]
        i += 1
print(modified_word)
#7
text = "906518123"
reversed_text = ""
i = len(text) - 1
while i >= 0:
    reversed_text += text[i]
    i -= 1
if text.isdigit():
    print(reversed_text)
else:
    print("Matn raqam.")
#8
word = "hello nurislom"
modified_word = ""
length = len(word)
middle_index = length // 2
i = 0
while i < length:
    if i != middle_index:
        modified_word += word[i]
    i += 1
print(modified_word)
#9
name = "Nurisloma"
if name.endswith("a"):
    name = name.lower()
print(name)
#10
text = "puthon dasturcha"
unique_chars = ""
i = 0
while i < len(text):
    if text[i] not in unique_chars:
        unique_chars += text[i]
    i += 1
print(unique_chars)
#11
word = "audi"
vowels = "aoiueAUOIE"
is_all_vowels = True
i = 0
while i < len(word):
    if word[i] not in vowels:
        is_all_vowels = False
        break
    i += 1
if is_all_vowels:
    print(word.upper())
else:
    print(word)
