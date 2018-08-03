fld = [['' for i in range(8)] for j in range(8)]
move = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
fld[3][3] = 'W'
fld[3][4] = 'B'
fld[4][3] = 'B'
fld[4][4] = 'W'

def show(_fld):
  for f in _fld:
    print(f)

def isArea(x,y):
  if 0 <= x < 8 and 0<= y < 8:
    return True
  else:
    return False

def repaint(x,y,vx,vy):
  p = fld[y][x]
  next_x = x + vx
  next_y = y + vy
  cnt = 0
  while True:
    # エリア外が空白マスなら塗り替え数を0に
    if not isArea(next_x, next_y) or fld[next_y][next_x] == '':
      cnt = 0
      break
    # 自分の色なら
    elif fld[next_y][next_x] == p:
      break
    # 相手の色なら
    else:
      next_x += vx
      next_y += vy
      cnt += 1
  # 実際の塗り替え
  for c in range(cnt):
    y += vy
    x += vx
    fld[y][x] = p
  return
    
  
def eval(p,x,y):
  fld[y][x] = p
  for _x,_y in move:
    repaint(x,y,_x,_y)
  # show(fld)
  # print('-----------------------')

# eval('w',3,5)
# eval('b',2,5)
# eval('w',1,5)
# eval('b',3,6)
# eval('w',3,7)
# eval('b',4,5)

n = int(input())
for i in range(n):
  _inp = input().split()
  p = _inp[0]
  x = int(_inp[1]) - 1
  y = int(_inp[2]) - 1
  eval(p,x,y)

# カウント
b_cnt = 0
w_cnt = 0
for f_row in fld:
  for f in f_row:
    if f == 'B':
      b_cnt += 1
    elif f == 'W':
      w_cnt += 1

# 勝敗判定
if b_cnt > w_cnt:
  str = 'The black won!'
elif b_cnt < w_cnt:
  str = 'The white won!'
else:
  str = 'Draw!'

bb = '{0:02d}'.format(b_cnt)
ww = '{0:02d}'.format(w_cnt)
print('{}-{} {}'.format(bb,ww,str))