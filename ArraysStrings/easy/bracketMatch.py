# https://www.pramp.com/challenge/xJZA01AxdlfpM2vZ2Wwa
def bracket_match(text):
  left_to_pair = 0
  unmatched = 0
  for char in text:
    if char == '(':
      left_to_pair += 1
    elif char == ')':
      if left_to_pair == 0:
        unmatched += 1
      else:
        left_to_pair -= 1
        
  return unmatched + left_to_pair

print(bracket_match('(()')) # 1
print(bracket_match('(())')) # 0
print(bracket_match('())(')) # 2