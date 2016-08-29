# -*- coding: utf-8 -*-

# Author: Ricardo Dani (https://github.com/ricardodani)

"""
N Queens Problem
There are N queens to be placed on the chessboard NxN so they don’t threaten
each other. Create program that computes the number of ways this is possible
for the given N.

I.e: N = 4
Board should be: 4x4

Correct answer
|   | Q |   |   |
|   |   |   | Q |
| Q |   |   |   |
|   |   | Q |   |
Qs = [{0: 2}, {1: 0}, {2: 3}, {3: 1}]
        ↓
        k: the column
        v: the row
Rules:

Consider 2 queens {i: j} & {k: l}

They can attack each other if:
    - They are on the same row: k == l
    - They are on the same column: i == k
    - They are on the same diagonal: |i - k| == |j - l|

I'll start the test consider the first possible queen on coord. {0, 0}.
So, I'll propagate those tests on every other coordinate different than
{0, 0} to test if they are eligible. The not eligibles will be sinalized.
After the propagation, I'll search for the next possible coordinate that
is eligible, and propagate the tests again.
If we can't reach the N possible queens on the end of the coordinate {0, 0}
test then we backtrack and test on {0, 1} 'til {0, 3}.

The program return a Board configuration when founded or None if not founded.

Input: N
Default N: 4
"""

import sys

if __name__ == '__main__':
    print sys.argv
