class Day19:

    def solution(self):
        with open("input.txt", "r") as file:
            lines = [line.strip() for line in file]

        patterns = []
        i = 0
        while lines[i] != "":
            patterns.extend(lines[i].split(", "))
            i += 1

        def backtrack(cur):
            res = 0

            for pattern in patterns:
                if len(pattern) > len(cur):
                    continue
                elif pattern == cur:
                    return 1
                elif pattern == cur[0:len(pattern)]:
                    if backtrack(cur[len(pattern):]) > 0:
                        return 1

            return res

        return sum(backtrack(towel) for towel in lines[1:])


day19 = Day19()
print(day19.solution())
