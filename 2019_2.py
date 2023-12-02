#%%
import numpy as np

import utilities.helper_functions as utils

input_lst, input_str = utils.aoc_input_fetch(day=2, year=2019)
print(input_lst)
#%% Parsing
input = list(map(int, input_str.split(',')))
test_input = [1,9,10,3,2,3,11,0,99,30,40,50]
#%% Part 1
class Intcode:
    def __init__(self, code):
        self.code_initial = code.copy()
        self.code = code.copy()
        self.position = 0
        self.action = self.code[self.position]
        self.terminator = 99
        self.output = self.code[0]

    def get_pointers(self):
        idx_1 = self.code[self.position + 1]
        idx_2 = self.code[self.position + 2]
        idx_res = self.code[self.position + 3]
        # print("Indicies:",idx_1, idx_2, idx_res)
        return idx_1, idx_2, idx_res

    def add_code(self):
        idx_1, idx_2, idx_res = self.get_pointers()
        # print(f"{self.code[idx_1]} + {self.code[idx_2]} = {self.code[idx_1] + self.code[idx_2]}->{idx_res}")
        result = self.code[idx_1] + self.code[idx_2]
        self.code[idx_res] = result
        return result

    def mult_code(self):
        idx_1, idx_2, idx_res = self.get_pointers()
        # print(f"{self.code[idx_1]} * {self.code[idx_2]} = {self.code[idx_1] * self.code[idx_2]}->{idx_res}")
        result = self.code[idx_1] * self.code[idx_2] 
        self.code[idx_res] = self.code[idx_1] * self.code[idx_2]
        return result
    
    def move_position(self):
        self.position += 4

    def run_code(self):
        while True:
            self.action = self.code[self.position]

            # print(f"Pos:{self.position} -> action {self.action}")
            if self.action == 1:
                self.add_code()
            elif self.action == 2:
                self.mult_code()
            elif self.action == self.terminator:
                break

            self.move_position()

        self.output = self.code[0]

    # def run_code_part2(self, find_output):
    #     while True:
    #         self.action = self.code[self.position]
    #         print(f"Pos:{self.position} -> action {self.action}")
    #         if self.action == 1:
    #             result = self.add_code()
    #         elif self.action == 2:
    #             result = self.mult_code()
    #         elif self.action == self.terminator:
    #             break
            
    #         if result == find_output:
    #             idx_1, idx_2, _ = self.get_pointers()

    #             noun = self.code[idx_1]
    #             verb = self.code[idx_2]
    #             answer = str(100*noun) + str(verb)
    #             print(noun, verb, answer)
    #             return noun, verb, answer
    #         else:
    #             self.code = self.code_initial
    #             self.move_position()

            
#%% Test
intcode_test = Intcode(test_input)
intcode_test.run_code()

#%% Part 1
input_part1 = input.copy()
input_part1[1] = 12
input_part1[2] = 2

intcode_part1= Intcode(input_part1)
intcode_part1.run_code()
print(f"Part 1: {intcode_part1.output}")

#%% Part 2
input_part2 = input.copy()

def run_inputs(output_search):
    for noun in range(0,100):
        # print(noun)
        for verb in range(0,100):
            intcode_part2 = Intcode(input_part2)
            intcode_part2.code[1] = noun
            intcode_part2.code[2] = verb
            intcode_part2.run_code()

            if intcode_part2.output == output_search:
                return noun, verb, intcode_part2.output
    
    return None

noun, verb, output = run_inputs(output_search=19690720)
print(run_inputs(output_search=19690720))
print(f"Part 2: {100*noun}{verb}")
