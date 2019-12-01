## Unpacking Packed Values

Unpacking is the act of splitting packed values into individual variables containing in a list or tuple. The unpacking into individual variables is based on the relative positions of each element.

The entire RHS is evaluated first and completely then assignments are made to the LHS.

## Extended Unpacking

- The * operator can only be used once in the LHS of an unpacking assignment
- The ** unpacking


- We set a default for dt to None
- Inside the function, we test to see if dt is still None
- If dt is None, set it to the current data/time
- Otherwise, use what the caller specified for dt

In general, always beware of using a mutable object (or a callable) for an argument default