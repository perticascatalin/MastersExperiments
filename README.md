# MastersExperiments

## E1: Statistically learning the correct order and other relational operations (in progress)

### Motivation

Whatever tasks they have to model, neural networks often encounter the problem of modeling relevance - how to assign 1st, 2nd, 3rd and so on to data chunks such that it answers some questions. Such an example is the spatial ordering of elements in a visual scene as shown below.

|Example|Description|
|:-----:|:---------:|
|![logico_visual](https://raw.githubusercontent.com/perticascatalin/MastersExperiments/master/Permutation/images/logico_visual.png)|Start from logico-visual tasks learned by a neural network and continue with set theory and an analysis to solve particular questions.|

Understanding how neural networks and other supervised learning models learn to answer such questions by processing large amounts of labeled data is of importance to any visual automated tasks from tracking objects of interest in scenes to self-driving cars. From this perspective, we look at the challenges that come with an increased number of objects (above 10 typically).

### Introduction

The experiment models the manipulation of arrays with different numbers and of different lenghts. First, we formulate the problem of predicting the sorted order of the initial numbers. This problem involves the concepts of order relations, counting and permutations.

- N = 5
- MAX = 50
- distinct integers in range [1, MAX]

|Initial position|  1|  2|  3|  4|  5|
|:--------------:|:-:|:-:|:-:|:-:|:-:|
|Value           | 49|  3|  2|  5| 17|
|Sorted position |  5|  2|  1|  3|  4|
|Maximum         |  1|  0|  0|  0|  0|
|Minimum         |  0|  0|  1|  0|  0|

- Order relations: Is A smaller than B?
- 0/1 for pair (A/B)

|  N| 49|  3|  2|  5| 17|
|:-:|:-:|:-:|:-:|:-:|:-:|
| 49|  -|  0|  0|  0|  0|
|  3|  1|  -|  0|  1|  1|
|  2|  1|  1|  -|  1|  1|
|  5|  1|  0|  0|  -|  1|
| 17|  1|  0|  0|  0|  -|

- Elementwise comparison vector:
- list entries from order matrix (left-right, top-bottom)
- [0 0 0 0 1 0 1 1 1 1 1 1 1 0 0 1 1 0 0 0]

In the above case, the sorted position of 49 is equal to O(1,1) + O(2,1) + O(3,1).... Similarly, the final position of 3 is equal to O(2,1) + O(2,2) + O(2,3).... Although the operations involved in finding the sorted positions are quite simple, statistical learning models have troubles with computing the correct answer.

### Models

1. **Comparison** between decision tree and multilayer perceptron. Multiple variants of decision trees: decision, forest and extreme.

2. **Input data**: initial numbers and their elementwise comparison vector.

We show how this poses scalability problems for the chosen machine learning models (neural networks and decision trees). For instance:

|Size|   6|   8|   9|  10|  11|  12|  16|  20|  24|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|  NN|1.00|1.00|1.00|0.95|0.66|0.44|0.23|0.07|0.04|
|  DT|1.00|0.99|0.92|0.75|0.68|0.60|0.34|0.23|0.15|
|Rand|0.17|0.12|0.11|0.10|0.09|0.08|0.06|0.05|0.04|

Up to N = 10 we get very good results with both models. 
For N = 24, the neural network starts predicting worse than random guessing.
The neural network performs better than the decision tree-based models up to N = 10, then it has a sudden drop. However, decision trees have a slower drop in accuracy.

|Accuracy|Model Description|
|:------:|:---------------:|
|![asm_plot](https://raw.githubusercontent.com/perticascatalin/MastersExperiments/master/Permutation/results/asm.png)|Extreme forest with 96 estimators vs. multilayer_perceptron with ~1000 neurons in 4 layers (512, 256, 128) dense + N multi-label outputs.|


3. **Metrics**: We compute a partial accuracy - the average number of elements guessed in N arrays.

- Data: DC
- Range 6:         E_96 6.0 NN 6.0
- Range 8:  D  6.0 E_96 7.9 NN 8.0
- Range 10: D  4.0 E_96 7.5 NN 9.5
- Range 12: NN 5.3 E_96 7.2
- Range 16: NN 3.6 E_96 5.4
- Range 20: NN 1.4 E_96 4.6
- Range 24: NN 1.0 E_96 3.5

Next, we try to find some of the underlying reasons. For instance, by measuring the impact of data representation: bare numbers or numbers with an order relation. This is done by investigating the properties of the input and target spaces.

- important space dimensions (set cardinality):
- N! vs. MAXINT!/(MAXINT-N)! vs. 2^((N)x(N-1)/2) vs. 2^N

Then we look for changes in the models or the problem formulation that could help improve our solution.

*To investigate further*

1. Representation: sequence of numbers vs. bag of numbers (count sort)

2. Multilabel Classification.
Vectors for small arrays of numbers. 
Largest enhancements and smallest shrinking preserve array class (all labels).
Bent surface on n-2 space.

3. Regression.
Directly predict the numbers in the correct order.
Neural network has to store the numbers.

4. Temporal Generation

5. Pre-order to/vs. Post-order

6. Constraint non-identical labels

7. Views
Display graphic array before and after - barchart, stacking vs. coloring.

8. Input-output matching cardinality

### Experiments vs Theory

Adding comparison prior knowledge to data

Storage capability: predicting the order vs. predicting elements in order

Maximizing expected value vs. optimization

Impurity vs. local minima

Attribute split vs. non-linear combinations

Models scalability

### Related work

Links to information theory and deep learning [X], [Y].

The importance of prior information and pre-learned intermediate concepts. Composition of 2 highly non-linear tasks and other hypothesis such as local minima obstacle and guided/transfer learning [X].

Gradients in highly composed functions or hard constraints [Y].

There are some other works where simple algorithms are inferred via neural networks. For example, in [A], the operations of copying and sorting an array are performed with a fully differentiable network connected to an eternal memory via attention. 

In another approach, [B] presents a sorting experiment for sets of numbers using a sequence to sequence model.

[A] A. Graves, G. Wayne, and I. Danihelka, “Neural Turing Machines,” arXiv:1410.5401v2, 2014.

[B] O. Vinyals, S. Bengio, and M. Kudlur, “OrderMatters: Sequence to Sequence for Sets”, in 4th International Conference on Learning Representations (ICLR), 2016.

[X] C. Gulcehre and Y. Bengio, "Knowledge Matters: Importance of Prior Information for Optimization"

[Y] S. Shalev-Shwartz and O. Shamir and S Shammah, "Failures of Gradient-Based Deep Learning"