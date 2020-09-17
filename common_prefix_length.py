def commonPrefix(inputs):
    # Write your code here
    out_list = []
    for this_input in inputs:
        total = len(this_input) # true for all strings 

        for cut_index in range(1, len(this_input)):
            suffix = this_input[cut_index:]

            for charA, charB in zip(suffix, this_input):
                if charA == charB:
                    total += 1
                else:
                    break
        out_list.append(total)
    
    return out_list  