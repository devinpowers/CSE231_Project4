#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:55:56 2020

@author: devinpowers
"""
# Project 4

import math


# this function accepts as the user inputs a (string) as a numerical value and returns the sim of the s


def sum_natural_squares(N):
    
   if  N.isdigit() == True:
       #converting the string entered into a integar so we can perfrom math on it
       N_int = int(N)
       Sum = (N_int*(N_int+1))/2
       return Sum
       
   else:
       Sum = N
       return None
     

# Pie value is good 
       
def approximate_pi():
    
    # hand Calc
    pi = 0.0
    for i in range(1,10000000,4):
        pi += 4/i
        pi -= 4/(i+2)
        return pi

    # using Computer to Calc pi
    pi_math = math.pi
    return pi_math
    
    #difference in pi
    difference = (pi_math - pi)
    return difference
    
    # accepts a float and returns the approximate value of sine x
    
def approximate_sin(x):
    
    
    answer = math.sin(x)
    return answer
         
    
# function accepts as input numeric value x

def approximate_cos(x):
    answer_cos = math.cos(x)
    return answer_cos

    
def main():
    
    running = True
    while running == True:
        
        
        response = str(input("Please Choose one of the options below:\n"
              "\nA. Display the sum of squares of the first N natural "
              "\nB.  Display the approximate value of Pi."
              "\nC.  Display the approximate value of the sine of X."
              "\nD.  Display the approximate value of the cosine of X."
              "\nM.  Display the menu of options."
              "\nX. Exit from the program."
              " "
              ))
        
        # Once Entered the Letter this will convert to lowercase letter and decide which function to run
        
        response_lower = response.lower()
        if response_lower == 'a':
            
            ask_for_naturual_number = str(input("Please Enter a Number to calculate: "))
            N = ask_for_naturual_number
            #call funciton
            Sum = sum_natural_squares(N)
            
            # printing return values 
            if Sum != None:
                print("The Sum: ", Sum)
            else:
                print("Error: N was not a valid natural number", "[", N, "]" )
        
        # Pi calculation    
            
        elif response_lower =='b':
            print("\n Calculating Pi: ")
            
            #call function
            approximate_pi()
            
            #pi from equation
            pi = approximate_pi()
            print("Approximation: ", round(pi,15))
            
            #pi from math module
            
            pi_math = approximate_pi()
            print("Math Module: ", round(pi_math,10))
            
            #pi difference
            difference = approximate_pi()
            print("Difference: ", round(difference,10))
            
            
            
            
            
        elif response_lower =='c':
            
            ask_for_sin = float(input("What value of Sine would you like to figure out?: "))
            
            x = ask_for_sin
            #call function
            print("The Approximate Value of Sine is equal to: ", approxitmate_sin(x))
            
            
        elif response_lower == 'd':
            
            ask_for_cos = int(input("what value of Cosine would you like to figure out?: "))
            
            x = ask_for_cos
            #Call function
            print("The approximate value of cosine of")
            print(approximate_cos(x))
            
        
        elif response_lower == 'm':
            continue
        elif response_lower == 'x':
            print("BYE!!!!!")
            running = False
            break
        
        elif response_lower != 'a' or 'b' or 'c' or 'd' or 'm' or 'x':
            print("Error, please try again: ")
            continue
        
    
        question = input("Would you like to solve another problem? (yes or no):")
        
        question_lower =question.lower()
        
        if question_lower =='yes':
            continue
        else:
            print("Hope to See you again!")
            running == False
            break
        

        
main()


