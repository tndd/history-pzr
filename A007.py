def get_vec(y, x):
  vec['y'] = y
  vec['x'] = x
  return vec

def chg_vector(mirror, vec):
  if mirror == '_':
    return vec
  elif mirror == '\\':
    if vec['y'] == 0 and vec['x'] == 1: return get_vec(1, 0)
    elif vec['y'] == 1 and vec['x'] == 0: return get_vec(0, 1)
    elif vec['y'] == 0 and vec['x'] == -1: return get_vec(-1, 0)
    elif vec['y'] == -1 and vec['x'] == 0: return get_vec(0, -1)
  elif mirror == '/':
    if vec['y'] == 0 and vec['x'] == 1: return get_vec(-1, 0)
    elif vec['y'] == 1 and vec['x'] == 0: return get_vec(0, -1)
    elif vec['y'] == 0 and vec['x'] == -1: return get_vec(1, 0)
    elif vec['y'] == -1 and vec['x'] == 0: return get_vec(0, 1)

def is_area(loc, h, w):
  if 0<=loc['y']<h and 0<=loc['x']<w:
    return True
  else:
    return False

# 位置
loc = {'y': 0,'x': 0}
# ベクトル
vec = {'y': 0,'x': 1}
# 入力
H, W = list(map(int, input().split()))
fld = []
for h in range(H):
  fld.append(list(input()))

score = 0
while(is_area(loc, H, W)):
  # 新たな向き
  vec = chg_vector(fld[loc['y']][loc['x']], vec)
  # 一つ進む
  loc['y'] += vec['y']
  loc['x'] += vec['x']
  score += 1

print(score)