from client import SagaRollbackOrchestrator

saga = SagaRollbackOrchestrator()
log = []
saga.execute_step("step1", lambda: log.append("step1 done"), lambda: log.append("step1 reverted"))
print("Executed step 1. Log:", log)
