class Solution:
    @staticmethod
    def one_away(strA: str, strB: str):
        if strA == strB:
            return True

        list_strA = [i for i in strA]
        for i in list_strA:
            mylist = list_strA.copy()
            mylist.remove(i)
            if ''.join(mylist) == strB:
                return True
        
        list_strB = [j for j in strB]
        for i in list_strB:
            mylist = list_strB.copy()
            mylist.remove(i)
            if ''.join(mylist) == strA:
                return True

        for idx, i in enumerate(list_strA): 
            newlist_A = list_strA.copy()
            newlist_A.remove(i)
            newlist_B = list_strB.copy()
            newlist_B.remove(list_strB[idx])
            if ''.join(newlist_A) == ''.join(newlist_B):
                return True

        return False

if __name__ == '__main__':
    print(Solution.one_away('hello', 'hello'))
    print(Solution.one_away('jello', 'hello'))
    print(Solution.one_away('hello', 'jfdkfjkd'))
    print(Solution.one_away('bale', 'yale'))
    print(Solution.one_away('bale', 'bakr'))