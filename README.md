# Project Chimera

**Role:** Forward Deployed Engineer (FDE) Trainee  
**Author:** Tigrem Sahilu  
**Mission:** Architect the Factory that builds the Autonomous Influencer  
**Status:** Governed, Spec-Driven, Pre-Implementation  
**Date:** February 6, 2026  

---

## Overview

Project Chimera is an **AI-native, specification-governed software factory** designed to produce **Autonomous AI Influencers** safely and at scale.

Rather than relying on fragile prompt-based logic, Chimera is engineered using **Specification-Driven Development (SDD)**, **Test-Driven Development (TDD)**, and **automated governance**. Autonomy is treated as an outcome of strong infrastructure, not a shortcut.

This repository represents the completion of **Tasks 1–3**:
1. Research & Domain Strategy  
2. Specification & Context Engineering  
3. Infrastructure, Testing, and Governance  

Implementation is intentionally incomplete. The system is prepared for **controlled autonomy**, not accidental execution.

---

## Core Principles

- **Specs are Law** – `/specs` is the single source of truth  
- **Tests define intent** – failing tests establish goalposts  
- **Autonomy requires guardrails** – governance is mandatory  
- **Environment parity matters** – Docker and CI eliminate drift  
- **Human oversight is explicit** – safety is designed, not assumed  

---

## Architecture Summary

Chimera follows a **Hierarchical Swarm** agent pattern:

- Governor / Orchestrator coordinates execution  
- Planner decomposes goals  
- Specialized skills execute deterministic tasks  
- Safety / Judge Agent enforces policy  
- Human approval gates protect publication  

The system is designed to operate as a **first-class citizen in the Agent Social Network**, supporting future integration with OpenClaw-style capability advertisement and reputation signaling.

---

## Repository Structure

```plaintext
ProjectChimera/
├── .cursor/rules            # AI context & governance rules
├── .github/workflows/       # CI/CD automation
├── docs/                    # Research & architecture strategy
├── skills/                  # Runtime agent skill stubs
│   ├── skill_fetch_trends/
│   ├── skill_generate_content/
│   └── skill_safety_check/
├── specs/                   # Master specifications (source of truth)
├── tests/                   # Failing tests (TDD goalposts)
├── Dockerfile               # Reproducible runtime environment
├── Makefile                 # Standardized automation commands
└── pyproject.toml           # Python dependency management
Specifications (/specs)
The /specs directory defines what the system is allowed to do.

Key files include:

_meta.md – Vision, constraints, and non-goals

functional.md – Agent-centric user stories

technical.md – API contracts and data models

openclaw_integration.md – Agent social protocols and security rules

Agents must read specs before generating code.

Skills (/skills)
Skills represent deterministic, governed execution units.

Implemented as stubs with explicit contracts:

skill_fetch_trends – Retrieves trend intelligence

skill_generate_content – Produces influencer content

skill_safety_check – Evaluates policy and safety compliance

Each skill:

Defines clear input/output contracts

Has no hidden side effects

Is intentionally unimplemented to support TDD

Testing Strategy (/tests)
Tests were written before implementation.

Current tests:

test_trend_fetcher.py – Validates trend schema contracts

test_skills_interface.py – Ensures skill interfaces exist and conform

All tests currently fail by design, representing governed execution slots waiting to be filled.

Environment & Tooling
Python
Python 3.x

Virtual environments via venv

Dependencies managed in pyproject.toml

Docker
Ensures environment parity across machines and CI.

Makefile Commands
make setup        # Install dependencies
make test         # Run tests locally
make docker-test  # Run tests inside Docker
CI/CD & Governance
A GitHub Actions workflow enforces governance on every push:

Automated test execution

Spec-alignment validation

Security and behavior review simulation

Pipeline failure is intentional, signaling readiness for implementation rather than completion.

Observability
Tenx MCP Sense was used throughout development to:

Track engineering activity

Maintain traceability

Enforce accountability

Observability is treated as a first-class system requirement.

Current State
✔ Research completed
✔ Architecture defined
✔ Specifications written
✔ Tests established
✔ CI/CD active
✔ Governance enforced

🚫 Business logic intentionally absent

