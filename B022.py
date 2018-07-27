M, N, K = map(int, input().split())
# 支持者の記録(支持者の数 + 無党派集団)
supporters = [0 for _ in range(M + 1)]
# 無党派集団に全投票
supporters[-1] = N
# 演説の回数ループ
for k in range(K):
  # 演説者
  a = int(input())
  # 移動する支持者数
  move_spd = 0
  for idx, sps in enumerate(supporters):
    # 演説者ではないかつ0人以上
    if (idx + 1) != a and sps > 0:
      # spsを更新しても、本体のsupportersは更新されないので注意
      supporters[idx] -= 1
      move_spd += 1
  supporters[a - 1] += move_spd
# 結果
_maxnum = max(supporters[:-1])
for idx, num in enumerate(supporters[:-1]):
  if num == _maxnum:
    print(idx + 1)