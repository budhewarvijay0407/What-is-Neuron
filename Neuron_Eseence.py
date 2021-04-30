import scipy as sc
import numpy as np

###This code assumes the input value to every neuron will be a 1x1 matrix i.e a single value, For sake of simplicity####

class neuron():
    
    def __init__(self,input_x=0,weights=0,act=0):
        self.input_x=input_x
        self.weights=weights
        if type(input_x)==list:
            print('Multiple Input Neuron')
            self.weights=np.random.rand(len(self.input_x))
            self.linear_input_x=self.input_x*self.weights
            if act!=0:
                self.__avtivation_type(act,i_type='multi')
            else:
                self.activation=1/(1+np.e**-sum(self.linear_input_x))    ##### We wont be considering bias here, lets focus on how back propagation shows effect on the weights only ######
                print('The default activation funciton is Logistic',self.activation)
        else:
            print('Singe input Neuron')
            self.linear_input_x=self.input_x
            if act!=0:
                self.__avtivation_type(act,i_type='single')
            else:
                self.activation=1/(1+np.e**-(self.linear_input_x))    ##### We wont be considering bias here, lets focus on how back propagation shows effect on the weights only ######
                print('The default activation funciton is Logistic',self.activation)
                
    def __avtivation_type(self,act,i_type):   #####Making this class private so that it can't be altered from outside the class definition
        if i_type=='multi':
            
            if act=='tanh':
                self.activation=np.tanh(sum(self.input_x))  ####No need to show of the formula of tanh (((e**x-e**(-x))/(e**x+e**(-x)))
                print('Tanh Activation Function',self.activation)
                
            if act=='relu':
                self.activation=max(0,sum(self.input_x))
                print('Relu output',self.activation)
                
        if i_type=='single':
            
             if act=='tanh':
                self.activation=np.tanh(self.input_x)  ####No need to show of the formula of tanh (((e**x-e**(-x))/(e**x+e**(-x)))
                print('Tanh Activation Function',self.activation)
             if act=='relu':
                self.activation=max(0,self.input_x)
                print('Relu output',self.activation)
