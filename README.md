# my notes on the ML starter

## naive bayes [1](http://scikit-learn.org/stable/modules/naive_bayes.html) [2](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

`accuracy(terrain): 0.88`

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/52bd0ca5938da89d7f9bf388dc7edcbd546c118e)
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/b0122d84d632cc399d2a49924797f37a7db53b0c)

* calculates posterior probability based on prior probability and likelihood of additional features [1](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gender_classification)
* `naive` -> assumes data points are independent (i.e. text classifier > word order doesn't matter)
* biggest use case text classification
* gaussian NB assumes data to be gaussian distribution
  * not sure if this holds true for text classificiation
  * medicinal use cases have gauss. distribution


## support vector machines

`accuracy(terrain): 0.94`

* basically splits x/y scatter data in two classes by drawing a line between them
* maximizes the margin (space between boundary and nearest data points) for each set
* additional featuers allow for non-linear svms [1](https://classroom.udacity.com/courses/ud120/lessons/2252188570/concepts/24280485540923)
  * `z = abs(x)`
  * `z = x^2 + y^2`
* kernel trick creates a multi-dimensional dataset from 2D input data
  * kernel = function that creates additional features
  * if data is linearily separable on one of those features it is transformed back into the original 2D space
  * SVM is now non-linear in 2D space as inverse transformation of the new feature
  * default kernels available in most libs [1](http://scikit-learn.org/stable/modules/svm.html#kernel-functions)
* not too good on large/overlapping datasets > use naive bayes
  * takes looong to train/test

## decision trees

`accuracy(terrain): 0.912`

* split dataset by recursively putting conditions onto the dataset
* builds a tree of decisions `x > 3 && y < 5 && x > 8`
* defining the minimum number of points to keep splitting for depends on # dataset
* DTclassifier optimizes for information gain: `entropy(parent) - sum(entropy children)`
  * max: 1 as entropy can range from 0 (pure data) to 1 (evenly distributed data)
* easy to understand how the data is split
* limit tree to prevent overfitting
* very fast in classifying

## k nearest neighbors

`accuracy(terrain): 0.94`

* builds groups of data points that represent a specific class
* classification happens by checking surrounding classified points
* majority vote determines the class of the new point
* bigger `k_neighbors` makes it more robust/smooth
* very fast classification
* good for datasets without clear seperations
* unpredictable/unexpected behavior in intersection of classes

## random forest [1](https://en.wikipedia.org/wiki/Random_forest) [2](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

`accuracy(terrain): 0.92`

* builds a bunch of decision trees
* classification is done by averaging all classifications by the individual DT in the forest
* averages out overfitted singular decision trees

## adaboost (adaptive boosting)

`accuracy(terrain): 0.92`

* another ensemble learning method (like random forest)
* takes multiple weak classifiers
* differences to random forest
  * specifically trains the weak classifiers so that each handles previously hard-to-classify datapoints well
  * generates weighted output instead of strict average

## overview

[![](http://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_001.png)](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#sphx-glr-auto-examples-classification-plot-classifier-comparison-py)

## regression

* used for continous outputs (e.g. estimated house prices, weight)
* linear regression as `y= m*x + c`

## outliers

* outliers might be removed or selected depending on use case (e.g. anomaly detection)
* to identify outliers:
  * train a regression algorithm
  * calculate each points error
  * remove 10% (or more/less) with the highest error
  * could be continued as long as there is a significant difference in errors visible

## k means clustering

* [visualization](http://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
* assign and optimize loop
  * create K start points in the 2D space
  * assign each data point to the nearest cluster center
  * optimize by moving the center so that the distance to all associated points is minimized
  * re-assign, ..


