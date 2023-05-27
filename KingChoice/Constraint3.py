from CSP.Constraint import Constraint


class Constraint3(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'red' and self.variables[0].value != 'green':
            return True
        return False
