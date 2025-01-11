operations = []

with open("../../inputs/19-25/day_24.txt") as file:
    for line in file:
        if line == "\n":
            continue

        if "->" not in line:
            split = line.split(":")
        else:
            operations.append(line.strip())


"""
we need to find errors in operations

we're dealing with a 44-bit ripple carry adder, z00 being the least significant bit
that means our output will have 45 bit and we're starting with z00

we have OR, XOR, and AND.
for every bit pair, we need to a) know what it outputs and b) if it carries over
so for each bit pair, we need both those values in some way

we know that 4 output gates are swapped

now, since I am kind of dumb, I looked for inspiration on reddit:
https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3kt1je/
and stole the rules. we are basically checking for wrong operations and getting those output gates
"""
wrong_gates = set()

for operation in operations:
    parts = operation.split("->")
    output_gate = parts[1].strip()

    first, operator, second = parts[0].strip().split(" ")

    match operator:
        case "AND":
            if "x00" not in (first, second):
                for operation_2 in operations:
                    parts = operation_2.split("->")
                    first_2, operator_2, second_2 = parts[0].strip().split(" ")

                    if (output_gate == first_2 or output_gate == second_2) and operator_2 != 'OR':
                        wrong_gates.add(output_gate)

            if output_gate[0] == "z" and output_gate != "z45":
                wrong_gates.add(output_gate)

        case "OR":
            if output_gate[0] == "z" and output_gate != "z45":
                wrong_gates.add(output_gate)
        case "XOR":
            if (output_gate[0] not in ('x', 'y', 'z') and
                    first[0] not in ('x', 'y', 'z') and
                    second[0] not in ('x', 'y', 'z')):
                wrong_gates.add(output_gate)

            for operation_2 in operations:
                parts = operation_2.split("->")
                inputs = parts[0].strip().split(" ")

                first_2, operator_2, second_2 = inputs

                if (output_gate == first_2 or output_gate == second_2) and operator_2 == 'OR':
                    wrong_gates.add(output_gate)

# sort and print the wrong gates
print(",".join(sorted(wrong_gates)))
