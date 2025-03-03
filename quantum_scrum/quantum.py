import random
from qiskit import transpile
from qiskit_aer import AerSimulator      # <-- this line

from .circuits import interpret_measure

_BACKEND = AerSimulator()                # <-- one global backend


def measure_once(qc):
    """Run one shot and map bit → DONE / BLOCKED."""
    tqc = transpile(qc, _BACKEND)
    job = _BACKEND.run(tqc, shots=1, memory=True)
    bitstring = job.result().get_memory()[0]
    bit = int(bitstring[-1])
    return interpret_measure(bit)

def random_noise():
    return random.uniform(0.1, 0.4)
