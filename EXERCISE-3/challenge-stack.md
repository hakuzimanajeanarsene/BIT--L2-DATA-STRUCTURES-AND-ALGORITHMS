# Stack Challenge: Show stack behavior for ["X", "Y", "Z"] with 2 pops and 1 push "W"

## Algorithmic Steps
1. **Initialize stack**: Start with an empty stack.
2. **Push elements**: Push "X", then "Y", then "Z" onto the stack.
3. **Pop twice**: Remove the top two elements (LIFO order).
4. **Push "W"**: Add "W" to the stack.
5. **Result**: Show the stack after each operation.

## Code & Explanation
```python
stack = []              # Step 1: Empty stack
stack.append("X")       # Step 2: Push X
stack.append("Y")       # Step 2: Push Y
stack.append("Z")       # Step 2: Push Z
print(stack)           # ['X', 'Y', 'Z']
stack.pop()            # Step 3: Pop Z
stack.pop()            # Step 3: Pop Y
print(stack)           # ['X']
stack.append("W")       # Step 4: Push W
print(stack)           # ['X', 'W']
```

### Step-by-step:
- After pushes: `["X", "Y", "Z"]`
- After 2 pops: `["X"]`
- After push "W": `["X", "W"]`
