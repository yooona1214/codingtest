'''
지금 당장 탐욕적인 최선의 방법을 탐색
'''

## 1이 될때까지
# N 1~100,000 K 2 ~ 100,000 둘다 자연수
# Q) 첫째 줄에 N이 1이 될때 까지 [1. 1을빼거나 / 2. K로 나누거나]을 수행해야 하는 횟수의 최솟값 출력
# 시간제한 2초, 메모리 제한 128mb

def solution(N, K):
    
    # 생각, N에서 1을 뺀다. 언제까지? K로 나눠질때까지 
    # 그리고 계속 반복. 1이 될때까지
    cnt = 0
    while N != 1:
        trash = N % K    
        if trash == 0:
            N = N/K
        else:
            N -=1
        cnt +=1
    

    return cnt

print(solution(25, 5))


## 곱하기 혹은 더하기
# 각자리가 숫자 인 문자열 S
# 숫자 사이에 x, + 만 넣어서 만들 수 있는 가장 큰수
# 연산은 가장 왼쪽 부터
# S길이 1~ 20

def solution(S):
    
    result = 0
    
    for i in range(len(S)-1):
        
        if i == 0 :
            result = int(S[i])
            
        plus = result + int(S[i+1])
        mul = result * int(S[i+1])
        
        result = max(plus, mul)       
    
    return result

print(solution("567"))


## 모험가 길드
# N명 공포도 X, X인애들은 X명 이상, 최대 몇개의 그룹
# 꼭 N명 다 그룹이 아니어도 됨, 낙동강 오리알 가능

def solution(N,X_list):
    # 생각
    # sort 작은 애들 부터 그룹을 해야 최대한 많이 생김
    # 현재 인덱스의 X를 기준으로 그만큼 추가하고, 추가하는 X의 공포도랑 현재 인원수 확인
    # 얘는 지금 공포도랑, 인원수를 모두 비교해야하니까, 두가지 변수(공포도랑, 인원수)로 비교하고
    # 그룹이 결성되면 그걸 cnt에 추가.
    
    return


## 상하좌우
def solution(N,plans):
    mv = ['l','r','u','d']
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    x,y =1,1
    for plan in plans:
        # 이동 후 좌표 구하기
        # 4개 중 맞는 인덱스를 매 plan 찾아서 그 인덱스 값 만큼 증가 시켜주자
        for i in range(len(mv)):
            if plan ==mv[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny< 1 or nx>N or ny > N:
            continue
        
        x , y = nx, ny
            
    
    return


## 시각
# 3이 들어간 모든 경우의 수 , N시 기준
# N까지의 전체 경우의수 - 3이 없는 모든 경우의 수
# 분기 나누기 - 3일 때 / 3이 아닌 한자리 수 시간 / 23 / 10~22
# 00시 00분 00 초
# 분까지 고려한 전체 경우의 수 6*10*6*10 - 5*9*5*9
# 쉣 이건 너무 수학적

# 파이썬은 1초에 20,000,000 2천만번 계산
# 이건 완전탐색 문제
# 가능한 경우의 수 모두 확인 24*60*60
# 완전 탐색가능한지 아닌지 먼저 확인해보자
# 그냥 00 00 00 에 1씩 더하면서 3이 포함되는지만 체크


## 왕실의 나이트

def solution(coor):
    row = ['a','b','c','d','e','f','g','h']
    # x 구하기
    for i in range(len(row)):
        if row[i] == coor[0]:
            x = i+1
    
    y = int(coor[1])
    # print(x,y)
    
    # 동서남북 * 좌우
    dx = [1,-1,1,-1,2,2,-2,-2] 
    dy = [2,2,-2,-2,1,-1,1,-1]
    # 이렇게 말고 [(1,2), ---] 이렇게 방향벡터 쌍으로 나둬도 됨
    
    
    # cnt
    cnt = 0
    
    # 체크
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        # print(nx, ny)
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            # print('pass')
            continue
        
        cnt +=1
    
    return cnt
    
print(solution("a1"))


## 문자열 재정렬
# 문자인지 숫자인지 확인하는 문법. 
# x.isalpha()
def solution(inp):
    inp_list = list(inp)
    result  = []
    for i in inp_list:
        if i.isalpha():
            result.append(i)
        else:
            value += int(i)
    
    return
