# my notes on the ML starter

## naive bayes [1](http://scikit-learn.org/stable/modules/naive_bayes.html) [2](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/52bd0ca5938da89d7f9bf388dc7edcbd546c118e)
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/b0122d84d632cc399d2a49924797f37a7db53b0c)

* calculates posterior probability based on prior probability and likelihood of additional features [1](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gender_classification)
* `naive` -> assumes data points are independent (i.e. text classifier > word order doesn't matter)
* biggest use case text classification
* gaussian NB assumes data to be gaussian distribution
  * not sure if this holds true for text classificiation
  * medicinal use cases have gauss. distribution


## support vector machines

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
    * linear
    * polynomial
    * 
* not too good on large/overlapping datasets > use naive bayes

