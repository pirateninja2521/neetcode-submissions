class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        charges = {5:0, 10:0}

        for bill in bills:
            match bill:
                case 5:
                    charges[5] += 1
                case 10:
                    if charges[5] == 0:
                        return False
                    charges[5] -= 1
                    charges[10] += 1
                case 20:
                    if charges[5] == 0:
                        return False
                    elif charges[10] == 0:
                        if charges[5] <= 2:
                            return False
                        charges[5] -= 3
                    else:
                        charges[5] -= 1
                        charges[10] -= 1
        
        return True