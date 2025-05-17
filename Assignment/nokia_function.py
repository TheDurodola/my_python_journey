
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
		messages_menu()
	if navigate == 3:
		chat_menu()
	if navigate == 4:
		chat_menu()
	if navigate == 5:
		tones_menu()
	if navigate == 6:
		settings_menu()
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

def settings_menu():
	display = """
1 => Call settings
2 => Phone settings
3 => Security settings
4 => Restore factory settings

0 =>  Back"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		call_settings_menu()
	if navigate == 2:
		phone_settings_menu()
	if navigate == 3:
		security_settings_menu()
	if navigate == 4:
		restore_factory_settings_menu()
	if navigate == 0:
		main_menu()

def settings_menu():
	display = """
1 => Call settings
2 => Phone settings
3 => Security settings
4 => Restore factory settings

0 =>  Back"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		call_settings_menu()
	if navigate == 2:
		phone_settings_menu()
	if navigate == 3:
		security_settings_menu()
	if navigate == 4:
		restore_factory_settings_menu()
	if navigate == 0:
		main_menu()

def call_settings_menu():
	display = """
╔════════════════════════╗
║     Call settings      ║
╠════════════════════════╣
║ > 1. Automatic redial  ║
║   2. Speed dialling    ║
║   3. Call waiting      ║
║   4. Own number sending║
║   5. Phone line in use ║
║   6. Automatic answer  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		settings_menu()
	if navigate == 1:
		automatic_redial_menu()
	if navigate == 2:
		speed_dialling_menu()
	if navigate == 3:
		call_waiting_menu()
	if navigate == 4:
		own_number_sending_menu()
	if navigate == 5:
		phone_line_in_use_menu()
	if navigate == 6:
		automatic_answer_menu()

def automatic_redial_menu():
	display = """
╔════════════════════════╗
║   Automatic redial     ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		call_settings_menu()

def speed_dialling_menu():
	display = """
╔════════════════════════╗
║    Speed dialling      ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		call_settings_menu()


def call_waiting_menu():
	display = """
╔════════════════════════╗
║  Call waiting options  ║
╠════════════════════════╣
║ > Activate             ║
║   Cancel               ║
║   Check status         ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		call_settings_menu()

def own_number_sending_menu():
	display = """
╔════════════════════════╗
║  Own number sending    ║
╠════════════════════════╣
║ > Set by network       ║
║   On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		call_settings_menu()


def phone_line_in_use_menu():
	display = """
╔════════════════════════╗
║  Phone line in use     ║
╠════════════════════════╣
║ > Line 1               ║
║   Line 2               ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		call_settings_menu()


def automatic_answer_menu():
	display = """
╔════════════════════════╗
║   Automatic answer     ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
║ (Only with headset)    ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		call_settings_menu()

def phone_settings_menu():
	display = """
╔═════════════════════════╗
║     Phone settings      ║
╠═════════════════════════╣
║ > 1. Language           ║
║   2. Cell info display  ║
║   3. Welcome note       ║
║   4. Network selection  ║
║   5. Lights             ║
║   6. Confirm SIM actions║
╠═════════════════════════╣
║     [Select]  [0.Back]  ║
╚═════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		language_menu()
	if navigate == 2:
		cell_info_display_menu()
	if navigate == 3:
		welcome_note_menu()
	if navigate == 4:
		network_selection_menu()
	if navigate == 5:
		lights_menu()
	if navigate == 6:
		confirm_sim_service_actions_menu()
	if navigate == 0:
		settings_menu()

def language_menu():
	display = """
╔════════════════════════╗
║        Language        ║
╠════════════════════════╣
║ > English              ║
║   Français             ║
║   Deutsch              ║
║   Español              ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phone_settings_menu()

def cell_info_display_menu():
	display = """
╔════════════════════════╗
║   Cell info display    ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phone_settings_menu()

def welcome_note_menu():
	display = """
╔════════════════════════╗
║      Welcome note      ║
╠════════════════════════╣
║ Message:               ║
║ “Hello!”               ║
║                        ║
╠════════════════════════╣
║   [Edit] [0.Back]      ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phone_settings_menu()

def network_selection_menu():
	display = """
╔════════════════════════╗
║   Network selection    ║
╠════════════════════════╣
║ > Automatic            ║
║   Manual               ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phone_settings_menu()

def lights_menu():
	display = """
╔════════════════════════╗
║         Lights         ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phone_settings_menu()

def confirm_sim_service_actions_menu():
	display = """
╔════════════════════════╗
║ Confirm SIM actions    ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		phone_settings_menu()

def security_settings_menu():
	display = """
╔═════════════════════════╗
║   Security settings     ║
╠═════════════════════════╣
║ > 1. PIN code request   ║
║   2. Call barring       ║
║   3. Fixed dialling     ║
║   4. Closed user group  ║
║   5. Phone security     ║
║   6. Change access codes║
╠═════════════════════════╣
║     [Select]  [0.Back]  ║
╚═════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		pin_code_request_menu()
	if navigate == 2:
		call_barring_service_menu()
	if navigate == 3:
		fixed_dialling_menu()
	if navigate == 4:
		closed_user_group_menu()
	if navigate == 5:
		phone_security_menu()
	if navigate == 6:
		change_access_code_menu()
	if navigate == 0:
		settings_menu()


def pin_code_request_menu():
	display = """
╔════════════════════════╗
║    PIN code request    ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║ Enter PIN: ____        ║
║     [OK]     [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		security_settings_menu()


def call_barring_service_menu():
	display = """
╔════════════════════════╗
║  Call barring service  ║
╠════════════════════════╣
║ > Outgoing calls       ║
║   Incoming calls       ║
║   Cancel all barrings  ║
║   Change barring code  ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		security_settings_menu()

def fixed_dialling_menu():
	display = """
╔════════════════════════╗
║     Fixed dialling     ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
║   Edit fixed list      ║
╠════════════════════════╣
║ PIN2: ____             ║
║   [OK]     [0.Back]    ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		security_settings_menu()

def closed_user_group_menu():
	display = """
╔════════════════════════╗
║   Closed user group    ║
╠════════════════════════╣
║ > Default              ║
║   Group 1              ║
║   Group 2              ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		security_settings_menu()

def phone_security_menu():
	display = """
╔════════════════════════╗
║     Phone security     ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║ Code: ____             ║
║     [OK]   [0.Back]    ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		security_settings_menu()

def change_access_code_menu():
	display = """
╔════════════════════════╗
║  Change access codes   ║
╠════════════════════════╣
║ > Change PIN           ║
║   Change PIN2          ║
║   Change security code ║
╠════════════════════════╣
║   [Select]  [0.Back]   ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		security_settings_menu()


def restore_factory_settings_menu():
	display = """
╔═════════════════════════╗
║ Restore factory settings║
╠═════════════════════════╣
║ Restore all settings?   ║
║                         ║
║ Code: ______            ║
╠═════════════════════════╣
║    [OK]      [0.Back]   ║
╚═════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		settings_menu()

def messages_menu():
	display ="""
╔═════════════════════════╗
║       Messages          ║
╠═════════════════════════╣
║ > 1. Write messages     ║
║   2. Inbox              ║
║   3. Outbox             ║
║   4. Picture messages   ║
║   5. Templates          ║
║   6. Smileys            ║
║   7. Messages Settings  ║
║   8. Info service       ║
║   9. Voice mailbox no.  ║
║  10. Service cmd editor ║
╠═════════════════════════╣
║     [Select]  [0.Back]  ║
╚═════════════════════════╝
"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		write_messages_menu()
	if navigate == 2:
		inbox_menu()
	if navigate == 3:
		outbox_menu()
	if navigate == 4:
		picture_messages_menu()
	if navigate == 5:
		templates_menu()
	if navigate == 6:
		smileys_menu()
	if navigate == 7:
		messages_settings_menu()
	if navigate == 8:
		info_services_menu()
	if navigate == 9:
		voice_mailbox_number_menu()
	if navigate == 10:
		service_command_editor_menu()
	if navigate == 0:
		main_menu()


def write_messages_menu():
	display = """
╔════════════════════════╗
║     Write message      ║
╠════════════════════════╣
║ To: ____________       ║
║                        ║
║ Msg:                   ║
║ Hello! How are you?    ║
╠════════════════════════╣
║   [Send] [0.Back]      ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()


def inbox_menu():
	display = """
╔═════════════════════════╗
║          Inbox          ║
╠═════════════════════════╣
║ > 1 New Message         ║
║   2 Yesterday           ║
║   3 Last week           ║
╠═════════════════════════╣
║     [Open]    [0.Back]  ║
╚═════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()

def outbox_menu():
	display = """
╔════════════════════════╗
║         Outbox         ║
╠════════════════════════╣
║ > Msg to Mum           ║
║   Msg to Office        ║
║   Msg failed           ║
╠════════════════════════╣
║     [Open]    [0.Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()

def picture_messages_menu():
	display = """
╔════════════════════════╗
║   Picture messages     ║
╠════════════════════════╣
║ > Birthday Cake        ║
║   Happy Face           ║
║   Love You             ║
╠════════════════════════╣
║     [Select]  [0.Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()

def templates_menu():
	display = """
╔════════════════════════╗
║        Templates       ║
╠════════════════════════╣
║ > I’m in a meeting     ║
║   Call you later       ║
║   Happy Birthday!      ║
╠════════════════════════╣
║     [Use]     [0.Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()

def smileys_menu():
	display = """
╔════════════════════════╗
║         Smileys        ║
╠════════════════════════╣
║ > :-)     Happy        ║
║   :-(     Sad          ║
║   ;-)     Wink         ║
╠════════════════════════╣
║     [Insert]  [0.Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()

def info_services_menu():
	display = """
╔════════════════════════╗
║      Info service      ║
╠════════════════════════╣
║ > Headlines            ║
║   Weather              ║
║   Network alerts       ║
╠════════════════════════╣
║     [View]    [0.Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()

def voice_mailbox_number_menu():
	display = """
╔════════════════════════╗
║  Voice mailbox number  ║
╠════════════════════════╣
║ Number: +1234567890    ║
╠════════════════════════╣
║    [Edit]     [0.Back] ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()

def service_command_editor_menu():
	display = """
╔════════════════════════╗
║ Service cmd editor     ║
╠════════════════════════╣
║ Command: *#06#         ║
║                        ║
╠════════════════════════╣
║   [Send]     [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		messages_menu()


def messages_settings_menu():
	display = """
1 => Set
2 => Common

0 =>  Back"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		set_menu()
	if navigate == 2:
		common_menu()
	if navigate ==0:
		messages_menu()

def set_menu():
	display = """
1 => Message centre number
2 => Messages sent as 
3 => Message validity

0 =>  Back"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		message_centre_number()
	if navigate == 2:
		messages_sent_as()
	if navigate ==3:
		message_validity()
	if navigate ==0:
		messages_settings_menu()

def message_centre_number():
	display = """
╔════════════════════════╗
║  Message centre number ║
╠════════════════════════╣
║ +1234567890            ║
╠════════════════════════╣
║   [Edit]     [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		set_menu()

def messages_sent_as():
	display = """
╔════════════════════════╗
║     Message sent as    ║
╠════════════════════════╣
║ > Text                 ║
║   Fax                  ║
║   Paging               ║
╠════════════════════════╣
║   [Select]   [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		set_menu()

def message_validity():
	display = """
╔════════════════════════╗
║    Message validity    ║
╠════════════════════════╣
║ > 1 hour               ║
║   6 hours              ║
║   24 hours             ║
║   1 week               ║
╠════════════════════════╣
║   [Select]   [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		set_menu()


def common_menu():
	display = """
1 => Delivery reports
2 => Reply via same centre
3 => Character support

0 =>  Back"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 1:
		delivery_reports()
	if navigate == 2:
		reply_via_same_centre()
	if navigate ==3:
		character_support()
	if navigate ==0:
		messages_settings_menu()

def reply_via_same_centre():
	display = """
╔════════════════════════╗
║ Reply via same centre  ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║     [Select] [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		common_menu()

def character_support():
	display = """
╔════════════════════════╗
║    Character support   ║
╠════════════════════════╣
║ > Full                 ║
║   Reduced              ║
╠════════════════════════╣
║     [Select] [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		common_menu()

def delivery_reports():
	display = """
╔════════════════════════╗
║     Delivery reports   ║
╠════════════════════════╣
║ > On                   ║
║   Off                  ║
╠════════════════════════╣
║     [Select] [0.Back]  ║
╚════════════════════════╝"""
	print(display)
	navigate = int(input("Enter a number to move: "))
	if navigate == 0:
		common_menu()

