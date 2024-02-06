#!/usr/bin/python3

"""
Display the pascal triangle

The algorithm to find a number in a certain location is:
    (n!)/(k!(n-k)!)
    This approach has a complexity of O(n^3)
    which is pretty slow (plus python speed)
    Another speed concern is how the factorial is derived.
    May the speed be with you all.
"""


def pascal_triangle(n):
    """Return the pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    for j in range(1, n):
        new_row = [1]
        for i in range(1, j):
            # Calculate the next value in the row using the formula
            # (n!)/(k!(n-k)!) where n = j, k = i
            new_value = triangle[j-1][i-1] + triangle[j-1][i]
            new_row.append(new_value)
        new_row.append(1)
        triangle.append(new_row)

    return triangle


def get_value_at_pos(n, k):
    """Get a value at certain location"""
    top_div = get_fact(n)
    bot_div = get_fact(k) * get_fact(n-k)

    return int(top_div/bot_div)


def get_fact(num):
    """Get the factorial of a number (positive/unsigned) int"""
    if num < 1:
        return 1
    else:
        return num*get_fact(num-1)
