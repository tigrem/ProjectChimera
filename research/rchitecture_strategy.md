# Architecture Strategy for Project Chimera

## Agent Pattern
- **Chosen:** Hierarchical Swarm (uses FastRender pattern).

## Human-in-the-Loop
- Approval needed at strategic junctions (e.g., content generation).

## Database Choice
- **Selection:** NoSQL for high-velocity video metadata due to scalability.

```mermaid
graph TD;
    A[Global Orchestrator] --> B{Planner};
    B --> C[Worker Node];
    B --> D[Judge];