from typing import List


# Bài toán, tìm số min trong rotated sorted list
# VD: [3, 4, 5, 1, 2], list này đã được rotated 3 lần => dịch số 3, 4, 5 về phía trước

# Idea:
# Dùng binary search nhưng với 1 trick đặc biệt
# với example trên, áp dụng binary search vào thì l = 3, m = 5, r = 2
# so sánh nums[m] vs nums[r], nếu lớn hơn thì dịch sang phải, ngược lại thì sang trái
# tại sao lại vậy? bởi vì số 5 vốn là số cuối cùng của phần được rotate
# nên xét về phía bên phải sẽ không có số nào lớn hơn được

# Xét trường hợp khác cũng đúng:
# VD: [2, 3, 4, 5, 1]
# 4 > 1 => dịch về phía bên phải

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            else:
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


so = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
res = so.search(nums, target)
print(res)
