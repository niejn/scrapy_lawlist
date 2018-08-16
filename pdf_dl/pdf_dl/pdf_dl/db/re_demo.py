import re

line = '2018-07-18'
nums = re.findall(r'(\d+)', line)
ans = ''.join(nums)
print(ans)