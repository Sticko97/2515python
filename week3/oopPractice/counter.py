class Countdown:
    def __init__(self, start, step=1):
        self.current = start
        self.step = step
        if self.current <= 0:
            self.complete = True
        else:
            self.complete = False
        # self.check_for_current_value() #no need just used to check

    def down(self):
        self.current -= self.step
        # self.check_for_current_value() #no need just used to check

        """check_for_current_value was used to check
        """
    # def check_for_current_value(self):
    #     if self.current <= 0:
    #         self.complete = True
    #     else:
    #         self.complete = False
        # return self.current
    
    def complete(self):
        if self.current <= 0:
            return True
        else:
            return False