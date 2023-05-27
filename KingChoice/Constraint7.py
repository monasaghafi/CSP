from CSP.Constraint import Constraint


class Constraint7(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'acid' and self.variables[0].value != 'healing' and self.variables[0].value != 'transform' and self.variables[0].value != 'invisible':
            return True
        return False