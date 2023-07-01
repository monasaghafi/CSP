from CSP.Problem import Problem
from CSP.Variable import Variable
from KingChoice.Constraint1 import Constraint1
from KingChoice.Constraint2 import Constraint2
from KingChoice.Constraint3 import Constraint3
from KingChoice.Constraint4 import Constraint4
from KingChoice.Constraint5 import Constraint5
from KingChoice.Constraint6 import Constraint6
from KingChoice.Constraint7 import Constraint7
from KingChoice.Constraint8 import Constraint8
from KingChoice.Constraint9 import Constraint9
from KingChoice.Constraint10 import Constraint10
from KingChoice.Constraint11 import Constraint11



class KingChoice(Problem):
    def __init__(self):
        super().__init__([], [], "King Problem")

        color1 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'color1')
        color2 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'color2')
        color3 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'color3')
        color4 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'color4')
        color5 = Variable[str](['red', 'black', 'green', 'blue', 'purple'], 'color5')
        type1 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type1')
        type2 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type2')
        type3 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type3')
        type4 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type4')
        type5 = Variable[str](['acid', 'poison', 'healing', 'transform', 'invisible'], 'type5')

        c1 = Constraint1([color1, color2, color3, color4, color5])
        c2 = Constraint1([type1, type2, type3, type4, type5])
        c3 = Constraint2([type1])
        c4 = Constraint3([color1])
        c5 = Constraint4([type2])
        c6 = Constraint5([color2])
        c7 = Constraint6([color3])
        c8 = Constraint7([type3])
        c9 = Constraint8([type4])
        c10 = Constraint9([color4])
        c11 = Constraint10([type5])
        c12 = Constraint11([color5])

        self.constraints = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
        self.variables = [color1, color2, color3, color4, color5, type1, type2, type3, type4, type5]
