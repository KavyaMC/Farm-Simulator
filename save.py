import os
import json

class Save:

	def __init__(self):
		self.save_folder = "slots"
		os.makedirs(self.save_folder, exist_ok=True)

	def _get_slot_path(self, slot_number):
		return os.path.join(self.save_folder, f"slot{slot_number}.json")

	def save_exists(self, slot):
		path = self._get_slot_path(slot)
		return os.path.exists(path)

	def get_gamestate(self, slot):
		if self.save_exists(slot):
			return "saved"
		else:
			return "new"