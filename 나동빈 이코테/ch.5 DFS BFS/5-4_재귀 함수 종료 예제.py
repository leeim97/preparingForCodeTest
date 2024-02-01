def recursive_f(i):
    if i==101:
        return print('재귀함수 종료')
    print(f'{i}번째 재귀 함수를 호출')
    return recursive_f(i+1)

recursive_f(1)