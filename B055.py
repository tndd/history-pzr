N, X = map(int, input().split())
_min = float('inf')
_max = 0
for _ in range(N):
  length = X
  cost = 0
  a, b, c, d = map(int, input().split())
  # 必須の初乗り料
  cost += b
  length -= a
  # 道が残っている限りループ
  while length >= 0:
    cost += d
    length -= c
  # コストの評価
  _max = max(_max, cost)
  _min = min(_min, cost)
# 最終結果
print('{} {}'.format(_min, _max))