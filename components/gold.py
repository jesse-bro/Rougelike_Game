class Gold:
    def __init__(self, current_gold=0):
        self.current_gold = current_gold

    def add_gold(self, gold):
        self.current_gold += gold

    def remove_gold(self, cost):
        if self.current_gold >= cost:
            self.current_gold -= cost
            return True
        else:
            return False
