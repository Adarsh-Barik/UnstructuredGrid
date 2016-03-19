##
# @file geo_treat.py
# @Description Grid adaptivity for a circular cylinder
# @author Adarsh, Raghuvir, Gaurav
# @version 1
# @date 2012-11-04


from numpy import *
from input import *
from unstructured_grid_v3 import boundary, area, int_bound
from edge_swap import angle3
from math import atan2, pi

input_data = genfromtxt('input_out.txt')
edge_conn_data = genfromtxt('edge_conn_out.txt')
vertex_conn_data = genfromtxt('vertex_conn_out.txt')

temp=[]
a=zeros((shape(input_data)))
for i in range(shape(input_data)[0]):
	a[i,:]=input_data[i,:]
for i in int_bound:
	if input_data[i-1,1]-2.5>0:
		ang = angle3(array([2.5,2.5]),array([3.,2.5]),input_data[i-1,:])
	else:
		ang = 360-angle3(array([2.5,2.5]),array([3.,2.5]),input_data[i-1,:])	
	temp.append(ang)
for i in range(shape(temp)[0]):
	input_data[int_bound[i]-1,:]=[2.5+0.5*cos(temp[i]*pi/180),2.5+0.5*sin(temp[i]*pi/180)]

savetxt('input_out.txt',input_data)

