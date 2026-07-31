def quest_status(starting_gold, item_cost, starting_health, battle_damage):
    return f"Gold: {starting_gold - item_cost}, Health: {starting_health - battle_damage}"