import actions

class Menu:
	def __init__(self, title, options):
		self.title = title
		self.options = options

	def run(self):
		while True:
			print(f"\n---{self.title}---")
			for key, (text, action) in self.options.items():
				print(f"{key}. {text}")
			choice=input("\nSelect an option: ").strip()
			if choice in self.options:
				action = self.options[choice][1]
				result = action()
				if result == "back":
					break

			else:
				print("invalid choice")

main_menu = Menu(
	"Main Menu", {
		"1": ("New Game", actions.new_game),
		"2": ("Help Screen", actions.help_screen),
		"3": ("Credits Screen", actions.credits_screen),
		"4": ("Quit", actions.exit_game)
	}
)