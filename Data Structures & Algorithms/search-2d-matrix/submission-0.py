class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        x = len(matrix) - 1
        y = len(matrix[0]) - 1

        left_ = 0
        right_ = x

        while left_ <= right_:
            mid_ = (left_ + right_) // 2

            if matrix[mid_][0] <= target <= matrix[mid_][y]:
                left = 0
                right = y

                while left <= right:
                    mid = (left + right) // 2

                    if matrix[mid_][mid] == target:
                        return True
                    elif matrix[mid_][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                return False

            elif matrix[mid_][0] > target:
                right_ = mid_ - 1
            else:
                left_ = mid_ + 1

        return False

        
        