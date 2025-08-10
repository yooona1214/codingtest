'''
n ~ 500 : O(n세제곱)
n ~ 2000: n제곱
n ~ 100,000 : nlogn
n ~ 10,000,000 : n

임의의 큰 수
그래프 알고리증에서
임의의 큰수 INF사용 = 1e9

파이썬에서 나누기 연산자 / 쓰면, 실수형 반환
나머지 연산자 % --> 홀수 인지
몫 연산자 //
거듭제곱연산자 **

'''

'''
리스트 컴프리 핸션
리스트안에 for 구문 넣기
a = [i for i in range(10) if i%2 ==1]

얘는 2차원 리스트 초기화 할 때 좋음 n*m 행일 때
arr = [[0] * m for _ in range(n)]  m = 3, n = 4 (행이 n 열이 n)
000
000
000
000

만약, arr = [ [0] * m ] * n 으로 만들면
a[1][1] = 5 로하면
050
050
050
050 이 되어버림

'''

'''
리스트 메서드 arr.메서드이름()
append() 1
sort(reverse=True) nlogn (디폴트 오름)
reverse() n
insert(인덱스, 값) n
count(특정값) n 특정값을 가지는 데이터의 개수
remove(특정값) n 특정값 가지는 원소 제거, 값을 가진 원소가 여러개면 하나만 제거 - 모두 제거하려면 별도로 코드를 작성
'''

'''
리스트에서 특정 값을 가지는 원소 모두 제거하기 remove_all 없음
--> remove_list에는 포함되지 않는 값만 저장하기
'''
# a = [1,2,3,4,5,5,5]
# remove_set = {3,5}

# remove_a = [i for i in a if i not in remove_set ]
# print(remove_a)

'''
튜플은 한번 선언된 값 변경 불가
리스트에 비해 상대적으로 공간 효율적
그럼 튜플은 언제쓰냐?
* 서로 다른 성질의 데이터를 묶어서 관리할때 
- 최단 경로 알고리즘에서 (비용, 노드번호) (학번, 성적)
- 집합 자료형에서 해싱의 키값으로 사용해야할 때
- 리스트보다 메모리를 효율적으로 사용해야할 때
'''

'''
사전 자료형 딕셔너리 O(1) {'': , }
리스트로 볼거면 list(a.keys())
a.values()
'''

'''
잡합자료형 set
중복 허용하지 않음, 순서가 없음
그래서 데이터가 존재하는지, 존재하지 않는지 여부를 확인할 때
data = {1,2,3}

data.add(4)
data.update([5,6])
'''

# data = {1,2,3}

# data.add(4)
# data.update({5,6,5}) # 이러면 그냥 5 1개만 들어감
# data.update([7,8])

# print(data)

'''
리스트나 튜플은 순서가 있으니까 인덱싱 쓸 때
딕셔너리나 셋은 순서가 없으니까 key나 원소로 O(1)이 필요할 때
'''

'''
입력 받는것 몇개 없을때
공백 기준 입력 받기 map() 리스트의 모든 원소에 각각 특정한 함수를 적용
list(map(int,input().split()))

입력 많이 빨리 받기
import sys
sys.stdin.readline().rstrip() 이진탐색, 그래프

'''

# a = list(map(int, input().split()))
# import sys

# a =sys.stdin.readline().rstrip()

# print(a)
'''
람다 함수 = 익명 함수(이름이 없는 함수)
자체를 또다른 입력으로 받을 때 유용, 혹은 한번만 사용될 때
print((lambda a, b: a+b)(3,7))
'''

'''
sorted() 라는 내장함수가 있음, 얘는 리스트의 메서드가 아님
list.sort()
sorted(data, key=some_function) 얘는 튜플 딕셔너리 set 다 가능 / 원본은 안 바뀜
data는 iterable이어야 함 → 예: list, tuple, set, 등등
some_function은 data의 각 요소에 대해 호출됨
즉, key 함수는 data 안의 "각 요소"를 하나씩 받아서, 그것을 기준값(key)으로 반환합니다
🔹 x는 data의 "각 원소" (즉, iterable의 단위)임.
'''
# arr = [('a', 50), ('b', 40)]

# arr_ = sorted(arr, key=lambda x: x[1])
# print(arr_)

'''
만약 sorted()의 조건이 두개면 key 함수에서 튜플로 주자. 파이썬의 튜플 비교는 자동으로 다음 순서로 넘어갑니다
data = [('a', 50), ('b', 40), ('c', 40), ('d', 30)]
#먼저 숫자(x[1]) 기준, 숫자가 같으면 알파벳(x[0]) 기준
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
print(sorted_data)

sorted(data, key=lambda x: -x[1])

딕셔너리 sort 방법
d = {'b': 3, 'a': 1, 'c': 2}

sorted_by_key = sorted(d.items())  # 기본은 key 기준 정렬 d.items()는 딕셔너리 안의 key, value 쌍을 튜플로 꺼내주는 메서드
print(sorted_by_key)  # [('a', 1), ('b', 3), ('c', 2)]

sorted_by_value = sorted(d.items(), key=lambda x: x[1])
print(sorted_by_value)  # [('a', 1), ('c', 2), ('b', 3)]

'''
# data = [('a', 50), ('b', 40), ('c', 40), ('d', 30)]
# print(sorted(data, key=lambda x: x[1])) # 오름차순
# print(sorted(data, key=lambda x: -x[1])) # 내림차순
# print(sorted(data, key=lambda x: (x[1], x[0]))) # 숫자 오름차순, 그리고 알파벳 오름차순

# data = [('Alice', 90), ('Bob', 90), ('Charlie', 80)]

# # 점수 오름차순 → 이름 알파벳 내림차순
# sorted_data = sorted(data, key=lambda x: (x[1], -ord(x[0][0])))

'''
itertools 순열 조합
heapq 우선순위 큐 다익스트라 최단 경로
bisect 이진탐색
collections deque, Counter 
math
'''

'''
모든 경우의 수를 고려할 때! itertools
순열 permutations nPr
조합 combitations nCr
중복순열 product
중복조합 combinations_with_replacement
'''
# from itertools import permutations, combinations
# data = ['a','b','c']

# perm = list(permutations(data, 3))
# comb = list(combinations(data,2))

# print(perm, comb)

'''
Counter
iterable 있을때, 내부 원소 몇개 있는지
c = Counter([리스트 좌라랄])
갯수 = c['원소이름']

'''

'''
최대 공약수
math.gcd()

최소 공배수
a*b//maht.gcd()
'''