import copy
from note import Note

class MajorScale:
    # the pattern of half and whole steps to create the major scale from the first note
    majorIntervals = ['whole', 'whole', 'half', 'whole', 'whole', 'whole', 'half']

    # option 0: from key + interval list
    def __init__(self, args, option=0):
        if option == 0:
            self.keys = [Note(args)]
            for interval in self.majorIntervals:
                lastNote = self.keys[-1]
                newNote = copy.deepcopy(lastNote)
                if interval == 'half':
                    newNote.moveHalfStepUp()
                elif interval == 'whole':
                    newNote.moveWholeStepUp()
                else:
                    raise ValueError
                self.keys.append(newNote)

        # option 1: from parallel minor
        elif option == 1:
            self.keys = copy.deepcopy(args.keys)
            self.keys[2].moveHalfStepUp()
            self.keys[5].moveHalfStepUp()
            self.keys[6].moveHalfStepUp()

        # option 2: from relative minor
        elif option == 2:
            self.keys = copy.deepcopy(args.keys)
            self.keys = self.keys[2:] + self.keys[1:3]

    # found by flattenning the 3rd, 6th, and 7th scale degrees of the relative major
    def parallelMinor(self):
        from minorScale import MinorScale
        return MinorScale(self, 1)

    # found by starting 3 semitons below relative major
    def relativeMinor(self):
        from minorScale import MinorScale
        return MinorScale(self, 2)

    def __str__(self):
        s = ''
        for k in self.keys:
            s = s + str(k) + ' '
        return s
