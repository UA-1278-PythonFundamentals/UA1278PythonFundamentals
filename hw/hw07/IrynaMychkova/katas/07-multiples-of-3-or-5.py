def solution(number):
    return sum([n for n in range(number) if n % 3 == 0 or n % 5 == 0])

print(solution(10))  # 23
print(solution(20))  # 78