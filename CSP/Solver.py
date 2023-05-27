import os
import subprocess
import time
from collections import deque
from copy import deepcopy
from typing import Optional

from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:

    def __init__(self, problem: Problem, use_mrv=False, use_lcv=False, use_forward_check=False):
        self.problem = problem
        self.use_lcv = use_lcv
        self.use_mrv = use_mrv
        self.use_forward_check = use_forward_check

    def is_finished(self) -> bool:
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        self.problem.calculate_neighbors()
        start = time.time()
        for var in self.problem.variables:
            if not self.forward_check(var):
                print("Problem Unsolvable")
                return
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')

    def backtracking(self):
        if self.is_finished():
            return True
        unassigned = self.problem.get_unassigned_variables()
        var = self.select_unassigned_variable()
        original_domain = var.domain.copy()
        ordered_values = self.order_domain_values(var)
        for value in ordered_values:
            var.value = value
            if self.forward_check(var):
                result = self.backtracking()
                if result:
                    return True
            var.value = None
            var.domain = original_domain
        return False

    def forward_check(self, var):
        constraints = self.problem.get_neighbor_constraints(var)
        for constraint in constraints:
            if not constraint.is_satisfied():
                return False
        if self.use_forward_check:
            for neighbor in var.neighbors:
                if neighbor.has_value:
                    continue
                neighbor.domain = [x for x in neighbor.domain if constraint.is_satisfied()]
                if len(neighbor.domain) == 0:
                    return False
        return True

    def select_unassigned_variable(self) -> Optional[Variable]:
        if self.use_mrv:
            return self.mrv()
        unassigned_variables = self.problem.get_unassigned_variables()
        return unassigned_variables[0] if unassigned_variables else None

    def order_domain_values(self, var: Variable):
        if self.use_lcv:
            return self.lcv(var)
        return var.domain

    def mrv(self) -> Optional[Variable]:
        unassigned = self.problem.get_unassigned_variables()
        if not unassigned:
            return None
        mrv = unassigned[0]
        for var in unassigned:
            if len(var.domain) < len(mrv.domain):
                mrv = var
        return mrv

    def is_consistent(self, var: Variable):
        # Write your code here
        return all(constraint.is_satisfied() for constraint in self.problem.constraints if var in constraint.variables)

    def lcv(self, var):
        domain_values = var.domain
        constraints = self.problem.get_neighbor_constraints(var)
        conflicts_count = {}
        for value in domain_values:
            var.value = value
            conflicts_count[value] = 0
            for constraint in constraints:
                if not constraint.is_satisfied():
                    conflicts_count[value] += 1
            var.value = None
        ordered_values = sorted(domain_values, key=lambda value: conflicts_count[value])
        return ordered_values
