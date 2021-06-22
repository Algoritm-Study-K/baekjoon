n = int(input())

li = []
for _ in range(n):
    li.append(input())

word_li = list(set(li))

word_sort = []
for i in word_li:
    word_sort.append((len(i), i))

word_sort = sorted(word_sort)
for len_word, li in word_sort:
    print(li)