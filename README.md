# genpark-compensation-saga-rollback-orchestrator-skill

Distributed Saga orchestrator executing compensating rollbacks in reverse topological order when external API or agent steps fail.

## Architecture

```mermaid
sequenceDiagram
    participant Agent
    participant Saga
    participant Resource
    Agent->>Saga: execute_step(Action A, Compensation A)
    Saga->>Resource: Perform Action A (Success)
    Agent->>Saga: execute_step(Action B, Compensation B)
    Saga->>Resource: Perform Action B (Fails!)
    Saga->>Resource: Execute Compensation A (Rollback)
```

## Features
- **Strict LIFO Rollback**: Undoes operations in exact reverse order.
- **Zero Dependencies**: 100% Python Standard Library.
