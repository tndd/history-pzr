class Status:
  def __init__(self, enemys, beated_num):
    self.enemys = enemys
    self.beated_num = beated_num
  
  # 魔法に対する最大スコア
  def get_score(self, magic):
    ret_score = 0
    ret_enemys = []
    if magic.type == 'all':
      for n in range(len(self.enemys)):
        if self.enemys[n] - magic.dmg <= 0:
          ret_score += 1
        else:
          # リスト更新(hpを減らす)
          ret_enemys.append(self.enemys[n] - magic.dmg)
    elif magic.type == 'single':
      ret_enemys = self.enemys
      ret_enemys.sort(reverse=True)
      for idx, enm in enumerate(ret_enemys):
        if enm - magic.dmg <= 0:
          # 要素の取り出し
          ret_enemys.pop(idx)
          ret_score = 1
          break
    return (ret_score, ret_enemys)
  
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
dp = [[Status(enemys, 0) for i in range(P + 1)] for j in range(M + 1)]

for m in range(1, M + 1):
  for p in range(1, P + 1):
    # スコアを追加できない場合
    if p - magics[m - 1].mp < 0:
      dp[m][p] = dp[m - 1][p]
    else:
      a = dp[m][p - magics[m - 1].mp]
      mg = magics[m - 1]
      # 左のマスからの追加スコア、敵配列状態
      score, chged_enemys = dp[m][p - magics[m - 1].mp].get_score(magics[m - 1])
      print(score)
      # 左のマスのスコア
      pre_beated_num = dp[m][p - magics[m - 1].mp].beated_num
      # 状態更新
      if dp[m - 1][p].beated_num > (pre_beated_num + score):
        dp[m][p] = dp[m - 1][p]
      else:
        dp[m][p] = Status(chged_enemys, pre_beated_num + score)

print(dp[M][P].beated_num)

# 最大のダメージをスコアとして定義したほうがよかったかもしれない
