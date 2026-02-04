## System Architecture Diagram

```mermaid
graph TD
    A[Governor / Orchestrator]
    A --> B[Planner Agent]
    B --> C[Trend Fetcher]
    B --> D[Content Generator]
    C --> E[Metadata Store]
    D --> F[Safety / Judge Agent]
    F --> G[Human Approval Gate]
