##
# @file unstructured_grid_v3.py
# @Description Generates Unstructured Grid
# @author Adarsh Barik, Raghuvir, Gaurav
# @version 3
# @date 2012-10-20

from numpy import *
from input import *
# -------------------------------------------------------
##
# @Description Calculates area
#
# @Parameter n1
# @Parameter n2
# @Parameter n3
# @Parameter input_point_set
#
# @End 
# -------------------------------------------------------
def area(n1,n2,n3,input_point_set):
	"""calculates area"""
	a=array([[1,1,1],[input_point_set[n1-1][0], input_point_set[n2-1][0],input_point_set[n3-1][0]],[input_point_set[n1-1][1], input_point_set[n2-1][1],input_point_set[n3-1][1]]])
	ar = 0.5*abs(linalg.det(a))
	return ar
	
edge_encounter = shape(edge_conn)[0]
cell_encounter = shape(vertex_conn)[0]
delete_list=[]
boundary = [1,2,3,4,5,6,7,8]
int_bound = [1,2,3,4]
for iteration in range(1000):
#while amin(vertex_conn[:,4])>0.003:
	
# -------------------------------------------------------
##
# @Description Sorting vertex_conn in ascending order and identifying the cell to be subdivided 
# -------------------------------------------------------
	vertex_conn=vertex_conn[vertex_conn[:,vertex_conn_area].argsort()]
	i = int(vertex_conn[-1][vertex_conn_node1])
	j = int(vertex_conn[-1][vertex_conn_node2])
	k = int(vertex_conn[-1][vertex_conn_node3])
# -------------------------------------------------------
##
# @Description Getting edge with maximum length and getting its end points
# -------------------------------------------------------
	dij = linalg.norm(input_point_set[i-1][:]-input_point_set[j-1][:])
	djk = linalg.norm(input_point_set[j-1][:]-input_point_set[k-1][:])
	dki = linalg.norm(input_point_set[k-1][:]-input_point_set[i-1][:])
	check_max = array([[dij, i, j],[djk, j , k],[dki, k, i]])
	ind_max = check_max[:,0].argmax()
	p1 = int (check_max[ind_max,1])
	p2 = int (check_max[ind_max,2])

# -------------------------------------------------------
##
# @Description Getting new point
# -------------------------------------------------------
	mid_point_x = 0.5*(input_point_set[p1-1][0]+input_point_set[p2-1][0])
	mid_point_y = 0.5*(input_point_set[p1-1][1]+input_point_set[p2-1][1])
	ind_opp=[i,j,k][argmax([abs((p1-i)*(p2-i)),abs((p1-j)*(p2-j)),abs((p1-k)*(p2-k))])]
	next_pt = array([mid_point_x,mid_point_y])
	input_point_set = vstack([input_point_set,next_pt])
	next_node = shape(input_point_set)[0]
# -------------------------------------------------------
##
# @Description Updating the connectivity matrices
# -------------------------------------------------------
	mask_edge_delete=edge_conn[:,edge_conn_node1]==min(p1,p2)
	temp1 = edge_conn[mask_edge_delete]
	mask_edge_delete1=temp1[:,edge_conn_node2]==max(p1,p2)
	mask_edge_delete2 = edge_conn[:,0]==temp1[mask_edge_delete1,0]
	edge_delete = edge_conn[mask_edge_delete2]
	delete_ind = where(edge_conn[:,0]==edge_delete[:,0])
	check_position = edge_conn[delete_ind,3]
	if check_position==0:
		int_bound.append(next_node)
	if check_position!=2:
		boundary.append(next_node)
		#delete_list.append(delete_ind[0][0])
		vertex_conn = delete(vertex_conn,-1,0)
		added_cell = array([[cell_encounter+1,next_node,p1,ind_opp,area(next_node,p1,ind_opp,input_point_set)],[cell_encounter+2,next_node,p2,ind_opp,area(next_node,p2,ind_opp,input_point_set)]])
		vertex_conn = vstack([vertex_conn,added_cell])
		edge_conn=delete(edge_conn,delete_ind,0)
		added_edge = array([[edge_encounter+1,ind_opp,next_node,2],[edge_encounter+2,p1,next_node,check_position],[edge_encounter+3,p2,next_node,check_position]])
		edge_conn = vstack([edge_conn,added_edge])
		edge_encounter = edge_encounter+3
		cell_encounter = cell_encounter+2
		#print "no error"
	else:
# -------------------------------------------------------
##
# @Description Finding Second Cell
# -------------------------------------------------------
		for i in vertex_conn:
			if (p1 in i and p2 in i and ind_opp not in i):
				cell2 = i
				#print "no error"
		i2 = cell2[1]
		j2 = cell2[2]
		k2 = cell2[3]
		ind_opp2=[i2,j2,k2][argmax([abs((p1-i2)*(p2-i2)),abs((p1-j2)*(p2-j2)),abs((p1-k2)*(p2-k2))])]
		ind_opp2 = int(ind_opp2)
		cell2_mask = vertex_conn[:,0]==cell2[0]
		delete_ind1 = where(cell2_mask==True)
		vertex_conn = delete(vertex_conn,delete_ind1,0)
		vertex_conn = delete(vertex_conn,-1,0)
		added_cell = array([[cell_encounter+1,next_node,p1,ind_opp,area(next_node,p1,ind_opp,input_point_set)],[cell_encounter+2,next_node,p2,ind_opp,area(next_node,p2,ind_opp,input_point_set)],[cell_encounter+3,next_node,p1,ind_opp2,area(next_node,p1,ind_opp2,input_point_set)],[cell_encounter+4,next_node,p2,ind_opp2,area(next_node,p2,ind_opp2,input_point_set)]])
		vertex_conn = vstack([vertex_conn,added_cell])
		edge_conn=delete(edge_conn,delete_ind,0)
		added_edge = array([[edge_encounter+1,ind_opp,next_node,2],[edge_encounter+2,ind_opp2,next_node,2],[edge_encounter+3,p1,next_node,2],[edge_encounter+4,p2,next_node,2]])
		edge_conn = vstack([edge_conn,added_edge])
		edge_encounter = edge_encounter+4
		cell_encounter = cell_encounter+4

savetxt('edge_conn_out.txt',edge_conn)
savetxt('vertex_conn_out.txt',vertex_conn)
savetxt('input_out.txt',input_point_set)


