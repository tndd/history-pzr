lv_dict = {1: 'ABC'}
def get_abc(lv_num):
  if lv_num in lv_dict:
    return lv_dict[lv_num]
  else:
    lv_dict[lv_num] = 'A' + get_abc(lv_num - 1) + 'B' + get_abc(lv_num - 1) + 'C'
    return lv_dict[lv_num]
  
k,s,t = list(map(int, input().split()))
print(get_abc(k)[s-1:t])