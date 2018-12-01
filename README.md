# som-visualizer
A python console application to simulate Self Organizing Map computation

# Using The Application
## Configurations
Easily set-up the computation for SOM by overriding these values in ```app.py```
```python
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
```


## Running the Application
After configuring the variables for SOM computation, its time to run the computation.
First, run the function  ```generate_patterns(number_of_iterations, patterns_per_batch)```  
  
The first argument, *number_of_iterations* is the amount of iterations to be done. The variable ```iterations``` will be passed here.

The second argument, *patterns_per_batch* is the amount of pattern in a batch. The variable ```pattern_per_batch``` will be passed here.    
Note: In case of online learning, you'd want to put 1 pattern per batch.

  
After running ```generate_patterns```, run the function ```online_learning``` to do the actual computations and prints out the results.

## Result
Here goes the sample results from a SOM calculation (2 iterations, online learning):
```
Current Iteration: 1
	Calculating data: 1
	===================================================
	Distance 1 : 	√(-1-1.0)^2 + (1-2.0)^2 + (3-1.0)^2 = √9.0 = 3.0
	Distance 2 : 	√(-1-2.0)^2 + (1--2.0)^2 + (3-2.0)^2 = √19.0 = 4.358898943540674
	Distance 3 : 	√(-1-1.0)^2 + (1--1.0)^2 + (3-1.0)^2 = √12.0 = 3.4641016151377544
	Distance 4 : 	√(-1-1.0)^2 + (1-3.0)^2 + (3-1.0)^2 = √12.0 = 3.4641016151377544
	Winner: 1
	Weights to Update: [1, 2]

	Updating weight: 1
	-------------------------
		Sigma 1 : 0.6065306597126334
		Neighbor strength: 1.0
		W1 = [1. 2. 1.] + (1.0)(1)([-1  1  3] - [1. 2. 1.])
[[-1.  1.  3.]
 [ 2. -2.  2.]
 [ 1. -1.  1.]
 [ 1.  3.  1.]]

	Updating weight: 2
	-------------------------
		Sigma 2 : 0.6065306597126334
		Neighbor strength: 0.2568813653134702
		W2 = [ 2. -2.  2.] + (0.2568813653134702)(1)([-1  1  3] - [ 2. -2.  2.])
[[-1.          1.          3.        ]
 [ 1.2293559  -1.2293559   2.25688137]
 [ 1.         -1.          1.        ]
 [ 1.          3.          1.        ]]

Ending current iteration, Updating weight... 
Final weight: 
[[-1.          1.          3.        ]
 [ 1.2293559  -1.2293559   2.25688137]
 [ 1.         -1.          1.        ]
 [ 1.          3.          1.        ]]



Current Iteration: 2
	Calculating data: 1
	===================================================
	Distance 1 : 	√(1--1.0)^2 + (-2-1.0)^2 + (1-3.0)^2 = √17.0 = 4.123105625617661
	Distance 2 : 	√(1-1.2293559040595894)^2 + (-2--1.2293559040595894)^2 + (1-2.25688136531347)^2 = √2.226247219807057 = 1.4920613994762604
	Distance 3 : 	√(1-1.0)^2 + (-2--1.0)^2 + (1-1.0)^2 = √1.0 = 1.0
	Distance 4 : 	√(1-1.0)^2 + (-2-3.0)^2 + (1-1.0)^2 = √25.0 = 5.0
	Winner: 3
	Weights to Update: [2, 3, 4]

	Updating weight: 2
	-------------------------
		Sigma 2 : 0.36787944117144233
		Neighbor strength: 0.024859183199194095
		W2 = [ 1.2293559  -1.2293559   2.25688137] + (0.024859183199194095)(1)([ 1 -2  1] - [ 1.2293559  -1.2293559   2.25688137])
[[-1.          1.          3.        ]
 [ 1.2236543  -1.24851349  2.22563632]
 [ 1.         -1.          1.        ]
 [ 1.          3.          1.        ]]

	Updating weight: 3
	-------------------------
		Sigma 3 : 0.36787944117144233
		Neighbor strength: 1.0
		W3 = [ 1. -1.  1.] + (1.0)(1)([ 1 -2  1] - [ 1. -1.  1.])
[[-1.          1.          3.        ]
 [ 1.2236543  -1.24851349  2.22563632]
 [ 1.         -2.          1.        ]
 [ 1.          3.          1.        ]]

	Updating weight: 4
	-------------------------
		Sigma 4 : 0.36787944117144233
		Neighbor strength: 0.024859183199194095
		W4 = [1. 3. 1.] + (0.024859183199194095)(1)([ 1 -2  1] - [1. 3. 1.])
[[-1.          1.          3.        ]
 [ 1.2236543  -1.24851349  2.22563632]
 [ 1.         -2.          1.        ]
 [ 1.          2.87570408  1.        ]]

Ending current iteration, Updating weight... 
Final weight: 
[[-1.          1.          3.        ]
 [ 1.2236543  -1.24851349  2.22563632]
 [ 1.         -2.          1.        ]
 [ 1.          2.87570408  1.        ]]
```