# フィールドの高さ、幅、プレイヤー数
H, W, N = list(map(int, input().split()))
# カード取得状況
fld_flg = [[True for i in range(W)] for j in range(H)]
# カード配置図
fld = []
for h in range(H):
  fld.append(list(map(int, input().split())))
player_num = 0
player_score = [0 for i in range(N)]
# トランプめくり回数
for l in range(int(input())):
  y1,x1,y2,x2 = list(map(int, input().split()))
  # めくったカードが同じ種類なら
  if fld[y1-1][x1-1] == fld[y2-1][x2-1]:
    # カードの取得フラグを下ろす
    fld_flg[y1 - 1][x1 - 1] = False
    fld_flg[y2 - 1][x2 - 1] = False
    # スコアを加算しプレイヤーはそのままで続行
    player_score[player_num] += 2
    continue
  # 違うならばプレイヤー数を加算して続行
  player_num += 1
  # プレイヤー一巡処理
  if player_num >= N:
    player_num = 0

# スコア表示
for score in player_score:
  print(score)
