# 완전탐색 모의고사
def solution(answers):
    answer = []
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0

    a_pat = [1, 2, 3, 4, 5]
    b_pat = [2, 1, 2, 3, 2, 4, 2, 5]
    c_pat = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, ans in enumerate(answers):
        a = a_pat[i % len(a_pat)] # 패턴이 나와있으면 패턴을 그냥 쓰고 그 길이로 나누자~!!!!
        b = b_pat[i % len(b_pat)] # 괜히 어렵게 i로 풀려고 하지말자
        c = c_pat[i % len(c_pat)]

        if a == ans: a_cnt += 1 # elif말고 if로 해야 모든 조건 다검사함
        if b == ans: b_cnt += 1
        if c == ans: c_cnt += 1

    max_cnt = max(a_cnt, b_cnt, c_cnt)
    if a_cnt == max_cnt:
        answer.append(1) # 빈 리스트에다가 오름차순 순서대로 추가하면 됨 슈바레;;;;
    if b_cnt == max_cnt:
        answer.append(2)
    if c_cnt == max_cnt:
        answer.append(3)

    return answer