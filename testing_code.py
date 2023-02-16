def twosum(nums,target):
    result = []
    length = len(nums)
    start = 1
    for x in range(length):
        
        for y in range(x+1,length):
            
            print("(x,y):",x,' ',y)
            if nums[x] + nums[y] == target:
                result.append(x)
                result.append(y)
                
        
    return result
print (twosum([3,2,4],6))

