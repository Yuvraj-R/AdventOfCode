class Day19:

    def solution(self):
        with open("input.txt", "r") as file:
            lines = [line.strip() for line in file if line.strip() != ""]

        patterns = lines[0].split(", ")

        def backtrack(index, design, memo):
            if index in memo:
                return memo[index]

            if index == len(design):
                return 1

            res = 0
            for pattern in patterns:
                if design.startswith(pattern, index):
                    res += backtrack(index + len(pattern), design, memo)

            memo[index] = res
            return res

        total_ways = 0
        for towel in lines[1:]:
            total_ways += backtrack(0, towel, {})

        return total_ways


if __name__ == "__main__":
    day19 = Day19()
    print(day19.solution())
