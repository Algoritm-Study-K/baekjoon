n = int(input())

count = 0
for _ in range(n):
    word = input()
    error = 0
    for i in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[i] != word[i+1]:  # 연달은 두 문자가 다른 때,
            new = word[i+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new.count(word[i]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        count += 1  # error가 0이면 그룹단어
print(count)