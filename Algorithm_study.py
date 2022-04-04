## 자료구조 1

#스택
# import sys
# input = sys.stdin.readline
# stack = []
# N = int(input())
# for _ in range(N):
#     a = input().split()
#     if a[0] == "push":
#         stack.append(int(a[1]))
#     elif a[0] == "pop":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif a[0] == "size":
#         print(len(stack))
#     elif a[0] == "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])

#단어뒤집기
# t = int(input())
# for _ in range(t):
#     text = input().split()
#     for word in text:
#         print(word[::-1], end = " ")
#     print("")

#괄호
# t = int(input())
# for _ in range(t):
#     stack = []
#     a = list(input())
#     for i in a:
#         if i == "(":
#             stack.append(i)
#         else:
#             if len(stack) == 0:
#                 stack.append(i)
#             elif stack[-1] == "(":
#                 stack.pop()
#             else:
#                 stack.append(i)
#     if len(stack) == 0:
#         print("YES")
#     else:
#         print("NO")

#스택 수열
# n = int(input())
# num_li = []
# for _ in range(n):
#     num_li.append(int(input()))
# i = 0
# num = 1
# stack = []
# answer = []
# while i != n:
#     if num > n + 1:
#         break
#     if len(stack) == 0:
#         stack.append(num)
#         answer.append("+")
#         num += 1
#     elif stack[-1] == num_li[i]:
#         stack.pop()
#         answer.append("-")
#         i += 1
#     else:
#         stack.append(num)
#         answer.append("+")
#         num += 1
    
# if len(stack) == 0:
#     for i in answer:
#         print(i)
# else:
#     print("NO")

#에디터
# import sys
# input = sys.stdin.readline

# sen_left = list(input().strip()) 
# sen_right = []
# M = int(input())
# for _ in range(M):
#     c = input().split()
#     if c[0] == "L":
#         if len(sen_left) != 0:
#             sen_right.append(sen_left.pop())
#     elif c[0] == "D":
#         if len(sen_right) != 0:
#             sen_left.append(sen_right.pop())
#     elif c[0] == "B":
#         if len(sen_left) != 0:
#             sen_left.pop()
#     else:
#         sen_left.append(c[1])
# print("".join(sen_left + list(reversed(sen_right))))

#큐
# import sys
# input = sys.stdin.readline
# n = int(input())
# q = []
# for i in range(n):
#     a = input().split()
#     if a[0] == "push":
#         q.append(a[1])
#     elif a[0] == "pop":
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[0])
#             s = q[0]
#             q.remove(s)
#     elif a[0] == "size":
#         print(len(q))
#     elif a[0] == "empty":
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == "front":
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[0])
#     else:
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[-1])

#조세푸스 문제
# n, k = map(int, input().split())
# arr = [i for i in range(1, n + 1)]
# answer = []
# num = k - 1

# for i in range(n):
#     if len(arr) > num:
#         answer.append(arr.pop(num))
#         num += k - 1
#     elif len(arr) <= num:
#         num = num % len(arr)
#         answer.append(arr.pop(num))
#         num += k -1
        
# print("<", ', '.join(str(i) for i in answer), ">", sep = '')

##자료구조 1(연습)

#단어 뒤집기2
# s = list(input())
# i = 0
# start = 0
# while i <= len(s) - 1:
#     if s[i] == "<":
#         while s[i] != ">":
#             i += 1
#         i += 1
#     elif s[i].isalnum():
#         start = i
#         while i != len(s) and s[i].isalnum():
#             i += 1
#         tmd = s[start:i]
#         tmd.reverse()
#         s[start:i] = tmd
#     else:
#         i += 1
# print("".join(s))

#쇠막대기
# s = list(input())
# answer = 0
# stack = []
# for i in range(len(s)):
#     if s[i] == "(":
#         stack.append(s[i])
#     elif s[i] == ")":
#         if s[i - 1] == "(":
#             stack.pop()
#             answer += len(stack)
#         else:
#             stack.pop()
#             answer += 1
# print(answer)

#오큰수
# N = int(input())
# s = list(map(int, input().split()))
# stack = []
# answer = []
# for i in s[::-1]:
#     if len(stack) == 0:
#         stack.append(i)
#         answer.append(-1)
#     else:
#         if i < stack[-1]:
#             answer.append(stack[-1])
#             stack.append(i)
#         else:
#             while stack and i >= stack[-1]:
#                 stack.pop()
#             if stack:
#                 answer.append(stack[-1])
#             else:
#                 answer.append(-1)
#             stack.append(i)
# answer.reverse()
# answer = list(map(str, answer))
# print(" ".join(answer))

#오등큰수
# N = int(input())
# s = input().split()
# dic = {}
# for i in s:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# stack = []
# answer = []
# for i in s[::-1]:
#     if len(stack) == 0:
#         stack.append(i)
#         answer.append(-1)
#     else:
#         if dic[i] < dic[stack[-1]]:
#             answer.append(stack[-1])
#             stack.append(i)
#         else:
#             while stack and dic[i] >= dic[stack[-1]]:
#                 stack.pop()
#             if stack:
#                 answer.append(stack[-1])
#             else:
#                 answer.append(-1)
#             stack.append(i)
# answer.reverse()
# answer = list(map(str, answer))
# print(" ".join(answer))

##자료구조식1(참고)

#후위표기식
# N = int(input())
# s = list(input())
# num = [0] * N
# for i in range(N):
#     num[i] = int(input())
# stack = []
# for i in s:
#     if i.isalpha():
#         stack.append(num[ord(i) - 65])
#     else:
#         b = stack.pop()
#         a = stack.pop()
#         if i == "*":
#             stack.append(a * b)
#         elif i == "/":
#             stack.append(a / b)
#         elif i == "+":
#             stack.append(a + b)
#         elif i == "-":
#             stack.append(a - b)
# print("{:.2f}".format(stack[0]))

#알파벳 세기
# s = list(input())
# answer = []
# for i in range(26):
#     answer.append(s.count(chr(i + 97)))
# print(" ".join(map(str, answer)))

#알파벳 찾기
# s = list(input())
# answer = [-1] * 26
# for i in range(len(s)):
#     a = ord(s[i]) - 97
#     if answer[a] == -1:
#         answer[a] = i 
# print(" ".join(map(str, answer)))

#문자열 분석
# import sys
# input = sys.stdin.readline
# while True:
#     s = list(input().rstrip("\n"))
#     if not s:
#         break
#     small, large, num, empty = 0, 0, 0, 0
#     for word in s:
#         if word.islower():
#             small += 1
#         elif word.isupper():
#             large += 1
#         elif word.isdigit():
#             num += 1
#         else:
#             empty += 1
#     print(small, large, num, empty)

#단어 길이 재기
# s = input()
# print(len(s))

#ROT13
# s = list(input())
# for i in range(len(s)):
#     if s[i].isupper():
#         if ord(s[i]) <= 77:
#             s[i] = chr(ord(s[i]) + 13)
#         else:
#             s[i] = chr(65 + ord(s[i]) + 13 - 91)
#     elif s[i].islower():
#         if ord(s[i]) <= 109:
#             s[i] = chr(ord(s[i]) + 13)
#         else:
#             s[i] = chr(97 + ord(s[i]) + 13 - 123)
# print("".join(s))

#네 수 
# a, b, c, d = map(str, input().split())
# A = int(a + b)
# B = int(c + d)
# print(A + B)

#접미사 배열
# s = input()
# li = []
# for i in range(len(s)):
#     li.append(s[i:])
# li.sort()
# for word in li:
#     print(word)

##수학1

#나머지
# A, B, C = map(int, input().split())
# print((A + B) % C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep = "\n")

#최대공약수와 최소공배수
# a, b = map(int, input().split())
# a1, b1 = a, b
# while b != 0:
#     a, b = b, a % b
# print(a)
# print(a1 * b1 // a)

#소수 찾기
# n = int(input())
# num_li = list(map(int, input().split()))
# count = n
# for num in num_li:
#     if num == 1:
#         count -= 1
#     elif num == 2:
#         continue
#     else:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 count -= 1
#                 break
# print(count)

#소수구하기
# n, m = map(int, input().split()) #에라토스테네스의 체
# li = [True] * (m + 1)
# li[1] = False
# for i in range(2, m + 1):
#     if li[i]:
#         for j in range(2 * i, m + 1, i):
#             li[j] = False
# for i in range(n, m + 1):
#     if li[i]:
#         print(i)

#골드바흐의 추측
# li = [True] * (1000001)
# li[1] = False
# for i in range(2, 1001):
#     if li[i]:
#         for j in range(2 * i, 1000001, i):
#             li[j] = False
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     for i in range(3, n//2 + 1):
#         i, j = i, n - i
#         if li[i] and li[j]:
#             break
#     print(str(n), "=", str(i), "+", str(j))

#팩토리얼
# n = int(input())
# answer = 1
# for i in range(n, 0, -1):
#     answer *= i
# print(answer)

#팩토리얼 0의 갯수
# n = int(input())
# answer = 1
# for i in range(n, 0, -1):
#     answer *= i
# answer = list(str(answer))
# cnt = 0
# while True:
#     if answer.pop() == "0":
#         cnt += 1
#     else:
#         break
# print(cnt)

#조합 0의 개수
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# m = min(m, n-m)
# a = 1
# b = 1
# for i in range(n, n - m, -1):
#     a *= i 
# for i in range(m, 0, -1):
#     b *= i
# answer = a // b
# answer = list(str(answer))
# cnt = 0
# while True:
#     if answer.pop() == "0":
#         cnt += 1
#     else:
#         break
# print(cnt)

#수학 1(연습)

#GCD 합
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
# n = int(input())
# for _ in range(n):
#     answer = []
#     s = list(map(int, input().split()))
#     for i in range(1, s[0] + 1):
#         for j in range(i + 1, s[0] + 1):
#             answer.append(gcd(s[i], s[j]))
#     print(sum(answer))

#숨바꼭질 6
# import sys
# input = sys.stdin.readline
# n, s = map(int, input().split())
# place = list(map(int, input().split()))
# for i in range(len(place)):
#     place[i] = abs(s - place[i])
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
# if len(place) >= 2:
#     answer = place[0]
#     for i in range(1, len(place)):
#         answer = gcd(answer, place[i])
#     print(answer)
# else:
#     print(place[0])

#2진수 8진수
# n = int(input(), 2)
# print("{0:o}".format(n))

#8진수 2진수
# n = int(input(), 8)
# print("{0:b}".format(n))

#-2진수 (잘 모르겠음;;)
# import sys
# input = sys.stdin.readline

# N = int(input())

# if not N:
#     sys.stdout.write('0')
#     exit()
# res = ""
# while N:
#     # print(N)
#     if N % (-2):
#         res = '1' + res
#         N = N //- 2 + 1
#     else:
#         res = '0' + res
#         N //= -2

# sys.stdout.write(res)

#골드바흐 파티션
# import sys
# input = sys.stdin.readline

# t = int(input())
# nums = []
# for _ in range(t):
#     nums.append(int(input()))
# li = [True] * 1000001

# m = max(nums)
# for i in range(2, int(m ** 0.5) + 1):
#     if li[i] == True:
#         for j in range(2 * i, m + 1, i):
#             li[j] = False
            
# for n in nums:
#     cnt = 0
#     for i in range(2, n // 2 + 1):
#         if li[i] and li[n - i]:
#             cnt += 1
#     print(cnt)

#수학 1(참고)

#진법 변환2
# n, b = map(int, input().split())
# answer = ""
# while n >= 1:
#     k = n % b 
#     if k <= 9:
#         answer = str(k) + answer
#     else:
#         answer = chr(k + 55) + answer
#     n //= b
# print(answer)

#진법 변환
# n, b = input().split()
# b = int(b)
# answer = 0
# for i in n:
#     if i.isalpha():
#         num = ord(i) - 55
#         answer = answer * b + num
#     else:
#         answer = answer * b + int(i)
# print(answer)

#Base conversion
# a, b = map(int, input().split())
# m = int(input())

# num_li = list(map(int, input().split()))
    
# num_10 = 0
# for i in num_li:
#     num_10 = num_10 * a + i
    
# answer = []
# while num_10 >= 1:
#     answer.append(num_10 % b)
#     num_10 //= b
# answer.reverse()
# print(" ".join(map(str, answer)))

#소인수 분해
# n = int(input())
# if n == 1:
#     exit()
# while n != 1:
#     i = 2
#     while n % i != 0:
#         i += 1
#     print(i)
#     n //= i

#다이내믹 프로그래밍 1

#1로 만들기
# n = int(input())
# dp = [0] * (n + 1)

# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)
# print(dp[n])

#2xn 타일링
# n = int(input())
# dp = [0] * (1001)
# dp[1] = 1
# dp[2] = 2
# for i in range(3, 1001):
#     dp[i] = dp[i - 2] + dp[i - 1]
# print(dp[n] % 10007)

#2xn 타일링2
# n = int(input())
# dp = [0] * (1001)
# dp[1] = 1
# dp[2] = 3
# for i in range(3, 1001):
#     dp[i] = dp[i - 2] * 2 + dp[i - 1]
# print(dp[n] % 10007)

#1,2,3 더하기
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     dp = [0] * 11
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4
#     for i in range(4, 11):
#         dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
#     print(dp[n])

#카드 구매하기
# n = int(input())
# card = [0] + list(map(int, input().split()))
# dp = [0] * (n + 1)
# dp[1] = card[1]
# for i in range(2, n + 1):
#     for j in range(0, i + 1):
#         if dp[i] <= dp[j] + card[i - j]:
#             dp[i] = dp[j] + card[i - j]
# print(dp[n])

#카드 구매하기2
# n = int(input())
# card = [0] + list(map(int, input().split()))
# dp = [0] * (n + 1)
# dp[1] = card[1]
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + card[1]
#     for j in range(0, i):
#         if dp[i] >= dp[j] + card[i - j]:
#             dp[i] = dp[j] + card[i - j]
# print(dp[n])

#1,2,3 더하기 5
# import sys
# input = sys.stdin.readline
# t = int(input())
# dp = []
# for _ in range(100001):
#     dp.append([0, 0, 0, 0])
# dp[1] = [0, 1, 0, 0]
# dp[2] = [0, 0, 1, 0]
# dp[3] = [0, 1, 1, 1]

# for i in range(4, 100001):
#     dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
#     dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
#     dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009

# for _ in range(t):
#     n = int(input())
#     print(sum(dp[n]) % 1000000009)

#쉬운 계단 수
# n = int(input())
# dp = []
# for i in range(101):
#     dp.append([0] * 10)
# dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# for i in range(2, 101):
#     dp[i][0] = dp[i - 1][1]
#     for j in range(1, 9):
#         dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
#     dp[i][9] = dp[i - 1][8]
# print(sum(dp[n]) % 1000000000)

#이친수
# n = int(input())
# dp = [0, 1]
# for i in range(1, n):
#     dp = [dp[0] + dp[1], dp[0]]
# print(sum(dp))

#가장 긴 증가하는 부분 수열
# n = int(input())
# num_li = list(map(int, input().split()))
# dp = [1] * (n + 1)
# for i in range(n):
#     for j in range(i):
#         if num_li[i] > num_li[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

#가장 긴 증가하는 부분 수열4
#풀이 1
# n = int(input())
# num_li = list(map(int, input().split()))
# dp = []
# for i in range(n):
#     dp.append([num_li[i]])
# for i in range(n):
#     for j in range(i):
#         if num_li[i] > num_li[j]:
#             if len(dp[i]) < len(dp[j]) + 1:
#                 dp[i] = dp[j] + [num_li[i]]
# ix = []
# for i in range(n):
#     ix.append(len(dp[i]))
# print(max(ix))
# a = ix.index(max(ix))
# print(" ".join(map(str, dp[a])))

#풀이 2
# n = int(input())
# num_li = list(map(int, input().split()))
# dp = [1] * (n)
# for i in range(n):
#     for j in range(i):
#         if num_li[i] > num_li[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))
# k = len(dp) - 1
# m = max(dp)
# answer = []
# while k >= 0:
#     a = dp.pop()
#     if a == m:
#         answer.append(k)
#         m -= 1
#     k -= 1
# real_ans = []
# for i in answer[::-1]:
#     real_ans.append(num_li[i])
# print(" ".join(map(str, real_ans)))

#연속합
# n = int(input())
# li = list(map(int, input().split()))
# dp = [li[0]] + [0] * (n - 1)
# for i in range(1, len(li)):
#     a = max(li[i], li[i] + dp[i - 1])
#     dp[i] = a
# print(max(dp))

#제곱수의 합
# import sys
# input = sys.stdin.readline
# n = int(input())
# dp = [0] * (n + 1)
# for i in range(1, n + 1):
#     dp[i] = i
#     for j in range(1, int(i ** 0.5) + 1):
#         if dp[i] > dp[i - j * j] + 1:
#             dp[i] = dp[i - j * j] + 1
# print(dp[n])

#합분해
# n, k = map(int, input().split())
# dp = []
# for i in range(n + 1):
#     dp.append([0] * (k + 1))
# dp[0][0] = 1
# for i in range(0, n + 1):
#     for j in range(1, k + 1):
#         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# print(dp[n][k] % 1000000000)

#1, 2, 3 더하기 3
# dp = [0] * (1000001)
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# for j in range(4, 1000001):
#     dp[j] = (dp[j - 1] + dp[j - 2] + dp[j - 3]) % 1000000009
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(dp[n] % 1000000009)

#RGB 거리
# n = int(input())
# rgb = []
# for _ in range(n):
#     rgb.append(list(map(int, input().split())))
# dp = []
# for _ in range(n):
#     dp.append([0] * 3)
# dp[0] = rgb[0]
# for i in range(1, n):
#     dp[i][0] = rgb[i][0] + min(dp[i - 1][1], dp[i - 1][2])
#     dp[i][1] = rgb[i][1] + min(dp[i - 1][0], dp[i - 1][2])
#     dp[i][2] = rgb[i][2] + min(dp[i - 1][0], dp[i - 1][1])
# print(min(dp[n - 1]))

#동물원
# n = int(input())
# dp = []
# for _ in range(n + 1):
#     dp.append([0] * 3)
# dp[1] = [1, 1, 1]
# for i in range(2, n + 1):
#     dp[i][0] = sum(dp[i - 1]) % 9901
#     dp[i][1] = (sum(dp[i - 1]) - dp[i - 1][1]) % 9901
#     dp[i][2] = (sum(dp[i - 1]) - dp[i - 1][2]) % 9901
# print(sum(dp[n]) % 9901)

#오르막수
# n = int(input())
# dp = []
# for _ in range(n + 1):
#     dp.append([0] * 10)
# dp[1] = [1] * 10
# for i in range(2, n + 1):
#     for j in range(10):
#         dp[i][j] = sum(dp[i - 1][:j + 1]) % 10007
# print(sum(dp[n]) % 10007)

#스티커
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     sticker = [list(map(int, input().split())), list(map(int, input().split()))]
#     dp = []
#     for __ in range(n + 1):
#         dp.append([0, 0, 0])
#     dp[1] = [0, sticker[0][0], sticker[1][0]]
#     for i in range(2, n + 1):
#         dp[i][0] = max(dp[i - 1])
#         dp[i][1] = max(dp[i - 1][0] + sticker[0][i - 1], dp[i - 1][2] + sticker[0][i - 1])
#         dp[i][2] = max(dp[i - 1][0] + sticker[1][i - 1], dp[i - 1][1] + sticker[1][i - 1])
#     print(max(dp[n]))

#포도주 시식
# n = int(input())
# wine = [0]
# for _ in range(n):
#     wine.append(int(input()))
# dp = [0] * (n + 1)
# dp[1] = wine[1]
# if n > 1:
#     dp[2] = wine[1] + wine[2]
# for i in range(3, n + 1):
#     dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])
# print(dp[n])

#정수 삼각형
# n = int(input())
# tr = [[0]]
# for _ in range(n):
#     tr.append([0] + list(map(int, input().split())))
# dp = [[0]]
# for i in range(1, n + 1):
#     dp.append([0] * (n + 1))
# dp[1] = tr[1]
# for i in range(2, n + 1):
#     dp[i][1] = tr[i][1] + dp[i - 1][1]
#     dp[i][i] = tr[i][i] + dp[i - 1][i - 1]
#     for j in range(2, i):
#         dp[i][j] = tr[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
# print(max(dp[n]))
        
#가장 큰 증가 부분 수열
# n = int(input())
# arr = [0] + list(map(int, input().split()))
# dp = [0] * (n + 1)
# dp[1] = arr[1]
# for i in range(2, n + 1):
#     dp[i] = arr[i]
#     for j in range(1, i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + arr[i])
# print(max(dp))

#가장 긴 감소하는 부분 수열
# n = int(input())
# arr = [0] + list(map(int, input().split()))
# dp = [1] * (n + 1)
# for i in range(2, n + 1):
#     for j in range(1, i):
#         if arr[i] < arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

#가장 긴 바이토닉 부분 수열
# n = int(input())
# a = list(map(int, input().split()))
# arr = [0] + a
# arr2 = [0] + a[::-1]
# dp1 = [1] * (n + 1)
# dp2 = [1] * (n + 1)
# for i in range(2, n + 1):
#     for j in range(1, i):
#         if arr[i] > arr[j]:
#             dp1[i] = max(dp1[i], dp1[j] + 1)
#         if arr2[i] > arr2[j]:
#             dp2[i] = max(dp2[i], dp2[j] + 1)
# dp = []
# for i in range(1, n + 1):
#     dp.append(dp1[i] + dp2[-i])
# print(max(dp) - 1)

#연속합 2
# n = int(input())
# arr = [0] + list(map(int, input().split()))
# answer = arr[1]
# dp = []
# for _ in range(2):
#     dp.append([0] * (n + 1))
# dp[0][1] = arr[1]
# dp[1][1] = 0
# for i in range(2, n + 1):
#     dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
#     dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
#     answer = max(dp[0][i], dp[1][i], answer)
# print(answer)

#타일 채우기
# n = int(input())
# dp = [0] * (n + 1)
# if n > 1:
#     dp[2] = 3
# for i in range(4, n + 1, 2):
#     dp[i] = dp[i - 2] * 3
#     for j in range(2, i - 3, 2):
#         dp[i] += dp[j] * 2
#     dp[i] += 2
# print(dp[n])

#RGB거리 2
# from numpy import Inf
# n = int(input())
# rgb = [[0, 0, 0]]
# for _ in range(n):
#     rgb.append(list(map(int, input().split())))
# dp1, dp2, dp3 = [], [], []
# for _ in range(n + 1):
#     dp1.append([0] * 3)
#     dp2.append([0] * 3)
#     dp3.append([0] * 3)
# dp1[1] = [rgb[1][0], Inf, Inf]
# dp2[1] = [Inf, rgb[1][1], Inf]
# dp3[1] = [Inf, Inf, rgb[1][2]]
# for i in range(2, n + 1):
#     dp1[i][0] = rgb[i][0] + min(dp1[i - 1][1], dp1[i - 1][2])
#     dp1[i][1] = rgb[i][1] + min(dp1[i - 1][0], dp1[i - 1][2])
#     dp1[i][2] = rgb[i][2] + min(dp1[i - 1][0], dp1[i - 1][1])
#     dp2[i][0] = rgb[i][0] + min(dp2[i - 1][1], dp2[i - 1][2])
#     dp2[i][1] = rgb[i][1] + min(dp2[i - 1][0], dp2[i - 1][2])
#     dp2[i][2] = rgb[i][2] + min(dp2[i - 1][0], dp2[i - 1][1])
#     dp3[i][0] = rgb[i][0] + min(dp3[i - 1][1], dp3[i - 1][2])
#     dp3[i][1] = rgb[i][1] + min(dp3[i - 1][0], dp3[i - 1][2])
#     dp3[i][2] = rgb[i][2] + min(dp3[i - 1][0], dp3[i - 1][1])
# print(min(dp1[n][1], dp1[n][2], dp2[n][0], dp2[n][2], dp3[n][0], dp3[n][1]))

##브루트포스

#일곱난쟁이
# yodle = []
# for _ in range(9):
#     yodle.append(int(input()))
# yodle.sort()
# find = sum(yodle) - 100
# a, b = 0, 0
# for i in range(9):
#     for j in range(i + 1, 9):
#         if yodle[i] + yodle[j] == find:
#             a, b = i, j
#             break
#     if a:
#         break
# for i in range(9):
#     if i != a and i != b:
#         print(yodle[i])

#사탕게임
