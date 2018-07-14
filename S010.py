def get_step(now_char, tgt_char):
  if now_char == tgt_char: return 0
  if now_char == 'T':
    if tgt_char == 'B': return 2
    else: return 1
  if now_char == 'B':
    if tgt_char == 'T': return 2
    else: return 1
  if now_char == 'L':
    if tgt_char == 'R': return 2
    else: return 1
  if now_char == 'R':
    if tgt_char == 'L': return 2
    else: return 1
  if now_char == 'U':
    if tgt_char == 'D': return 2
    else: return 1
  if now_char == 'D':
    if tgt_char == 'U': return 2
    else: return 1

# 入力
dice_lst = list(map(int, input().split()))
# key: 数値、value: 文字
chr_dict = {
  dice_lst[0]: 'T',
  dice_lst[1]: 'B',
  dice_lst[2]: 'U',
  dice_lst[3]: 'D',
  dice_lst[4]: 'L',
  dice_lst[5]: 'R'
}

# 回転数
roll_num = 0
# 現在の面
now_chr = 'T'
for _ in range(int(input())):
  brd = int(input())
  roll_num += get_step(now_chr, chr_dict[brd])
  now_chr = chr_dict[brd]

print(roll_num)
