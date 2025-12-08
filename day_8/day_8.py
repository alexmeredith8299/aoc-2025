import numpy as np

def load_vec():
    vec = np.genfromtxt('input.txt', delimiter=',')
    return vec

def get_norms(vec):
    norms = []
    for i in range(vec.shape[0]):
        for j in range(i+1, vec.shape[0]):
            norms.append((i, j, np.linalg.norm(vec[i, :]-vec[j, :])))
    return norms

def construct_circuits(sorted_norms, n_boxes):
    circuits = []
    for (start, end, dist) in sorted_norms:
        start_circuit = None
        end_circuit = None
        for i, circuit in enumerate(circuits):
            if start in circuit:
                start_circuit = i
            if end in circuit:
                end_circuit = i
        if start_circuit is None and end_circuit is None:
            circuits.append([start, end])
        elif start_circuit is None and end_circuit is not None:
            new_circuit = circuits[end_circuit]
            new_circuit.append(start)
            circuits[end_circuit] = new_circuit
        elif start_circuit is not None and end_circuit is None:
            new_circuit = circuits[start_circuit]
            new_circuit.append(end)
            circuits[start_circuit] = new_circuit
        elif start_circuit != end_circuit:
            new_circuit_1 = circuits[start_circuit]
            new_circuit_2 = circuits[end_circuit]
            new_circuit_1.extend(new_circuit_2)
            combined = list(set(new_circuit_1))
            circuits[start_circuit] = combined
            del circuits[end_circuit]
        if len(circuits) == 1 and len(circuits[0]) == n_boxes:
            return circuits, start, end
    return circuits, -1, -1

def part_1(vec):
    norms = get_norms(vec)
    sorted_norms = sorted(norms, key=lambda x:x[2])
    circuits, _, _ = construct_circuits(sorted_norms[:1000], 1000)
    circuit_sizes = [len(circuit) for circuit in circuits]
    sorted_sizes = sorted(circuit_sizes)
    return sorted_sizes[-1]*sorted_sizes[-2]*sorted_sizes[-3]

def part_2(vec):
    norms = get_norms(vec)
    sorted_norms = sorted(norms, key=lambda x:x[2])
    circuits, box_1, box_2 = construct_circuits(sorted_norms, 1000)
    return vec[box_1, 0]*vec[box_2, 0]


vec = load_vec()
#ans_1 = part_1(vec)
ans_2 = part_2(vec)
breakpoint()
