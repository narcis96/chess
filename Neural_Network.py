#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import random
from random import seed
from math import exp
import sys,  json
from array import *
class NeuralNetwork:

    def __init__(self, layers):
        self.__network = layers

    def __activate(self, weights, inputs):
        activation = weights[-1]  # bias
        assert(len(weights)-1 == len(inputs))
        for i in range(len(weights) - 1):
            activation += weights[i] * inputs[i]
        sys.stderr.flush()
        return activation

    # tansig function
    def __transfer(self, activation):
        return 2.0 / (1.0 + exp(-2.0*activation)) - 1

    def predict(self, row):
        outputs = self.__forward_propagate(row)
        return outputs

    def __forward_propagate(self, row):
        inputs = row
        for layer in self.__network:
            new_inputs = []
            new_inputs = [self.__transfer(self.__activate(neuron, inputs)) for neuron in layer]
            inputs = new_inputs
        return inputs

    def __str__(self):
        string = ''
        for layer in self.__network:
            string += str(layer) + '\n'
        return string

    def predict2(self, board):
        boardString = board.fen().split()[0]
        pawnDiff = boardString.count("P")-boardString.count("p")
        rookDiff = boardString.count("R")-boardString.count("r")
        knightDiff = boardString.count("N")-boardString.count("n")
        bishopDiff = boardString.count("B")-boardString.count("b")
        queenDiff = boardString.count("Q")-boardString.count("q")
        return 1*pawnDiff + 3*bishopDiff + 3*knightDiff + 5*rookDiff + 9*queenDiff


class PythonBot():
    def __init__(self, executable, path, blockedCells, moves):
        self.executable = executable
        self.path = path
        self.blockedCells = int(blockedCells)
        self.moves = int(moves)
    def __str__(self):
        return self.executable + ' -path ' + self.path +  ' -blockedCells ' + str(self.blockedCells) + ' -moves ' + str(self.moves)

    def __ToJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def WriteJson(self, path):
        with open(path, 'w') as outfile:
            json.dump(self.__ToJson(), outfile)

    @staticmethod
    def json2obj(data):
        return json.loads(data, object_hook=lambda d: Namespace(**d))

    @staticmethod
    def ReadFromJson(path):
        with open(path) as data_file:
            param = PythonBot.json2obj(json.load(data_file))
        return PythonBot(param.executable, param.path, param.blockedCells, param.moves)

