"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""
def summaryRanges(nums):
    if len(nums) == 0:
        return  []
    elif len(nums) == 1:
        return [str(each) for each in nums]

    start = nums[0]
    current = nums[0]
    end = None

    arr = []

    for each in nums[1:]:
        current += 1
        if each == current:
            end = each
        else:
            if not end:
                arr.append(str(start))
            else:
                arr.append(str(start)+"->"+str(end))
            start = each
            current = each
            end = None
    if not end:
            arr.append(str(start))
    else:
        arr.append(str(start)+"->"+str(end))

    return arr