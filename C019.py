def g_divisor_sum(num):
  d_lst_sum = 0
  for n in range(1,num):
    if num % n == 0:
      d_lst_sum += n
  return d_lst_sum

Q = int(input())
for q in range(Q):
  num = int(input())
  sum = g_divisor_sum(num)
  if num == sum:
    print('perfect')
  elif(abs(num - sum) == 1):
    print('nearly')
  else:
    print('neither')
  