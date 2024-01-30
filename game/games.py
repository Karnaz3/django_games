import random

class SPR:
    def __init__(self):
        self.vals = {
            0: "scissor",
            1: "paper",
            2: "rock"
        }
    
        self.beats = {
            "scissor":"paper",
            "paper":"rock",
            "rock":"scissor"
        }
        
    def return_random(self):
        return self.vals[random.randint(0, 2)]
    
    def check_winner(self, computer_choice, user_choice):
        if user_choice == computer_choice:
            return "draw"
    
        elif self.beats[computer_choice] == user_choice:
            return "Computer"

        elif self.beats[user_choice] == computer_choice:
            return "User"
    
        return None
        
    def execute(self, user_choice: str):
        computer_choice = self.return_random()
        user_choice = user_choice.lower()
            
        return {
            "user_choice" : user_choice,
            "computer_choice": computer_choice,
            "Winner": self.check_winner(computer_choice, user_choice)
        }
        

class HeadTails:
    def __init__(self):
        self.head_tails = {
            0:"head",
            1:'tail'
        }
    
    def return_random(self):
        return self.head_tails[random.randint(0, 1)]
    
    def execute(self):
        return self.return_random()
    

if __name__ == '__main__':
    obj = SPR()
    user_choice = "scissor"

    result = obj.execute(user_choice)
    print(result)


    head_tail_obj = HeadTails()
    print(head_tail_obj.execute())

