#!/usr/bin/python3

#定义函数
# def twoSum(self,nums,target):
# 	for i in range(0,len(nums)):
# 		for j in range(i+1,len(nums)):
# 			if nums[i]+nums[j] == target:
# 				self = [i,j];
# 	print(self)
#定义函数时间复杂度 O(n)
def twoSum(self,nums,target):
	mydict ={};
	for (i,v) in enumerate(nums):
		u = target - v;
		if u not in mydict:
			mydict[v] = i;
			print(u)
		else:
			self.extend([i,mydict[u]])
	print(self)
	return self
 
#调用函数
str = input();
target = int(input());
nums = str.split(",");
for i in range(0,len(nums)):
	nums[i]=int(nums[i]);
self = [];
twoSum(self,nums,target)