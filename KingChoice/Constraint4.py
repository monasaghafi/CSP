from CSP.Constraint import Constraint


class Constraint4(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value != 'acid':
            return True
        return False
