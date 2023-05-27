from CSP.Constraint import Constraint


class Constraint2(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'acid' and self.variables[0].value != 'healing' and self.variables[0].value != 'poison' and self.variables[0].value != 'invisible':
        # if self.variables[0].value == 'transform':
            return True
        return False