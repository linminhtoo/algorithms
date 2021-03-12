# https://leetcode.com/problems/integer-to-roman/discuss/1102673/Python-Short-solution-explained
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        while num >= 1000:
            res += "M"
            num -= 1000        
        if num >= 900:
            res += "CM"
            num -= 900
        while num >= 500:
            res += "D"
            num -= 500
        if num >= 400:
            res += "CD"
            num -= 400
        while num >= 100:
            res += "C"
            num -= 100
        if num >= 90:
            res += 'XC'
            num -= 90
        while num >= 50:
            res += 'L'
            num -= 50
        if num >= 40:
            res += 'XL'
            num -= 40
        while num >= 10:
            res += 'X'
            num -= 10
        if num >= 9:
            res += 'IX'
            num -= 9
        while num >= 5:
            res += 'V'
            num -= 5
        if num >= 4:
            res += 'IV'
            num -= 4
        while num > 0:
            res += 'I'
            num -= 1
        return res

class Solution_mathy_concise:
    def intToRoman(self, num):
        def digit(a,b,c,dig):
            return ["",a,2*a,3*a,a+b,b,b+a,b+2*a,b+3*a,a+c][dig]
        
        l = ["I","V","X","L","C","D","M","!","!"]
        out, i = "", 0

        while num != 0:
            num, last = divmod(num, 10)
            out = digit(l[i], l[i+1], l[i+2], last) + out
            i += 2
        return out