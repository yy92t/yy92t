nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Examples for Selecting:")
some_nums = nums[2:7]
print("some_nums:",some_nums)       # [30, 40, 50, 60, 70]
print("nums[2:7:2]:",nums[2:7:2])   # [30, 50, 70]
print("nums[6:1:-1]",nums[6:1:-1])  # [70, 60, 50, 40, 30]
print("nums[6:1]:",nums[6:1])       # [] 
print("nums[2:]:",nums[2:])     # [30, 40, 50, 60, 70, 80, 90] 
print("nums[:7]:",nums[:7])     # [10, 20, 30, 40, 50, 60, 70]
print("nums[:1:-1]:",nums[:1:-1])   # [90, 80, 70, 60, 50, 40, 30] 
print("nums[-7:-2]:",nums[-7:-2])   # [30, 40, 50, 60, 70]
print("nums[-7:7]:",nums[-7:7])     # [30, 40, 50, 60, 70] 
print("nums[:]:",nums[:])       # [10, 20, 30, 40, 50, 60, 70, 80, 90]
print()
print("Examples for Retriving:")
some_nums = nums[2:7]
print("some_nums:",some_nums)       # [30, 40, 50, 60, 70]
print("nums[2:7:2]:",nums[2:7:2])   # [30, 50, 70]
print("nums[6:1:-1]",nums[6:1:-1])  # [70, 60, 50, 40, 30]
print("nums[6:1]:",nums[6:1])       # [] 
print("nums[2:]:",nums[2:])     # [30, 40, 50, 60, 70, 80, 90] 
print("nums[:7]:",nums[:7])     # [10, 20, 30, 40, 50, 60, 70]
print("nums[:1:-1]:",nums[:1:-1])   # [90, 80, 70, 60, 50, 40, 30] 
print("nums[-7:-2]:",nums[-7:-2])   # [30, 40, 50, 60, 70]
print("nums[-7:7]:",nums[-7:7])     # [30, 40, 50, 60, 70] 
print("nums[:]:",nums[:])       # [10, 20, 30, 40, 50, 60, 70, 80, 90]
print()
print("Examples for Replacing:")
nums2a = nums[:]
nums2a[2:7:2] = ["a", "b", "c"]
print("nums2a[2:7:2]:",nums2a)      # [10, 20, 'a', 40, 'b', 60, 'c', 80, 90]
nums2b = nums[:]
nums2b[6:1:-1] = ["a", "b", "c", "d", "e"]
print("nums2b[6:1:-1]:",nums2b)     # [10, 20, 'e', 'd', 'c', 'b', 'a', 80, 90] 
nums2c = nums[:]
# nums2c[6:1:-1] = ["a", "b", "c"]  # Error!
print()
print("Examples for Removing:")
nums3a = nums[:]
del nums3a[2:7:2]
print("nums3a[2:7:2]:",nums3a)      # [10, 20, 40, 60, 80, 90] 
nums3b = nums[:]
del nums3b[6:1:-1]
print("nums3b[6:1:-1]:",nums3b)     # [10, 20, 80, 90]
print()
print("Examples for Adding:")
nums4a = nums[:]
nums4a[:0] = ["a", "b"]
print("nums4a[:0]:",nums4a)     # ['a', 'b', 10, 20, 30, 40, 50, 60, 70, 80, 90] 
nums4b = nums[:]
nums4b[9:] = ["a", "b"]
print("nums4b[9:]:",nums4b)     # [10, 20, 30, 40, 50, 60, 70, 80, 90, 'a', 'b'] 
nums4c = nums[:]
nums4c[99:] = ["a", "b"]
print("nums4c[99:]:",nums4c)        # [10, 20, 30, 40, 50, 60, 70, 80, 90, 'a', 'b']
nums4d = nums[:]
nums4d[99:3333] = ["a", "b"]
print("nums4d[99:3333]:",nums4d)    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 'a', 'b']
nums4e = nums[:]
nums4e[3333:99] = ["a", "b"]
print("[3333:99]:",nums4e)          # [10, 20, 30, 40, 50, 60, 70, 80, 90, 'a', 'b']
nums4f = nums[:]
nums4f[2:2] = ["a", "b"]
print("nums4f[2:2]:",nums4f)        # [10, 20, 'a', 'b', 30, 40, 50, 60, 70, 80, 90]
print()
print("Examples for Relacing and Adding/Removing:")
nums5a = nums[:]
nums5a[2:4] = ["a", "b", "c"]       # two selected but three is assigning
print("nums5a[2:4] with 3 elements:", end=" ")
print(nums5a)                       # [10, 20, 'a', 'b', 'c', 50, 60, 70, 80, 90]
nums5b = nums[:]
nums5b[2:4] = ["a"]                 # two selected but one is assigning
print("nums5b[2:4] with 1 element:", end=" ")
print(nums5b)                       # [10, 20, 'a', 50, 60, 70, 80, 90]
  
