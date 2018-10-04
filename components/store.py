class Store:
    def __init__(self, store):
        self.store = store




# Temporary stay, don't know where to put it
def check_item_price(bought):
    cost = 0
    if len(bought) != 0:
        if bought == 'healing_potion':
            cost = 15
            return cost
        elif bought == 'mega_potion':
            cost = 30
            return cost
        elif bought == 'hard_shell':
            cost = 80
            return cost
        elif bought == 'Lightning Scroll':
            cost = 80
            return cost
        elif bought == 'fireball_scroll':
            cost = 50
            return cost
        elif bought == 'confusion_scroll':
            cost = 30
            return cost
        elif bought == 'freeze_scroll':
            cost = 50
            return cost
    return cost
