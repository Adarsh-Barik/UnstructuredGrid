from numpy import *
from input import *
from unstructured_grid_v3 import boundary, area 
from math import atan2, pi
from edge_swap import angle3

input_data = genfromtxt('input_out.txt')
edge_conn_data = genfromtxt('edge_conn_out.txt')
vertex_conn_data = genfromtxt('vertex_conn_out.txt')

angle=[]
for i in vertex_conn_data:
	angle.append(angle3(input_data[int(i[1])-1],input_data[int(i[2])-1],input_data[int(i[3])-1]))
	angle.append(angle3(input_data[int(i[2])-1],input_data[int(i[1])-1],input_data[int(i[3])-1]))
	angle.append(angle3(input_data[int(i[3])-1],input_data[int(i[2])-1],input_data[int(i[1])-1]))
