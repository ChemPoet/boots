def quest_status(starting_gold, item_cost, starting_health, battle_damage):
    current_gold = starting_gold - item_cost
    current_health = starting_health - battle_damage
    #print(f"{starting_gold}-{item_cost} = {current_gold}")
    #print(f"{starting_health}-{battle_damage} = {current_health}")
    starting_gold = current_gold
    starting_health = current_health
    print(f'Gold: {current_gold}, Health: {current_health}')
    return(f'Gold: {current_gold}, Health: {current_health}')
# PRINT only displays an output on the screen.
# RETURN generates an actual RESPONSE / OUTPUT that can be used further.    

