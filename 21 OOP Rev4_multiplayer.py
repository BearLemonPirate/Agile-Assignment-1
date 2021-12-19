"""
Pontoon/blackjack game for Programming fundamentals
Ben Lyon, UP2038975, 16/01/2020
"""



######## importing external libs ########
import random
import time



######## declare classes and methods ########
class Card():
    """
    a class to represent a card
    takes arguments to build a card from the deck class' build method
    can return a readable string to define each card (used for printing to screen)
    """

    def __init__(self, face_data, suit_data, face_data_index):
        """
        reads arguments in __init__ from deck building method to create cards
        ace_set is set to false, and when dealt will trigger user_input which will change the value and update ace_set to true
        """

        #values for each of the cards (at default)
        card_weight_arr = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        10,
        10,
        10]

        #set the face of the card to the face_data argument
        self.face = face_data
        #set the suit of the card to the suit_data argument
        self.suit = suit_data
        #finds the corrisponding card weight from an array for the card, based on the findex of the card face in the deck build process
        self.weight = card_weight_arr[face_data_index]
        #sets ace_set value to false so ace cards that havent been modified can trigger a user input on deal function
        self.ace_set = False

    def __str__(self):
        """
        Returns a string used for printing the card in a readable format
        """
        #returns a string in the form "face of suit"
        return (self.face +" of " +self.suit)



class Deck():
    """
    class to represent a deck
    creates 52 cards in an array by calling on the card class
    has a build, shuffle, and deal function
    """

    def __init__(self):
        """
        creates array for deck and calls build method
        """

        #creates an array for the deck called order
        self.order = []
        #initiates the method for building the deck
        self.Build_deck()

    def Build_deck(self):
        """
        Builds a deck of instances of the card class using arrays
        """

        #suits for generating cards
        card_suits_arr = ["Clubs", "Diamonds", "Hearts", "Spades"]

        #full card faces
        card_face_arr = [
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "King",
        "Queen"]

        print("Building the deck")
        print("")
        time.sleep(2)

        #nested for loops that generate arguments for cards
        for x in card_face_arr:
            for y in card_suits_arr:
                z = Card(x, y, card_face_arr.index(x))
                self.order.append(z)

        print("Finished building the deck")
        print("")
        time.sleep(1)
    
    def Shuffle_deck(self):
        """
        Shuffles the deck into a random order using the random lib
        """

        #shuffles the deck
        random.shuffle(self.order)

        print("Shuffled the deck")
        print("")
        time.sleep(1)

    def Deal(self, player):
        """
        Takes a player as an argument and deals a card to that players hand
        checks for human player and follows seperate tree with print statements and without autologic
        checks if card is an ace and has not been set yet
        """
        dealing_card = self.order[0]

        #deal tree for the human player
        if player.is_human == True:

            #print statments for the human player
            print("You have been dealt the " +dealing_card.__str__() +"!")
            print("")
            time.sleep(1)

            #if card is an ace and hasnt been set, ask the player for their choice of 1 or 11
            if (dealing_card.face == "Ace") and (dealing_card.ace_set == False):
                deal_ace_input = input ("Please choose if you would like your Ace to be worth 1 or 11? ")
                deal_ace_input = int(deal_ace_input)
                print("")
                time.sleep(2)

                #while the input is invalid, ask for them to choose again
                while (deal_ace_input != 1) and (deal_ace_input != 11) == True:
                    print("ERROR:  Value is not 1 or 11")
                    deal_ace_input = input ("Please type the integers 1 or 11 for your Ace card: ")
                    print("")
                    time.sleep(2)

                #when the value is valid, set worth to that value and set ace_set to true
                dealing_card.weight = deal_ace_input
                dealing_card.ace_set = True

            #if not an ace, skip any ace functions and deal as normal
            else:
                pass

            #adds card to players hand and removes it from
            player.hand.append(dealing_card)
            self.order.remove(dealing_card)

            #if more than 1 card in your hand it will print your hand
            if len(player.hand) > 1:

                #for loop to print every card in hand
                print("Your hand now contains...")
                for x in player.hand:
                    print("    " +x.__str__())
                print("")
                time.sleep(1)

                #recalculates players hand and dusplays value
                player.Calc_hand_val()
                print("These cards are worth " +str(player.hand_val))
                print("")
                time.sleep(2)
            
            else:
                pass

        #deal tree for all computer players
        else:

            #print functions for when computer plays
            print("A card has been dealt to an opponent!")
            print("")
            time.sleep(1)

            #if card is an ace and hasnt been set, decide on value using hand value
            if (dealing_card.face == "Ace") and (dealing_card.ace_set == False):
                if player.hand_val <= 10:
                    dealing_card.weight = 11
                else:
                    dealing_card.weight = 1
            else:
                pass

            #adds card to players hand and removes it from
            player.hand.append(dealing_card)
            self.order.remove(dealing_card)



class Player():
    """
    a class to represent a player and their hand
    has a hand, hand value variable, can_play bool(default False), and is_human bool(default False)
    will have the method for calculating the hand value
    """

    def __init__(self):
        """
        initiates all variables for a player class
        has hand array and a hand_val int
        """
        self.hand = []
        self.hand_val = 0
        self.can_play = False
        self.is_human = False
    
    def Calc_hand_val(self):
        """
        function used to recalculate the hand value before operations to ensure accuracy
        """
        self.hand_val = 0
        for x in self.hand:
            self.hand_val = self.hand_val + x.weight



######## functions to run the game logic ########


def bust_check(player):
    """
    Takes a player as an argument
    checks their hand to see if it is bust (true when worth > 21)
    if bust, sets can_play value to false
    runs once per round
    """

    #recalculates the players hand
    player.Calc_hand_val()

    #if the players hand value is low enough, nothing happens
    if player.hand_val <= 21:
        pass
    
    else:
        #if hand value is too high, sets can_play to false
        player.can_play = False

        #if a human player, print a message saying youve gone bust
        if player.is_human == True:
            print("Your card value is too high!")
            print("You've gone bust")
            print("")
            time.sleep(1)
        
        #if a computer player, print saying a player is bust
        else:
            print("A player has declared themselves bust!")
            print("")
            time.sleep(1)



def play_game():
    """
    calls all variables into play to generate/reset them for new games
    has player list and active player list for running rounds on valid players
    while more than one player is not busted, calls the play round function
    when no players are still able to play, goes to the scoring function
    """

    #welcome messages on launching the game
    print("Setting up new game...")
    print("")
    time.sleep(2)

    #generates the player roster, all inactive by default, and sets the first one to human
    arr_player_list = []
    for x in range(5):
        y = Player()
        arr_player_list.append(y)
    arr_player_list[0].is_human = True

    #generates deck for the game
    new_deck = Deck()
    new_deck.Shuffle_deck()

    #inital deal function
    for x in arr_player_list:
        if x.can_play == True:
            new_deck.Deal(x)
        else:
            pass

##############################################################################

    #asks for computer player input and generates players
    ai_count = input("Please state the number of AI opponents you would like to face: (min = 0, max = 4) ")
    ai_count = int(ai_count)
    print("")
    time.sleep(2)

    #if input isnt valid, asks player again
    while (ai_count < 0) or (ai_count > 4):
        print("ERROR:  Value is not 0, 1, 2, 3, or 4")
        ai_count = input("Please enter a valid number of computer opponents: ")
        print("")
        time.sleep(1)
    
    #print statments for valid ai_count entries
    print("Input received")
    print("Building incredibly complex AI opponents...")
    print("")
    time.sleep(1)

    #uses computer player input to set that many players to active, plus 1 more for the human to play as
    for x in range(ai_count+1):
        arr_player_list[x].can_play = True

##############################################################################

    #round loop as long as at least 1 player is active
    while game_over(arr_player_list) > 0:
        play_round(arr_player_list, new_deck)
    
    #when no players are active calls the scoring function to end the game
    print("No player has any legal moves remaining")
    print("")
    time.sleep(1)

    #scoring function
    scoring_endgame(arr_player_list, ai_count)



def play_round(roster, playing_deck):
    """
    game logic for playing 1 round
    deals a card to all available players
    calculates bust players
    all available players get option to play or stay (show hand val for human_player)
    players who play their hand have can_play set to false
    players who stay pass though and will be active on the next call of the function
    """

    print("##################################################################################")
    print("")
    time.sleep(1)

    #deals a card to all available players and checks for bust
    for x in roster:
        if x.can_play == True:
            playing_deck.Deal(x)
            bust_check(x)
        else:
            pass
    
    #option to stick or twist for each player
    for x in roster:

        #filters out unavailable players
        if x.can_play == True:

            #if player is the human player, give them a different tree
            if x.is_human == True:

                #if hand value is to low you have to stay 
                if x.hand_val < 17:
                    print("Due to low hand value, you must stay another round!")
                    print("")
                    time.sleep(2)

                #if hand value is high enough you can make a choice
                else:

                    #input for stick or twist
                    stay_or_play = input("Please state whether you would like to play your hand or stay: ")
                    print("")
                    time.sleep(1)

                    #while input is invalid, cannot continue
                    while (stay_or_play != "play") and (stay_or_play != "stay"):
                        print("ERROR:  input is not 'play' or 'stay'!")
                        stay_or_play = input("Please state whether you would like to play your hand or stay: ")
                        print("")
                        time.sleep(1)
                    
                    #if player chose to play
                    if stay_or_play == "play":
                        x.can_play = False
                        print("You have played your hand with " +str(x.hand_val) +" points!")
                        print("Please wait for all other players to finsih")
                        print("")
                        time.sleep(2)
  
                    #if player chose to stay
                    else:
                        print("You have chosen to stay another round!")
                        print("")
                        time.sleep(2)

            #if not human get a logic tree that decides the best outcome
            else:

                #if hand value is to low you have to stay
                if x.hand_val < 17:
                    print("a player has been forced to stay!")
                    print("")
                    time.sleep(1)

                #if score is nearly there, play it
                elif x.hand_val == 20 or x.hand_val == 21:
                    print("A player plays their hand")
                    print("")
                    time.sleep(1)
                    x.can_play = False
                
                #if score is in the middle of the pack, generate a slight randomiser to the decision to stay or play
                else:
                    #get random adapter value to add to the hand value
                    randomiser_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -1, 2, -2]
                    #(62.5% chance for 0 // 12.5% chance for +1 // 12.5% chance for -1 // 6.25% chance for +2 // 6.25% chance for -2)
                    random.shuffle(randomiser_array)
                    randomiser = randomiser_array[0]

                    #make a variable based on teh hand value with the random bias
                    decision_val = x.hand_val + randomiser

                    #if biassed value is less than or equal to 18, stay another round
                    if decision_val <= 18:
                        print("a player has chosen to stay!")
                        print("")
                        time.sleep(1)
                    
                    #if biassed value is too high play the hand
                    else:
                        print("A player plays their hand")
                        print("")
                        time.sleep(1)
                        x.can_play = False

        #options for non available players       
        else:

            #pass through for players who are not available for play
            pass



def game_over(player_list):
    """
    checks all active players and returns an int for number of remaining players
    """

    #creates variable for available players
    available_players = 0

    #adds 1 to the variable for every player whos can_play bool is true
    for x in player_list:
        if x.can_play == True:
            available_players = available_players + 1

        else:
            pass

    #returns the number of available players
    return available_players



def scoring_endgame(player_list, comp_player_count):
    """
    calculates winner and scores from all players
    uses ai count from game start up to only count players who have been active
    asks to play again after scores have been displayed
    playing again will pass into final while loop, not playing again will cause sleep and then exit program
    """

    #game over print
    print("The game is over!!!")
    time.sleep(1)
    print("Lets see how everyone did...")
    print("")
    time.sleep(1)

    #set up number of players (computer count + 1)
    active_player_count = comp_player_count + 1
    #setup array as a leaderboard, which will add players in order of score and win-type
    leaderboard_array = []
    #sets counters for different types of scores
    royal_flush_count = 0
    pontoon_count = 0
    blackjack_count = 0
    points_score_count = 0
    busted_count = 0

    """
    points tier system:
    21 in 5 cards is 5 royal flush
    21 in 2 cards is pontoon
    21 in 3 or 4 cards is blackjack
    < 21 points are worth their val
    > 21 points are bust
    """

##############################################################################

    #royal flush check
    for x in range(active_player_count):
        if (player_list[x].hand_val == 21) and (len(player_list[x].hand) == 5):
            leaderboard_array.append(player_list[x])
            royal_flush_count = royal_flush_count + 1
        else:
            pass

    #pontoon check
    for x in range(active_player_count):
        if (player_list[x].hand_val == 21) and (len(player_list[x].hand) == 2):
            leaderboard_array.append(player_list[x])
            pontoon_count = pontoon_count + 1
        else:
            pass

    #blackjack check
    for x in range(active_player_count):
        if (player_list[x].hand_val == 21) and (len(player_list[x].hand) == (2 or 3)):
            leaderboard_array.append(player_list[x])
            blackjack_count = blackjack_count + 1
        else:
            pass

    #points check
    for x in range(active_player_count):
        if player_list[x].hand_val < 21:
            leaderboard_array.append(player_list[x])
            points_score_count = points_score_count + 1
        else:
            pass

    #busted check
    for x in range(active_player_count):
        if player_list[x].hand_val > 21:
            leaderboard_array.append(player_list[x])
            busted_count = busted_count + 1
        else:
            pass
    
    #find human_player position
    for x in leaderboard_array:
        if x.is_human == True:
            human_player_pos = leaderboard_array.index(x) + 1
        else:
            pass

##############################################################################

    print("##################################################################################")
    print("")

    #print human player position followed by special scores
    print("You came in position " +str(human_player_pos) +"!!!")
    print("")
    time.sleep(1)

    print("##################################################################################")
    print("")

    #Leaderboard print out
    for x in leaderboard_array:
        print("Position " +str(leaderboard_array.index(x) + 1) +" got a final card total of " +str(x.hand_val))
    print("")
    time.sleep(2)

    print("##################################################################################")
    print("")

    #print number of players with a royal flush
    print(str(royal_flush_count) +" players got a royal flush this game!")
    print("")
    time.sleep(1)

    #print number of players with a pontoon
    print(str(pontoon_count) +" players got a pontoon this game!")
    print("")
    time.sleep(1)

    #print number of players with a blackjack score
    print(str(blackjack_count) +" players got a blackjack score this game!")
    print("")
    time.sleep(1)

    #print number of players who scored points
    print(str(points_score_count) +" players scored points this game!")
    print("")
    time.sleep(1)

    #print number of players who went bust
    print(str(busted_count) +" players went bust this game!")
    print("")
    time.sleep(1)

##############################################################################

    #asks if the user would like to play again
    play_again = input("Would you like to play again?  yes or no? ")
    print("")
    time.sleep(1)

    #while invalid, asks for input again
    while (play_again != "yes") and (play_again != "no"):
        print("ERROR: Input invalid")
        play_again = input("""Please enter "yes" or "no" """)
        print("")
        print("")
        time.sleep(1)
    
    if play_again == "yes":
        print("Excellent, setting up a new game shortly...")
        print("")
        time.sleep(1)
    
    else:
        print("Thank you for playing!")
        print("Exitting program...")
        time.sleep(3)
        exit()

##############################################################################

#welcome messages on launching the game
print("")

print("Welcome to the classic card game 21!!!")
print("")
time.sleep(1)

print("##################################################################################")
print("")

print("Please read the rules while we get the game ready...")
print("")
print("HOW TO PLAY:")
print("Every turn all players will be dealt a card")
print("The goal is to get your card total as close to 21 as possible, but not over")
print("Certain combos are worth more, such as 21 in 2 cards, or 21 in 5 cards")
print("Aces can be worth either 1 or 11, you decide...but choose wisely")
print("If you meet the minimum hand value, you can choose to play your hand, or stay another turn in every round")
print("You'll have to risk playing too low, or waiting too long and going bust with too many cards")
print("Good luck and have fun!")
print("")

print("##################################################################################")
print("")

time.sleep(5)
#final while loop that plays the game for as long as the prgram is running
while True:
    play_game()