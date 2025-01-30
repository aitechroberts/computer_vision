If you can interpret what an SVD (Singular Value Decomposition) is doing, then you know all about Linear Algebra

**Slide 25**
Orthonormal basis
    - V.T * V =  [1 0 
                 0 1 ] = 
                [v.T_1 * v_1   v.T_2 * v_1  
                 v.T_1 * v_2   v.T_2 * v_2 ]
**Slide 26**
So applying transformation here is
 P_1 = V_1.T * X
 P_2 = V_2.T * X               and then multiply each P_1 and P_2 by a Scale Factor (sigma) Not sum

C_1 = Sigma_1 * P_1
C_2 = Sigma_2 * P_2

Small sigma is a coordinate and Big Sigma is a Vector (collection of sigma coordinates)

c = SIGMA * P

How we are going to avoid multiplying by rows of all 0?

A is equivalent to the product of a horizontal vector and a vertical vector


Rank 1 A matrix, mapping all of the input space to a line. Low rank matrices are powerful and save compute

Corollary 0: Low-rank approximation
Take associated right singular vectors and associated left singular vectors
- The 3 largest singular values

Another way to get savings on the filter bank
- Write the filter bank as a matrix, then do low-rank approximation. Left and right singular values applied as separable filters
    - so 2500x48 * 48*12  rank 12 approximation
    - Filter by 12 basic filters at that point

Application of SVD as low-rank filter banks = PCA which eigenvectors of A.T * A rather than the singular vectors of A. So SVD of A is better

What “Separable” Usually Means
In image processing, a 2D filter  H(x,y) is called separable if it can be written as the product of two 1D filters:

H(x,y)=f(x)g(y).
For convolution, this means you can apply a 1D filter in one dimension (e.g., rows) and then another 1D filter in the other dimension (e.g., columns), rather than a single 2D convolution.
The result is computationally more efficient because a 2D convolution with a separable filter can be broken into two 1D convolutions.
Linear Combinations vs. Transformations of a Base Filter
When you say “a linear combination of vectors,” you usually mean something like
where V is a set of basis vectors (or basis filters), and are scalars.

Linear combination is more general:

A “transformation of a base filter” typically suggests operations like scaling, rotating, shifting, etc. of one template or kernel.
A linear combination of multiple “basis” filters can produce shapes or frequency responses not obtainable by merely transforming a single base filter.
Why basis filters are used:

Sometimes we choose a set of filters (e.g., wavelets, Gabor filters, principal components) that can span a rich space of possible filters or appearances.
By taking linear combinations, we can adapt to different patterns or frequency ranges in the image.
Separable filters as a product vs. sum:

In the strict sense, “separability” refers to rewriting a 2D filter as 

f(x)⋅g(y), so it is a product of two 1D filters.
We also can approximate non-separable filters by a sum of such separable terms:
is one separable component, and the total filter is a linear combination of these components.
Putting It All Together
In the context of separable filters, we often seek to decompose a 2D filter into a small set of 1D filters (each pair forming a separable component).
A single base filter transformed (scaled, rotated, shifted) usually will not capture all possible variations you might want in 2D filtering.
Instead, a set of basis filters—each possibly capturing different orientations or frequencies—lets you form a wide variety of 2D filters by linear combination.
Hence, while you can view a single separable component 

f(x)g(y) as derived from 1D filters “in each direction,” a linear combination of multiple such components is more general than just “transforming a single base filter.” It provides a richer way to construct or approximate arbitrary 2D filters.


Corollary 1: Positive Semi-Definite (Spectral Eigendecomposition)
- B is a positive number can be written as the square of any other number
    - So then B is the same as the above SVD equation but just with SIGMA^2

With all the left SVDs * SIGMA^2
- Can compute Eigenvalues of B and will get the V vector


Corollary 2: Homogenous Least Squares
- Apply the last column or the smallest Singular Vlaue

Corollary 3: Pseudoinverse
- Used to take the end result and find what transformation took place to make that happen

Corollary 4: Least Squares
- X that solves the problem trying to minimize ||Ax-b||^2
    - And fortunately (A.T * A)^(-1) * A.T
    - Faster to compute if A is an overdetermine system (A is tall and skinny)


Think of it like a linear auto-encoder
- Take the X number of SVD's to create a plane, then project the stuff from the image you want
    - Just the dot product of the vector with the SVD plane
    - Then project it back up z = u[:,:k].T * X
    X hat (recreated image) = u_1 * Z_1 + u_2 * Z_2 = the Z from above






