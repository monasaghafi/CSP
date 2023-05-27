from CSP.Constraint import Constraint


class Constraint9(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'red' and self.variables[0].value != 'black' and self.variables[0].value != 'blue' and self.variables[0].value != 'purple':
            return True
        return False

