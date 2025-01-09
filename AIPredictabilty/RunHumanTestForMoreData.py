
datafile = "testAuto.txt" #file containg the number series
humanfile = "humanAuto.txt" #file containg the human gusses

with open(datafile, "r") as file:
    # Read the content of the file
    data = file.read()
data = [int(num.strip()) for num in data.split(',') if num.strip()]

with open(humanfile, "r") as file:
    # Read the content of the file
    humanData = file.read()
humanData = [int(num.strip()) for num in humanData.split(',') if num.strip()]

HumanKeyPressedAmounts = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0
        }


HumanRightGuessesAmount = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0
        }

right = 0
for i in range(len(data)):
    HumanKeyPressedAmounts[humanData[i]] += 1
    if (data[i] == humanData[i]):
        right += 1
        HumanRightGuessesAmount[data[i]] += 1
        
print(f"Amount of numbers gussed right: {right}")
print(f"Accuracy: {right/len(data)}")
print(f"How many times the key got pressed by player: {HumanKeyPressedAmounts}")
print(f"How many times the AI guessed right of each number: {HumanRightGuessesAmount}")
