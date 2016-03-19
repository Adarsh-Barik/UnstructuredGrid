from numpy import *

# -------------------------------------------------------
##
# @Description Calculates the cell area
#
# @Parameter vertex_conn
# @Parameter input_point_set
#
# @End 
# -------------------------------------------------------
def triarea(vertex_conn,input_point_set):
	"""calculates triangle area"""
	i = shape(vertex_conn)[0]
	j = shape(vertex_conn)[1]
	temp = zeros((i,j+1))
	temp[:,0:j]=vertex_conn
	for k in range(i):
		a = array([[1,1,1],[input_point_set[int(temp[k][1])-1][0],input_point_set[int(temp[k][2])-1][0],input_point_set[int(temp[k][3])-1][0]],[input_point_set[int(temp[k][1])-1][1],input_point_set[int(temp[k][2])-1][1],input_point_set[int(temp[k][3])-1][1]]])
		temp[k][j]=0.5*abs(linalg.det(a))
	return temp

# -------------------------------------------------------
##
# @Description Input parameters
# -------------------------------------------------------
input_point_set = genfromtxt('input_points_square.txt') 
input_pt_x = 0
input_pt_y = 1
cell_required = 500
edge_conn = genfromtxt('edge_conn.txt') 
edge_conn_edge = 0
edge_conn_node1 = 1
edge_conn_node2 = 2
edge_conn_position = 3
edge_conn_cell1 = 4
edge_conn_cell2 = 5
vertex_conn = genfromtxt('vertex_conn.txt')
vertex_conn = triarea(vertex_conn,input_point_set)
vertex_conn_cell = 0
vertex_conn_node1 = 1
vertex_conn_node2 = 2
vertex_conn_node3 = 3
vertex_conn_area = 4
