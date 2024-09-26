#uy ishi 3
# import random
# b = (range(100, 1001), 100)
# a= random.tanla(b)
# print("son", n)
# b = [son for son in range(a + 1) if son % 2 == 0]
# print(b)
#uy ishi 4 
# import random
# a = random.sample(range(1, 1000001), 1000)
# n = random.choice(a)
# print(" son:", n)
# def asosiy(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# tub_sonlar = [son for son in range(n + 1, 1000001) if asosiy(son)]
# print(tub_sonlar)
#uy ishi 5 
# import random
# n = 20
# r = [random.randint(-50, 50) for _ in range(n)]
# print(r)
# musbat = [s for s in r if s > 0]
# manfiy = [s for s in r if s < 0]
# with open("musbat.txt", "w") as f:
#     f.write("\n".join(map(str, musbat)))
# with open("manfiy.txt", "w") as f:
#     f.write("\n".join(map(str, manfiy)))
# print("Musbat sonlar:", musbat)
# print("Manfiy sonlar:", manfiy)
#uy ishi 2 
# def aniqlash(a):
#     a = ''
#     for raqam in str(a):
#         raqam = (int(raqam) + 7) % 10
#         a += str(raqam)
#     return a
# b = int(input("sonni kiriting "))
# s = aniqlash(b)
# print(s)
# def rangli_harf(a):
#     for harf in a:
#         if harf in "AaBbCcDdEeFfGgHh":
#             print(f"\033[91m{harf}\033[0m", end='')  
#         elif harf in "IiJjKkLlMmNnOoPp":
#             print(f"\033[93m{harf}\033[0m", end='')  
#         elif harf in "QqRrSsTtUuVvWwXxYyZz":
#             print(f"\033[92m{harf}\033[0m", end='')  
#         else:
#             print(harf, end='')  
#     print()  
# b = input("Textni kiriting: ")
# rangli_harf(b)
#sinf ishi 1 
# with open("nomi.txt", "r") as f:
#     a = f.readlines() [-1]
#     print(a)
#sinf ishi 2 
# with open("nomi.txt","r") as f:
#     a=0
#     for line in f:
#         a+=1
# print(a)
#sinf ishi 3 
# with open("3m.txt", "w") as a:
#     a.write("Abdurauf Hasan Usmon")
# with open("nomi.txt", "r") as f:
#     b = " "
#     for qator in f:
#         n= qator.split()
#         for c in n:
#             if len(c) > len(b):
#                 b = c
#     print(f"Eng uzun soz: {b}")
#sinf ishi 5
# import json
# a = [
#     {"ism": "Ali", "yosh": 20, "ball": 85},
#     {"ism": "Zaynab", "yosh": 22, "ball": 90},
#     {"ism": "Sardor", "yosh": 19, "ball": 78}
# ]
# b = [talaba for talaba in a if talaba["yosh"] > 20]
# print("Yoshi 20 dan katta talabalar:")
# for d in b:
#     print(d)
#sinf ishi 6 
# import json
# a = [
#     {"nomi": "Olma", "narxi": 5000, "soni": 30},
#     {"nomi": "Banan", "narxi": 8000, "soni": 20},
#     {"nomi": "Anor", "narxi": 12000, "soni": 10}
# ]
# b = sum(m["narxi"] * m["soni"] for m in a)
# print(f"Mahsulotlarning umumiy qiymati: {b} so'm")
#sinf ishi 4 
# with open('text.txt', 'r') as f:
#     a = f.read()
#
# with open('text1.txt', 'w') as f1:
#     f1.write(a)
#
# print("Done!")
