from CSP.Constraint import Constraint


class Constraint11(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'black' and self.variables[0].value != 'blue':
            return True
        return False