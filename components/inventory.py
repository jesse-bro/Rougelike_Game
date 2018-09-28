from game_messages import Message
from components.item import Item
from entity import Entity
from render_functions import RenderOrder
from item_functions import heal, hard_shell, cast_freeze, cast_confuse, cast_fireball, cast_lightning

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item, colors):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message': Message('You cannot carry any more, your inventory is full', colors.get('yellow'))
            })
        else:
            results.append({
                'item_added': item,
                'message': Message('You pick up the {0}!'.format(item.name), colors.get('blue'))
            })

            self.items.append(item)

        return results

    def add_store_item(self, item, colors):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message': Message('You cannot carry any more, your inventory is full', colors.get('yellow'))
            })

        elif item == 'mega_potion':
            item_component = Item(use_function=heal, amount=80)
            item = Entity(0, 0, '!', colors.get('gold'), 'Mega Healing Potion', render_order=RenderOrder.ITEM,
                          item=item_component)
            results.append({
                'item_added': item,
                'message': Message('You bought the {0}!'.format(item.name), colors.get('blue'))
            })
            self.items.append(item)
        elif item == 'healing_potion':
            item_component = Item(use_function=heal, amount=40)
            item = Entity(0, 0, '!', colors.get('violet'), 'Healing Potion', render_order=RenderOrder.ITEM,
                          item=item_component)
            results.append({
                'item_added': item,
                'message': Message('You bought the {0}!'.format(item.name), colors.get('blue'))
            })
            self.items.append(item)
        elif item == 'hard_shell':
            item_component = Item(use_function=hard_shell, amount=1)
            item = Entity(0, 0, '!', colors.get('yellow'), 'Hard Shell Potion', render_order=RenderOrder.ITEM,
                          item=item_component)
            results.append({
                'item_added': item,
                'message': Message('You bought the {0}!'.format(item.name), colors.get('blue'))
            })
            self.items.append(item)
        else:
            results.append({
                'item_added': None,
                'message': Message('This is wrong', colors.get('yellow'))
            })

        return results

    def use(self, item_entity, colors, **kwargs):
        results = []

        item_component = item_entity.item

        if item_component.use_function is None:
            equippable_component = item_entity.equippable

            if equippable_component:
                results.append({'equip': item_entity})
            else:
                results.append({'message': Message('The {0} cannot be used'.format(item_entity.name), colors.get('yellow'))})
        else:
            if item_component.targeting and not (kwargs.get('target_x') or kwargs.get('target_y')):
                results.append({'targeting': item_entity})
            else:
                kwargs = {**item_component.function_kwargs, **kwargs}
                item_use_results = item_component.use_function(self.owner, colors, **kwargs)

                for item_use_result in item_use_results:
                    if item_use_result.get('consumed'):
                        self.remove_item(item_entity)

                results.extend(item_use_results)

        return results

    def remove_item(self,item):
        self.items.remove(item)

    def drop_item(self,item,colors):
        results = []

        if self.owner.equipment.main_hand == item or self.owner.equipment.off_hand == item or self.owner.equipment.chest_armor == item \
                or self.owner.equipment.shoulder_armor == item or self.owner.equipment.leg_armor == item:
            self.owner.equipment.toggle_equip(item)

        item.x = self.owner.x
        item.y = self.owner.y

        self.remove_item(item)
        results.append({'item_dropped': item, 'message': Message('You dropped the {0}'.format(item.name), colors.get('yellow'))})

        return results