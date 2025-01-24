class Day17:
    def solution(self):
        with open("input.txt", "r") as file:
            lines = [line.strip() for line in file]

        registers = [int(lines[i].split(":")[1].strip()) for i in range(3)]
        program = list(map(int, lines[-1].split(":")[1].strip().split(",")))

        def combo(x): return x if x <= 3 else registers[x - 4]
        output = []

        def adv(ip):
            registers[0] //= 2 ** combo(program[ip + 1])
            return ip + 2

        def bxl(ip):
            registers[1] ^= program[ip + 1]
            return ip + 2

        def bst(ip):
            registers[1] = combo(program[ip + 1]) % 8
            return ip + 2

        def jnz(ip):
            return program[ip + 1] if registers[0] != 0 else ip + 2

        def bxc(ip):
            registers[1] ^= registers[2]
            return ip + 2

        def out(ip):
            output.append(str(combo(program[ip + 1]) % 8))
            return ip + 2

        def div_helper(ip, reg_index):
            registers[reg_index] = registers[0] // (2 **
                                                    combo(program[ip + 1]))
            return ip + 2

        ip = 0  # instruction pointer

        instruction_map = {
            0: adv,
            1: bxl,
            2: bst,
            3: jnz,
            4: bxc,
            5: out,
            6: lambda ip: div_helper(ip, 1),
            7: lambda ip: div_helper(ip, 2)
        }

        while ip < len(program):
            ip = instruction_map[program[ip]](ip)

        print(",".join(output))

    def solution2(self):
        import re
        with open("input.txt") as f:
            puzzle_input = f.read()

        reg_part, prog_part = puzzle_input.split('\n\n')
        _, B, C = map(int, re.findall(r'\d+', reg_part))
        program = [int(x) for x in re.findall(r'\d+', prog_part)]
        n = len(program)

        def run_program(A):
            r = {'A': A, 'B': B, 'C': C}

            def combo(op):
                if op == 4:
                    return r['A']
                if op == 5:
                    return r['B']
                if op == 6:
                    return r['C']
                return op
            i = 0
            out = []
            while i < n:
                opcode, operand = program[i:i+2]
                match opcode:
                    case 0: r['A'] >>= combo(operand)
                    case 1: r['B'] ^= operand
                    case 2: r['B'] = combo(operand) % 8
                    case 3:
                        if r['A']:
                            i = operand - 2
                    case 4: r['B'] ^= r['C']
                    case 5: out.append(combo(operand) % 8)
                    case 6: r['B'] = r['A'] >> combo(operand)
                    case 7: r['C'] = r['A'] >> combo(operand)
                i += 2
            return out

        A = 0
        for i in reversed(range(n)):
            A <<= 3
            while run_program(A) != program[i:]:
                A += 1

        print(A)


day17 = Day17()
day17.solution()
day17.solution2()
