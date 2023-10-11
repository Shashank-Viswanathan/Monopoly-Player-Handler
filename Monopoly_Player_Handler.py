try:
  players = True
  players_money = dict()
  players_properties = dict()
  stats = True
  #assign players 1500
  while players != "DONE":
    players = input("Player name...(type DONE for having no more)\n\t")
    if players == "DONE":
      break
    else:
      players_money[players] = 1500
      players_properties[players] = 0
  #code
  while True:
    for player in players_money:
      print("\n" + player +  " has "  + str(players_money[player]) + "\n")
      change_in_money = input("Any change in " + player + "'s money? y/n Type RENT is they are paying rent to anybody, or, Type PROPERTY if you are getting a property. If you are playing with outside of game transactions, type TRANS to do a transaction\t")
      if change_in_money.lower() == 'y':
        change = int(input('How much are you changing it by?\n'))
        players_money[player] = players_money[player] + change
        print(player + ' now has ' + str(players_money[player]))
      elif change_in_money.lower() == 'rent': #Collecting rent
        rent = input('Who are you paying rent to? Formatting: Person that is collecting rent,rent amount\t')
        rent = rent.split(',')
        players_money[player] = players_money[player] - int(rent[1])
        players_money[str(rent[0])] = players_money[str(rent[0])] + int(rent[1])
        print(player + ' now has ' + str(players_money[player]))
        print(rent[0] + ' now has ' + str(players_money[str(rent[0])]))
      elif change_in_money.lower() == "property":#Buying Properties
        properties = dict()
        properties["Medeteranean Avenue"] = 60
        properties["Baltic Avenue"] = 60
        properties["Reading Railroad"] = 200
        properties["Oriental Avenue"] = 100
        properties["Vermont Avenue"] = 100
        properties["Conneticut Avenue"] = 120
        properties["St. Charles Place"] = 140
        properties["Electric Company"] = 150
        properties["States Avenue"] = 140
        properties["Virginia Avenue"] = 160
        properties["Pennsylvania Railroad"] = 200
        properties["St. James Place"] = 180
        properties["Tennesee Avenue"] = 180
        properties["New York Avenue"] = 200
        properties["Kentucky Avenue"] = 220
        properties["Indiana Avenue"] = 220
        properties["Illinois Avenue"] = 240
        properties["B. & O. Railroad"] = 200
        properties["Atlantic Avenue"] = 260
        properties["Ventnor Avenue"] = 260
        properties["Water Works"] = 150
        properties["Marvin Gardens"] = 280
        properties["Pacific Avenue"] = 300
        properties["North Carolina Avenue"] = 300
        properties["Pennsylvania Avenue"] = 320
        properties["Short Line"] = 200
        properties["Park Place"] = 350
        properties["Boardwalk"] = 400
        #properties
        print("\nThe properties are\n" + str(properties))
        property_choice = str(input("\nWhich property number are you purchasing?\t"))
        players_properties[player] = players_properties[player] + 1
        players_money[player] = players_money[player] - properties[property_choice]
        print("\n" + player + " bought " + property_choice + "!")
      elif change_in_money.lower() == "trans":#Outside of game transactions
        print("\n Transaction formatting\n")
        print("\tProperties that the player is gaining,Money that the player is gaining,Name of the other player,Properties that the other player is gaining,Money that the other player is gaining.\n")
        transaction = input("What is the transaction? Type \"Nan\" if they are not getting anything in that category. To split multiple properties, split them with ; and no spaces. \t")
        trans_simp = transaction.split(",")
        #[2] is other player. [0,1] and [3,4] are items
        #Handling properties
        if trans_simp[0] == "Nan":
          continue
        else:
          for property_trans in trans_simp[0].split(";"):
            players_properties[player] = players_properties[player] + 1
            players_properties[trans_simp[2]] = players_properties[trans_simp[2]] - 1
        if trans_simp[3] == "Nan":
          continue
        else:
          for property_trans in trans_simp[3].split(";"):
            players_properties[player] = players_properties[player] - 1
            players_properties[trans_simp[2]] = players_properties[trans_simp[2]] + 1
        #Handling Money
        if trans_simp[1] == "Nan":
          continue
        else:
          players_properties[player] = players_properties[player] + int(trans_simp[1])
          players_properties[trans_simp[2]] = players_properties[trans_simp[2]] - int(trans_simp[1])
        if trans_simp[4] == "Nan":
          continue
        else:
          players_properties[player] = players_properties[player] - int(trans_simp[4])
          players_properties[trans_simp[2]] = players_properties[trans_simp[2]] + int(trans_simp[4])
        print("\nTransaction Complete!")
      elif change_in_money.lower() == 'n':
        continue
      print('\n' + str(players_money))
      print('\n' + str(players_properties))
except:
  print("\n\n\tAn ERROR has occured :(")
