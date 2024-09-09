from collections import deque


# BFS
# def solution(numbers, target):
#     answer = 0
#     leaves = deque([0])

#     for i in numbers:
#         temp = []
#         while leaves:
#             leaf = leaves.popleft()
#             temp.append(leaf+i)
#             temp.append(leaf-i)
#         leaves = deque(temp)

#     for leaf in leaves:
#         if leaf == target:
#             answer +=1

#     return answer

# DFS
def solution(numbers, target):
    answer = 0
    answer = DFS(numbers, target, 0)

    return answer


def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            answer += 1
            return 1
        else:
            return 0

    else:
        answer += DFS(numbers, target, depth + 1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth + 1)
        return answer

