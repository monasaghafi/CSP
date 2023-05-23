from CSP.Constraint import Constraint

class Const0(Constraint):
    '''check if one state is not duplicated'''
    def is_satisfied(self) -> bool:
        list_of_values = [x.value for x in self.variables if x.value is not None]
        return len(list_of_values) == len(set(list_of_values))

class Const1(Constraint):
    '''0 = color , 1 = type'''
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'red' and self.variables[0].value != 'green' and self.variables[1].value != 'transform' :
            return True
        return False

class Const2(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value == 'blue' and self.variables[1].value != 'healing' and self.variables[1].value != 'acid':
            return True
        return False


class Const3(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'black' and self.variables[0].value != 'purple' and self.variables[1].value != 'poison':
            return True
        return False



class Const4(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value == 'green' and self.variables[1].value != 'poison' :
            return True
        return False

class Const5(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'black' and self.variables[0].value != 'blue' and self.variables[1].value == 'invisible' :
            return True
        return False


