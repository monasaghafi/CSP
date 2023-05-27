from CSP.Problem import Problem
from CSP.Variable import Variable
from KingChoice.KingConstraints import *


class KingChoice(Problem):
    def __init__(self):
        super().__init__([], [], "King Problem")

        color1 = Variable[str](['red', 'black', 'green', 'black', 'purple'], 'color1')
        color2 = Variable[str](['red', 'black', 'green', 'black', 'purple'], 'color2')
        color3 = Variable[str](['red', 'black', 'green', 'black', 'purple'], 'color3')
        color4 = Variable[str](['red', 'black', 'green', 'black', 'purple'], 'color4')
        color5 = Variable[str](['red', 'black', 'green', 'black', 'purple'], 'color5')
        type1 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type1')
        type2 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type2')
        type3 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type3')
        type4 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type4')
        type5 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type5')

        c00 = Const0([color1, color2, color3, color4, color5])
        c01 = Const0([type1, type2, type3, type4, type5])
        c1 = Const1([color1, type1])
        c2 = Const2([color2, type2])
        c3 = Const3([color3, type3])
        c4 = Const4([color4, type4])
        c5 = Const5([color5, type5])

        self.constraints = [c00, c01, c1, c2, c3, c4, c5]
        self.variables = [color1, color2, color3, color4, color5, type1, type2, type3, type4, type5]
