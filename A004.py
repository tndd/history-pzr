class Rod:
  def __init__(self, point, p1_h, p2_h):
    self.p1 = point
    self.p2 = point + 1
    self.p1_h = p1_h
    self.p2_h = p2_h
  # [1]線番号, [2]高さ
  def warp(self, line, height):
    if line == self.p1 and height == self.p1_h:
      return (self.p2, self.p2_h)
    elif line == self.p2 and height == self.p2_h:
      return (self.p1, self.p1_h)
    else:
      return (-1, -1)

# ほんへ
L, n, m = list(map(int, input().split()))
rod_list = list()
for _ in range(m):
  point, p1_h, p2_h = list(map(int, input().split()))
  rod_list.append(Rod(point, p1_h, p2_h))

line = 1
while(L > 0):
  for rd in rod_list:
    line_, L_ = rd.warp(line, L)
    if line_ == -1:
      continue
    else:
      line = line_
      L = L_
      rod_list.remove(rd)
      break
  L -= 1
    
# out
print(line)