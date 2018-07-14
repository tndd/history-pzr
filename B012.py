N = int(input())
for _ in range(N):
  inp = input()
  # リスト化
  even_lst = list(map(lambda str: int(str), inp[0:15:2]))
  odd_lst = list(map(lambda str: int(str), inp[1:15:2]))

  # 偶数の合計
  even = 0
  for ev in even_lst:
    if (ev * 2) > 9:
      even += ((ev * 2) % 10) + 1
    else:
      even += ev * 2
  # 奇数の合計
  odd = sum(odd_lst)

  # 回答 
  for n in range(10):
    if (even + odd + n) % 10 == 0:
      print(n)
      continue
