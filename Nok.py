while(true){
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
        print("14. WAP Services")
        print("15. SIM Services")
        print("0. Exit")
        
            main = input("Enter main menu: ")
            if(mainMenu == 0): break

           match(mainMenu) {
                case 1 -> {
                    while(true){
                        print("Phone book:")
                        print("1 Search")
                        print("2 Service Nos.")
                        print("3 Add name")
                        print("4 Erase")
                        print("5 Edit")
                        print("6 Assign tone")
                        print("7 Send b card")
                        print("8 Options")
                        print("9 Speed dials")
                        print("10 Voice tags")
                        print("0  Exit")
                        print("Enter: ")
                        
                        if(phonebookoptions == 0): break
                        match(phonebookoptions) {
                            case 1 -> print("Search:")
                            case 2 -> print("Service Nos.")
                            case 3 -> print("Add name")
                            case 4 -> print("Erase")
                            case 5 -> print("Edit")
                            case 6 -> print("Copy")
                            case 7 -> print("Assign tone")
                            case 8 -> print("Send b card")
                            case 9 -> {
                                while(true){
                                    print("1 Memory in use")
                                    print("2 Type of view")
                                    print("3 Memory status")
                                    print("0 Exit")
                                    print("Enter: ")
                                    
                                    if(options == 0): break
                                    match(options) :
                                        case 1 -> print("Memory in use")
                                        case 2 -> print("Type of view")
                                        case 3 -> print("Memory status")
                                       default -> print("Invalid")
                                    }
                                }
                            }
                            case 10 -> print("Speed dials")
                            case 11 -> print("Voice tags")
                            default -> print("Invalid")
                        }
                    }
                }
                case 2 -> {
                    while(true){
                        print("Messages:")
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
                        print("0 Exit")
                        print("Enter: ")
                                
                        if(messages == 0): break
                        match(messages) :
                            case 1 -> print("Write messages")
                            case 2 -> print("Inbox")
                            case 3 -> print("Outbox")
                            case 4 -> print("Picture messages")
                            case 5 -> print("Templates")
                            case 6 -> print("Smileys")
                            case 7 -> {
                                while(true){
                                    print("1 Set 1")
                                    print("2 Common")
                                    print("0 Exit")
                                    print("Enter: ")
                                    
                                    if(set1 == 0): break
                                    match(set1) :
                                        case 1 -> print("1 Message centre number")
                                                  print("2 Messages sent as")
                                                  print("3 Message validity")
                                        case 2 -> print("1 Delivery reports")
                                                  print("2 Reply via same centre")
                                                  print("3 Character support")
                                        default -> print("Invalid")
                                    }
                                }
                            }
                            case 8 -> print("Info service")
                            case 9 -> print("Voice mailbox number")
                            case 10 -> print("Service command editor")
                            default -> print("Invalid")
                        }
                    }
                }
                case 3 -> print("Chat")
                case 4 -> {
                    while(true){
                        print("Call register:")
                        print("1 Missed calls")
                        print("2 Received calls")
                        print("3 Dialled numbers")
                        print("4 Erase recent call lists")
                        print("5 Show call duration")
                        print("6 Show call costs")
                        print("7 Call cost settings")
                        print("8 Prepaid credit")
                        print("0 Exit")
                        print("Enter: ")
                        
                        if(callregister == 0): break
                        match(callregister) :
                            case 1 -> print("Missed calls")
                            case 2 -> print("Received calls")
                            case 3 -> print("Dialled numbers")
                            case 4 -> print("Erase recent call lists")
                            case 5 -> {
                                while(true){
                                    print("1 Last call duration")
                                    print("2 All calls duration")
                                    print("3 Received calls duration")
                                    print("4 Dialled calls duration")
                                    print("5 Clear timers")
                                    print("0 Exit")
                                    print("Enter: ")
                                    
                                    if(callduration == 0): break
                                    match(callduration) :
                                        case 1 -> print("Last call duration")
                                        case 2 -> print("All calls duration")
                                        case 3 -> print("Received calls duration")
                                        case 4 -> print("Dialled calls duration")
                                        case 5 -> print("Clear timers")
                                        default -> print("Invalid")
                                    }
                                }
                            }
                            case 6 -> {
                                while(true){
                                     6 -> { 
                                    print("1 Last call cost")
                                    print("2 All calls’ cost")
                                    print("3 Clear counters")
                                    print("0 Exit")
                                    print("Enter: ")
                                    
                                    if(showcallcost == 0): break
                                    match(showcallcost):
                                        case 1 -> print("Last call cost")
                                        case 2 -> print("All calls' cost")
                                        case 3 -> print("Clear counters")
                                        default -> print("Invalid")
                                    }
                                }
                            }
                            case 7 -> {
                                while(true){
                                   print("1 Call cost settings")
                                   print("2 Show costs in")
                                   print("0 Exit")
                                   print("Enter: ")
                                    
                                    if(callcostsettings == 0): break
                                    match(callcostsettings):
                                        case 1 -> print("Call cost limit")
                                        case 2 -> print("Show costs in")
                                        default -> print("Invalid")
                                    }
                                }
                            }
                            case 8 -> print("Prepaid credit")
                            default -> print("Invalid")
                        }
                    }
                }       
            case 5 -> {
                while(true){
                        print("Tones:")
                        print("1 Ringing tone")
                        print("2 Ringing volume")
                        print("3 Incoming call alert")
                        print("4 Composer")
                        print("5 Message alert tone")
                        print("6 Keypad tones")
                        print("7 Warning and game tones")
                        print("8 Vibrating alert")
                        print("9 Screen saver")
                        print("0 Exit")
                        print("Enter: ")
                        
                        if(tones == 0): break
                        match(tones):
                            case 1 -> print("Ringing tone")
                            case 2 -> print("Ringing volume")
                            case 3 -> print("Incoming call alert")
                            case 4 -> print("Composer")
                            case 5 -> print("Message alert tone")
                            case 6 -> print("Keypad tones")
                            case 7 -> print("Warning and game tones")
                            case 8 -> print("Vibrating alert")
                            case 9 -> print("Screen saver")
                            default -> print("Invalid")
                        }
                    }
                
            case 6 -> {
                while(true){
                        print("Settings:");
                        print("1 Call settings");
                        print("2 Phone settings");
                        print("3 Security settings");
                        print("4 Restore factory settings");
                        print("0 Exit");
                        print("Enter: ");
                        
                        if(settings == 0): break
                        match(settings) :
                            case 1 -> {
                                while(true){
                                    print("1 Automatic redial")
                                    print("2 Speed dialling")
                                    print("3 Call waiting options")
                                    print("4 Own number sending")
                                    print("5 Phone line in use")
                                    print("6 Automatic answer")
                                    print("0 Exit")
                                    print("Enter: ")
                                    
                                    if(callsettings == 0): break
                                    match(callsettings):
                                        case 1 -> print("Automatic redial")
                                        case 2 -> print("Speed dialling")
                                        case 3 -> print("Call waiting options")
                                        case 4 -> print("Own number sending")
                                        case 5 -> print("Phone line in use")
                                        case 6 -> print("Automatic answer")
                                        default -> print("Invalid")
                                     }
                                }
                            
                            case 2 -> {
                                while(true){
                                    print("1 Language")
                                    print("2 Cell info display")
                                    print("3 Welcome note")
                                    print("4 Network selection")
                                    print("5 Confirm SIM service actions")
                                    print("0 Exit")
                                    print("Enter: ")
                                    
                                    if(phonesettings == 0): break
                                    match(phonesettings):
                                        case 1 -> print("Language")
                                        case 2 -> print("Cell info display")
                                        case 3 -> print("Welcome note")
                                        case 4 -> print("Network selection")
                                        case 5 -> print("Confirm SIM service actions")
                                        default -> print("Invalid")
                                     }
                                }
                            
                            case 3 -> {
                                while(true){
                                    print("1 PIN code request")
                                    print("2 Call barring service")
                                    print("3 Fixed dialling")
                                    print("4 Closed user group")
                                    print("5 Security level")
                                    print("6 Change access codes")
                                    print("0 Exit")
                                    print("Enter: ")
                                    
                                    if(securitysettings == 0): break
                                    match(securitysettings):
                                        case 1 -> print("PIN code request")
                                        case 2 -> print("Call barring service")
                                        case 3 -> print("Fixed dialling")
                                        case 4 -> print("Closed user group")
                                        case 5 -> print("Security level")
                                        case 6 -> print("Change access codes")
                                        default ->print("Invalid")
                                    }
                                }
                            
                            case 4 -> print("Restore factory settings")
                            default -> print("Invalid")
                        }
                    }
                }
                case 7 -> print("Call divert")
                case 8 -> {
                    while(true){
                        print("Music:")
                        print("1 Music player")
                        print("2 Radio")
                        print("3 Recorder")
                        print("4 Track list")
                        print("0 Exit")
                        print("Enter: ")
                        
                        if(music == 0): break
                        match(music) :
                            case 1 -> print("Music player")
                            case 2 -> print("Radio")
                            case 3 -> print("Recorder")
                            case 4 -> print("Track list")
                            default -> print("Invalid")
                        }
                    }
                
                case 9 -> print("Games")
                case 10 -> print("Calculator")
                case 11 -> print("Reminders")
                case 12 -> {
                    while(true){
                        print("Clock:")
                        print("1 Alarm clock")
                        print("2 Clock settings")
                        print("3 Date setting")
                        print("4 Stopwatch")
                        print("5 Countdown timer")
                        print("6 Auto update of date and time")
                        print("0 Exit")
                        print("Enter: ")
                        
                        if(clock == 0): break
                        match(clock):
                            case 1 -> print("Alarm clock")
                            case 2 -> print("Clock settings")
                            case 3 -> print("Date setting")
                            case 4 -> print("Stopwatch")
                            case 5 -> print("Countdown timer")
                            case 6 -> print("Auto update of date and time")
                            default -> print("Invalid")
                        }
                    
                case 13 -> print("Profiles")
                case 14 -> print("Services")
                case 15 -> print("SIM Services")
                default -> print("Invalid main menu")
            }
        }
    }


