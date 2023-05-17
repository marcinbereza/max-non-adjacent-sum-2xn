def add_numbers(sum_: list[list[int]]) -> list[int]:
    """Reconstructs selected values by backtracking througth partial sums."""
    if not sum_ or not sum_[0]:
        return []

    backwards_sum = []
    chosens = []
    index = 0 if sum_[0][-1] >= sum_[1][-1] else 1

    # Starting from the end, sums are added to the array;
    # for each of these, the maximum value is calculated.
    for i in range(len(sum_[0])-1, -1, -1):
        prev_val = sum_[index][i-1] if i>0 else 0
        if sum_[index][i]!=prev_val:
            if sum_[index][i]!=0:
                backwards_sum.append(sum_[index][i])
            index = (index+1)%2

    # The differences between successive partial sums yield specific numbers.
    for i in range(len(backwards_sum)-1):
        number = backwards_sum[i] - backwards_sum[i+1]
        if number!=0:
            chosens.append(number)

    if len(backwards_sum)>0:
        chosens.append(backwards_sum[-1])

    return list(reversed(chosens))