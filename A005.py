a,b,n=map(int, input().split())
frames=input().split()
frames.append(0)
frames.append(0)
# framesを数値に変換
for idx,score in enumerate(frames):
  # 数値に変換
  if score == 'G': score = 0
  frames[idx] = int(score)
# 各フレームのスコア
frame_score = []
# スペアかストライクか
stk_flg = []
# フレーム毎投擲数
t_cnt = 0
# スコア表を埋める
for idx,score in enumerate(frames):
  # 未投擲ならば
  if t_cnt == 0:
    frame_score.append(score)
    # ストライクなら追加スコアの加算
    if score == b:
      frame_score[-1] += frames[idx + 1]
      frame_score[-1] += frames[idx + 2]
    else:
      # 次の投擲へ
      t_cnt += 1
    continue
  # 二回目の投擲なら(t_cntが0以外)
  else:
    # スコア加算
    frame_score[-1] += score
    # スペアだったら追加スコア加算
    if frame_score[-1] == b:
      frame_score[-1] += frames[idx + 1]
    # カウント初期化
    t_cnt = 0
    continue

print(sum(frame_score))