'''
list(map()) 써보기
-> 여러 개의 값을 한꺼번에 변환(형변환, 계산 등)
-> map은 iterable에 나오는 값들을 순차적으로 한번에 함수를 적용한 것
list(map(함수, iterable))
함수: 각 요소에 적용할 함수 (예: int, str, lambda x: x + 1)
iterable: 리스트, 튜플, 문자열, input().split() 등
'''
## k번째 수, i,j,k
#### lambda x가 뭐가 될 지 생각해봐라
#### 얜 map으로 commands 2차원 배열안에 있는 모든 1차원 배열 값들을 가져오는게 핵심

# commands가 2차원 배열이고 각 안에있는 리스트마다 모든 원소값들을 arr에 적용해야함
# 그리고 그 값을 list에 넣어야 하기 때문에, lambda의 x 는 commands의 안의 1차원 배열
# 여기서 commands의 각 원소들 [2,5,3] 이런게 x로 대응되고, 그 뒤에 나오는 : 뒤의 함수가 리스트 안에 저장됨
def solution(array, commands):
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer  = list(map(lambda x: sorted(array[x[0]-1: x[1]])[x[2]-1], commands)) # map을 썼기 때문에 람다 뒤에 iterable이 나오는것
    return answer



## 문자열 정렬 strings ["sun", "bed", "car"] n 2
#### 얘는 string의 n번째가 sort 기준이고, 문자열로 한번 더 정렬하는게 핵심
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n],x)) 


## 가장 큰수 문제
#### 정석 cmp_to_key 가 핵심
# compare('3', '30') → '330' > '303' → '3'이 앞
# compare('30', '34') → '3034' < '3430' → '34'이 앞
# compare('5', '9') → '59' < '95' → '9'이 앞
from functools import cmp_to_key
def compare(x,y): # x,y 모두 str
    if x+y > y+x: 
        return -1 # x+y
    elif y+x > x+y:
        return 1 # y+x
    else:
        return 0 # 둘다 같음

def solution(numbers):
    # 가장 첫자리가 큰 숫자부터 더하기
    numbers = list(map(str,numbers))
    num = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join(num) #'구분자'.join(리스트) 리스트안에 있는 모든 요소들을 구분자로 엮어서 str 타입으로 변환하는 것
    return answer if answer[0] != '0' else '0'

#### 트릭 이용
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# numbers = [3, 30, 34, 5, 9, 321, 320]
#    3 → 333
#   30 → 303030
#   34 → 343434
#    5 → 555
#    9 → 999
#  321 → 321321321
#  320 → 320320320

# 파이썬에서 문자열 숫자를 비교할땐 앞자리수부터 사전적으로 비교함
# 만약 3, 30 이면 3 < 30
# 앞자리가 같으면 3이 더 길이가 짧으니까 30이 더 김
# 5, 30 이면 5 > 30
# print("31">"30")

# 아무튼 그래서 큰 순서대로라는 의미는, 단순히 맨 앞자리가 큰게 아니라, 큰거부터 나열하되,
# 만약에 같은 부분이 곂치는 숫자들이 있을 때,그 다음 숫자가 더 큰것부터 나열해야함
# 그러니까 이걸 자릿수가 3개니까 그걸 모두 공평하게 보기위해 세번 곱함
# 예를들어 9, 90, 991 로보면 9 991 90 이렇게 되야함
# 근데 맨 첫자리 비교하고 나머지 차례로 봐야함 ascii 구조로 비교하니까
# 991 > 90 > 9 임
# 세번 곱하면 999 909090 991991991 이니까
# 9 991 90 가능 
# 현재 내 숫자가 더 쎄다라는 걸 증명하려면 최소 자리수 * n = 최대 자리수 가 될만큼 n번 곱해서 비교




