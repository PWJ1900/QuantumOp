"""
Pulse-efficient transpilation

"""
from qiskit.transpiler import PassManager
from qiskit.circuit.library.standard_gates.equivalence_library import (
    StandardEquivalenceLibrary as std_eqlib,
)
from qiskit.transpiler.passes import (
    Collect2qBlocks,
    ConsolidateBlocks,
    UnrollCustomDefinitions,
    BasisTranslator,
    Optimize1qGatesDecomposition,
)
from qiskit.transpiler.passes.calibration.builders import RZXCalibrationBuilderNoEcho
from qiskit.transpiler.passes.optimization.echo_rzx_weyl_decomposition import (
    EchoRZXWeylDecomposition,
)

from matplotlib import pyplot as plot
from qiskit.test.mock import FakeBelem

backend = FakeBelem()

inst_map = backend.defaults().instruction_schedule_map
channel_map = backend.configuration().qubit_channel_mapping
rzx_basis = ["rzx", "rz", "x", "sx"]

pulse_efficient = PassManager(
    [
        # Consolidate consecutive two-qubit operations.
        Collect2qBlocks(),
        ConsolidateBlocks(basis_gates=["rz", "sx", "x", "rxx"]),
        # Rewrite circuit in terms of Weyl-decomposed echoed RZX gates.
        EchoRZXWeylDecomposition(backend.defaults().instruction_schedule_map),
        # Attach scaled CR pulse schedules to the RZX gates.
        RZXCalibrationBuilderNoEcho(
            instruction_schedule_map=inst_map, qubit_channel_mapping=channel_map
        ),
        # Simplify single-qubit gates.
        UnrollCustomDefinitions(std_eqlib, rzx_basis),
        BasisTranslator(std_eqlib, rzx_basis),
        Optimize1qGatesDecomposition(rzx_basis),
    ]
)

from qiskit import QuantumCircuit

circ = QuantumCircuit(3)
circ.h([0, 1, 2])
circ.rzx(0.5, 0, 1)
circ.swap(0, 1)
circ.cx(2, 1)
circ.rz(0.4, 1)
circ.cx(2, 1)
circ.rx(1.23, 2)
circ.cx(2, 1)
circ.draw("mpl")

pulse_efficient.run(circ).draw("mpl", scale=0.5, fold=False)
plot.show()

