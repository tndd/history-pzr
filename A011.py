# ブロック幅、 移動数
d,n = list(map(int, input().split()))
a_lst = []
for _ in range(n):
  a_lst.append(int(input()))

end_flg = False

def rec(idx, loc, log):
  global end_flg
  # フィルタ
  if abs(loc) > d or end_flg: return ''
  if len(log) == n:
    end_flg = True
    print(log)
  if idx >= n: return ''
  rec(idx + 1, loc - a_lst[idx], log + 'L')
  rec(idx + 1, loc + a_lst[idx], log + 'R')

# 現在地
loc = 0
vec_str = rec(0, 0, '')