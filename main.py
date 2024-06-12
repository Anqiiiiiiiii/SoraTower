import room as r
import characterSetting as c
import map as m

main1 = True

player_action = ["walk", "explore", "check bagpack", "load", "save"]
m.create_puzzle_order()
m.initial_map()

def player_actions():
    """
    This function will help to choose player choosing action,
    player could choose the action they want to do from the
    given list, also they could quit at this menu.
    """
    global main1
    try:
        current_pos = m.sora_tower.map[c.PlayerAn.pos_z][c.PlayerAn.pos_x][c.PlayerAn.pos_y].name
        print("\nYou are now in " + str(current_pos) + "\n")
        if m.sora_tower.map[c.PlayerAn.pos_z][c.PlayerAn.pos_x][c.PlayerAn.pos_y].print_description():
            if c.PlayerAn.pos_z < (m.sora_tower.map_level - 1):
                print("You arrived the next layer!")
                c.PlayerAn.pos_z += 1
                c.PlayerAn.pos_x = 0
                c.PlayerAn.pos_y = 0
            elif c.PlayerAn.pos_z == (m.sora_tower.map_level - 1):
                c.PlayerAn.pos_y += 1
                r.notWin = m.sora_tower.map[c.PlayerAn.pos_z][c.PlayerAn.pos_x][c.PlayerAn.pos_y].print_description()
                print("You got the crystal! congratulations!")
        if not r.notWin:
            return
        print(
            "\nChoose what you want to do from following list\nEnter 'quit'" +
            " if you want to quit")
        print(player_action)
        action = input("\nWhat do you want to do? ")
    except ValueError:
        print("Please enter in correct form")
    else:
        if action.lower() == player_action[0]:
            with open('map.txt', 'r') as file:
                print(file.read())
            c.PlayerAn.move()
            c.meet_npc(c.PlayerAn)
        elif action.lower() == player_action[1]:
            c.PlayerAn.explore()
            print("\nScavengers, now you have:")
            print(c.PlayerAn.backpack)
        elif action.lower() == player_action[2]:
            print(f"\n{c.PlayerAn.backpack}")
            print("\nEnter the tool's name for checking details")
            check_bag = input("Enter 'NO' to skip checking: ")
            print("\n")
            if check_bag.lower() in c.PlayerAn.backpack:
                print(m.sora_tower.map[c.PlayerAn.pos_z][c.PlayerAn.pos_x][c.PlayerAn.pos_y].tool_description)
            elif check_bag.lower() == "no":
                print("skip!")
        elif action.lower() == "load":
            c.read_game()
            m.read_puzzle_order()
            m.initial_map()
            print("Welcome back, " + c.PlayerAn.name + "!")
        elif action.lower() == "save":
            c.save_game()
            m.write_puzzle_order()
        elif action.lower() == "quit":
            main1 = False
        else:
            print("Wrong input!")



def main_menu():
    """This function will ask the user input of choosing action
  and if they want to quit or not, this is the main menu
  """
    global main1
    print(
        "Your mission is:\n1:discover the missing kingdom history, sora kingdom\n2:Find the missing knowledge and solve the puzzle, get out from the tower"
    )
    print("\nEnter 1: For choosing an action")
    print("Enter 2: To load the game")
    print("Enter 3: For quit")
    m_des = True
    while m_des:
        try:
            playerInput = int(input("\nPlease make your first choice："))
        except ValueError:
            print("Please enter in number form, scavenger!")
        else:
            if playerInput == 1:
                c.PlayerAn.name = input("Welcome, adventure. Please tell me your name: ")
                while main1 and c.calive and r.notWin:
                    player_actions()
                m_des = False
            elif playerInput == 2:
                c.read_game()
                m.read_puzzle_order()
                m.initial_map()
                print("Welcome back, " + c.PlayerAn.name + "!")
                while main1 and c.calive and r.notWin:
                    player_actions()
                m_des = False
            elif playerInput == 3:
                m_des = False
            else:
                print("Wrong input number~")
        finally:
            print("See you next time!")


main_menu()