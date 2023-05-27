from CSP.Constraint import Constraint


class Constraint6(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'purple' and self.variables[0].value != 'black':
            return True
        return False