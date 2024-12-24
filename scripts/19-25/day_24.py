from collections import deque

gate_values = {}
operations = []

with open("../../inputs/19-25/day_24.txt") as file:
    for line in file:
        if line == "\n":
            continue

        if "->" not in line:
            split = line.split(":")
            gate_values.update({split[0].strip(): int(split[1].strip())})
        else:
            operations.append(line.strip())

queue = deque(operations)

while queue:
    operation = queue.popleft()

    parts = operation.split("->")
    output_gate = parts[1].strip()

    inputs = parts[0].strip().split(" ")

    first, operator, second = inputs

    if first not in gate_values or second not in gate_values:
        queue.append(operation)  # re-queue if inputs not ready
        continue

    match operator:
        case "AND":
            gate_values[output_gate] = 1 if gate_values[first] == gate_values[second] == 1 else 0
        case "OR":
            gate_values[output_gate] = 1 if gate_values[first] == 1 or gate_values[second] == 1 else 0
        case "XOR":
            gate_values[output_gate] = 1 if gate_values[first] != gate_values[second] else 0

output_gates = []

for gate in gate_values.keys():
    if gate.startswith("z"):
        name = int(gate.replace("z", ""))
        output_gates.append((name, gate_values[gate]))

output_gates.sort(key=lambda tup: (tup[0]), reverse=True)

bits = ""

for gate in output_gates:
    number = gate[1]
    bits += str(number)

print(int(bits, 2))
