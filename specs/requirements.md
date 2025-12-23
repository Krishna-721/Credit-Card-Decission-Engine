## Requirements

# 1. Introduction

This project is a browser-based application that helps users deterministically decide which credit card to use for a given transaction in order to maximize effective reward value (cashback, points, or miles).

The system evaluates credit card reward rules, spending categories, caps, exclusions, and user goals to generate explainable, consistent, and optimized recommendations.

# 2. Problem Statement

Credit card reward programs in India are increasingly complex and rule-heavy, resulting in low effective reward utilization for cardholders.

Key challenges include:

- Lack of clarity on which card provides the highest effective value for a given transaction

- Hidden restrictions and exclusions that invalidate expected rewards

- Reward caps and devaluations that reduce real monetary benefits

- Low awareness of redemption value, leading to wasted or underutilized points

As a result, users often make suboptimal card usage decisions, despite owning multiple credit cards with overlapping reward structures.

# 3. Actors
## 3.1 End User

- Owns one or more credit cards

- Declares spending categories and estimated usage

- Expects clear, explainable recommendations

## 3.2 Admin

- Manages card metadata and reward rules

- Updates reward structures without code changes

- Ensures correctness and data integrity

# 4. Functional Requirements
## 4.1 Card Management

- Users must be able to add, view, and remove credit cards

- Each card must be associated with reward rules and metadata

## 4.2 Transaction Recommendation

- The system must accept a transaction context (amount + category)

- The system must evaluate all eligible cards

- The system must recommend the optimal card based on effective reward value

## 4.3 Reward Evaluation

- The system must apply reward caps and exclusions
 
- The system must normalize rewards into a monetary (₹) value
 
- The system must handle monthly or statement-cycle resets

## 4.4 Explainability

- The system must explain why a card was recommended

- Explanations must reference rules, caps, and reward rates

# 5. Non-Functional Requirements
## 5.1 Determinism

Given the same inputs, the system must always produce the same output

## 5.2 Performance

Recommendation responses should complete within acceptable latency (<200ms for cached paths)

## 5.3 Security

User data must be securely stored

Admin access must be restricted

## 5.4 Maintainability

Reward rules must be updatable without redeploying application logic

# 6. Constraints

- No integration with bank or credit card provider APIs (Phase 1)

- All user spending data is user-declared

- No machine learning–based decision making in Phase 1

- Browser-based access only

- The system must not encourage increased spending or provide financial advice

# 7. Out of Scope (Phase 1)

- Automatic transaction ingestion
 
- Credit score analysis
 
- Fraud detection
 
- Personalized ML recommendations
 
- Mobile applications

# 8. Success Criteria

- System produces correct, explainable recommendations
 
- Reward calculations match published card rules
 
- New card rules can be added without code changes