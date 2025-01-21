
# Edges

## Canny Edges
3 std rule of thumb is simply statistics that 98% fall in that realm

A common method is to specify the filter size rather than set sigma, 3-tap and 5-tap Gaussian filter

How can we find pixels with high gradients and not find the noise?

Too large of a Gaussian filter can miss finer details aka finer edges

Mathematically sometimes equivalent to a finite difference filter

Naive Thresholding of gradient magnitude results in thick edges, how to thin it out?

### Canny Post Processing
Non-maximal suppression (Thinning)
- Check if pixel q is larger than neighbors along gradient direction, requires checking (nearest neighbor) interpolated pixels

Hysteresis thresholding
- Check max val of gradient value is sufficiently large

AKA morphological image processing or image dilation is what it's called in openCV
- special case of nonlinear binary image processing
    - Max over a local neighborhood defined by the structuring element (SE) set by a "mask"

Can also "erode" by min-ing rather than max-ing

## Filter banks
Take a Gaussian with 2 different covariances
Rather than a symmetric, just take a very long Gaussian and slowly rotate it
- Then take derivatives, 1st for edges and 2nd for bars "orientation"

Insert LeungMalik filter bank

#### Gabor filter
Take a gaussian and element-wise multply that with a cosine curve
- "modulate" gaussian with a cosine/sine wave
- Think about it like a dot product

## HOGs
Histograms of Oriented Gradients
- Alternative to Canny

#### SIFT image patch descriptor
Seems like convolving with a gaussian at a really small scale
- check demo_canny.ipynb

HOGs is faster because you compute gradients once on whole image and compute histograms of gradient orientation once. Slide over according to "bin size"




