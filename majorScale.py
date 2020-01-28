import copy
from note import Note
from scale import Scale

class MajorScale(Scale):
    # the pattern of half and whole steps to create the major scale from the first note
    majorIntervals = ['whole', 'whole', 'half', 'whole', 'whole', 'whole', 'half']

    def __init__(self, args, option=0):
        # option 0: from key + interval list
        if option == 0:
            self.option0(args, self.majorIntervals)

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
