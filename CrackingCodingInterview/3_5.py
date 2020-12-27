from typing import List

class Solution:
    @staticmethod
    def sort_stack(stack: List[int]):
        temp_stack = []
        result_stack = []

        orig_len_stack = len(stack)
        curr_len_stack = len(stack)

        while len(result_stack) < orig_len_stack:
            while len(temp_stack) < curr_len_stack:
                popped = stack.pop()
                if len(temp_stack) == 0:
                    temp_stack.append(popped)
                else:
                    if popped > temp_stack[-1]:
                        temp_popped = temp_stack.pop()
                        temp_stack.append(popped)
                        temp_stack.append(temp_popped)
                    else:
                        temp_stack.append(popped)

            result_stack.append(temp_stack.pop())
            curr_len_stack -= 1
            stack = temp_stack.copy()
            temp_stack = []
        
        stack = []
        while result_stack:
            stack.append(result_stack.pop())

        return stack

if __name__ == '__main__':
    print(Solution.sort_stack([0, 2, 5]))
        
