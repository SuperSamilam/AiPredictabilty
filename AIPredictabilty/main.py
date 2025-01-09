import numpy as np
import os
import ML as ml
import PatternFinder as pf
import Data as data

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

modelName = "model-2"
trainFile = "./data/data09/train09.txt"
testFile = "./data/data09/testAuto.txt"
neuronsmiddle = 18
epoch = 2000

depth = 3
atrimeticDepth = 4
strictDepth = 100

#AI
def makeNewNN():
    trainData = data.Data()
    testData = data.Data()
    trainData.loadDataFromFile(trainFile, depth)
    testData.loadDataFromFile(testFile, depth)
    nn = ml.NeuralNetwork()

    nn.ctt(depth, neuronsmiddle, trainData, testData, epoch)
    nn.save(modelName, neuronsmiddle, depth)
    return nn

def loadAndTestOldNetwork():
    nn = ml.NeuralNetwork()
    nn.load(modelName)
    testData = data.Data()
    testData.loadDataFromFile(testFile, depth)
    nn.test(testData)
    return nn

def loadNetwork():
    nn = ml.NeuralNetwork()
    nn.load(modelName)
    return nn

#Helpers
def get_last_three_elements(list):
    if len(list) < 3:
        return [0] * (3 - len(list)) + list
    else:
        return list[-3:]

def initalizeNewGame():
    patternFinder = pf.PatterFinder()
    nn = loadNetwork()
    return patternFinder, nn
