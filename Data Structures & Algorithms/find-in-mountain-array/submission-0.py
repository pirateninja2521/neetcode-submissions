class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Step 1: find peak i (binary search)
        l = 1
        r = mountainArr.length() - 2
        peak = 0
        while l <= r:
            mid = (l + r)//2
            num1, num2, num3 = mountainArr.get(mid-1), mountainArr.get(mid), mountainArr.get(mid+1)
            if num1 < num2 and num2 > num3:
                peak = mid
                break
            elif num1 < num2 < num3:
                l = mid+1
            else:
                r = mid - 1
        
        if mountainArr.get(peak) == target:
            return peak
        # Step 2: binary search target in mountainArr[:peak]
        l = 0
        r = peak - 1
        while l <= r:
            mid = (l + r)//2
            result = mountainArr.get(mid)
            if result == target:
                return mid
            elif result > target:
                r = mid - 1
            else:
                l = mid + 1

        # Step 3: binary search target in mountainArr[peak+1:]
        l = peak + 1
        r = mountainArr.length() - 1
        while l <= r:
            mid = (l + r)//2
            result = mountainArr.get(mid)
            if result == target:
                return mid
            elif result < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1