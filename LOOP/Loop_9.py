c= 0
v = input("Enter a word: ")
for i in range(len(v)):
    if(v[i] == 'a' or v[i] == 'e' or v[i] == 'i' or v[i] == 'o' or v[i] == 'u'):
      c = c + 1
print("Total vowels in the word are: ", c)

c = 0

v = input("Enter a word: ")

for i in v:
    if i in "aeiou":
        c = c + 1

print("Total vowels in the word are:", c)