import os
from math import floor
from random import random
from DNA import  DNA
from script import Battle
from Bots import  PythonBot
class Population(object):
    def __init__(self, population, mutationRate):
        self.__count = len(population)
        self.__mutationRate = mutationRate
        self.__population = population
        self.__scores = [0 for i in range(self.__count)]

        os.makedirs('temp', exist_ok = True)
        self.__names = ['./temp/' + str(i) + '.json' for i in range (self.__count)]

    def GetDNAs(self):
        return  self.__population

    def CalcFitness(self, params):
        bots = []
        for i,dna in enumerate(self.__population):
            dna.WriteNetworkJson(self.__names[i])
            bots.append(PythonBot('python3 main.py', self.__names[i], params['blockedCells'], params['moves']))
        bots.extend(params['extraBots'])
        params['players'] = bots
        scores = Battle(params)
        self.__scores = scores[0:self.__count]
        return self.__scores
    

    def __PickOne(self, cumulativeSums, maxSum):
        index = 0
        value = np.random.rand() * maxSum
        return bisect.bisect_left(cumulativeSums, value)

    def Stuck(self, maxScore):
        if maxScore == self.__lastScore:
            self.__consecutiveScores = self.__consecutiveScores + 1
        else:
            self.__consecutiveScores = 1
        
        self.__lastScore = maxScore
        if self.__consecutiveScores == 10:
           return True
        return False

    def Generate(self):
        length = len(self.__data)
        maxScore = max(self.__scores)
        if self.Stuck(maxScore):
            for dna in self.__data:
                if(dna.GetScore() == maxScore):
                    mutation = 1
                else:
                    mutation = 0.5
                dna.Mutate(mutation, self.__hints)
            
            print ('Forced mutations was did...')
            randNumbers = [np.random.random() for i in range(len(self.__encoded))]
            randSum = sum(randNumbers)
            length = len(self.__encoded)
            for i in range(length):
                self.__weights[i] = randNumbers[i]/randSum*length
            return None
    
        cumulativeSums = np.array(self.__scores).cumsum().tolist()
        maxSum = cumulativeSums[-1]
        newGeneration = []
        currentMutation = self.__mutationRate# + (self.__generation/1000)
        print ('mutation:', currentMutation*100, '%')
        for i in range(length):
            parent1 = self.__data[self.__PickOne(cumulativeSums, maxSum)]
            parent2 = self.__data[self.__PickOne(cumulativeSums, maxSum)]
            child = parent1.CrossOver(parent2, currentMutation, self.__hints)
            newGeneration.append(child)

        self.__data = newGeneration






