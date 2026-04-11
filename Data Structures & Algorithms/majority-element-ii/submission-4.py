from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Find candidates
        count1 = count2 = 0
        candidate1 = candidate2 = None

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        res = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)

        return res


'''
🔥 Algorithm (2 Phases)
Phase 1: Find candidates
Maintain a hashmap of size ≤ (k - 1)
Do vote cancelation
Phase 2: Verify
Count actual frequency
Keep those > n/k

from typing import List

class Solution:
    def majorityElement(self, nums: List[int], k: int) -> List[int]:
        if k < 2:
            return []

        # Step 1: Find candidates
        candidates = {}

        for num in nums:
            if num in candidates:
                candidates[num] += 1

            elif len(candidates) < k - 1:
                candidates[num] = 1

            else:
                # cancel out
                to_remove = []
                for key in candidates:
                    candidates[key] -= 1
                    if candidates[key] == 0:
                        to_remove.append(key)

                for key in to_remove:
                    del candidates[key]

        # Step 2: Verify actual counts
        counts = {c: 0 for c in candidates}

        for num in nums:
            if num in counts:
                counts[num] += 1

        res = []
        for num, cnt in counts.items():
            if cnt > len(nums) // k:
                res.append(num)

        return res

'''