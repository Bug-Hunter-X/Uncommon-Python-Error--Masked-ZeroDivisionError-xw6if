# Uncommon Python Error: Masked ZeroDivisionError

This repository demonstrates a subtle and uncommon error in Python that can be easily overlooked: a masked ZeroDivisionError.

The `bug.py` file contains a function that has a potential for a ZeroDivisionError, but this potential error isn't immediately apparent.

The `bugSolution.py` file shows how to fix this issue by adding a more robust check for the divisor before attempting the division. This illustrates a best practice for handling division by zero, preventing unexpected crashes and improving code reliability.

## How to reproduce the bug:
1. Run `bug.py` with `a = 0` and `b = any number` . You'll see a ZeroDivisionError
2. Run `bug.py` with `a = any number !=0` and `b = any number`. It will work fine but this does not mean the code is error free.

## How to solve the bug:
Refer to `bugSolution.py` for the solution. The solution checks for a zero divisor before the division operation occurs.