#Erik Hansen
#10/2/2017
#warmup7.py
total = 0
for i in range(1,100001):
    if i%3==0 and i%10==0 and i%17==0:
        total += i
print(total)