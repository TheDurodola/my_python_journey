
def main_menu():
	main_menu = """
1 => PhoneBook
2 => Messages
3 => Chat
4 => Call Register
5 => Tones
6 => Settings
7 => Call Divert
8 => Games
9 => Calculator
10=> Reminders
11=> Clock
12=> Profiles
13=> SIM Services
0 => Back
"""

	print(main_menu)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		chat_menu()
	if navigate == 2:
		chat_menu()
	if navigate == 3:
		chat_menu()
	if navigate == 4:
		chat_menu()
	if navigate == 5:
		tones_menu()
	if navigate == 6:
		chat_menu()
	if navigate == 7:
		call_divert_menu()
	if navigate == 8:
		games_menu()
	if navigate == 9:
		chat_menu()
	if navigate == 10:
		chat_menu()
	if navigate == 11:
		chat_menu()
	if navigate == 12:
		profiles_menu()
	if navigate == 13:
		sim_services_menu()



def chat_menu():
	chat = """

╔════════════ CHAT ═════════════════════╗
║ You:        Hey, how are you?         ║
║ Friend:     I'm good, thanks! You?    ║
║ You:        Doing well. Free later?   ║
║ Friend:     Yeah, after 6 PM.         ║
║ You:        Cool. Let's catch up.     ║
║ Friend:     Sounds great!             ║
╚═══════════════════════════════════════╝

0 => Back
"""
	print(chat)
	navigate = int(input("Enter a number to move: "))
	if navigate==0:
		main_menu()

def games_menu():
	games ="""
╔════════════════════════════════════════╗
║     ☠ WELCOME TO THE HAUNTED REALM ☠   ║
╠════════════════════════════════════════╣
║        █▓░░░░░░░░░░░░░░░░░░░░ 13%      ║
║      Tip: Don't follow the whispers.   ║
║                                        ║
║        ☠ BLOOD IS STILL FRESH...       ║
║        ║║║                             ║
║        ╚╝ dripping...                  ║
╚════════════════════════════════════════╝
0 => Back
"""
	print(games)
	navigate = int(input("Enter a number to move: "))
	if navigate ==0 :
		main_menu()


def call_divert_menu():
	call_divert = """
╔═════════════════════════════════╗
║     ☎ CALL DIVERT ACTIVE!       ║
╠═════════════════════════════════╣
║    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 100%       ║
║    Tip: You can edit this later.║
║                                 ║
║     Press 0 to return to menu.  ║
╚═════════════════════════════════╝
"""
	print(call_divert)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		main_menu()

def sim_services_menu():
	sim_services = """
╔═══════════════════════════════════╗
║       📶 SIM SERVICES SETUP       ║
╠═══════════════════════════════════╣
║   Initializing SIM toolkit...     ║
║                                   ║
║   ▓▓░░░░░░░░░░░░░░░░░ 25%         ║
║   Tip: Do not remove the SIM card ║
║                                   ║
║   Reading service profiles...     ║
╚═══════════════════════════════════╝

0 => Back
"""
	print(sim_services)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		main_menu()

def profiles_menu():
	profiles = """
╔══════════════════════════════════╗
║      👤 LOADING PROFILES...      ║
╠══════════════════════════════════╣
║   Fetching user settings...      ║
║                                  ║
║   ▓▓▓░░░░░░░░░░░░░░░░ 35%        ║
║   Tip: Personalize your profile  ║
║        for better experience.    ║
║                                  ║
║   Active Profile: [Guest]        ║
╚══════════════════════════════════╝

0 => Back"""
	print(profiles)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		main_menu()

def tones_menu():
	tones ="""
1 => Ringing tone
2 => Ringing volume
3 => Incoming call alert
4 => Composer
5 => Message alert tone
6 => Keypad tones
7 => Warning and game tones
8 => Vibrating alert
9 => Screen saver
"""
	print(tones)
	navigate = int(input("Enter a number to move: "))
