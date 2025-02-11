DFT's put images into frequencies allows you to modify frequencies to change image
- So a low-pass filter allows the low frequencies through which makes it similar to a Gaussian filter
    - Blurs the image
    - also called anti-aliasing
        - Best one is called a sinc filter
    - Gaussian gradually lowers frequencies 
- High-pass filter basically keeps the edges
    - Looks similar to a Canny edge filter

Nyquist rate: Sample according to your highest frequency aka argmax()

# Anti-aliasing in resizing but not anymore
clean-FID works well
    - But PyTorch FID sucks and TF-FID sucks

Common to clean and improve pictures by DFT and then remove random "peaks" random like high frequencies

Phase contains more visual information than the magnitude



