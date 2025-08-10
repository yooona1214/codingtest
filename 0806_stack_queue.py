# ✅ 스택 (Stack)
# 📌 개념 요약
# “뒤에서 넣고, 뒤에서 뺀다”
# → 후입선출(Last In, First Out, LIFO)

stack = []
stack.append(1)   # push
stack.append(2)
stack.pop()       # pop → 2

# ✅ 큐 (Queue)
# 📌 개념 요약
# “앞에서 빼고, 뒤에 넣는다”
# → 선입선출(First In, First Out, FIFO)

from collections import deque
queue = deque()
queue.append(1)       # enqueue
queue.append(2)
queue.popleft()       # dequeue → 1

# 스택에 값이 있을 때만 pop하고 없을 땐 예외처리 하는 법 if stack
if stack:
    stack.pop()
else:
    # 예외 상황 처리
    print("스택이 비어있어요!")
    
'''
import math
math.ceil(x)	올림	math.ceil(2.1) → 3
math.floor(x)	내림	math.floor(2.9) → 2
round(x)	반올림 (0.5 기준)	round(2.5) → 2, round(3.5) → 4
int(x)	버림 (소수점 이하 제거)	int(3.9) → 3
'''

'''
두개의 길이가 같은 리스트1,2끼리 인덱스 별로 연산을 할 때는
map() + lambda를 사용
list(map(lambda x,y: f(x,y), 리스트1, 리스트2))


for p, s in zip(progresses, speeds):
아니면 이렇게 for 구문으로 zip 돌리면 괜춘

queue =  [(i,p) for i,p in enumerate(priorities)]
priorities 의 길이만큼 i 번째 p 의값을 할때는 enumerate로 하자
'''

# 기능 개발 문제
from math import ceil
from collections import deque

# 내풀이 queue 원리이지만 리스트로 품 
def solution(progresses, speeds):
    result = []
    day = list(map(lambda x,y : ceil((100-x)/y), progresses, speeds)) # 복잡도 n
    bp_day = day[0] # 이게 deque에서 popleft랑 동일
    bp_count = 0

    for i in day: # 복잡도 n
        if i <= bp_day:
            bp_count += 1        
        elif i > bp_day:
            bp_day = i 
            result.append(bp_count)
            bp_count = 1

    result.append(bp_count)
    return result
# deque로 풀었을 때
def solution(progresses, speeds):
    queue = deque([ceil((100 - p) / s) for p, s in zip(progresses, speeds)])
    result = []

    while queue:
        day = queue.popleft()
        count = 1

        while queue and queue[0] <= day:
            queue.popleft()
            count += 1

        result.append(count)

    return result


'''
특정 리스트나 큐에서 어떤 값이 조건을 만족하는지 보는 빠른 방법
하나라도 조건 만족	any(x > 기준값 for x in q)
전부 조건 만족	all(x > 기준값 for x in q)

'''


from collections import deque
def solution(priorities, location): 
    p_que = deque((x, y) for x, y in zip(priorities, range(len(priorities))))
    # print(p_que)
    count = 0

    while p_que:
        p = p_que.popleft()

        if p_que and any(p[0] < p_[0] for p_ in p_que):
            p_que.append(p)
        else:
            count += 1
            if p[1] == location:
                return count