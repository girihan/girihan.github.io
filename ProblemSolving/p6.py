from collections import Counter

'''
5 4
3 1
3 2
4 3
5 3
'''
N, M = map(int, input().split())

A = list() # mentee
B = list() # mentor
answer = list()

for i in range(M):
    mentee, mentor = map(int, input().split())
    A.append(mentee)
    B.append(mentor)

most_mentor = (Counter(B).most_common(1)[0])[0] # 멘티를 가장 많이 가지고 있는 멘토

for idx, m in enumerate(A):
    if m == most_mentor:
        answer.append(B[idx])

for n in answer:
    print(n, end=' ')
