# 1202

# import sys
# import heapq

# input = sys.stdin.readline

# n, k = map(int, input().split())
# jew = []

# for i in range(n):
# 	m, v = map(int, input().split())
# 	jew.append([m, v])
	
# limit = []
# for i in range(k):
# 	limit.append(int(input()))
	
# jew.sort()
# limit.sort()
# ans = []
# answer = 0

# for weight in limit:
#     while jew and weight >= jew[0][0]:
#         heapq.heappush(ans, -jew[0][1])
#         heapq.heappop(jew)
        
#     if ans:
#         answer += heapq.heappop(ans)
#     elif not jew:
#         break
# print(-answer)

# 1744
 
# N = int(input())
# li_plus = []
# li_minus = []
# hab = 0
# for _ in range(N):
#     n = int(input())
#     if n > 1:
#         li_plus.append(n)
#     elif n == 1:
#         hab += n
#     elif n <= 0:
#         li_minus.append(n)
# li_plus.sort(reverse = True)
# li_minus.sort()
# if len(li_plus) % 2 == 1:
#     li_plus.append(1)
# if len(li_minus) % 2 == 1:
#     li_minus.append(1)
# for i in range(0, len(li_plus), 2):
#     hab += li_plus[i] * li_plus[i + 1]
# for i in range(0, len(li_minus), 2):
#     hab += li_minus[i] * li_minus[i + 1]
# print(hab)

# 1049

# N, M = map(int, input().split())
# package = []
# each = []
# for _ in range(M):
#     a, b = map(int, input().split())
#     package.append(a)
#     each.append(b)

# cheap_pack = min(package)
# cheap_each = min(each)

# if cheap_each * 6 <= cheap_pack:
#     print(cheap_each * N)
# else:
#     n1 = N // 6
#     n2 = N % 6
#     if cheap_each * n2 <= cheap_pack:
#         print(n1 * cheap_pack + n2 * cheap_each)
#     else:
#         print(n1 * cheap_pack + cheap_pack)

# 2864

# a, b = map(str, input().split())
# small_a = a.replace("6", "5")
# small_b = b.replace("6", "5")
# big_a = a.replace("5", "6")
# big_b = b.replace("5", "6")

# print(int(small_a) + int(small_b), int(big_a) + int(big_b))

# 1080

# n, m = map(int, input().split())
# matrix_a = []
# matrix_b = []
# for _ in range(n):
#     matrix_a.append(list(map(int, input())))
    
# for _ in range(n):
#     matrix_b.append(list(map(int, input())))
# def change(mat, i, j):
#     for x in range(i, i + 3):
#         for y in range(j, j + 3):
#             if mat[x][y] == 1:
#                 mat[x][y] = 0
#             else:
#                 mat[x][y] = 1
        
# matrix_diff = []

# for i in range(n):
#     li = []
#     for j in range(m):
#         if matrix_a[i][j] != matrix_b[i][j]:
#             li.append(1)
#         else:
#             li.append(0)
#     matrix_diff.append(li)
# count = 0
# for i in range(n - 2):
#     for j in range(m - 2):
#         if matrix_diff[i][j] == 1:
#             change(matrix_diff, i, j)
#             count += 1
# error = 0
# for i in range(n):
#     if sum(matrix_diff[i]) != 0:
#         error = -1
#         break
# if error == 0:
#     print(count)
# else:
#     print(error)

# 2437

# n = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()
# sum = 0
# for i in num_list:
#     if sum + 1 < i:
#         break
#     sum += i
# print(sum + 1)

# 1449

# n, l = map(int, input().split())
# water_leak = list(map(int, input().split()))
# water_leak.sort()
# count = 0
# i = 0
# stk = 0
# while i <= len(water_leak) - 1:
#     if water_leak[i] > stk:
#         stk = water_leak[i] + l - 1
#         count += 1
#     i += 1
# print(count)

# 1543

# text = input()
# search = input()
# length = len(search)
# count = 0
# while True:
#     a = text.find(search)
#     if a == -1:
#         break
#     else:
#         text = text[a + length :]
#         count += 1
# print(count)


##클래스 정의
# class Hero: 
#     def __init__(self, name, place, weapon):
#         self.name = name
#         self.place = place
#         self.weapon = weapon
#     def introduce(self):
#         print(f"Hi, I\'m {self.name} from {self.place}.")
#     def attack(self):
#         print(f"Attack with {self.weapon}!")
        
# class Ironman(Hero):
#     def attack(self):
#         print("I\'m... Iron Man.")
        
# class Spiderman(Hero):
#     def attack(self):
#         print("Psst!!!")
#     def web_swing(self):
#         print("Hi, everyone!")
        
# class Thor(Hero):
#     def attack(self):
#         print("I\'m Thor, god of thunder!")

# #실행 코드
# hero = Hero("Doctor Strange", "New York", "magic")
# hero.introduce()
# hero.attack()

# ironman = Ironman("Tony", "Long Island", "iron suit")
# spiderman = Spiderman("Peter", "Queens", "web")
# thor = Thor("Thor", "Asgard", "hammer")

# ironman.introduce()
# ironman.attack()

# spiderman.introduce()
# spiderman.attack()
# spiderman.web_swing()

# thor.introduce()
# thor.attack()

# 1783

# n, m = map(int, input().split())    
# if n == 1:
#     print(1)
# elif n == 2:
#     print(min(((m - 1) // 2 + 1), 4))
# else:
#     if 5 <= m < 7:
#         print(4)
#     elif m <= 4:
#         print(m)
#     else:
#         print(5 + (m - 7))

# 11000

# n = int(input())
# li = []
# for _ in range(n):
#     li.append(list(map(int, input().split())))
# li.sort(reverse = True)
# class_set = []
# while True:
#     cla = []
#     last = []
#     while True:
#         if len(cla) == 0 or li[-1][0] >= cla[-1][1]:
#             cla.append(li.pop())
#         else:
#             last.append(li.pop())
#         if len(li) == 0:
#             break
#     li = last
#     class_set.append(cla)
#     if len(li) == 0:
#         break
# print(len(class_set))

# import heapq
# n = int(input())

# q = []

# for i in range(n):
#     start, end = map(int, input().split())
#     q.append([start, end])

# q.sort()

# room = []
# heapq.heappush(room, q[0][1])

# for i in range(1, n):
#     if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
#         heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
#     else: # 현재 회의실에 이어서 회의 개최 가능
#         heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
#         heapq.heappush(room, q[i][1])

# print(len(room))

        