from game_messages import Message
from components.ai import ConfusedMonster, FrozenMonster

def heal(*args, **kwargs):
    entity = args[0]
    colors = args[1]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at full health', colors.get('yellow'))})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('Your wounds start to feel better', colors.get('green'))})

    return results

def xp_boost(*args, **kwargs):
    entity = args[0]
    colors = args[1]
    amount = kwargs.get('amount')

    results = []

    entity.level.add_xp(amount)
    results.append({'consumed': True, 'message': Message('You gain some experience!', colors.get('yellow'))})

    return results


def hard_shell(*args, **kwargs):
    entity = args[0]
    colors = args[1]
    amount = kwargs.get('amount')

    results = []

    entity.fighter.boost_defense(amount)
    results.append({'consumed': True, 'message': Message('You gain a boost in defense!', colors.get('green'))})

    return results

def cast_freeze(*args, **kwargs):
    caster = args[0]
    colors = args[1]
    entities = kwargs.get('entities')
    game_map = kwargs.get('game_map')
    maximum_range = kwargs.get('maximum_range')

    results = []
    closest_distance = maximum_range + 1
    target = None

    for entity in entities:
        if entity.fighter and entity != caster and game_map.fov[entity.x, entity.y]:
            distance = caster.distance_to(entity)

            if distance < closest_distance:
                target = entity
                closest_distance = distance

            if target and entity.fighter:
                frozen_ai = FrozenMonster(entity.ai, 20)
                frozen_ai.owner = entity
                entity.ai = frozen_ai
               # break

    if target:
        results.append({'consumed': True, 'target': target, 'message': Message(
            'A large gush of cold wind strikes the room, freezing the enemy in place!')})
    else:
        results.append({'consumed': False, 'target': None,
                        'message': Message('No enemy is close enough to strike.', colors.get('red'))})

    return results


def cast_lightning(*args, **kwargs):
    caster = args[0]
    colors = args[1]
    entities = kwargs.get('entities')
    game_map = kwargs.get('game_map')
    damage = kwargs.get('damage')
    maximum_range = kwargs.get('maximum_range')

    results = []

    target = None
    closest_distance = maximum_range + 1

    for entity in entities:
        if entity.fighter and entity != caster and game_map.fov[entity.x,entity.y]:
            distance = caster.distance_to(entity)

            if distance < closest_distance:
                target = entity
                closest_distance = distance

    if target:
        results.append({'consumed': True, 'target': target, 'message': Message(
            'A lighting bolt strikes the {0} with a loud thunder! The damage is {1}'.format(target.name, damage))})
        results.extend(target.fighter.take_damage(damage))
    else:
        results.append({'consumed': False, 'target': None, 'message': Message('No enemy is close enough to strike.', colors.get('red'))})

    return results

def cast_fireball(*args, **kwargs):
    colors = args[1]
    entities = kwargs.get('entities')
    game_map = kwargs.get('game_map')
    damage = kwargs.get('damage')
    radius = kwargs.get('radius')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not game_map.fov[target_x,target_y]:
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view.', colors.get('yellow'))})

        return results

    results.append({'consumed': True, 'message': Message('The fireball explodes, burning everything withing {0} tiles!'.format(radius), colors.get('orange'))})

    for entity in entities:
        if entity.distance(target_x,target_y) <= radius and entity.fighter:
            results.append({'message': Message('The {0} gets burned for {1} hit points.'.format(entity.name,damage), colors.get('orange'))})
            results.extend(entity.fighter.take_damage(damage))

    return results

def cast_confuse(*args, **kwargs):
    colors = args[1]
    entities = kwargs.get('entities')
    game_map = kwargs.get('game_map')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not game_map.fov[target_x, target_y]:
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view.', colors.get('yellow'))})

        return results

    for entity in entities:
        if entity.x == target_x and entity.y == target_y and entity.ai:
            confused_ai = ConfusedMonster(entity.ai, 10)

            confused_ai.owner = entity
            entity.ai = confused_ai

            results.append({'consumed': True, 'message': Message('The eyes of the {0} look vacant, as he starts to stumble around!'.format(entity.name), colors.get('light_green'))})

            break
    else:
        results.append({'conusmed': False, 'message': Message('There is no target-able enemy at that location.', colors.get('yellow'))})

    return results