from engine.optimizer.scorer import score_rule

rule = {
    "rate": "0.05",
    "type": "CASHBACK",
    "cap_amount": 1000,
    "cap_period": "MONTHLY"
}

result = score_rule(2000, rule)
print(result)
