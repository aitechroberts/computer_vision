## Intro Machine Learning for CV
On a simple area, you can use and do this with HOG detectors on training data and then run
- Super cool and really need to try

How can we fix output from naive thresholding? 

Just like with edge detector, nonmaximal suppression
- Zero out responses that overlap, repeat until highest remaining score is below a threshold

**Dalal and Triggs**- Research here to execute
- Could be great to run as inference

Architecture- check slides before statistical classification review

Good Texts- Elements of Statistical Learning and Pattern Recognition- Chris Bishop

Could do well with 500 positives and 1000 negatives

**All machine learning is either nearest-neighbors or linear regression**
- With infinite data, theoreticlaly nearest neighbors is the 'optimal' method but in reality, crazy slow


Linear Classification
- Think about it as average positive vs average negative and doing the threshold

- Then covariance matrix to compute centroids in whitened space or apply Sigma transformation to weight vector
    - Derived from variance minimization perspective. Linear Discriminant Analysis or Fischer Discriminant Analysis

**Share slides with Cole**
Alternative derivation is probabilistic Gaussians
- Aka run it through Bayesian probability calculation 
    - And 1/(1+e^-(w.T*x + b))
    - Which is the **Sigmoid** or a "squashing function" that squashes the output to between 0 and 1

Alternative: Discriminative fitting (logistic regression)

Difference between Linear and Logistic Regression
- One line change in the code to change what y_hat is Slide 47

