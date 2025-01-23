### PART 1 ###

class Day17:
    def solution(self):
        with open("input.txt", "r") as file:
            lines = [line.strip() for line in file]

        registers = [int(lines[i].split(":")[1].strip()) for i in range(3)]
        program = [int(x) for x in lines[-1].split(":")[1].strip().split(",")]

        def combo(x):
            if x <= 3:
                return x
            else:
                return registers[x-4]

        output = []

        def adv(ip):
            numerator = registers[0]
            denominator = 2 ** combo(program[ip+1])
            registers[0] = numerator // denominator
            return ip + 2

        def bxl(ip):
            registers[1] = registers[1] ^ program[ip+1]
            return ip + 2

        def bst(ip):
            registers[1] = combo(program[ip+1]) % 8
            return ip + 2

        def jnz(ip):
            if registers[0] == 0:
                return ip + 2

            return program[ip+1]

        def bxc(ip):
            registers[1] = registers[1] ^ registers[2]
            return ip + 2

        def out(ip):
            output.append(str(combo(program[ip+1]) % 8))
            return ip + 2

        def bdv(ip):
            numerator = registers[0]
            denominator = 2 ** combo(program[ip+1])
            registers[1] = numerator // denominator
            return ip + 2

        def cdv(ip):
            numerator = registers[0]
            denominator = 2 ** combo(program[ip+1])
            registers[2] = numerator // denominator
            return ip + 2

        ip = 0  # instruction pointer

        instruction_map = {0: adv, 1: bxl, 2: bst,
                           3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

        while ip < len(program):
            ip = instruction_map[program[ip]](ip)

        print(",".join(output))


day17 = Day17()
day17.solution()
