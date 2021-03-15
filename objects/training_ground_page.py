class BaseElement():
    def __init__(self):
        pass

class Inputs(BaseElement):
    def __init__(self):
        pass

class TrainingGroundPage():
    def __init__(self, browser):
        self.browser = browser
        url = 'https://techstepacademy.com/training-ground'
        inputs_names = {'ipt1', 'ipt2'}
        self.inputs = Inputs(inputs_names)

    def go(self):
        pass
