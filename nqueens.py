# -*- coding: utf-8 -*-

# Author: Ricardo Dani (https://github.com/ricardodani)

import sys


def new_board(n):
    return {"%dx%d" % (x % n, x / n): '-' for x in range(n*n)}

def can_attack_test(position, queens):
    '''
    Consider 2 queens {i: j} & {k: l}

    They can attack each other if:
        - They are on the same row: i == k
        - They are on the same column: j == l
        - They are on the same diagonal: |i - k| == |j - l|
    '''
    i, j = position.split('x')
    for queen in queens:
        k, l = queen.split('x')
        if i == k or j == l or abs(int(i) - int(k)) == abs(int(j) - int(l)):
            return True
    return False

# def print_board(board, n):

    # def _empty_if_none(value):
        # if value is None:
            # return ' '
        # return value

    # print ''.join([
        # '|  %s  %s' % (_empty_if_none(board["%dx%d" % (x, y)]), '|\n' if y % n == n - 1 else '')
            # for x in range(n)
            # for y in range(n)
    # ])


def nqueens(n):
    '''
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
    '''
    print "Solving N-Queens problem with n == %d" % n

    # one attempt per column
    results = []
    for attempt in range(n):
        board = new_board(n)
        queen = '0x%d' % attempt
        queens = [queen]
        board[queen] = 'Q'
        positions = board.keys()
        positions.sort()
        for position in positions:
            if not can_attack_test(position, queens):
                board[position] = 'Q'
                queens.append(position)
        if len(queens) == n:
            results.append(queens)

    if results:
        print "{} results found: \n{}".format(len(results), results)
    else:
        print "No results found"

if __name__ == '__main__':
    default = 4 # min 1
    try:
        n = max(int(sys.argv[1]), 1) if len(sys.argv) == 2 else default
    except ValueError:
        print "Invalid argument."
    else:
        nqueens(n)

