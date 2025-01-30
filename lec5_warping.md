# Warping

## Bilateral Filter
Tough to smooth with gaussian without fucking up the edges in an image

### Spatial Filtering vs Bilateral Filtering
Spatial = just the gaussian stuff
Bilateral looks at neighboring values and if they're significantly different, it basically 0s out that so that the weighted average of pixels stops there at the edge and doesn't blur the edge. 
- Walking grass to stones, big change detect? stop there and take similar pixels weighted average. Then, continue along

Filtering however changes pixel values whereas warping changes pixel coordinates



Check out Graphics on 5 Minutes on Youtube

So to conduct affine transformations, you just change the values in the identity matrix

Forward vs inverse warp
- Find out where you want the pixels to be, then use the inverse deal to figure out the transformation of how to make it happen
    - YOu can also bilinearly inerpolate
    