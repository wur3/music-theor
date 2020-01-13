import copy
from note import Note

class MinorScale:

    # the pattern of half and whole steps to create the natural minor scale from the first note
    minorIntervals = ['whole', 'half', 'whole', 'whole', 'half', 'whole', 'whole']

    def __init__(self, args, option=0):
        # option 0: from key + interval list
        if option == 0:
            self.keys = [Note(args)]
            for interval in self.minorIntervals:
                lastNote = self.keys[-1]
                newNote = copy.deepcopy(lastNote)
                if interval == 'half':
                    newNote.moveHalfStepUp()
                elif interval == 'whole':
                    newNote.moveWholeStepUp()
                else:
                    raise ValueError
                self.keys.append(newNote)

        # option 1: from parallel major
        elif option == 1:
            self.keys = copy.deepcopy(args.keys)
            self.keys[2].moveHalfStepDown()
            self.keys[5].moveHalfStepDown()
            self.keys[6].moveHalfStepDown()

        # option 2: from relative major
        elif option == 2:
            self.keys = copy.deepcopy(args.keys)
            self.keys = self.keys[-3:] + self.keys[1:-2]

    # found by sharpenning the 3rd, 6th, and 7th scale degrees of the relative minor
    def parallelMajor(self):
        from majorScale import MajorScale
        return MajorScale(self, 1)

    # found by starting 3 semitons above relative minor
    def relativeMajor(self):
        from majorScale import MajorScale
        return MajorScale(self, 2)

    def __str__(self):
        s = ''
        for k in self.keys:
            s = s + str(k) + ' '
        return s
