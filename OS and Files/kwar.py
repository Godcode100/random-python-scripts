import argparse

class my_parameters:
    def __init__(self,**kwargs):
        self.param1 = kwargs.get('param1')
        self.param2 = kwargs.get('param2')

def see_my_parameters(Insert_parameters):
    print(Insert_parameters.param1)
    print(Insert_parameters.param2)

parser = argparse.ArgumentParser(description='Test 2 arguments')
parser.add_argument("-q1",dest="Input1",help="Input1")
parser.add_argument("-q2",dest="Input2",help="Input2")
prophets = parser.parse_args()
all_parameters = my_parameters(param1=prophets.Input1,param2=prophets.Input2)
see_my_parameters(all_parameters)

