def NSBS2(lst: list[list[int]]) -> list[list[int]]:
    """computes and returns the array of partial sums for a 2xN grid without adjacent selections."""
    if not lst or len(lst)!=2 or not lst[0]:
        return [[], []]

    n = len(lst[0])
    if n==1:
        return [[max(lst[0][0], 0)], [max(lst[1][0], 0)]]

    grid_sum = [[
            max(lst[0][0], 0),
            max(lst[1][0]+lst[0][1], lst[0][1], lst[0][0], lst[1][0], 0)
        ], [
            max(lst[1][0], 0),
            max(lst[0][0]+lst[1][1], lst[1][1], lst[1][0], lst[0][0], 0)
        ]
    ]
    
    for i in range(2, n):
        best_prev_two = max(grid_sum[0][i-2], grid_sum[1][i-2])
        best_prev_one = max(grid_sum[0][i-1], grid_sum[1][i-1])

        grid_sum[0].append(max(
            best_prev_two + lst[0][i],
            grid_sum[1][i-1] + lst[0][i],
            best_prev_one
        ))

        grid_sum[1].append(max(
            best_prev_two + lst[1][i],
            grid_sum[0][i-1] + lst[1][i],
            best_prev_one
        ))

    return grid_sum


def max_sum(sum_: list[list[int]]) -> list[int]:
    """returns the array of maximum sums for each prefix length."""
    if not sum_ or not sum_[0]:
        return []
    
    return [max(sum_[0][i], sum_[1][i]) for i in range(len(sum_[0]))]