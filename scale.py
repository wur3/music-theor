import copy
from note import Note
from abc import ABC, abstractmethod

class Scale(ABC):

    def __init__(self):
        pass

    def option0(self, args, intervals):
        self.keys = [Note(args)]
        for interval in intervals:
            lastNote = self.keys[-1]
            newNote = copy.deepcopy(lastNote)
            if interval == 'half':
                newNote.moveHalfStepUp()
            elif interval == 'whole':
                newNote.moveWholeStepUp()
            else:
                raise ValueError
            self.keys.append(newNote)

    def __str__(self):
        s = ''
        for k in self.keys:
            s = s + str(k) + ' '
        return s
