# Reflection: Why does stack naturally support undo actions?

A stack uses Last-In-First-Out (LIFO) order. The most recent action is always on top, so when you "undo," you remove the last thing you did. This matches how undo works in real life: you always reverse your most recent step first. Stacks make it easy to keep track of and reverse actions in the correct order.
