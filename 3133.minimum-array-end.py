# @leet start


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        return (            (q := n - 1 << 1) * 0 + sum(
                (
                    1 << i & x
                )  # First attempt: Check if bit i is set in x  # If first part is 0, use second part
                or
                # Right-shift q and use its last bit, shifted to position i
                (q := q >> 1) % 2 << i
                for i in range(50)
            )
        )


# LOOP:

# -----
# If x -> 1 -> copy to result
# If x -> 0 -> give q's last bit
# Right-shift q
# -----


# @leet end
