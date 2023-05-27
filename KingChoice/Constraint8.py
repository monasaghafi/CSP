from CSP.Constraint import Constraint


class Constraint8(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'healing':
            return True
        return False