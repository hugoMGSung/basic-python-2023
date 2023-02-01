# for문
arr = [1,2,3,4,5]
sum = 0

for item in arr:
    print(item)
    sum += item # sum = sum + item


print('합계는', sum)

# 리스트를 편하게 만드는 방법
vals = [i for i in range(1, 11)]
print(vals)

# continue / break
# num = 0
for item in vals:
    # num += 1
    if item % 2 == 0:
        continue # 이후의 것을 수행하지 않고 다시 for문으로 감
        # break # break를 만나면 for문을 완전히 탈출
    else:
        print(item, '번 수는', item, '입니다')

