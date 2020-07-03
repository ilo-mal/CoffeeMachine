
class CoffieMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.user_input = ''
        while self.user_input != 'exit':
            self.act()


    def buy(self):
        espresso = '1'
        latte = '2'
        cappuccino = '3'
        back = 'back'
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.user_input = input()
        if self.user_input == espresso:
            if CoffieMachine.water < 250:
                print("Sorry, not enough water!")
            elif CoffieMachine.beans < 16:
                print("Sorry, not enough beans!")
            elif CoffieMachine.cups < 1:
                print("Sorry, no cups!")
            else:
                print("I have enough resources, making you a coffee!")
                CoffieMachine.water -= 250
                CoffieMachine.beans -= 16
                CoffieMachine.money += 4
                CoffieMachine.cups -= 1

        elif self.user_input == latte:
            if CoffieMachine.water < 350:
                print("Sorry, not enough water!")
            elif CoffieMachine.milk < 75:
                print("Sorry, not enough milk!")
            elif CoffieMachine.beans < 20:
                print("Sorry, not enough beans!")
            elif CoffieMachine.cups < 1:
                print("Sorry, no cups!")
            else:
                print("I have enough resources, making you a coffee!")
                CoffieMachine.water -= 350
                CoffieMachine.milk -= 75
                CoffieMachine.beans -= 20
                CoffieMachine.money += 7
                CoffieMachine.cups -= 1

        elif self.user_input == cappuccino:
            if CoffieMachine.water < 200:
                print("Sorry, not enough water!")
            elif CoffieMachine.milk < 100:
                print("Sorry, not enough milk!")
            elif CoffieMachine.beans < 12:
                print("Sorry, not enough beans!")
            elif CoffieMachine.cups < 1:
                print("Sorry, no cups!")
            else:
                print("I have enough resources, making you a coffee!")
                CoffieMachine.water -= 200
                CoffieMachine.milk -= 100
                CoffieMachine.beans -= 12
                CoffieMachine.money += 6
                CoffieMachine.cups -= 1
        elif self.user_input == 'back':
            return

    def fill(self):
        print("Write how many ml of water do you want to add:")
        CoffieMachine.water += int(input())
        print("Write how many ml of water do you want to add:")
        CoffieMachine.milk += int(input())
        print("Write how many ml of water do you want to add:")
        CoffieMachine.beans += int(input())
        print("Write how many ml of water do you want to add:")
        CoffieMachine.cups += int(input())

    def take(self):
        if self.user_input == "take":
            print(f"I gave you ${CoffieMachine.money}")
            CoffieMachine.money = 0

    def remaining(self):
        print(f"\nThe coffee machine has:\n{CoffieMachine.water} of water\n",
          f"{CoffieMachine.milk} of milk\n{CoffieMachine.beans} of coffee beans\n",
          f"{CoffieMachine.cups} of disposable cups\n{CoffieMachine.money} of money")

    def act(self):
        self.user_input = input("Write action (buy, fill, take, remaining, exit):")
        if self.user_input == 'remaining':   # it maybe wrong , will nedd to take a look, doesn't show if chosen first, to initialize
            return CoffieMachine.remaining(self)
        elif self.user_input == 'fill':
            return CoffieMachine.fill(self)
        elif self.user_input == 'take':
            return CoffieMachine.take(self)
        elif self.user_input == 'buy':
            return CoffieMachine.buy(self)
        elif self.user_input == 'exit':
            return
        else:
            print('Wrong commend, try again.')
            return
