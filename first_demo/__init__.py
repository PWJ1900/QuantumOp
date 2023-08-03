from qiskit_ibm_provider import IBMProvider

provider = IBMProvider()
print(provider.backends())
# for ran_job in provider.backend.jobs(limit=5):
#     print(str(ran_job.job_id()) + " " + str(ran_job.status()))
"""
    one of my qaoa projects
"""
job = provider.backend.retrieve_job("62e7d52d3e1ce0b36e75d6d8")
print(job.result().get_counts())


