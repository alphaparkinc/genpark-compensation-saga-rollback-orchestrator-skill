"""Compensation Saga Rollback Orchestrator.
100% Python Standard Library.
"""

class SagaRollbackOrchestrator:
    """Executes multi-step transactions with reverse compensating rollbacks upon failure."""
    def __init__(self):
        self.executed_steps = []

    def execute_step(self, step_name: str, action_func, rollback_func) -> bool:
        try:
            action_func()
            self.executed_steps.append({
                "step": step_name,
                "rollback": rollback_func,
                "status": "committed"
            })
            return True
        except Exception:
            self.rollback_all()
            return False

    def rollback_all(self) -> list:
        rollback_log = []
        while self.executed_steps:
            step = self.executed_steps.pop()
            try:
                step["rollback"]()
                rollback_log.append(f"Successfully rolled back {step['step']}")
            except Exception as e:
                rollback_log.append(f"Rollback failed for {step['step']}: {e}")
        return rollback_log
