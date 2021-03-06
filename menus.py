import tdl

import textwrap

def menu(con, root, header, options, width, screen_width, screen_height):
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')

    # calculate total height for the header (after textwrap) and one line per option
    header_wrapped = textwrap.wrap(header, width)
    header_height = len(header_wrapped)
    height = len(options) + header_height

    # create an off-screen console that represents the menu's window
    window = tdl.Console(width, height)

    # print the header, with wrapped text
    window.draw_rect(0,0, width, height, None, fg=(255,255,255), bg=None)
    for i, line in enumerate(header_wrapped):
        window.draw_str(0,0 + i, header_wrapped[i])

    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        window.draw_str(0,y, text, bg=None)
        y += 1
        letter_index += 1

    # blit the contents of "window" to the root console
    x = screen_width // 2 - width // 2
    y = screen_height // 2 - height // 2
    root.blit(window, x, y, width, height, 0,0)

def inventory_menu(con, root, header, player, inventory_width, screen_width, screen_height):
    # show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []

        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (on main hand)'.format(item.name))
            elif player.equipment.off_hand == item:
                options.append('{0} (on off hand)'.format(item.name))
            elif player.equipment.chest_armor == item:
                options.append('{0} (on chest)'.format(item.name))
            elif player.equipment.shoulder_armor == item:
                options.append('{0} (on shoulders)'.format(item.name))
            elif player.equipment.leg_armor == item:
                options.append('{0} (on legs)'.format(item.name))
            else:
                options.append(item.name)

    menu(con, root, header, options, inventory_width, screen_width, screen_height)

def main_menu(con, root_console, background_image, screen_width, screen_height, colors):
    background_image.blit_2x(root_console, 0,0)

    title = 'TOMBS OF THE ANCIENT KINGS'
    center = (screen_width - len(title)) // 2
    root_console.draw_str(center, screen_height - 2 - 4, title, bg=None, fg=colors.get('light_yellow'))

    title = 'By Jesse'
    center = (screen_width - len(title)) //2
    root_console.draw_str(center, screen_height -2 , title, bg=None, fg=colors.get('light_yellow'))

    menu(con, root_console,'', ['Play a new game', 'Continue last game', 'Quit'], 24, screen_width, screen_height)

def message_box(con, root_console, header, width, screen_width, screen_height):
    menu(con, root_console, header, [], width, screen_width, screen_height)

def level_up_menu(con, root, header, player, menu_width, screen_width, screen_height):
    options = ['Constitution (+20 HP, from {0})'.format(player.fighter.max_hp),
               'Strength (+1 attack, from {0})'.format(player.fighter.power),
               'Agility (+1 defense, from {0})'.format(player.fighter.defense),
               ]
    menu(con, root, header, options, menu_width, screen_width, screen_height)

def store_menu(con, root, header, store, menu_width, screen_width, screen_height):
    options = ['Healing Potion (15 Gold)',
                'Mega Potion (30 Gold)',
                'Hard Shell (80 Gold)',
                'Lightning Scroll (80 Gold)',
                'Fireball Scroll (50 Gold)',
                'Confusion Scroll (30 Gold)',
                'Freeze Scroll (50 Gold)']

    menu(con, root, header, options, menu_width, screen_width, screen_height)

def character_screen(root_console, player, character_screen_width, character_screen_height, screen_width,
                     screen_height):
    window = tdl.Console(character_screen_width, character_screen_height)

    window.draw_rect(0, 0, character_screen_width, character_screen_height, None, fg=(255, 255, 255), bg=None)

    window.draw_str(0, 1, 'Character Information')
    window.draw_str(0, 2, 'Level: {0}'.format(player.level.current_level))
    window.draw_str(0, 3, 'Experience: {0}'.format(player.level.current_xp))
    window.draw_str(0, 4, 'Experience to Level: {0}'.format(player.level.experience_to_next_level))
    window.draw_str(0, 5, 'Gold: {0}'.format(player.gold.current_gold))
    window.draw_str(0, 7, 'Maximum HP: {0}'.format(player.fighter.max_hp))
    window.draw_str(0, 8, 'Attack: {0}'.format(player.fighter.power))
    window.draw_str(0, 9, 'Defense: {0}'.format(player.fighter.defense))


    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    root_console.blit(window, x, y, character_screen_width, character_screen_height, 0, 0)

def control_screen(root_console, character_screen_width, character_screen_height, screen_width, screen_height):
    window = tdl.Console(character_screen_width, character_screen_height)

    window.draw_str(0, 1, 'GAME CONTROLS - ESC/x to quit')
    window.draw_str(0, 2, 'W - Move Up')
    window.draw_str(0, 3, 'S - Move Down')
    window.draw_str(0, 4, 'A - Move Left')
    window.draw_str(0, 5, 'D - Move Right')

    window.draw_str(0, 7, 'I - Open Inventory (ESC to quit)')
    window.draw_str(0, 8, 'G - Pick-Up Item')
    window.draw_str(0, 9, 'R - Drop Item')

    window.draw_str(0, 11, 'STAIRS - Next Level')
    window.draw_str(0, 12, 'Shift + . - Go Down the Stairs')

    window.draw_str(0, 14, 'Store Controls')
    window.draw_str(0, 15, 'Q - Open Store/Quit Store')

    window.draw_str(0, 17, 'Character Information')
    window.draw_str(0, 18, 'C - Open/Close Character Info. Screen')

    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    root_console.blit(window, x, y, character_screen_width, character_screen_height, 0, 0)





