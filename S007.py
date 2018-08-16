from collections import defaultdict

# 文字数をカウントする辞書
d_word = defaultdict(int)
# 入力文字列
s = input()

for i,c in enumerate(s):
  # 単純にアルファベットだった場合
  if str.isalpha(c):
    d_word[c] += 1
  # 数字が来た場合
  if str.isdigit(c):
    # 数字が一文字なら
    if str.isdigit(s[i + 1]):
      d_word[s[i + 1]] += int(c)
      print(int(c))

print(d_word)