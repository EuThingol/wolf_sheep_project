#mohammad
import numpy as np
import pandas as pd
import time
import decimal
import random
import matplotlib.pyplot as plt
import fanstatic
#set decimal number
decimal.getcontext().prec = 20
NUMBER_OF_ITERATION = 3000000
list_of_num = list(range(0,NUMBER_OF_ITERATION))
first_df = pd.DataFrame(list_of_num,columns=["A"]).reset_index(drop=True)
second_df = pd.DataFrame(list_of_num,columns=["A"]).reset_index(drop=True)

#-------------------------------------------------------------
number_list = list(range(NUMBER_OF_ITERATION))
change = number_list

#first method
first_method_start_time = decimal.Decimal(time.time())
first_df["A"].apply(lambda x: x+100)
first_method_end_time = decimal.Decimal(time.time())

#second_method
second_method_start_time = decimal.Decimal(time.time())
second_df["A"] = second_df["A"].map(lambda x: x+100)
second_method_end_time = decimal.Decimal(time.time())

first_method_time_per_second_method_time = (first_method_end_time - first_method_start_time)/(second_method_end_time - second_method_start_time) if (second_method_end_time - second_method_start_time)!=0 else "division by is zero"

print(f" The time of the first method is: {first_method_end_time - first_method_start_time} \n The time of the second method is: {second_method_end_time - second_method_start_time} \n improvement rate of second method: {first_method_time_per_second_method_time}")
