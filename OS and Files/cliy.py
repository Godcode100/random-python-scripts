import argparse

class Input:
    def __init__(self,**kwargs):
        self.inner1 = kwargs.get("inner1")
        self.inner2 = kwargs.get("inner2")

def see_inputs(Inputs):
    print(Inputs.inner1)
    print(Inputs.inner2)

parser = argparse.ArgumentParser(description="Test 2 inputs ")
parser.add_argument("-he1",dest="input1",help="Input1")
parser.add_argument("-he2",dest="input2",help="Input2")
winners = parser.parse_args()
finalists = Input(inner1=winners.input1,inner2=winners.input2)
see_inputs(finalists)


