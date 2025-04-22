import random
import numpy as np
import networkx as nx
 
#coordinate of the points/cities
coordinates_berlin52 = np.array([
    [565.0, 575.0], [25.0, 185.0], [345.0, 750.0], [945.0, 685.0], [845.0, 655.0],
    [880.0, 660.0], [25.0, 230.0], [525.0, 1000.0], [580.0, 1175.0], [650.0, 1130.0],
    [1605.0, 620.0], [1220.0, 580.0], [1465.0, 200.0], [1530.0, 5.0], [845.0, 680.0],
    [725.0, 370.0], [145.0, 665.0], [415.0, 635.0], [510.0, 875.0], [560.0, 365.0],
    [300.0, 465.0], [520.0, 585.0], [480.0, 415.0], [835.0, 625.0], [975.0, 580.0],
    [1215.0, 245.0], [1320.0, 315.0], [1250.0, 400.0], [660.0, 180.0], [410.0, 250.0],
    [420.0, 555.0], [575.0, 665.0], [1150.0, 1160.0], [700.0, 580.0], [685.0, 595.0],
    [685.0, 610.0], [770.0, 610.0], [795.0, 645.0], [720.0, 635.0], [760.0, 650.0],
    [475.0, 960.0], [95.0, 260.0], [875.0, 920.0], [700.0, 500.0], [555.0, 815.0],
    [830.0, 485.0], [1170.0, 65.0], [830.0, 610.0], [605.0, 625.0], [595.0, 360.0],
    [1340.0, 725.0], [1740.0, 245.0]
])

coordinates_a280 = np.array([
    [288, 149], [288, 129], [270, 133], [256, 141], [256, 157], [246, 157], [236, 169], [228, 169], [228, 161], 
    [220, 169], [212, 169], [204, 169], [196, 169], [188, 169], [196, 161], [188, 145], [172, 145], [164, 145], 
    [156, 145], [148, 145], [140, 145], [148, 169], [164, 169], [172, 169], [156, 169], [140, 169], [132, 169], 
    [124, 169], [116, 161], [104, 153], [104, 161], [104, 169], [90, 165], [80, 157], [64, 157], [64, 165], 
    [56, 169], [56, 161], [56, 153], [56, 145], [56, 137], [56, 129], [56, 121], [40, 121], [40, 129], [40, 137], 
    [40, 145], [40, 153], [40, 161], [40, 169], [32, 169], [32, 161], [32, 153], [32, 145], [32, 137], [32, 129], 
    [32, 121], [32, 113], [40, 113], [56, 113], [56, 105], [48, 99], [40, 99], [32, 97], [32, 89], [24, 89], 
    [16, 97], [16, 109], [8, 109], [8, 97], [8, 89], [8, 81], [8, 73], [8, 65], [8, 57], [16, 57], [8, 49], 
    [8, 41], [24, 45], [32, 41], [32, 49], [32, 57], [32, 65], [32, 73], [32, 81], [40, 83], [40, 73], [40, 63], 
    [40, 51], [44, 43], [44, 35], [44, 27], [32, 25], [24, 25], [16, 25], [16, 17], [24, 17], [32, 17], [44, 11], 
    [56, 9], [56, 17], [56, 25], [56, 33], [56, 41], [64, 41], [72, 41], [72, 49], [56, 49], [48, 51], [56, 57], 
    [56, 65], [48, 63], [48, 73], [56, 73], [56, 81], [48, 83], [56, 89], [56, 97], [104, 97], [104, 105], 
    [104, 113], [104, 121], [104, 129], [104, 137], [104, 145], [116, 145], [124, 145], [132, 145], [132, 137], 
    [140, 137], [148, 137], [156, 137], [164, 137], [172, 125], [172, 117], [172, 109], [172, 101], [172, 93], 
    [172, 85], [180, 85], [180, 77], [180, 69], [180, 61], [180, 53], [172, 53], [172, 61], [172, 69], [172, 77], 
    [164, 81], [148, 85], [124, 85], [124, 93], [124, 109], [124, 125], [124, 117], [124, 101], [104, 89], 
    [104, 81], [104, 73], [104, 65], [104, 49], [104, 41], [104, 33], [104, 25], [104, 17], [92, 9], [80, 9], 
    [72, 9], [64, 21], [72, 25], [80, 25], [80, 25], [80, 41], [88, 49], [104, 57], [124, 69], [124, 77], 
    [132, 81], [140, 65], [132, 61], [124, 61], [124, 53], [124, 45], [124, 37], [124, 29], [132, 21], [124, 21], 
    [120, 9], [128, 9], [136, 9], [148, 9], [162, 9], [156, 25], [172, 21], [180, 21], [180, 29], [172, 29], 
    [172, 37], [172, 45], [180, 45], [180, 37], [188, 41], [196, 49], [204, 57], [212, 65], [220, 73], [228, 69], 
    [228, 77], [236, 77], [236, 69], [236, 61], [228, 61], [228, 53], [236, 53], [236, 45], [228, 45], [228, 37], 
    [236, 37], [236, 29], [228, 29], [228, 21], [236, 21], [252, 21], [260, 29], [260, 37], [260, 45], [260, 53], 
    [260, 61], [260, 69], [260, 77], [276, 77], [276, 69], [276, 61], [276, 53], [284, 53], [284, 61], [284, 69], 
    [284, 77], [284, 85], [284, 93], [284, 101], [288, 109], [280, 109], [276, 101], [276, 93], [276, 85], 
    [268, 97], [260, 109], [252, 101], [260, 93], [260, 85], [236, 85], [228, 85], [228, 93], [236, 93], 
    [236, 101], [228, 101], [228, 109], [228, 117], [228, 125], [220, 125], [212, 117], [204, 109], [196, 101], 
    [188, 93], [180, 93], [180, 101], [180, 109], [180, 117], [180, 125], [196, 145], [204, 145], [212, 145], 
    [220, 145], [228, 145], [236, 145], [246, 141], [252, 125], [260, 129], [280, 133]
])
 
#adjacency matrix for a weighted graph based on the given coordinates
def generate_matrix(coordinate):
    matrix = []
    for i in range(len(coordinate)):
        for j in range(len(coordinate)) :       
            p = np.linalg.norm(coordinate[i] - coordinate[j])
            matrix.append(p)
    matrix = np.reshape(matrix, (len(coordinate),len(coordinate)))
    #print(matrix)
    return matrix
 
#stochastic  
def solution(matrix):
    points = list(range(0, len(matrix)))
    solution = []
    for i in range(0, len(matrix)):
        random_point = points[random.randint(0, len(points) - 1)]
        solution.append(random_point)
        points.remove(random_point)
    return solution

# #simple
# def solution_simple(matrix):
#     return list(range(len(matrix)))  # Start with cities in order
 
 
#calculate the path based on the random solution
def path_length(matrix, solution):
    cycle_length = 0
    for i in range(0, len(solution)):
        cycle_length += matrix[solution[i]][solution[i - 1]]
    return cycle_length
 
#generate neighbors of the random solution by swapping cities and returns the best neighbor
def neighbors(matrix, solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
             
    #assume that the first neighbor in the list is the best neighbor      
    best_neighbor = neighbors[0]
    best_path = path_length(matrix, best_neighbor)
     
    #check if there is a better neighbor
    for neighbor in neighbors:
        current_path = path_length(matrix, neighbor)
        if current_path < best_path:
            best_path = current_path
            best_neighbor = neighbor
    return best_neighbor, best_path
 
 
def hill_climbing(coordinate):
    matrix = generate_matrix(coordinate)
     
    current_solution = solution(matrix)
    current_path = path_length(matrix, current_solution)
    neighbor = neighbors(matrix,current_solution)[0]
    best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)
 
    while best_neighbor_path < current_path:
        current_solution = best_neighbor
        current_path = best_neighbor_path
        neighbor = neighbors(matrix, current_solution)[0]
        best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)
 
    return current_path, current_solution


final_solution_b = hill_climbing(coordinates_berlin52)
print("The solution for berlin52 \n", final_solution_b[1])


final_solution_a = hill_climbing(coordinates_a280)
print("The solution for a280 is \n", final_solution_a[1])