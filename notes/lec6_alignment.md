# Alignment
- Often used for tracking

### Estimating motion from Correspondences
- If we know all the starting and ending points, then $A*x=B$
    - numpy.linalg.solve(A,b) because X is simply the vector of the unknowns for the transformation
        - When is A invertible, if the points are not co-linear
    - And if trying to find the best affine transformation to execute that, then you just use leastsquares
        - numpy.linalg.lstsq(A,b), argmin of (B' - B)

### Piecewise affine warps
Triangles are god, can be changed for anything especially if you're doing piecewise
- Simple linear interpolation to find the intermediate vector

Instance of vision as inverse graphics 

# Local search with gradient descent
- Essentially starting somewhere and seemingly conducting gradient descent across the picture to find where your tracking object fits

But we can do better and open up our optimization toolbox
- Gaussian optimization

## Nonlinear optimization
- Approximate a complicated function (or error surface) with a Taylor series
- Generalize the first derivate to 2nd derivative and so on
    - Hessians are symmetric square matrix? Only for convex function
        - Because top right and bottom left values are the same
    
The source of nonlinearity is the image which is naturally nonlinear (neighboring pixels can have no relation)
- So essentially we will linearize the image

Jacobian Matrix ( matrix of partial derivatives)
- Rate of change of the warp
**So basically google Jacobians and Hessians**

Slide for how to solve LK
- Dimensions of B are number of pixels in template
- A equals number of unknowns (6 for affine)
    - So the (almost) approximate Hessian is 6x6 and always semi-definite because it's the local curvature of the thing when convex

Solve with np.linalg.lstsq(A,b) or np.linalg.SVD(A)

## Steps to Algoright
- nonlinear least squares optimization vs Gauss-Newton descent
    - Get jacobian J(u) of multivariate function
1. First order method (gradient descent)
    - You could do a descent inside the the minimum squared error
    **Gauss-Newton Descent**
        - Essentially fitting parabolas to your descent
2. 
