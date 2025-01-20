dot product is the length of each vector multiplied by each other and the cosine of their angle
- if 0, then orthogonal

www.cs.cmu.edu/~zkoler/course/linalg/index.html

Linear Time Invariance in 1D signal processing = Linear Shift Invariance in image processing

Any function can be written as a linear combination of shifted and scaled impulse responses

Any image as signal => F[i] = SUM(F[u] * Delta[i-u])
and T(F[i]) = SUM(F[u] * T(Delta[i-u]))
H[i] = T(delta[i]), G[i] = T(F[i]) === impulse response
==
G = F * H, H is either impulse response, filter, kernel
Think of the convolution operation is taking your filter and sliding it across your signal
- Can use parallel computation behind the scenes


Largest size of convolution is length of F = M  and length of H =N
so 'full' = N + M - 1 increases the size of the result by the filter minus 1
'valid' = N - M + 1  decreases the size of the result by the filter plus 1

Just don't flip the filter and it's correlation

Normalized cross-correlation is a little bit more invariant to illumination and light

Filtering is really a naive dot product between the filter and the image

