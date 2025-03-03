from qiskit import QuantumCircuit
import random


def new_story_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(1, 1, name="StoryQ")
    qc.h(0)
    qc.measure(0, 0)
    return qc


def entangle(a: QuantumCircuit, b: QuantumCircuit) -> QuantumCircuit:
    merged = QuantumCircuit(2, 2, name="EntangledStories")
    merged.compose(a.remove_final_measurements(inplace=False), qubits=[0], inplace=True)
    merged.compose(b.remove_final_measurements(inplace=False), qubits=[1], inplace=True)
    merged.cx(0, 1)
    if random.random() < 0.5:
        merged.x(1)
    merged.measure([0, 1], [0, 1])
    return merged


def interpret_measure(bit: int) -> str:
    return {0: "DONE", 1: "BLOCKED"}.get(bit, "WTF‑QUANTUM")
