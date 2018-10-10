from equipment_slots import EquipmentSlots

class Equipment:
    def __init__(self, main_hand=None, off_hand=None, chest_armor=None, shoulder_armor=None, leg_armor=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.chest_armor = chest_armor
        self.shoulder_armor = shoulder_armor
        self.leg_armor = leg_armor

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        if self.chest_armor and self.chest_armor.equippable:
            bonus += self.chest_armor.equippable.max_hp_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus

        if (self.shoulder_armor and self.shoulder_armor.equippable) and (self.leg_armor and self.leg_armor.equippable):
            bonus += self.shoulder_armor.equippable.power_bonus + self.leg_armor.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus

        if self.chest_armor and self.chest_armor.equippable:
            bonus += self.chest_armor.equippable.defense_bonus

        if self.shoulder_armor and self.shoulder_armor.equippable:
            bonus += self.shoulder_armor.equippable.defense_bonus

        if self.leg_armor and self.leg_armor.equippable:
            bonus += self.leg_armor.equippable.defense_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        elif slot == EquipmentSlots.CHEST_ARMOR:
            if self.chest_armor == equippable_entity:
                self.chest_armor = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.chest_armor:
                    results.append({'dequipped': self.chest_armor})

                self.chest_armor = equippable_entity
                results.append({'equipped': equippable_entity})

        elif slot == EquipmentSlots.SHOULDER_ARMOR:
            if self.shoulder_armor == equippable_entity:
                self.shoulder_armor = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.shoulder_armor:
                    results.append({'dequipped': self.shoulder_armor})

                self.shoulder_armor = equippable_entity
                results.append({'equipped': equippable_entity})

        elif slot == EquipmentSlots.LEG_ARMOR:
            if self.leg_armor == equippable_entity:
                self.leg_armor = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.leg_armor:
                    results.append({'dequipped': self.leg_armor})

                self.leg_armor = equippable_entity
                results.append({'equipped': equippable_entity})

        return results