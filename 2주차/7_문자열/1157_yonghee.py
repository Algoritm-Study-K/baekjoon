word = input().upper()
letters = list(set(word))
count_letter = []

for c in letters:
    count_letter.append(word.count(c))
    
if count_letter.count(max(count_letter)) >= 2:
    print('?')
else:
    print(letters[count_letter.index(max(count_letter))])