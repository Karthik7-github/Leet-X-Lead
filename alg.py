a=[]
score=[10,3,9,8,4]
s=[i for i in score]
score.sort()
score.reverse()
for i in s:
    if score.index(i)+1==1:
        a.append("Gold Medal")
    elif score.index(i)+1==2:
        a.append("Silver Medal")
    elif score.index(i)+1==3:
        a.append("Bronze Medal")
    else:
        k=str(score.index(i)+1)
        a.append(k)
print(a)