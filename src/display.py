from src import NSBS2, max_sum, add_numbers

def _as_grid(data: list[int] | list[list[int]]) -> list[list[int]]:
    if not data: return []
    if isinstance(data[0], list): return data
    return [data]


def _calc_width(grids: list[list[int]]) -> int:
    values = [str(x) for grid in grids for row in grid if row for x in row]
    return max((len(v) for v in values))+1


def print_array(
    data:  list[int] | list[list[int]],
    width: int | None = None,
    sep:   str = " "
) -> None:
    rows = _as_grid(data)
    if width is None: width = _calc_width([rows])
    for row in rows:  print(sep.join(f"{x:>{width}}" for x in row))


def view(lst: list[list[int]]) -> None:
    partial_sum = NSBS2(lst)
    maxs = max_sum(partial_sum)
    adds = add_numbers(partial_sum)

    grids = [_as_grid(x) for x in [lst, partial_sum, maxs, adds]]
    width = _calc_width(grids)

    print("Given array:")
    print_array(lst, width)

    print("\nPartial sums:")
    print_array(partial_sum, width)

    print("\nThe biggest sums:")
    print_array(maxs)

    print("\nAdds number:")
    print_array(adds)

    print(f'\nSum of non adjacent: {sum(adds)}')
