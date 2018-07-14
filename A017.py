class Block:
  def __init__(self, h, w, loc):
    self.w = w
    self.h = h
    self.loc = loc
  
  def bottom(self):
    # return [x for x in range(self.loc, self.loc + self.w)]
    return(self.loc, self.loc + self.w)

class Field:
  def __init__(self, height, width):
    self.fld = [['.' for i in range(width)] for j in range(height)]
    return
    
  # フィールドの塗りを行う
  def paint_fld(self, now_height, block):
    left, right = block.bottom()
    for rw in range(block.h):
      # 範囲内のものしか塗らない
      if 0 <= (now_height - rw) < len(self.fld):
        for cl in range(left, right):
          self.fld[now_height - rw][cl] = '#'
    return 0
  
  def upd_fld(self, block):
    # 現在の高さ
    now_height = -1
    # 落下ブロックの範囲
    left, right = block.bottom()
    while(now_height < (len(self.fld) - 1)):
      # 一つ下の範囲に障害物があれば
      if '#' in self.fld[now_height + 1][left:right]:
        self.paint_fld(now_height, block)
        return
      # ブロックを一つ下に落とす
      now_height += 1
    # whileを抜けたということは底に到達したということ
    self.paint_fld(now_height, block)
    return 0
      
  
  def show_fld(self):
    for line in self.fld:
      for cell in line:
        print(cell, end='')
      print()
    return 0
        
H, W, N = list(map(int, input().split()))
fld_cls = Field(H, W)
for n in range(N):
  h, w, loc = list(map(int, input().split()))
  fld_cls.upd_fld(Block(h, w, loc))
fld_cls.show_fld()