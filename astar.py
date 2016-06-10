#A star algorithm

def euclid_distance(startp, endp):
	"""Euclid distance"""
	return ((startp[0] - endp[0]) ** 2 + (startp[1] - endp[1]) ** 2) ** 0.500

def manhattan_distance(startp, endp):
	"""Manhattan distance"""
	return abs(startp[0] - endp[0]) + abs(startp[1] - endp[1])

def surround(point):
	"""Return the coordinations of surrounding points"""
	return [(point[0] + 1, point[1]), (point[0], point[1] + 1), (point[0] - 1, point[1]), (point[0], point[1] - 1)]

def filtering(points, barrier, closed_list):
	"""Filter points not in barrier"""
	return filter(lambda x: x not in barrier and x not in closed_list, points)

def astar(mapsize, barrier, startp, endp):
	"""param: mapsize: length and height of the map
			  barrier: coordination of barrier
	"""
	if endp in barrier or startp in barrier:
		print("No optimal path found, startp or endp is in barriers")
		return None
	g_mat = {}
	h_mat = {}
	f_mat = {}
	path = {}
	length, height = mapsize
	open_list = []
	closed_list = []
	optimal_path = []
	current = startp

	#------------------------step 1------------------------------
	closed_list.append(startp)

	#------------------------step 2------------------------------
	start_sur = list(filtering(surround(startp), barrier, closed_list))
	if (start_sur == []):
		print ("No optimal path found")
		return None
	g_mat = g_mat.fromkeys(start_sur, 1)
	for i in start_sur:
		h_mat[i] = manhattan_distance(i, endp)
		f_mat[i] = g_mat.get(i) + h_mat.get(i)
		path[i]  = startp
	open_list.extend(start_sur) #No use

	#------------------------step 3------------------------------
	while(True):
		if (open_list == None):
			print("No optimal path found")
			break
		if endp in closed_list:
			print("Optimal path found")
			path_point = endp
			while(path_point != startp):
				optimal_path.append(path_point)
				path_point = path.get(path_point)
			optimal_path.append(startp)
			return list(reversed(optimal_path))
		min_f = min(f_mat.values())
		target = [k for k in f_mat.keys() if (f_mat[k] == min_f)]
		last_target = target[-1]

		closed_list.append(last_target)
		del f_mat[last_target]

		#------------------------step 4------------------------------
		current = last_target
		cur_sur = filtering(surround(current), barrier, closed_list)
		for i in cur_sur:
			path[i] = current
			g_mat[i] = g_mat.get(last_target) + 1
			h_mat[i] = manhattan_distance(i, endp)
			f_mat[i] = g_mat.get(i) + h_mat.get(i)
			
op = astar((5,5), [(3, 2), (3, 4), (4, 3)], (3, 3), (3, 5))
print(op)
