import os
import json
from gamestate import Gamestate


class SaveManager:
	def __init__(self, max_slots=4):
		self.max_slots = max_slots
		base_dir = os.path.dirname(os.path.abspath(__file__))
		self.slot_folder = os.path.join(base_dir, "slots")
		os.makedirs(self.slot_folder, exist_ok=True)
		self.initialize_slots()

	def initialize_slots(self):
		for i in range(1, self.max_slots + 1):
			path = self._get_slot_filename(i)
			if not os.path.exists(path):
				empty_data = {"player_name": "empty"}
				with open(path, "w") as file:
					json.dump(empty_data, file, indent=4)

	def _get_slot_filename(self, slot_number, player_name=None):
		if player_name is None or player_name.strip() == "":
			player_name = "empty"
		filename = f"slot{slot_number}_{player_name}.json"
		return os.path.join(self.slot_folder, filename)

	def _find_slot_file(self, slot_number):
		for file in os.listdir(self.slot_folder):
			if file.startswith(f"slot{slot_number}_"):
				return os.path.join(self.slot_folder, file)
		return None

	def check_save_exists(self):
		for file in os.listdir(self.slot_folder):
			if file.startswith("slot") and "_empty" not in file:
				return True
		return False

	def save_game(self, slot_number, player_name):
		if slot_number not in range(1, self.max_slots + 1):
			print("Invalid slot number.")
			return False

		old_path = self._find_slot_file(slot_number)
		if old_path is None:
			print("Slot file not found.")
			return False

		new_path = self._get_slot_filename(slot_number, player_name)

		if old_path != new_path or os.path.exists(new_path):
			confirm = (
				input(
					f"Slot {slot_number} already has a save. Overwrite? (y/n): ")
				.strip()
				.lower()
			)
			if confirm not in ("y", "yes"):
				print("Save canceled.")
				return False

		if old_path != new_path:
			os.rename(old_path, new_path)

		save_data = {"player_name": player_name}
		with open(new_path, "w") as file:
			json.dump(save_data, file, indent=4)

		print(f"Saved to slot {slot_number} as '{player_name}'")
		return True
