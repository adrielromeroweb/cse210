from game.card import Card

class Director:


    def __init__(self):

        self.card = Card()
        self.nextcard = Card()
        self.is_playing = True
        self.answer = ""
        self.score = 300


    def start_game(self):
    
        while self.is_playing:
            self.show_card()
            self.get_input()
            self.next_card()
            self.update_score()
            self.play_again()


    def show_card(self):

        if not self.is_playing:
            return

        card = self.card
        card.roll()
        print()
        print(f"The card is: {card.value}")


    def get_input(self):

        if not self.is_playing:
            return

        self.answer = input(f"Higher or lower? [h/l]: ")


    def next_card(self):

        if not self.is_playing:
            return

        next_card = self.nextcard
        next_card.roll()

        print(f"Next card was: {next_card.value}")


    def update_score(self):

        if not self.is_playing:
            return

        card = self.card
        nextcard = self.nextcard

        if (self.answer == "h") and (nextcard.value > card.value):
            self.score += 100
        elif (self.answer == "h") and (nextcard.value < card.value):
            self.score -= 75
        elif (self.answer == "l") and (nextcard.value < card.value):
            self.score += 100
        elif (self.answer == "l") and (nextcard.value > card.value):
            self.score -= 75

        if self.score < 0:
            print("Your score is: 0")
            print("Game over")
            self.is_playing = (self.score > 0)

        if self.score > 0:
            print(f"Your score is: {self.score}")

        
    def play_again(self):

        if not self.is_playing:
            return

        play = input(f"Play again? [y/n] ")
        self.is_playing = (play == "y")



        



