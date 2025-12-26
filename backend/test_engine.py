import os
import django
from engine.db.cards import fetch_active_cards
from engine.db.rewards import fetch_active_reward_rules

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'config.settings')
django.setup()

cards=fetch_active_cards()
cards_ids=[c["id"] for c in cards]
rules = fetch_active_reward_rules(cards_ids)

print (rules)