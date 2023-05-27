from CSP.Constraint import Constraint


class Constraint1(Constraint):
    def is_satisfied(self) -> bool:
        list_of_values = [x.value for x in self.variables if x.value is not None]
        return len(list_of_values) == len(set(list_of_values))
