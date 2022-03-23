from enum import Enum
import random


class Game_mode(Enum):
    BEGINNER = 8
    INTERMEDIATE = 5
    ADVANCED = 3

class Player():
    letters: list
    name: str
    word_to_guess: str
    chances: int

    def __init__(self, word_to_guess, chances, name):
        self.chances = chances
        self.word_to_guess = word_to_guess
        self.name = name
        self.letters = []

class Game:
    number_of_players: int
    
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players

    def _play(self):
        print("Game has been started with {} players".format(self.number_of_players))

class Hangman(Game):
    players: list
    game_mode: Game_mode
    
    def _create_players(self):
        self.players = []
        if(self.number_of_players == 1):
            word_list = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']
            self.players.append(Player(random.choice(word_list), self.game_mode.value, "player 1"))
        elif self.number_of_players > 1:
            for i in range(0, self.number_of_players):
                print('Enter word for player number: {}'.format(i+1))
                self.players.append(Player(input().lower(), self.game_mode.value, "player {}".format(i+1)))

    def __init__(self, number_of_players, game_mode):
        super().__init__(number_of_players)
        self.game_mode = game_mode

        self._create_players()

    def _get_actual_word(self, player):
        actual_word = ''
        for element in player.word_to_guess:
            actual_word += ('_', element)[element in player.letters]
        return actual_word


    def _play(self):
        super()._play()
        game_ended = False
        while True:
            if not self.players:
                print("All players lost their chances. Game is over!")
                break
            print("##################################################")
            for player in self.players:
                print("TURN OF {} NUMBER OF CHANCES: {}".format(player.name.upper(), player.chances))
                print(self._get_actual_word(player))

                print("Guess the letter!")
                guessed_letter = input().lower()
                if(guessed_letter in player.letters):
                    print("You already guessed this letter!")
                    player.chances -= 1
                elif(len(guessed_letter) != 1):
                    print("You can guess only one letter!")
                    player.chances -=1
                elif(guessed_letter in player.word_to_guess):
                    print("Congrats, you guessed the letter")
                    player.letters.append(guessed_letter)
                    print(self._get_actual_word(player))
                else: 
                    print("Wrong letter!")
                    player.letters.append(guessed_letter)
                    player.chances -= 1

                if player.chances == 0:
                    print("You lost all chances. Your word: {}".format(player.word_to_guess))
                    self.players.remove(player)
                elif player.word_to_guess == str(self._get_actual_word(player)):
                    print("{} won the game".format(player.name))
                    game_ended = True
                    break

            if game_ended:
                break

    

#TEST
game = Hangman(2,Game_mode.BEGINNER)
game._play()