import random
import math
from FileParsing import parse_file
from EM_algorithm import em_algo_run
file="em_data.txt"
values=[]
values,min,max=parse_file(file, values)
k=5
varience_intial_value=0.5
em_algo_run(values, k, varience_intial_value,4)
