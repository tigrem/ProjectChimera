# Technical Specification

## Content Draft API

### Input Contract
```json
{
  "trend_name": "string",
  "platform": "string",
  "tone": "string",
  "max_length": "number"
}
```

### Output Contract
```json
{
  "text": "string",
  "hashtags": ["string"],
  "risk_score": "number"
}
```

## Database Schema (Logical ERD)

### Agent
- id (UUID, PK)
- name
- role
- created_at

### Trend
- id (UUID, PK)
- platform
- name
- score
- fetched_at

### Content
- id (UUID, PK)
- trend_id (UUID, FK → Trend.id)
- platform
- content_json (JSONB)
- status (draft | approved | rejected)
- created_at

### AuditLog
- id (UUID, PK)
- agent_id (UUID, FK → Agent.id)
- action
- timestamp
