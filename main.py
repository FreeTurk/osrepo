print("Checking for updates...")


print("                                                                                                                  ")
print("                                                                                                                  ")
print("     OOOOOOOOO        SSSSSSSSSSSSSSS                                                                             ")
print("   OO:::::::::OO    SS:::::::::::::::S                                                                            ")
print(" OO:::::::::::::OO S:::::SSSSSS::::::S                                                                            ")
print("O:::::::OOO:::::::OS:::::S     SSSSSSS                                                                            ")
print("O::::::O   O::::::OS:::::S           rrrrr   rrrrrrrrr       eeeeeeeeeeee    ppppp   ppppppppp      ooooooooooo   ")
print("O:::::O     O:::::OS:::::S           r::::rrr:::::::::r    ee::::::::::::ee  p::::ppp:::::::::p   oo:::::::::::oo ")
print("O:::::O     O:::::O S::::SSSS        r:::::::::::::::::r  e::::::eeeee:::::eep:::::::::::::::::p o:::::::::::::::o")
print("O:::::O     O:::::O  SS::::::SSSSS   rr::::::rrrrr::::::re::::::e     e:::::epp::::::ppppp::::::po:::::ooooo:::::o")
print("O:::::O     O:::::O    SSS::::::::SS  r:::::r     r:::::re:::::::eeeee::::::e p:::::p     p:::::po::::o     o::::o")
print("O:::::O     O:::::O       SSSSSS::::S r:::::r     rrrrrrre:::::::::::::::::e  p:::::p     p:::::po::::o     o::::o")
print("O:::::O     O:::::O            S:::::Sr:::::r            e::::::eeeeeeeeeee   p:::::p     p:::::po::::o     o::::o")
print("O::::::O   O::::::O            S:::::Sr:::::r            e:::::::e            p:::::p    p::::::po::::o     o::::o")
print("O:::::::OOO:::::::OSSSSSSS     S:::::Sr:::::r            e::::::::e           p:::::ppppp:::::::po:::::ooooo:::::o")
print(" OO:::::::::::::OO S::::::SSSSSS:::::Sr:::::r             e::::::::eeeeeeee   p::::::::::::::::p o:::::::::::::::o")
print("   OO:::::::::OO   S:::::::::::::::SS r:::::r              ee:::::::::::::e   p::::::::::::::pp   oo:::::::::::oo ")
print("     OOOOOOOOO      SSSSSSSSSSSSSSS   rrrrrrr                eeeeeeeeeeeeee   p::::::pppppppp       ooooooooooo   ")
print("                                                                              p:::::p                             ")
print("                                                                              p:::::p                             ")
print("                                                                             p:::::::p                            ")
print("                                                                             p:::::::p                            ")
print("                                                                             p:::::::p                            ")
print("                                                                             ppppppppp                            ")
print("                                                                                                                  ")



print("WELCOME TO THE BIGGEST REPO OF OPERATING SYSTEMS!")
print("HERE, YOU WILL FIND A GREAT SELECTION OF OPERATING SYSTEMS, ALL HAND PICKED!")
print("This is a dumb project, made by the priceless efforts of FreeTurk")
print("")

print("Throughout this script, you will be presented with a series of options.")
print("Select accordingly, you have to know the category if you want the OS.")
print("")

print("Now, please select the type of your OS from the options of (Just write the number): ")
print("1. *nix")
print("2. WindowsNT")
print("3. WindowsDOS")
print("4. Apple")
print("5. Legendary/Others")
os_type = input()

if os_type == "2":
    print("PLease Wait...")
    import winnt

elif os_type == "3":
    print("Please Wait...")
    import windos

elif os_type == "5":
    print("Please Wait...")
    import others


elif os_type == "1":
    print("Select from below options")
    print("Linux")
    print("Unix")
    print("BSD")
    nix_type = input()
    if nix_type == "Linux":
        import linux
    elif nix_type == "Unix":
        import unix
    elif nix_type == "BSD":
        import bsd

elif os_type == "4":
    print("Please Wait...")
    import apple