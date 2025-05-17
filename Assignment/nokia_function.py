
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
		phonebook_menu()
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
		calculator_menu()
	if navigate == 10:
		reminders_menu()
	if navigate == 11:
		clock_menu()
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
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
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		tones_menu()


def calculator_menu():
	display = """
╔════════════════════════╗
║        Calculator      ║
╠════════════════════════╣
║     0                  ║
║                        ║
╠════════════════════════╣
║  [1][2][3]  [+]        ║
║  [4][5][6]  [-]        ║
║  [7][8][9]  [×]        ║
║  [0][C][=]  [÷]        ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		main_menu()


def reminders_menu():
	display = """
╔════════════════════════╗
║        Reminders       ║
╠════════════════════════╣
║ > Meeting @ 3PM        ║
║   Take meds @ 8PM      ║
║   Call Sarah           ║
║                        ║
╠════════════════════════╣
║[View] [New] [0. Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		main_menu()

def clock_menu():
	display = """
1 => Alarm clock
2 => Clock settings
3 => Date setting
4 => Stopwatch
5 => Countdown timer
6 => Auto update of date and time
"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		alarm_clock_menu()
	if navigate == 2:
		clock_settings_menu()
	if navigate == 3:
		date_setting_menu()
	if navigate == 4:
		stopwatch_menu()
	if navigate == 5:
		countdown_timer_menu()
	if navigate == 6:
		auto_update_of_date_and_time_menu()

def alarm_clock_menu():
	display = """
╔════════════════════════╗
║       Alarm clock      ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
║                        ║
║ Time: 06:30 AM         ║
╠════════════════════════╣
║   [Select]   [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		clock_menu()

def clock_settings_menu():
	display = """
╔════════════════════════╗
║     Clock settings     ║
╠════════════════════════╣
║ Time: 14:35            ║
║ Format: 24-hour        ║
╠════════════════════════╣
║   [Change]   [0. Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		clock_menu()

def date_setting_menu():
	display = """
╔════════════════════════╗
║      Date setting      ║
╠════════════════════════╣
║ Date: 17/05/2025       ║
║ Format: DD/MM/YYYY     ║
╠════════════════════════╣
║   [Edit]     [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		clock_menu()

def stopwatch_menu():
	display = """
╔════════════════════════╗
║        Stopwatch       ║
╠════════════════════════╣
║        00:00:00        ║
║                        ║
╠════════════════════════╣
║ [Start] [Split][0.Back]║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		clock_menu()

def countdown_timer_menu():
	display = """
╔════════════════════════╗
║     Countdown timer    ║
╠════════════════════════╣
║ Set time: 00:05:00     ║
║                        ║
╠════════════════════════╣
║   [Start]   [0. Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		clock_menu()

def auto_update_of_date_and_time_menu():
	display = """
╔════════════════════════╗
║Auto update of date/time║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]   [0. Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		clock_menu()



def phonebook_menu():
	display = """
1 =>  Search
2 =>  Service Nos.
3 =>  Add name
4 =>  Erase
5 =>  Edit
6 =>  Assign tone
7 =>  Send b'card
8 =>  Options
9 =>  Speed dials
10 => Voice tags

0 =>  Back"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		main_menu()
	if navigate == 1:
		search_menu()
	if navigate == 2:
		service_nos_menu()
	if navigate == 3:
		add_name_menu()
	if navigate == 4:
		erase_menu()
	if navigate == 5:
		edit_menu()
	if navigate == 6:
		assign_tone_menu()
	if navigate == 7:
		send_bcard_menu()
	if navigate == 8:
		options_menu()
	if navigate == 9:
		speed_dials_menu()
	if navigate == 10:
		voice_tags_menu()

def search_menu():
	display = """
╔════════════════════════╗
║         Search         ║
╠════════════════════════╣
║ Find: [A__________]    ║
║                        ║
║ Matches:               ║
║ > Alice                ║
║   Andrew               ║
╠════════════════════════╣
║    [Find]   [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def service_nos_menu():
	display = """
╔════════════════════════╗
║      Service Nos.      ║
╠════════════════════════╣
║ > Voicemail            ║
║   Customer Care        ║
║   Balance Enquiry      ║
╠════════════════════════╣
║     [Call]   [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def add_name_menu():
	display = """
╔════════════════════════╗
║        Add Name        ║
╠════════════════════════╣
║ Name: ____________     ║
║ Number: ____________   ║
╠════════════════════════╣
║    [Save]   [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def erase_menu():
	display = """
╔════════════════════════╗
║          Erase         ║
╠════════════════════════╣
║ > Erase “John”?        ║
║                        ║
╠════════════════════════╣
║   [Yes]   [0.Back]     ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def edit_menu():
	display = """
╔════════════════════════╗
║          Edit          ║
╠════════════════════════╣
║ Name: John Smith       ║
║ Number: 07123456789    ║
╠════════════════════════╣
║    [Save]   [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def assign_tone_menu():
	display = """
╔════════════════════════╗
║      Assign Tone       ║
╠════════════════════════╣
║ Contact: Alice         ║
║ > Nokia Tune           ║
║   Waltz of the Demon   ║
║   Silent               ║
╠════════════════════════╣
║  [Select]   [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def send_bcard_menu():
	display = """
╔════════════════════════╗
║       Send B’card      ║
╠════════════════════════╣
║ > Send “David”?        ║
║ Via: Infrared          ║
║      SMS               ║
╠════════════════════════╣
║     [Send]    [0.Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def options_menu():
	display = """
1 => Type of view
2 => Memory status

0 => Back"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	if navigate == 1:
		type_of_view_menu()
	if navigate == 2:
		memory_status_menu()
	
def speed_dials_menu():
	display = """
╔════════════════════════╗
║       Speed Dials      ║
╠════════════════════════╣
║ 1: Voicemail           ║
║ 2: Dad                 ║
║ 3: Empty               ║
╠════════════════════════╣
║   [Assign]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	
def voice_tags_menu():
	display = """
╔════════════════════════╗
║       Voice Tags       ║
╠════════════════════════╣
║ > Record new tag       ║
║   David                ║
║   Voicemail            ║
╠════════════════════════╣
║   [Record] [0.Back]    ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phonebook_menu()
	

def type_of_view_menu():
	display = """
╔════════════════════════╗
║      Type of view      ║
╠════════════════════════╣
║ > Name list            ║
║   Name & number        ║
║   Name only            ║
╠════════════════════════╣
║  [Select]   [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		options_menu()

def memory_status_menu():
	display = """
╔════════════════════════╗
║     Memory status      ║
╠════════════════════════╣
║ Used:     22           ║
║ Free:     78           ║
║ Total:   100           ║
╠════════════════════════╣
║   [OK]    [0.Back]     ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		options_menu()


	