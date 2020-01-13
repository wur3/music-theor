import copy
from note import Note

class MajorScale:
    # the pattern of half and whole steps from a note to create the major scale
    sequenceOfIntervals = ['whole', 'whole', 'half', 'whole', 'whole', 'whole', 'half']

    def __init__(self, key):
        self.firstNote = Note(key)
        self.keys = []

        self.keys.append(self.firstNote)
        for interval in self.sequenceOfIntervals:
            lastNote = self.keys[-1]
            newNote = copy.deepcopy(lastNote)
            if interval is 'half':
                newNote.moveHalfStepUp()
            elif interval is 'whole':
                newNote.moveWholeStepUp()
            self.keys.append(newNote)



    def minorFromParallelMajor(self):
        pass

    def minorFromRelativeMajor(self):
        pass

    def __str__(self):
        return str(self.keys)
