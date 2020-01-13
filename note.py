class Note:
    notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    # TODO: implement a flat version
    # notes = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

    def __init__(self, note):
        self.index = self.notes.index(note)

    def moveHalfStepUp(self):
        self.index = (self.index + 1) % len(self.notes)

    def moveWholeStepUp(self):
        self.moveHalfStepUp()
        self.moveHalfStepUp()

    def moveHalfStepDown(self):
        self.index = (self.index - 1) % len(self.notes)

    def __str__(self):
        return self.notes[self.index]
