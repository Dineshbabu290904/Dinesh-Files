# Read the input string
s = input()

# Initialize a stack, a maximum length, a maximum count, a current length, a current count, and a current start
stack = []
max_len = 0
max_count = 0
cur_len = 0
cur_count = 0
cur_start = 0

# Loop through the string
for i in range(len(s)):
  # If the current character is an opening bracket, push its index to the stack
  if s[i] in "([": 
    stack.append(i)
  # If the current character is a closing bracket
  else:
    # If the stack is empty or the top of the stack does not match the current bracket, reset the stack, the current length, the current count, and the current start
    if not stack or (s[i] == ")" and s[stack[-1]] != "(") or (s[i] == "]" and s[stack[-1]] != "["):
      stack = []
      cur_len = 0
      cur_count = 0
      cur_start = i + 1
    # If the top of the stack matches the current bracket, pop it and update the current length and count
    else:
      stack.pop()
      cur_len = i - cur_start + 1
      cur_count = s[cur_start:i+1].count("[")
      # If the current length is greater than the maximum length, update the maximum length and the maximum count
      if cur_len > max_len:
        max_len = cur_len
        max_count = cur_count
      # If the current length is equal to the maximum length, update the maximum count if the current count is greater
      elif cur_len == max_len:
        max_count = max(max_count, cur_count)

# Print the maximum count and the maximum substring
print(max_count)
print(s[cur_start:cur_start+max_len])
