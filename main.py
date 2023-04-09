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
        self.var1 = self.get_number()

        # get values until user press n or no
        while True:
            self.get_operation()
            if self.opt.lower() in ['n', 'no']:
                break
            self.var2 = self.get_number()

    def get_number(self):
        number = input("Enter Value : ")
        self.history.append(number)
        try:
            number = float(number)
        except ValueError:
            raise ValueError(f'Please enter number instead ({number})')
        return number

    def get_operation(self):
        self.opt = input("Enter Operation : ")
        self.history.append(self.opt)

    def addition(self):
        self.ans = self.var2 + self.var1

    def subtraction(self):
        """"""

    def multiplication(self):
        """"""

    def division(self):
        """"""

    def check_operation(self):
        if self.opt.lower() in ['add', '+', 'addition']:
            self.addition()

        elif self.opt.lower() in ['sub', '-', 'subtraction']:
            self.subtraction()

        elif self.opt.lower() in ['multi', '*', 'multiplication']:
            self.multiplication()

        elif self.opt.lower() in ['div', '/', 'division']:
            self.division()

        else:
            raise ValueError(f"Please Enter Valid Operation ({self.opt})")


calc = Calc()
calc.main()