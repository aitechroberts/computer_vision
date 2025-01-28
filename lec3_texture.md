# Markov Models for Generating Text
Bag of Words basically
- Build out conditional probability table by counting
    - Untenable for large vocabularies at ~4TB for a million words at int32
    - BUUUTTT you can compute single rows of co-occurence "on-the-fly"
        - ORRRR Don't even compute the whole row, just randomly sample one of the 3 matches and spit out next word

**Now apply to texture generation**
Rather than a *temporal* Markov property, now you have a *spatial* Markov property
- Seems pretty Bayesian, Look at local texture generation using Bayesian ML

Build a vocabulary of K = 1000 textons or "visual words" or typical 50x50 patches
- Can then represent an image as a bag-of-visual words
- Then compare histogram of textons

Approaching creating a bank of textons, how to represent enough to generalize and pick the best 50x50 patches? Cluster and compare!

## K-Means
Start with randomly assigning centroids and iterate
Cost function here:
- Z is color of pixels, D is same dimensionality of the data
    - Look at the ith data point and compare with a centroid
    so Cost(X,Z,D) = Sum of distances squared
    - Min to Z for color and min to Z for centroids





