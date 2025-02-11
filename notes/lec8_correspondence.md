

## Multi-View Geometry
**DinoV2** Currently the best descriptor of patches in an image to semantic correspondence
- And colmap

### Building the Algorithm
1. Points are matchable if small shifts always produce a large SSD error
- No matter where I shift the pixel, I produce a large error, but 0,0 produces no error
    - So then you force the algorithm to use points where u^2 + v^2 = 1
    - Speed it up with local taylor series expansion
- Corner detection ~ Lucas Kanade Alignment method
    - Equivalent to A matrix for a translation warp in LK alignment
        - A patch at (x0,y0) is a corner if there's a unique solution to one iteration of LK-alignment
    - When you hit a vector with an X vector on the left side and an X vector on the right side, you get a Quadratic Form
        - Generalizes to the linear functions of (x1,x2) to quadratic functions of (x1,x2)

## Harris Corner Detector
Determinant - alpha*Trace
- Because it uses eigenvalues, it's invariant to rotations and transformations
- Not however invariant to scale (aka zoom)
Scale- Use Scale-Space theory
- Put together to make the Harris-Laplacian detector
    - You integrate over a larger region the more you blur
    - In practice, affine estimation generally not done

## Scale-invariant Feature Transform (SIFT)
- Essentially a Gaussian pyramid allowing a fraction of Gaussians using different covariances all at one "octave" before moving to the next octave
    - Then at a 2nd-order derivative (taylor expansion) aka (Hessian) to get subpixel accuracy
    - If you don't build scale into coordinate frame for path finding for interesting points, you have to add that to the descriptor
        - So just add it to scale = cornerness(x, y, sigma), then descriptor has to handle rotations and affine viewpoint changes
    
