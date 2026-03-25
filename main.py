from gamestate import Gamestate
from save_manager import SaveManager

save_manager = SaveManager()

def main_menu(current_state):
	has_save = save_manager.check_save_exists()
	print(f"\n----{current_state.value}----")
	if has_save:
		menu_items = ["continue", "save", "delete", "help", "credits", "exit"]
		actions = {
			"1": Gamestate.Agriculture_Menu,
			"2": Gamestate.Save_Slot_Menu,
			"3": Gamestate.Save_Slot_Menu,
			"4": Gamestate.Help_Menu,
			"5": Gamestate.Credits_Menu,
			"6": Gamestate.Exit
		}
	else:
		menu_items = ["new", "help", "credits", "exit"]
		actions = {
			"1": Gamestate.Save_Slot_Menu,
			"2": Gamestate.Help_Menu,
			"3": Gamestate.Credits_Menu,
			"4": Gamestate.Exit
		}

	for i, item in enumerate(menu_items, start=1):
		print(f"{i}. {item}")

	choice = input("Please choose an option: ").strip()
	action = actions.get(choice)

	if action == "delete":
		print("Select a slot to clear:")
		for i in range(1, save_manager.max_slots + 1):
			print(f"{i}. Slot {i}")
		slot = input("Slot number: ").strip()
		if slot.isdigit() and int(slot) in range(1, save_manager.max_slots + 1):
			save_manager.clear_save(int(slot))
		else:
			print("Invalid slot.")
		return Gamestate.Main_Menu
	elif isinstance(action, Gamestate):
		return action
	else:
		print("Invalid choice. Try again")
		return Gamestate.Main_Menu

def save_slot_menu(current_state):
	print(f"\n----{current_state.value}----")
	name = input("Enter your name: ").strip()
	if not name.isalpha() or not 3 <= len(name) <= 20:
		print("Invalid name. Use 3-20 alphabetic characters.")
		return Gamestate.Save_Slot_Menu

	slot = input("Select a slot (1-4): ").strip()
	if slot in "1234":
		save_manager.save_game(int(slot), name)
		return Gamestate.Agriculture_Menu
	print("Invalid choice.")
	return Gamestate.Save_Slot_Menu
def agriculture_menu(current_state):
	print(" Agriculture Building")
	print("1. Ranch")
	print("2. Cropland")
	print("3. Go to main menu")
	choice = input("Select an option: ").strip()

	match choice:
		case "1": return Gamestate.Ranch_Menu
		case "2": return Gamestate.Cropland_Menu
		case "3": return Gamestate.Main_Menu
		case _: return current_state

def ranch_menu(current_state):
	menu_items = ["Buy", "Sell", "Housing", "Storage", "Status", "End turn", "Go back"]
	print("The Ranch")
	for i, item in enumerate(menu_items, start=1):
		print(f"{i}. {item}")

	choice = input("Select an option: ").strip()
	if choice in {"1", "2"}:
		print("In development.")
		return current_state
	if choice == "7":
		return Gamestate.Agriculture_Menu
	return current_state

def help_menu(current_state):
	print("\nHelp: Manage farm, raise birds, buy housing, sell eggs, etc.")
	input("Press Enter to return to Main Menu.")
	return Gamestate.Main_Menu

def credits_menu(current_state):
	print("\nCredits: Designed by KavyaMC")
	input("Press Enter to return to Main Menu.")
	return Gamestate.Main_Menu

current_state = Gamestate.Main_Menu
print("Welcome to Farm Simulator!")

while current_state != Gamestate.Exit:
	match current_state:
		case Gamestate.Main_Menu:
			current_state = main_menu(current_state)
		case Gamestate.Save_Slot_Menu:
			current_state = save_slot_menu(current_state)
		case Gamestate.Agriculture_Menu:
			current_state = agriculture_menu(current_state)
		case Gamestate.Ranch_Menu:
			current_state = ranch_menu(current_state)
		case Gamestate.Cropland_Menu:
			print("Cropland is under development.")
			current_state = Gamestate.Agriculture_Menu
		case Gamestate.Help_Menu:
			current_state = help_menu(current_state)
		case Gamestate.Credits_Menu:
			current_state = credits_menu(current_state)
		case _:
			current_state = Gamestate.Exit