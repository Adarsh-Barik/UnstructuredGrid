##
# @file point_smooth.py
# @Description Smoothens initially formed grids
# @author Adarsh, Raghuvir, Gaurav
# @version 1
# @date 2012-10-22

from numpy import *
from input import *
from unstructured_grid_v3 import boundary

input_data = genfromtxt('input_out.txt')
edge_conn_data = genfromtxt('edge_conn_out.txt')
vertex_conn_data = genfromtxt('vertex_conn_out.txt')
for i in range(shape(input_data)[0]):
	if not i+1 in boundary:
		mask_interior = edge_conn_data[:,3]==2
		edge_conn_data1=edge_conn_data[mask_interior] 
		mask_node1 = edge_conn_data1[:,1]==i+1
		neighbour1 = edge_conn_data1[mask_node1,2]
		mask_node2 = edge_conn_data1[:,2]==i+1
		neighbour2 = edge_conn_data1[mask_node2,1]
		neighbour = concatenate([neighbour1,neighbour2])
		x_point = 0
		y_point = 0
		for j in range(shape(neighbour)[0]):
			x_point=x_point+input_data[int(neighbour[j])-1][0]
			y_point=y_point+input_data[int(neighbour[j])-1][1]
		x_point = x_point/shape(neighbour)[0]
		y_point = y_point/shape(neighbour)[0]
		input_data[i,:]=[x_point,y_point]
savetxt('edge_conn_out.txt',edge_conn_data)
savetxt('vertex_conn_out.txt',vertex_conn_data)
savetxt('input_out.txt',input_data)




