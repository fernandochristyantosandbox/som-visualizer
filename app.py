import numpy as np
import math

# Number of iterations
iterations = 10

# Patterns per batch, (1 for online learning)
pattern_per_batch = 1

# Learning Rate
alpha = 1

# Radius between neighbors
radius = 1

# Number of clusters
clusters = 4

# Number of features
features = 3

sigma0 = 1

# Weights
weight = np.array([
    [1.,2.,1.], [2.,-2.,2.], [1.,-1.,1.], [1.,3.,1.]
])

# Patterns
temp_patterns = np.array([
    [-1,1,3],
    [1,-2,1]
])

# Do not modify the variables in this block
# ==================================
curr_iteration = 0
patterns = []
# ==================================

def generate_patterns(iteration_count, pattern_per_it):
    j = 0
    for i in range(iteration_count*pattern_per_it):
        patterns.append(temp_patterns[j])
        j += 1
        if j>=len(temp_patterns):
            j = 0

def get_winner_index(distances):
    min = distances[0]
    winner = 0
    for idx, distance in enumerate(distances):
        if distance < min:
            min = distance
            winner = idx

    return idx

def get_winner_neighbours(winner):
    if(winner == 0):
        return [0,1]
    elif(winner == clusters - 1):
        return [clusters-1, clusters-2]
    else:
        return [winner-1, winner, winner+1]

def get_avg_weight(weights):
    temp_w = np.copy(weights[0])

    for i in range(features-1):
        for j in range(clusters-1):
            temp_w[i][j] = np.mean(list(x[i][j] for x in weights))
    return temp_w

def count_distances(pattern_count, patterns):
    global weight

    updated_weights = []
    # Loop pattern dalam online learning (incase kalo batch)
    for idx, pattern in enumerate(patterns):
        print("\tCalculating data: {}".format(idx+1))
        print("\t===================================================")
        distances = []
        # Loop distance dalam pattern
        for curr_cluster in range(clusters):
            calc_str = "\t√"
            total = 0
            for i in range(features):
                calc_str += "(" + str(pattern[i]) + "-" + str(weight[curr_cluster][i]) + ")^2"
                if i < features-1:
                    calc_str += " + "
                total += ((pattern[i] - weight[curr_cluster][i])**2)

            print("\tDistance {} : {} = √{} = {}".format(curr_cluster+1, calc_str, total, math.sqrt(total)))
            distances.append(float(math.sqrt(total)))
        # Get winner
        winner = distances.index(min(distances))
        print("\tWinner: {}".format(winner + 1))

        weights_to_update = get_winner_neighbours(winner)
        print("\tWeights to Update: {}".format(list(x + 1 for x in weights_to_update)))

        update_weights(pattern, winner, weights_to_update)
        updated_weights.append(weight)

    #avg
    print()
    print("Ending current iteration, Updating weight... \nFinal weight: ")

    weight = get_avg_weight(updated_weights)
    print(weight)

def get_curr_sigma():
    return float(sigma0 * math.exp(-curr_iteration/iterations))

def get_neighbor_str(rad, curr_sigma):
    power = (-rad/(2*(curr_sigma**2)))
    return math.exp(power)

def update_weights(pattern, winner, weights_to_update):
    global weight

    weights_to_update.sort()
    for node_idx in weights_to_update:
        distance_between = +(node_idx - winner)
        print()
        print("\tUpdating weight: {}".format(node_idx + 1))
        print("\t-------------------------")

        # Begin weight update calculation
        curr_sigma = get_curr_sigma()
        print("\t\tSigma {} : {}".format(node_idx+1, curr_sigma))

        rad = 0 if winner == node_idx else radius
        neighbor_strength = get_neighbor_str(rad, curr_sigma)
        print("\t\tNeighbor strength: {}".format(neighbor_strength))

        print("\t\tW{} = {} + ({})({})({} - {})".format(node_idx+1, weight[node_idx], neighbor_strength, alpha, pattern, weight[node_idx]))
        weight[node_idx] = weight[node_idx] + (neighbor_strength * alpha * (pattern - weight[node_idx]))
        print(weight)


def online_learning(iteration_count, pattern_per_it):
    global curr_iteration
    i = 0
    curr_iteration = 0
    while i < (iteration_count * pattern_per_it):
        curr_iteration = curr_iteration+1
        print("\n\n\nCurrent Iteration: {}".format(curr_iteration))
        count_distances(pattern_per_it, patterns[i:i+pattern_per_it])
        i += pattern_per_it


generate_patterns(iterations, pattern_per_batch)
online_learning(iterations, pattern_per_batch)
