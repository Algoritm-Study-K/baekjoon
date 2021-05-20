def star(n):
    if n==3:
        print('***')
        print('* *')
        print('***')
    else:
        return star(n/3)


n=int(input())
star(n)