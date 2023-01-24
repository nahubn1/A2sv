class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ptr1, ptr2 = 0, len(skill)-1
        total_skill  = skill[0] + skill[-1]
        chemistry = 0
        while ptr1 < ptr2:
            if skill[ptr1] + skill[ptr2] == total_skill:
                chemistry += skill[ptr1] * skill[ptr2]
                ptr1 += 1
                ptr2 -= 1
            else:
                return -1

        return chemistry 