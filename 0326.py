#BFS
'''
너비 우선 탐색
맹목적인 탐색
최단 경로를 찾을 때, 최단 길이를 보장해야 할 때

Method: queue - 먼저 들어온 값을 먼저 처리해준다는 특징때문에 사용
1. 큐는 탐색할 노드 정보를 넣는 용(그래프의 구조에 따른 breath를 기반으로 탐색해야해서)
2. 큐에 넣어서 방문을 할 후보라고 생각
3. 큐에서 값을 뽑았다는 건 방문을 했다는 의미니까, 그 결과를 새로운 리스트에 방문했다고 저장
3. 더이상 방문할 곳이 없을때(= 큐가 비었을 때) 까지 반복
'''

from collections import deque

# n번째 노드가 연결된 다른 노드들 (n = 1~8)
graph = [
    [], #0 : 직관적으로 하려고 0은 빈 리스트로 만들어 줌
    [2, 3], #1
    [1, 8], #2
    [1, 4, 5], #3
    [3, 5], #4
    [3, 4], #5
    [7, 8], #6
    [6, 8], #7
    [2, 6, 7] #8
]

visited = [False]*9 # [False, False, False, False, False, False, False, False, False]


def bfs(graph, node, visited): # node : int
    # 맨 처음 넣을 노드번호를 시작으로 큐를 생성
    # 큐는 이미 방문한 노드들. 난 얘네를 뽑아서 연접노드를 방문해야함
    queue = deque([node]) 
    # visited 리스트는 탐색한 결과 저장 리스트 --> 얘는 다시는 보지 않을 친구들
    visited[node] = True

    # 방문한노드의 연접노드가 없을때까지 시도
    while queue:
        # 연접노드를 확인해야할 이미 방문한 제일 오래된 인덱스 뽑기
        # 이 노드까지 가봤다. 방문했다.
        v = queue.popleft()
        print('v: ', v)

        # v의 연접 노드들 방문하기 얘네는 아직 방문 안한애들
        for i in graph[v]:
            if not (visited[i]):
                # 안방문한걸 알았으므로 방문한거니까 리스트 값 바꾸기
                visited[i] = True
                # 방문한 노드는 큐 뒤에 추가 -> 이제 얘네의 연접 노드를 봐야함
                queue.append(i) 


bfs(graph, 1, visited)
    