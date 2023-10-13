class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @cache
        def dp(i, swap):
            if i < 0:
                return 0, -inf, -inf

            sCost, sLimit1, sLimit2 = dp(i-1, True)
            dsCost, dsLimit1, dsLimit2 = dp(i-1, False)

            if not swap:
                if sCost < dsCost:
                    if sLimit1 < nums1[i] and sLimit2 < nums2[i]:
                        return sCost, nums1[i], nums2[i]
                    elif dsLimit1 < nums1[i] and dsLimit2 < nums2[i]:
                        return dsCost, nums1[i], nums2[i]
                else:                        
                    if dsLimit1 < nums1[i] and dsLimit2 < nums2[i]:
                        return dsCost, nums1[i], nums2[i]
                    elif sLimit1 < nums1[i] and sLimit2 < nums2[i]:
                        return sCost, nums1[i], nums2[i]
            else:
                if sCost < dsCost:
                    if sLimit1 < nums2[i] and sLimit2 < nums1[i]:
                        return 1+sCost, nums2[i], nums1[i]
                    elif dsLimit1 < nums2[i] and dsLimit2 < nums1[i]:
                        return 1+dsCost, nums2[i], nums1[i]
                else:                     
                    if dsLimit1 < nums2[i] and dsLimit2 < nums1[i]:
                        return 1+dsCost, nums2[i], nums1[i]
                    elif sLimit1 < nums2[i] and sLimit2 < nums1[i]:
                        return 1+sCost, nums2[i], nums1[i]
            
            return inf, inf, inf
        
        print(dp(0, True), dp(0, False))
        print(dp(1, True), dp(1, False))
        return min(dp(n-1, True)[0], dp(n-1, False)[0])