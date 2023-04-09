class Calc:
    def __init__(self):
        self.var1 = None
        self.var2 = None
        self.opt = None
        self.ans = None
        self.history = []

    def main(self):
        print("Which operation would you like to do?\n "
              "For Addition type Add\n"
              "For Subscription type Sub\n"
              "For Multiplication type Multi\n"
              "For Division type Div\n"
              "For Break the Calculation type N")

calc = Calc()
calc.main()