import math

class Camera:
  def __init__(self, x, y, deg, range, length):
    self.x = x
    self.y = y
    self.deg = deg
    self.range = range
    self.length = length
  # 対象物が範囲に入っているかを判定
  def is_capture(self, art):
    x_ofs = art.x - self.x
    y_ofs = art.y - self.y
    # 対象物との距離
    dist = math.sqrt(x_ofs**2 + y_ofs**2)
    # 射程外ならばFを返す
    if self.length < dist:
      return False
    # 対象物との角度
    deg_tgt = math.degrees(math.atan2(y_ofs, x_ofs))
    # マイナスの角度の返還
    if deg_tgt < 0:
      deg_tgt += 360
    # 対象物が範囲内ならT、違えばF
    if self.deg - (self.range / 2) <= deg_tgt <= self.deg + (self.range / 2):
      return True
    else:
      return False


class Art:
  def __init__(self, x, y):
    self.x = x
    self.y = y

W,H,M,N = map(int,input().split())
# 監視カメラリスト
cameras = []
for _ in range(M):
  x,y,t,d,r = map(int, input().split())
  cameras.append(Camera(x,y,t,d,r))
# 美術品リスト
arts = []
for _ in range(N):
  x,y = map(int, input().split())
  arts.append(Art(x,y))
# 美術品を判定
for art in arts:
  no_flg = True
  # カメラの台数分ループ
  for cam in cameras:
    if cam.is_capture(art):
      print('yes')
      no_flg = False
      break
  if no_flg:
    print('no')
