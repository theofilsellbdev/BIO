import itertools

outside_edges = [[1,6], [1,1], [2,6], [2,1], [3,6], [3,1], [4,6], [4,1], [5,6], [5,1], [21, 4], [22, 3], [23, 4], [23, 3], [24, 4], [24, 3], [25, 4], [25, 3], [5, 2], [10, 2], [10, 3], [10, 4], [15, 2], [20, 2], [20, 3], [20, 4], [25, 2], [1, 4], [1, 5], [6, 5], [11, 4], [11, 5], [11, 6], [16, 5], [21, 6], [25, 5]]

class Bee:
    def __init__(self, colour, hop_dist):
        self.colour = colour
        if colour == 'RED':
            self.hexagon = 1
            self.facing = 1
        elif colour == 'BLUE':
            self.hexagon = 25
            self.facing = 6
        self.hop_dist = hop_dist
        self.owned = []

    def rotate(self):
        if self.colour == 'RED':
            if self.facing == 6:
                self.facing = 1
            else:
                self.facing += 1

        elif self.colour == 'BLUE':
            if self.facing == 1:
                self.facing = 6
            else:
                self.facing -= 1

    def hop(self):
        self.hexagon += self.hop_dist
        if self.hexagon > 25:
            self.hexagon -= 25

    def claim_facing(self):
        self.owned.append([self.hexagon, self.facing])

    def return_facing(self):
        return [self.hexagon, self.facing]

    def forgive_control(self, side):
        if side in self.facing:
            list(self.facing).remove(side)


def run():
    bees = []
    rnb = [9,3]
    skirmishes = 50
    fueds = 10



    print(f"{rnb[0]}, {rnb[1]}")
    print(f"{skirmishes}, {fueds}")

    bees = [Bee(colour='RED', hop_dist=rnb[0])]
    bees = [Bee(colour='BLUE', hop_dist=rnb[1])]

    for s in range(skirmishes):
        for i in range(2):
            facing = Bee(bees[i]).return_facing()
            Bee(bees[i-1]).forgive_control()
            Bee(bees[i]).claim_facing()
            Bee(bees[i]).hop()

    for f in range(fueds):
        for i in range(2):

