import datetime

a,b,c = map(int, input().split())
N = int(input())
# 限界出社時間
lim_time = datetime.datetime(1900,1,1,8,59)
# c駅に到着すべき時間
lim_time -= datetime.timedelta(minutes=c)

for n in range(N):
  h,m = map(int, input().split())
  # 電車の出発時間
  ride_time = datetime.datetime(1900,1,1,h,m)
  if (ride_time + datetime.timedelta(minutes=b) > lim_time):
    break
  # 乗車時刻を更新
  must_ride_time = ride_time

print('{0:%H:%M}'.format(must_ride_time - datetime.timedelta(minutes=a)))