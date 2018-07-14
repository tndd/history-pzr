  # 距離の二乗を求める
  def distance(c_x, c_y, x, y):
    return pow(c_x - x, 2) + pow(c_y - y, 2)

  # 距離が特定の範囲内であるかを判定する
  def is_area(dis, r):
    if pow(r, 2) > dis:
      return 'noisy'
    else:
      return 'silent'

  area = input().split(' ')
  c_x = int(area[0])
  c_y = int(area[1])
  c_r = int(area[2])
  num = int(input())
  for i in range(num):
    line = input().split(' ')
    x = int(line[0])
    y = int(line[1])
    print(is_area(distance(c_x,c_y,x,y), c_r))
