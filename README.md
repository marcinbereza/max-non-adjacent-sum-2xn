## Problem & Assumptions
Find the maximum sum in a **2*N** grid (2 rows, N columns) without selecting adjacent cells (neither horizontally nor vertically).

### Assumptions
- **Negative numbers & zero:** When handling negative values, consider `0` as the floor / baseline choise rather than adding a negative number that would shrink the sum
- **Transitions (dynamic programming):** The maximum sum up to the current step can come from:
    1. The best sum from `2 steps back` plus the current cell value. 
    2. From the `top` cell: the previous step's sum from the `bottom` cell plus the current top value.
    3. For the `bottom` cell: the previous step's sum from the `top` cell plus the current bottom value.
    4. Carrying forward the best previous sum **without adding** the current value.