class Status:
  def __init__(self, total_beated, total_dmg, enemys):
    self.enemys = enemys
    self.total_beated = total_beated
    self.total_dmg = total_dmg
  
  # 魔法に対する最大ダメージ
  def get_score(self, magic):
    ret_beated = 0
    ret_score = 0
    ret_enemys = []
    if magic.type == 'all':
      for n in range(len(self.enemys)):
        if self.enemys[n] - magic.dmg <= 0:
          ret_beated += 1
          ret_score += self.enemys[n]
        else:
          # リスト更新(hpを減らす)
          ret_enemys.append(self.enemys[n] - magic.dmg)
          ret_score += magic.dmg
    elif magic.type == 'single':
      ret_enemys = self.enemys[:]
      ret_enemys.sort(reverse=True)
      flg = True
      for idx, enm in enumerate(ret_enemys):
        # 倒しきれるならば
        if enm - magic.dmg <= 0:
          # 要素の取り出し
          ret_enemys.pop(idx)
          ret_beated += 1
          ret_score += enm
          # 要素が一度でも取り出されたか
          flg = False
      # 倒しきれない場合
      if flg:
        ret_enemys[-1] -= magic.dmg
        ret_score += magic.dmg
    return (ret_beated, ret_score, ret_enemys)
  
class Magic:
  def __init__(self, type, dmg, mp):
    self.type = str(type)
    self.dmg = int(dmg)
    self.mp = int(mp)
  
# モンスター数、魔法数、魔法力
N,M,P = list(map(int, input().split()))
# 敵
enemys = []
for n in range(N):
  enemys.append(int(input()))
# 魔法
magics = []
for n in range(M):
  type, dmg, mp = input().split()
  magics.append(Magic(type, dmg, mp))
# dpテーブル
dp = [[Status(0, 0, enemys[:]) for i in range(P + 1)] for j in range(M + 1)]
for m in range(1, M + 1):
  for p in range(1, P + 1):
    # スコアを追加できない場合
    if p - magics[m - 1].mp < 0:
      dp[m][p] = dp[m - 1][p]
    else:
      # 左のマスからの追加スコア、敵配列状態
      beated, dmg, chged_enemys = dp[m][p - magics[m - 1].mp].get_score(magics[m - 1])
      # 左のマスのスコア
      pre_total_dmg = dp[m][p - magics[m - 1].mp].total_dmg
      pre_total_beated = dp[m][p - magics[m - 1].mp].total_beated
      # 状態更新
      if dp[m - 1][p].total_beated > (pre_total_beated + beated):
        dp[m][p] = dp[m - 1][p]
      elif dp[m - 1][p].total_beated < (pre_total_beated + beated):
        dp[m][p] = Status(pre_total_beated + beated, pre_total_dmg + dmg, chged_enemys)
      # 倒した数が同じならば、与えた総ダメージで決める
      else:
        if dp[m - 1][p].total_dmg > (pre_total_dmg + dmg):
          dp[m][p] = dp[m - 1][p]
        else:
          dp[m][p] = Status(pre_total_beated + beated, pre_total_dmg + dmg, chged_enemys)

total = dp[M][P].total_dmg
cnt = 0
enemys.sort()
for enm in enemys:
  total -= enm
  if total >= 0:
    cnt += 1

print(cnt)
