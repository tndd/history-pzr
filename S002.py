# 変数受け取り
w,h = map(int, input().split())
a = [list(input().split()) for _ in range(h)]

# 盤面を便利なように作り変え
for _h in range(h):
  for _w in range(w):
    if a[_h][_w] == 's':
      start = (_h, _w)
      a[_h][_w] = 0
    elif a[_h][_w] == 'g':
      goal = (_h, _w)
      a[_h][_w] = 0
    # 歩数カウントに数字を使うので中身の入れ替え
    elif a[_h][_w] == '1':
      a[_h][_w] = 'w'
    elif a[_h][_w] == '0':
      a[_h][_w] = 0

# エリア内科の判定
def isArea(loc):
  if 0 <= loc[0] < h and 0 <= loc[1] < w:
    return True
  else:
    return False

# 4方向の向き
vecs = [(1,0), (-1,0), (0,1), (0,-1)]

# 幅優先探索
def bfs(loc, goal):
  queue = [loc]
  while len(queue) > 0:
    l = queue.pop(0)
    # ゴールに到着していたら終了
    if l == goal:
      return a[goal[0]][goal[1]]
    # 探索
    for v in vecs:
      # 新たな探索先
      nl = (l[0] + v[0], l[1] + v[1])
      # 新たな探索先がエリア内or0なら探索を始める
      if isArea(nl) and a[nl[0]][nl[1]] == 0:
        # 一歩進める
        a[nl[0]][nl[1]] = a[l[0]][l[1]] + 1
        # キューに追加
        queue.append(nl)
  else:
    return 'Fail'


print(bfs(start,goal))