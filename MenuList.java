import java.util.Scanner;

public class MenuList {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("1. Phone book");
        System.out.println("2. Messages");
        System.out.println("3. Chat");
        System.out.println("4. Call register");
        System.out.println("5. Tones");
        System.out.println("6. Settings");
        System.out.println("7. Call divert");
        System.out.println("8. Music");
        System.out.println("9. Games");
        System.out.println("10. Calculator");
        System.out.println("11. Reminders");
        System.out.println("12. Clock");
        System.out.println("13. Profiles");
        System.out.println("14. WAP Services");
        System.out.println("15. SIM Services");

        System.out.print("Enter main menu: ");
        int mainMenu = input.nextInt();

        switch(mainMenu) {
            case 1 -> {
                System.out.println("Phone book:");
                System.out.println("1 Search");
                System.out.println("2 Service Nos.");
                System.out.println("3 Add name");
                System.out.println("4 Erase");
                System.out.println("5 Edit");
                System.out.println("6 Assign tone");
                System.out.println("7 Send b card");
                System.out.println("8 Options");
                System.out.println("9 Speed dials");
                System.out.println("10 Voice tags");
                System.out.print("Enter: ");
                int phonebookoptions = input.nextInt();
                switch(phonebookoptions) {
                    case 1 -> System.out.println("Search");
                    case 2 -> System.out.println("Service Nos.");
                    case 3 -> System.out.println("Add name");
                    case 4 -> System.out.println("Erase");
                    case 5 -> System.out.println("Edit");
                    case 6 -> System.out.println("Assign tone");
                    case 7 -> System.out.println("Send b card");
                    case 8 -> {
                        System.out.println("1 Type of view");
                        System.out.println("2 Memory status");
                        System.out.print("Enter: ");
                        int options = input.nextInt();
                        switch(options) {
                            case 1 -> System.out.println("Type of view");
                            case 2 -> System.out.println("Memory status");
                        }
                    }
                    case 9 -> System.out.println("Speed dials");
                    case 10 -> System.out.println("Voice tags");
                }
            }
            case 2 -> {
                System.out.println("Messages:");
                System.out.println("1 Write messages");
                System.out.println("2 Inbox");
                System.out.println("3 Outbox");
                System.out.println("4 Picture messages");
                System.out.println("5 Templates");
                System.out.println("6 Smileys");
                System.out.println("7 Message settings");
                System.out.println("8 Info service");
                System.out.println("9 Voice mailbox number");
                System.out.println("10 Service command editor");
                System.out.print("Enter: ");
                int messages = input.nextInt();
                switch(messages) {
                    case 1 -> System.out.println("Write messages");
                    case 2 -> System.out.println("Inbox");
                    case 3 -> System.out.println("Outbox");
                    case 4 -> System.out.println("Picture messages");
                    case 5 -> System.out.println("Templates");
                    case 6 -> System.out.println("Smileys");
                    case 7 -> {
                        System.out.println("1 Set 1");
                        System.out.println("2 Common");
                        int set1 = input.nextInt();
                        switch(set1) {
                            case 1 -> {
                                System.out.println("1 Message centre number");
                                System.out.println("2 Messages sent as");
                                System.out.println("3 Message validity");
                            }
                            case 2 -> {
                                System.out.println("1 Delivery reports");
                                System.out.println("2 Reply via same centre");
                                System.out.println("3 Character support");
                            }
                        }
                    }
                    case 8 -> System.out.println("Info service");
                    case 9 -> System.out.println("Voice mailbox number");
                    case 10 -> System.out.println("Service command editor");
                }
            }
            case 3 -> System.out.println("Chat");
            case 4 -> {
                System.out.println("Call register:");
                System.out.println("1 Missed calls");
                System.out.println("2 Received calls");
                System.out.println("3 Dialled numbers");
                System.out.println("4 Erase recent call lists");
                System.out.println("5 Show call duration");
                System.out.println("6 Show call costs");
                System.out.println("7 Call cost settings");
                System.out.println("8 Prepaid credit");
                System.out.print("Enter: ");
                int callregister = input.nextInt();
                switch(callregister) {
                    case 1 -> System.out.println("Missed calls");
                    case 2 -> System.out.println("Received calls");
                    case 3 -> System.out.println("Dialled numbers");
                    case 4 -> System.out.println("Erase recent call lists");
                    case 5 -> {
                        System.out.println("1 Last call duration");
                        System.out.println("2 All calls duration");
                        System.out.println("3 Received calls duration");
                        System.out.println("4 Dialled calls duration");
                        System.out.println("5 Clear timers");
                        int callduration = input.nextInt();
                        switch(callduration) {
                            case 1 -> System.out.println("Last call duration");
                            case 2 -> System.out.println("All calls duration");
                            case 3 -> System.out.println("Received calls duration");
                            case 4 -> System.out.println("Dialled calls duration");
                            case 5 -> System.out.println("Clear timers");
                               }
                        }
                    case 6 -> { 
                        System.out.println("1 Last call cost");
                        System.out.println("2 All calls’ cost");
                        System.out.println("3 Clear counters");
                        int showcallcost = input.nextInt();
                        switch(showcallcost ){
                            case 1 -> System.out.println("Last call cost");
                            case 2 -> System.out.println("All calls’ cost");
                            case 3 -> System.out.println("Clear counters");
                            }
                        }
                    case 7 -> {
                        System.out.println("1 Call cost settings");
                        System.out.println("2 Show cost limit");
                        int callcostsettings = input.nextInt();
                        switch(callcostsettings){
                            case 1 -> System.out.println("Call cost settings");
                            case 2 -> System.out.println("Show cost limit");
                        }
                    }
                 case 8 -> System.out.println("Prepaid credit");
                }
            }
            case 5 -> {
                System.out.println("Tones:");
                System.out.println("1 Ringing tone");
                System.out.println("2 Ringing volume");
                System.out.println("3 Incoming call alert");
                System.out.println("4 Composer");
                System.out.println("5 Message alert tone");
                System.out.println("6 Keypad tones");
                System.out.println("7 Warning and game tones");
                System.out.println("8 Vibrating alert");
                System.out.println("9 Screen saver");
            }
            case 6 -> {
                System.out.println("Settings:");
                System.out.println("1 Call settings");
                System.out.println("2 Phone settings");
                System.out.println("3 Security settings");
                System.out.println("4 Restore factory settings");
                System.out.print("Enter: ");
                int settings = input.nextInt();
                switch(settings) {
                    case 1 -> {
                        System.out.println("1 Automatic redial");
                        System.out.println("2 Speed dialling");
                        System.out.println("3 Call waiting options");
                        System.out.println("4 Own number sending");
                        System.out.println("5 Phone line in use");
                        System.out.println("6 Automatic answer");
                    }
                    case 2 -> {
                        System.out.println("1 Language");
                        System.out.println("2 Cell info display");
                        System.out.println("3 Welcome note");
                        System.out.println("4 Network selection");
                        System.out.println("5 Lights");
                        System.out.println("6 Confirm SIM service actions");
                    }
                    case 3 -> {
                        System.out.println("1 PIN code request");
                        System.out.println("2 Call barring service");
                        System.out.println("3 Fixed dialling");
                        System.out.println("4 Closed user group");
                        System.out.println("5 Phone security");
                        System.out.println("6 Change access codes");
                    }
                    case 4 -> System.out.println("Restore factory settings");
                }
            }
            case 7 -> System.out.println("Call divert");
            case 8 -> {
                System.out.println("Music:");
                System.out.println("1 Music player");
                System.out.println("2 Radio");
                System.out.println("3 Recorder");
                System.out.println("4 Track list");
                System.out.print("Enter: ");
                int music = input.nextInt();
                switch(music) {
                    case 1 -> System.out.println("Music player");
                    case 2 -> System.out.println("Radio");
                    case 3 -> System.out.println("Recorder");
                    case 4 -> System.out.println("Track list");
                }
            }
            case 9 -> System.out.println("Games:");
            case 10 -> System.out.println("Calculator:");
                
            case 11 -> System.out.println("Reminders");
            case 12 -> {
                System.out.println("Clock:");
                System.out.println("1 Alarm clock");
                System.out.println("2 Clock settings");
                System.out.println("3 Date setting");
                System.out.println("4 Stopwatch");
                System.out.println("5 Countdown timer");
                System.out.println("6 Auto update of date and time");
            }
            case 13 -> System.out.println("Profiles:");
            case 14 -> System.out.println("Services");
            case 15 -> System.out.println("SIM Services");
        }
    }
}
