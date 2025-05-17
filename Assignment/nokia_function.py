
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
	if navigate == 1:
		ringing_tones_menu()
	if navigate == 2:
		ringing_volume_menu()
	if navigate == 3:
		incoming_call_alert_menu()
	if navigate == 4:
		composer_menu()
	if navigate == 5:
		message_alert_tone_menu()
	if navigate == 6:
		keypad_tones_menu()
	if navigate == 7:
		warning_and_game_tones_menu()
	if navigate == 8:
		vibrating_alert_menu()
	if navigate == 9:
		screen_saver_menu()
	if navigate == 0:
		main_menu()

def ringing_tones_menu():
	ringing_tones ="""
╔════════════════════════╗
║     Ringing tone       ║
╠════════════════════════╣
║ > Nokia tune           ║
║   Waltz of the Demon   ║
║   Funky beat           ║
║   Kickstart            ║
╠════════════════════════╣
║  [Select]   [0. Back]  ║
╚════════════════════════╝

"""
	print(ringing_tones)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()
	
def ringing_volume_menu():
	ringing_volume ="""
╔════════════════════════╗
║    Ringing volume      ║
╠════════════════════════╣
║     ▓▓▓░░              ║
║     Level: 3           ║
╠════════════════════════╣
║    [OK]       [0. Back]║
╚════════════════════════╝

"""
	print(ringing_volume)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()

def incoming_call_alert_menu():
	display ="""
╔════════════════════════╗
║ Incoming call alert    ║
╠════════════════════════╣
║ > Ringing              ║
║   Vibrating            ║
║   Ring once            ║
║   Beep once            ║
║   Silent               ║
╠════════════════════════╣
║   [Select]  [0. Back]  ║
╚════════════════════════╝
"""
	print(display)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()

def composer_menu():
	display ="""
╔════════════════════════╗
║       Composer         ║
╠════════════════════════╣
║ Melody: _____          ║
║ Notes: C D E F G A B   ║
║ Tempo: ▓▓░░            ║
╠════════════════════════╣
║  [Play]      [0. Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()

def message_alert_tone_menu():
	display ="""
╔════════════════════════╗
║ Message alert tone     ║
╠════════════════════════╣
║ > Beep once            ║
║   Ascending            ║
║   Nokia tune           ║
║   Silent               ║
╠════════════════════════╣
║  [Select]   [0. Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()


def keypad_tones_menu():
	display ="""
╔════════════════════════╗
║    Keyboard tones      ║
╠════════════════════════╣
║ > Level 1              ║
║   Level 2              ║
║   Level 3              ║
║   Off                  ║
╠════════════════════════╣
║  [Select]   [0. Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()




def warning_and_game_tones_menu():
	display ="""
╔════════════════════════╗
║ Warning & game tones   ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║  [Select]   [0. Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()


def vibrating_alert_menu():
	display ="""
╔════════════════════════╗
║    Vibrating alert     ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]   [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()


def screen_saver_menu():
	display ="""
╔════════════════════════╗
║      Screen saver      ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
║                        ║
║ Current: Digital Clock ║
╠════════════════════════╣
║  [Select]   [0. Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a nuber to move: "))
	if navigate == 0:
		tones_menu()


def clock_menu():
	display = """
1 => Alarm clock
2 => Clock settings
3 => Date setting
4 => Stopwatch
5 => Countdown timer
6 => Auto update of date and time
"""
