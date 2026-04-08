f = open("numbers.txt", "r")
nums = [int(i) for i in f.read().split()]
f.close()

print(max(nums))
print(sum(nums)/len(nums))
print(len([i for i in nums if i > 100]))