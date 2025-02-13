#Asia Acosta Machine Assignment 3

I have included 2 seperate graphs, one that was created in Excel and one that was created in Google Sheets, but they are both the same. I did have a hard time figuring out how to make both axes into the logarithmic scale, but for sure the y-axis is in the logarithmic scale. 

To run MA3.py, use the following command: python3 -u "/Users/asiaacosta/Documents/GitHub/CS417_SPR2025/machine assignments/MA3/MA3.py" 


##After examining the graph
</br> The minimum value for the magnitude of the error is aproximately 0.000000000545510747684829, or 5.46E-10. This occurs at 2 different h-values: 2^-27 & 2^-28. </br>
</br> To compare it to $\sqrt{esp}$, lets look at the ratios: </br>
</br> $\frac{minimum value for magnitude of error}{actual estimated precision}$ </br>
</br> = $\frac{0.000000000545510747684829}{1.4901161193847656e-08}$ </br>
</br> = $\frac{5.46E-10}{1.49E-08}$ </br> 
</br> $\approx$ 0.0367 ... which as a percentage is 3.67% </br>
This means that the minimum absolute error is roughly 3.67% of $\sqrt{esp}$; the minimum absolute error is a small, small, SMALL fraction of the square root of estimated precision</br>
The relevance of the minimum absolute error being so much smaller than $\sqrt{esp}$ is that our calculation is pretty accurate. 

