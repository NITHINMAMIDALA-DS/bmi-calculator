### create a bmi calculation application

from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    height = input("please enter the height in cm ", type=FLOAT)
    weight = input("please enter the weight in kg", type=FLOAT)

    bmi = weight/(height/100)**2

    bmi_output = [(16, 'Severly underweight'), (18.5, 'underweight'),
                  (25, 'Normal'),(30,'overweight'),
                  (35, 'moderately obese'), (float('inf'), 'severely obese')]

    for tuple1, tuple2 in bmi_output:
        if bmi < tuple1:
            put_text('Your bmi is :%.1f and the person is :%s'%(bmi, tuple2))
            break


if __name__=='__main__':
    bmicalculator()




