# linuxとwindowsで実行結果が違う
# [入力]:
# [出力]
# windows -> 144
# linux -> 8

n,k = map(int, input().split())
all_lst = list(range(1, n * 2 + 1))
all_value = sum(all_lst)

def dfs(num_lst, idx, cnt):
  if cnt == n:
    total_dif = 0
    b_lst = list(set(all_lst) - set(num_lst))
    for a,b in zip(num_lst, b_lst):
      total_dif += abs(a - b)
    if total_dif <= k:
      return 1
    else:
      return 0
  if idx > n * 2:
    return 0
  else:
    add_lst = num_lst[:]
    add_lst.append(idx)
    return dfs(num_lst[:], idx + 1, cnt) + dfs(add_lst, idx + 1, cnt + 1)


print(dfs([],1,0))