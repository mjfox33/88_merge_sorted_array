from code_88_merge_sorted_array import Solution

def test_example_1():
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    output = [1,2,2,3,5,6]
    s.merge(nums1,m,nums2,n)
    assert  nums1 == output