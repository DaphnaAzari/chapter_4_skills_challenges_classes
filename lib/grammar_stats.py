class GrammarStats:
    def __init__(self):
        self.good_grammar = 0
        self.bad_grammar = 0
        
        
    def check(self, text):
        if text == "":
            raise Exception("Can't check the grammar of an empty string.")
        elif not isinstance(text,str):
            raise Exception("Input must be a string of text!")
        elif text[0].isupper() and text[-1] in ".!?":
            self.good_grammar += 1
            return True
        else:
            self.bad_grammar += 1
            return False

    def percentage_good(self):
        if self.good_grammar == 0 and self.bad_grammar ==0:
            raise Exception("No texts have been validated!")
        return self.good_grammar / (self.good_grammar + self.bad_grammar) * 100
        
