from qiskit import IBMQ

"""
    author: BuriPan
"""

# TODO:
#  1. upload a "qaoa" program
#  2. use PET to op this program


from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit import *

# Save an IBM Quantum account.
# QiskitRuntimeService.save_account(channel="ibm_quantum", token="d5f60eb7a8863b0814ae27e691ea0422e5bd7d814ebcf42ce46382e210a1813078a067d5345462a57963a9c5f3504e6087d936342376a270bef1b30bf8edfccc", overwrite=True)

service = QiskitRuntimeService(channel="ibm_quantum", token='d5f60eb7a8863b0814ae27e691ea0422e5bd7d814ebcf42ce46382e210a1813078a067d5345462a57963a9c5f3504e6087d936342376a270bef1b30bf8edfccc')
backend = service.get_backend("ibmq_qasm_simulator")
program_id = "qasm3-runner"
qaoa_program = service.runtime.program(program_id)
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0, 1)
# qc.measure_all()
#
# sampler = Sampler(session=backend)
# job = sampler.run(qc)
# print(f"job id: {job.job_id()}")
# result = job.result()
# print(f" > Quasi probability distribution: {result.quasi_dists[0]}")
print(f"Program name: {qaoa_program.name}, Program id: {qaoa_program.program_id}")
print(qaoa_program.parameters())