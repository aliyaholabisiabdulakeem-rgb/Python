
print("1. Phone book")
print("2. Messages")
print("3. Chat")
print("4. Call register")
print("5. Tones")
print("6. Settings")
print("7. Call divert")
print("8. Music")
print("9. Games")
print("10. Calculator")
print("11. Reminders")
print("12. Clock")
print("13. Profiles")
print("14. Services")
print("15. SIM Services")

main = input("Enter main menu: ")

if main == "1":
    print("1 Search")
    print("2 Service Nos.")
    print("3 Add name")
    print("4 Erase")
    print("5 Edit")
    print("6 Copy")
    print("7 Assign tone")
    print("8 Send b'card")
    print("9 Options")
    print("10 Speed dials")
    print("11 Voice tags")
    phonebookoptions = input("Enter: ")
    
    if phonebookoptions == "1":
        print("Search")
    elif phonebookoptions == "2":
        print("Service Nos.")
    elif phonebookoptions == "3":
        print("Add name")
    elif phonebookoptions == "4":
        print("Erase")
    elif phonebookoptions == "5":
        print("Edit")
    elif phonebookoptions == "6":
        print("Copy")
    elif phonebookoptions == "7":
        print("Assign tone")
    elif phonebookoptions == "8":
        print("Send b'card")
    elif phonebookoptions == "9":
        print("1 Memory in use")
        print("2 Type of view")
        print("3 Memory status")
        option = input("Enter option: ")
        if option == "1":
            print("Memory in use")
        elif option == "2":
            print("Type of view")
        elif option == "3":
            print("Memory status")
    elif phonebookoptions == "10":
        print("Speed dials")
    elif phonebookoptions == "11":
        print("Voice tags")

elif main == "2":
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
    messagesettingsoptions = input("enter: ")

    if messagesettingsoptions == "1":
        print("Write messages")
    elif messagesettingsoptions == "2":
        print("Inbox")
    elif messagesettingsoptions == "3":
        print("Outbox")
    elif messagesettingsoptions == "4":
        print("Picture settings")
    elif messagesettingsoptions == "5":
        print("Templates")
    elif messagesettingsoptions == "6":
        print("Smileys")
    elif messagesettingsoptions == "7":
        print("Set 1")
        print("Common")
        option = input("Enter: ")
        if option == "1":
            print("Message centre number")
            print("Message sent as")
            print("Message validity")
        if option == "2":
            print("Delivery reports")
            print("Reply via same centre")
            print("Character support")
elif main == "3":
    print("Chat")

elif main == "4":
    print("1 Missed calls")
    print("2 Received calls")
    print("3 Dialled numbers")
    print("4 Erase recent call lists")
    print("5 Show call duration")
    print("6 Show call costs")
    print("7 Call cost settings")
    print("8 Prepaid credit")
    callregisteroption = input("Enter: ")

    if callregisteroption == "1":
        print("Missed calls")
    elif callregisteroption == "2":
        print("Received calls")
    elif callregisteroption == "3":
        print("Dialed numbers")
    elif callregisteroption =="4":
        print("Erase recent call lists")
    elif callregisteroption == "5":
        print("Last call duration")
        print("All calls' duration")
        print("Received calls' duration")
        print("Dialed calls' duration")
        print("Clear timers")
    elif callregisteroption == "6":
        print("Last call cost")
        print("All calls' cost")
        print("Clear counters")
    elif callregisteroption == "7":
        print("Call cost limit")
        print("Show costs in")
    elif callregisteroption == "8":
        print("Prepaid credit")
       
elif main == "5":
    print("1 Ringing tone")
    print("2 Ringing volume")
    print("3 Incoming call alert")
    print("4 Message alert tone")
    print("5 Keypad tones")
    print("6 Warning tones")
    print("7 Warning and game tones")
    print("8 Vibrating alert")
    print("9 Screen saver")

elif main == "6":
    print("1 Call settings")
    print("2 Phone settings")
    print("3 Security settings")
    print("4 Restore factory settings")
    settingsoption = input("Enter: ")
    
    if settingsoption == "1":
        print("Automated redial")
        print("Speed dialing")
        print("Call waiting options")
        print("Own number sending")
        print("Phone line in use")
        print("Automatic answer")
    elif settingsoption == "2":
        print("Language")
        print("Cell info display")
        print("Welcome note")
        print("Network selection")
        print("Confirm SIM service actions")
    elif settingsoption == "3":
        print("PIN code request")
        print("Call barring service")
        print("Fixed dialing")
        print("Closed user group")
        print("Security level")
        print("Change access codes")
    elif settingsoptions =="4":
        print("Restore factory settings")

elif main == "7":
    print("Call divert")

elif main == "8":
    print("1 Music player")
    print("2 Radio")
    print("3 Recorder")
    print("4 Track list")

elif main == "9":
    print("Games")

elif main == "10":
    print("Calculator")

elif main == "11":
    print("Reminders")

elif main == "12":
    print("Alarm clock")
    print("Clock settings")
    print("Date settings")
    print("Stopwatch")
    print("Countdown timer")
    print("Auto update of date and time")

elif main == "13":
    print("Profiles")

elif main == "14":
    print("Services")

elif main == "15":
    print("SIM Services")


