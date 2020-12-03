class Enviroment:
    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self):
        pass

    def resetWav(self):
        pass


class Checker:
    def __init__(self):
        self.env = Enviroment()

    def reminder(self, file):
        hour = self.env.getTime()

        if hour > 17:
            self.env.playWavFile(file)
            return self.env.wavWasPlayed()
        else:
            return self.env.resetWav()
