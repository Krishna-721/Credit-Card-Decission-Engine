# Tasks Document — Phase 1

This document breaks down Phase 1 into concrete, sequential engineering tasks derived strictly from `requirements.md` and `design.md`.

The goal of Phase 1 is to deliver a **deterministic, explainable credit card decision engine** with a production-ready backend foundation.

---

## Phase 1 Goals

* Establish a clean backend foundation
* Implement a rule-driven decision engine
* Ensure correctness, explainability, and performance
* Prepare the system for future scaling and ML-assisted features

---

## 1. Repository & Project Setup

1. Initialize repository using the Universal Project Template
2. Create directory structure:

   * `/specs`
   * `/backend`
   * `/infra`
   * `/docs`
3. Add and lock `requirements.md` and `design.md`
4. Setup `.env.example`
5. Configure `.gitignore`

---

## 2. Backend Skeleton (Django)

1. Create Django project
2. Create core Django apps:

   * `users`
   * `cards`
   * `rules`
   * `engine`
3. Configure Django settings for:

   * PostgreSQL
   * Redis
   * environment-based configs
4. Add Django REST Framework

---

## 3. Data Modeling (ORM Level)

1. Define User model extensions (preferences, goals)
2. Define CreditCard model
3. Define RewardRule model
4. Define RewardCap model
5. Create and apply migrations
6. Add Django Admin registration for all models

---

## 4. Rule Engine Implementation (Core Logic)

1. Implement rule parsing layer (data → executable rules)
2. Implement Eligibility Filter
3. Implement Reward Rule Evaluator
4. Implement Cap & Cycle Resolver
5. Implement Reward Normalizer
6. Implement Ranking Engine
7. Implement Explanation Generator

> All logic must be framework-agnostic and unit-testable

---

## 5. API Layer

1. Design request/response schemas
2. Implement transaction recommendation endpoint
3. Validate inputs and edge cases
4. Wire API to decision engine

---

## 6. Caching Layer

1. Setup Redis connection
2. Cache card metadata and reward rules
3. Cache recommendation responses (short TTL)
4. Implement cache invalidation hooks

---

## 7. Testing

1. Unit tests for rule evaluation
2. Unit tests for cap handling
3. Unit tests for normalization logic
4. Integration tests for recommendation endpoint

---

## 8. Infra & DevOps (Phase 1)

1. Create Dockerfile for backend
2. Create `docker-compose.yml`:

   * Django app
   * PostgreSQL
   * Redis
3. Validate local environment bootstrapping

---

## 9. Documentation

1. Update README with setup instructions
2. Document decision engine flow
3. Document reward rule format

---

## Phase 1 Exit Criteria

Phase 1 is considered complete when:

* API returns correct, explainable recommendations
* Reward rules are fully data-driven
* New cards and rules can be added without code changes
* System runs locally using Docker
* Core logic is covered by tests
