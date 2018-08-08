h,w,n = map(int, input().split())
c = [input().split() for _ in range(h)]
vec = [(1,0),(-1,0),(0,1),(-1,0)]

def isArea(y,x):
  if 0 <= y < h and 0 <= x < w:
    return True
  else:
    return False

def isAreaWide(y,x):
  if -1 <= y <= h and -1 <= x <= w:
    return True
  else:
    return False

# cは残り曲がり回数
def dfs(y,x,vx,vy,ty,tx,cnt):
  # 3回以上曲がっているか、エリア外なら終了
  if cnt < 0 or (not isAreaWide(y,x)):
    return False
  # 目標地点に到達していればT
  elif y == ty and x == tx:
    return True
  # エリア内かつ他のカードが存在していれば終了
  elif isArea(y,x) and c[y][x] != '.':
    return False
  # その他なら続行
  else:
    for v_y,v_x in vec:
      # 同じ向きならば、カウントを進めない
      if v_y == vy and v_x == vx:
        _cnt = cnt
      else:
        _cnt = cnt - 1
      if dfs(y+v_y, x+v_x, v_y, v_x, ty, tx, _cnt):
        return True
    return False

# 実行
for _ in range(n):
  a,b,A,B = map(int, input().split())
  char = c[a-1][b-1]
  if char != c[A-1][B-1]:
    print('no')
    continue
  # 開始地点を空白に
  c[a-1][b-1] = '.'
  if dfs(a-1,b-1,0,0,A-1,B-1,3):
    print('yes')
  else:
    print('no')
  # 戻す
  c[a-1][b-1] = char