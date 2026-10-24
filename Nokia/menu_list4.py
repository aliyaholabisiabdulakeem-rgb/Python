def options_menu():
    while True:
        print("Options")
        print("1 Memory in use")
        print("2 Type of view")
        print("3 Memory status")
        print("0 Back | 99 Home")
        options = int(input("Enter a number: "))
        if options == 0:
            return "back"
        if options == 99:
            return "home"
        match options:
            case 1:
                print("Memory in use")
            case 2:
                print("Type of view")
            case 3:
                print("Memory status")
            case _:
                print("invalid")

def phonebook_menu():
    while True:
        print("Phone book")
        print("1 Search")
        print("2 Service Nos")
        print("3 Add name")
        print("4 Erase")
        print("5 Edit")
        print("6 Copy")
        print("7 Assign tone")
        print("8 Options")
        print("9 Send b card")
        print("10 Speed dials")
        print("11 Voice tags")
        print("0 Back | 99 Home")
        phonebookoptions = int(input("Enter a number: "))
        if phonebookoptions == 0:
            return "back"
        if phonebookoptions == 99:
            return "home"
        match phonebookoptions:
            case 1:
                print("Search")
            case 2:
                print("Service Nos")
            case 3:
                print("Add name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Copy")
            case 7:
                print("Assign tone")
            case 8:
                result = options_menu()
                if result == "home":
                    return "home"
            case 9:
                print("Send b card")
            case 10:
                print("Speed dials")
            case 11:
                print("Voice tags")
            case _:
                print("Invalid")

def message_settings_menu():
    while True:
        print("Message settings")
        print("1 Set 1")
        print("2 Common")
        print("0 Back | 99 Home")
        set1_option = int(input("Enter a number: "))
        if set1_option == 0:
            return "back"
        if set1_option == 99:
            return "home"
        match set1_option:
            case 1:
                print("1 Message centre number")
                print("2 Messages sent as")
                print("3 Message validity")
            case 2:
                print("1 Delivery reports")
                print("2 Reply via same centre")
                print("3 Character support")
            case _:
                print("Invalid")

def messages_menu():
    while True:
        print("Messages")
        print("1 Write messages")
        print("2 Inbox")
        print("3 Outbox")
        print("4 Picture messages")
        print("5 Templates")
        print("6 Smileys")
        print("7 Message settings")
        print("8 Info service")
        print("9 Voice mailbox number")
        print("10 Service command editor")
        print("0 Back | 99 Home")
        messages = int(input("Enter a number: "))
        if messages == 0:
            return "back"
        if messages == 99:
            return "home"
        match messages:
            case 7:
                result = message_settings_menu()
                if result == "home":
                    return "home"
            case _:
                print("Messages option")

def call_duration_menu():
    while True:
        print("Show call duration")
        print("1 Last call duration")
        print("2 All calls duration")
        print("3 Received calls duration")
        print("4 Dialled calls duration")
        print("5 Clear timers")
        print("0 Back | 99 Home")
        callduration = int(input("Enter a number: "))
        if callduration == 0:
            return "back"
        if callduration == 99:
            return "home"
        match callduration:
            case 1:
                print("Last call duration")
            case 2:
                print("All calls duration")
            case 3:
                print("Received calls duration")
            case 4:
                print("Dialled calls duration")
            case 5:
                print("Clear timers")
            case _:
                print("Invalid")

def call_cost_menu():
    while True:
        print("Show call costs")
        print("1 Last call cost")
        print("2 All calls cost")
        print("3 Clear counters")
        print("0 Back | 99 Home")
        showcallcost = int(input("Enter a number: "))
        if showcallcost == 0:
            return "back"
        if showcallcost == 99:
            return "home"
        match showcallcost:
            case 1:
                print("Last call cost")
            case 2:
                print("All calls cost")
            case 3:
                print("Clear counters")
            case _:
                print("Invalid")

def call_cost_settings_menu():
    while True:
        print("Call cost settings")
        print("1 Call cost limit")
        print("2 Show costs in")
        print("0 Back | 99 Home")
        callcostsettings = int(input("Enter a number: "))
        if callcostsettings == 0:
            return "back"
        if callcostsettings == 99:
            return "home"
        match callcostsettings:
            case 1:
                print("Call cost limit")
            case 2:
                print("Show costs in")
            case _:
                print("Invalid")

def call_register_menu():
    while True:
        print("Call register")
        print("1 Missed calls")
        print("2 Received calls")
        print("3 Dialled numbers")
        print("4 Erase recent call lists")
        print("5 Show call duration")
        print("6 Show call costs")
        print("7 Call cost settings")
        print("8 Prepaid credit")
        print("0 Back | 99 Home")
        callregister = int(input("Enter a number: "))
        if callregister == 0:
            return "back"
        if callregister == 99:
            return "home"
        match callregister:
            case 1:
                print("Missed calls")
            case 2:
                print("Received calls")
            case 3:
                print("Dialled numbers")
            case 4:
                print("Erase recent call lists")
            case 5:
                result = call_duration_menu()
                if result == "home":
                    return "home"
            case 6:
                result = call_cost_menu()
                if result == "home":
                    return "home"
            case 7:
                result = call_cost_settings_menu()
                if result == "home":
                    return "home"
            case 8:
                print("Prepaid credit")
            case _:
                print("Invalid")

def tones_menu():
    while True:
        print("Tones")
        print("1 Ringing tone")
        print("2 Ringing volume")
        print("3 Incoming call alert")
        print("4 Composer")
        print("5 Message alert tone")
        print("6 Keypad tones")
        print("7 Warning and game tones")
        print("8 Vibrating alert")
        print("9 Screen saver")
        print("0 Back | 99 Home")
        tones = int(input("Enter a number: "))
        if tones == 0:
            return "back"
        if tones == 99:
            return "home"
        match tones:
            case 1:
                print("Ringing tone")
            case 2:
                print("Ringing volume")
            case 3:
                print("Incoming call alert")
            case 4:
                print("Composer")
            case 5:
                print("Message alert tone")
            case 6:
                print("Keypad tones")
            case 7:
                print("Warning and game tones")
            case 8:
                print("Vibrating alert")
            case 9:
                print("Screen saver")
            case _:
                print("Invalid")

def settings_menu():
    while True:
        print("Settings")
        print("1 Call settings")
        print("2 Phone settings")
        print("3 Security settings")
        print("4 Restore factory settings")
        print("0 Back | 99 Home")
        settings = int(input("Enter a number: "))
        if settings == 0:
            return "back"
        if settings == 99:
            return "home"
        match settings:
            case 1:
                while True:
                    print("Call settings")
                    print("1 Automatic redial")
                    print("2 Speed dialling")
                    print("3 Call waiting options")
                    print("4 Own number sending")
                    print("5 Phone line in use")
                    print("6 Automatic answer")
                    print("0 Back | 99 Home")
                    callsettings = int(input("Enter a number: "))
                    if callsettings == 0:
                        break
                    if callsettings == 99:
                        return "home"
                    print("call settings option")
            case 2:
                while True:
                    print("Phone settings")
                    print("1 Language")
                    print("2 Cell info display")
                    print("3 Welcome note")
                    print("4 Network selection")
                    print("5 Confirm SIM service actions")
                    print("0 Back | 99 Home")
                    phonesettings = int(input("Enter a number: "))
                    if phonesettings == 0:
                        break
                    if phonesettings == 99:
                        return "home"
                    print("phone settings option")
            case 3:
                while True:
                    print("Security settings")
                    print("1 PIN code request")
                    print("2 Call barring service")
                    print("3 Fixed dialling")
                    print("4 Closed user group")
                    print("5 Security level")
                    print("6 Change access codes")
                    print("0 Back | 99 Home")
                    securitysettings = int(input("Enter a number: "))
                    if securitysettings == 0:
                        break
                    if securitysettings == 99:
                        return "home"
                    print("security option")
            case 4:
                print("Restore factory settings")
            case _:
                print("Invalid")

def music_menu():
    while True:
        print("Music")
        print("1 Music player")
        print("2 Radio")
        print("3 Recorder")
        print("4 Track list")
        print("0 Back | 99 Home")
        music = int(input("Enter a number: "))
        if music == 0:
            return "back"
        if music == 99:
            return "home"
        print("Music option")

def clock_menu():
    while True:
        print("Clock")
        print("1 Alarm clock")
        print("2 Clock settings")
        print("3 Date setting")
        print("4 Stopwatch")
        print("5 Countdown timer")
        print("6 Auto update of date and time")
        print("0 Back | 99 Home")
        clock = int(input("Enter a number: "))
        if clock == 0:
            return "back"
        if clock == 99:
            return "home"
        print("Clock option")

while True:
    print("MAIN MENU")
    print("1 Phone book")
    print("2 Messages")
    print("3 Chat")
    print("4 Call register")
    print("5 Tones")
    print("6 Settings")
    print("7 Call divert")
    print("8 Music")
    print("9 Games")
    print("10 Calculator")
    print("11 Reminders")
    print("12 Clock")
    print("13 Profiles")
    print("14 WAP Services")
    print("15 SIM Services")
    print("0 Exit")
    print("99 Home")
    
    main_menu = int(input("Enter main menu: "))
    
    if main_menu == 0:
        print("Exiting...")
        break
    if main_menu == 99:
        continue

    match main_menu:
        case 1:
            phonebook_menu()
        case 2:
            messages_menu()
        case 3:
            print("Chat")
        case 4:
            call_register_menu()
        case 5:
            tones_menu()
        case 6:
            settings_menu()
        case 7:
            print("Call divert")
        case 8:
            music_menu()
        case 9:
            print("Games")
        case 10:
            print("Calculator")
        case 11:
            print("Reminders")
        case 12:
            clock_menu()
        case 13:
            print("Profiles")
        case 14:
            print("WAP Services")
        case 15:
            print("SIM Services")
        case _:
            print("Invalid")
