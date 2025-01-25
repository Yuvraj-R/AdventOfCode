class Day19:

    def solution(self):
        with open("input.txt", "r") as file:
            lines = [line.strip() for line in file if line.strip() != ""]

        patterns = lines[0].split(", ")

        def backtrack(index, design, memo):
            # Check if the result for this index is already memoized
            if index in memo:
                return memo[index]

            # Base case: reached the end of the design
            if index == len(design):
                return 1

            res = 0
            # Try matching each pattern at the current index
            for pattern in patterns:
                if design.startswith(pattern, index):  # Pattern matches the substring
                    res += backtrack(index + len(pattern), design, memo)

            # Memoize the result for the current index
            memo[index] = res
            return res

        # Sum the results for all designs
        total_ways = 0
        for towel in lines[1:]:
            total_ways += backtrack(0, towel, {})

        return total_ways


if __name__ == "__main__":
    day19 = Day19()
    print(day19.solution())
