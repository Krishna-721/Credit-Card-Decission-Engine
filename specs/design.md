# Design Document

# Overview

This is a credit card decision-based engine that evaluates user inputs, reward rules, caps, and exclusions to recommend the optimal credit card for a given transaction.

The system is deterministic, backend-driven, and focused on correctness and explainability rather than predictive behavior.

---

## 1. Architecture Priorities

The system architecture prioritizes:

* **Correctness** – Reward calculations must strictly follow published card rules
* **Explainability** – Every recommendation must be traceable to explicit rules
* **High Throughput** – Optimized for read-heavy recommendation workloads
* **Rule-driven Extensibility** – New cards and rules can be added without code changes

---

## 2. High-Level Architecture

```
 Client (Browser / API Consumer) 
            |
            v
         API Layer 
   (Django REST Framework)
            |
            v
    Decision Engine Layer 
      ├── Eligibility Filter
      ├── Reward Rule Evaluator
      ├── Cap & Cycle Resolver
      ├── Reward Normalizer
      ├── Ranking Engine
      └── Explanation Generator
            |
            v
    Data Access Layer 
      ├── PostgreSQL (relational source of truth)
      └── Redis (in-memory cache)
```

**_PostgreSQL serves as the authoritative datastore for all entities, while Redis is used strictly as a non-persistent cache to improve read performance._**

---

## 3. Core Components

### 3.1 API Layer

The API layer is responsible for handling all external interactions.

Responsibilities:

* Accepts transaction context (amount, category)
* Validates request payloads
* Delegates processing to the decision engine
* Returns the recommended card along with an explanation

This layer contains no business logic.

---

### 3.2 Decision Engine (Core Brain)

This layer contains **pure business logic** and is fully isolated from HTTP, database, and framework concerns.

### Sub-components

**a) Eligibility Filter**

Filters available cards based on:

* Card active status
* Category-level exclusions
* Transaction-level constraints

Only eligible cards proceed to reward evaluation.

---

**b) Reward Rule Evaluator**

* Applies base and category-specific reward rates
* Handles overrides and conditional rules
* Computes raw rewards (points or cashback) before caps

---

**c) Cap & Cycle Resolver**

* Applies reward caps to evaluated rewards
* Determines remaining cap for the current cycle
* Handles monthly or statement-cycle resets

---

**d) Reward Normalizer**

* Converts rewards into effective monetary (₹) value
* Applies redemption multipliers based on reward type

This step ensures all rewards are comparable.

---

**e) Ranking Engine**

* Ranks eligible cards by effective reward value
* Applies deterministic tie-breaking rules

Ranking logic is consistent and repeatable.

---

**f) Explanation Generator**

* Generates a human-readable justification for the recommendation
* References:

  * reward rate applied
  * caps considered
  * exclusions avoided

Explanations are designed to build user trust and transparency.

---

## 4. Conceptual Data Model (Phase 1)

The following entities define the core domain model. This is a conceptual view; physical schema will be derived later.

### User

* id
* preferences (reward goal, redemption preference)

### CreditCard

* id
* issuer
* card_name
* card_type
* active_status

### RewardRule

* id
* card_id
* category
* reward_rate
* reward_type (cashback / points / miles)
* conditions
* exclusions

### RewardCap

* id
* rule_id
* cap_amount
* cycle_type (monthly / statement)
* reset_policy

### TransactionContext

* amount
* category
* evaluation_timestamp

---

## 5. Decision Flow (Step-by-Step)

1. User submits a transaction context (amount, category)
2. API layer validates the request
3. Eligible cards are fetched from cache or database
4. Eligibility filter removes invalid cards
5. Reward rules are evaluated per eligible card
6. Reward caps and cycle limits are applied
7. Rewards are normalized into effective ₹ value
8. Cards are ranked deterministically
9. Explanation is generated for the top recommendation
10. Final response is returned to the client

---

## 6. Caching Strategy (Phase 1)

### Cache Usage

* Card metadata
* Reward rules
* Computed recommendations (short TTL)

### Example Cache Keys

```
card_rules:{card_id}
recommendation:{user_id}:{category}:{amount_bucket}
```

### Invalidation Triggers

* Reward rule updates
* Card metadata changes
* Reward cycle resets

Redis is used strictly as an optimization layer and never as a source of truth.

---

## 7. Failure Scenarios & Edge Cases

* No eligible card found → return explicit "no recommendation" response
* Reward cap exhausted → fallback reward logic applied
* Conflicting rules → deterministic precedence resolution
* Invalid category → validation error

---

## 8. Non-Goals in Design (Phase 1)

* No real-time bank integrations
* No transaction history tracking
* No machine-learning-driven decisions
* No financial advice or spending nudges

---

## 9. Design Principles

* Deterministic over probabilistic
* Explainable over opaque
* Data-driven over hard-coded logic
* Correctness before optimization