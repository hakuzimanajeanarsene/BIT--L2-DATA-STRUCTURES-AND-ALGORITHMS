# Queue Challenge: UR Cafeteria Orders

## Algorithmic Steps
1. **Initialize queue**: Start with an empty queue.
2. **Enqueue orders**: Add orders as they arrive (FIFO).
3. **Serve orders**: Remove from the front.
4. **Stack problem**: If using a stack (LIFO), last order is served first, which is incorrect for food service.

## Code & Explanation
```python
queue = []
queue.append("Order1")  # Enqueue
queue.append("Order2")
queue.append("Order3")
print(queue)            # ['Order1', 'Order2', 'Order3']
served = queue.pop(0)   # Serve first order
print(served)           # 'Order1'
print(queue)            # ['Order2', 'Order3']
```

### What goes wrong with stack?
If you use a stack:
```python
stack = []
stack.append("Order1")
stack.append("Order2")
stack.append("Order3")
served = stack.pop()    # 'Order3' is served first! Wrong order.
```
- The last order is served first, not the first. This is not fair for food orders.
