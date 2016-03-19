##
# @file edge_swap.py
# @Description edge swaping algorithm
# @author Adarsh, Raghuvir, Gaurav
# @version 1
# @date 2012-11-04


from numpy import *
from input import *
from unstructured_grid_v3 import boundary, area 
from math import atan2, pi

# -------------------------------------------------------
##
# @Description Calculates angle at p1
#
# @Parameter p1
# @Parameter p2
# @Parameter p3
#
# @End 
# -------------------------------------------------------
def angle3(p1,p2,p3):
	"""docstring for angle3"""
	p12 = p2-p1
	#p23 = linalg.norm(p2-p3)
	p13 = p3-p1
	angle = atan2(linalg.norm(cross(p12,p13)),dot(p12,p13))
	return angle*180/pi

input_data = genfromtxt('input_out.txt')
edge_conn_data = genfromtxt('edge_conn_out.txt')
vertex_conn_data = genfromtxt('vertex_conn_out.txt')
for i in range(shape(edge_conn_data)[0]):
# -------------------------------------------------------
##
# @Description Computing cells associated to a particular edge 
# -------------------------------------------------------
	if edge_conn_data[i,3] == 2.:
		cell2 = zeros((2,shape(vertex_conn_data)[1]))
		ind_vert = zeros((2,1))
		count = 0
		for j in range(shape(vertex_conn_data)[0]):
			if (edge_conn_data[i,1] in vertex_conn_data[j] and edge_conn_data[i,2] in vertex_conn_data[j]):
				cell2[count] = vertex_conn_data[j]
				ind_vert[count]=j
				count = count+1
		i1 = cell2[0,1]
		j1 = cell2[0,2]
		k1 = cell2[0,3]
		ind_opp1=int ([i1,j1,k1][argmax([abs((edge_conn_data[i,1]-i1)*(edge_conn_data[i,2]-i1)),abs((edge_conn_data[i,1]-j1)*(edge_conn_data[i,2]-j1)),abs((edge_conn_data[i,1]-k1)*(edge_conn_data[i,2]-k1))])])
		i2 = cell2[1,1]
		j2 = cell2[1,2]
		k2 = cell2[1,3]
		ind_opp2=int ([i2,j2,k2][argmax([abs((edge_conn_data[i,1]-i2)*(edge_conn_data[i,2]-i2)),abs((edge_conn_data[i,1]-j2)*(edge_conn_data[i,2]-j2)),abs((edge_conn_data[i,1]-k2)*(edge_conn_data[i,2]-k2))])])
# -------------------------------------------------------
##
# @Description Swapping Criteria
# -------------------------------------------------------
		ang1 = angle3(input_data[ind_opp1-1,:],input_data[int(edge_conn_data[i,1])-1,:],input_data[int(edge_conn_data[i,2])-1,:])
		ang2 = angle3(input_data[ind_opp2-1,:],input_data[int(edge_conn_data[i,1])-1,:],input_data[int(edge_conn_data[i,2])-1,:])
		if ang1>90 and ang2>90:
			a=amax([ind_opp1,ind_opp2])
			b=amin([ind_opp1,ind_opp2])
			edge_conn_data[i,1] = a
			edge_conn_data[i,2] = b
			vertex_conn_data[int(ind_vert[0][0]),:]=[vertex_conn_data[int(ind_vert[0][0]),0],ind_opp1,ind_opp2,a,area(a,ind_opp1,ind_opp2,input_data)]
			vertex_conn_data[int(ind_vert[1][0]),:]=[vertex_conn_data[int(ind_vert[1][0]),0],ind_opp1,ind_opp2,b,area(b,ind_opp1,ind_opp2,input_data)]

savetxt('edge_conn_out.txt',edge_conn_data)
savetxt('vertex_conn_out.txt',vertex_conn_data)
savetxt('input_out.txt',input_data)






