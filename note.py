class Note:
    notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

    def __init__(self, note):
        self.index = self.notes.index(note)

    def moveHalfStepUp(self):
        self.index = (self.index + 1) % len(self.notes)

    def moveWholeStepUp(self):
        self.moveHalfStepUp()
        self.moveHalfStepUp()

    def __repr__(self):
        return '%s' % (self.notes[self.index])

    def __str__(self):
        return self.__repr__()
