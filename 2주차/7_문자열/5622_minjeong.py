a_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

t = 0
for unit in a_list :  
    for i in unit:  
        for x in word : 
            if i == x :
                t += a_list.index(unit) +3 
print(t)