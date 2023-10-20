# estimate-PSVR2-sales
Effort to estimate hardware unit sales of Sony PS VR2 based on relevant subreddit statistics and sparse official sales figures.

# Extended Description

Subreddit subscribers historically exhibit a linear correlation with sales of hardware.
However, the ratio of hardware sales to subscribers is highly platform- and subreddit-dependent.

Using the historical correlation between r/PSVR subscribers and PS VR sales from 2016-2022, this method
predicted PS VR2 sales of 684,000 within the first month.
A consulting firm hired by Bloomberg, IDC, predicted about 270,000-300,000 sales through March 2023, about 6 weeks after launch.
Sales figures released by Sony indicated 580,000 units of PS VR2 sold in the first 6 weeks, **so my estimate (27% error)
was considerably closer than that of IDC/Bloomberg (51% error), despite being based on the simple metric of 
subreddit statistics.**

I further found very strong linear correlation (R^2 > 0.99) between the reported PS VR2 sales by Sony in the first 
6 weeks and the subscriber numbers of the r/PSVR and r/psvr2 subreddits.

I have used these more recent linear regression fits to create updated estimates of PS VR2 sales.
r/psvr2 and r/PSVR give two indepedent estimates, allowing a crude estimate of uncertainty (68% and 95% CIs).

This script extracts the subscriber numbers from r/PSVR and r/psvr2 and estimates units of PS VR2 sold up to the
present date, as well as 66 and 95% confidence intervals.  A small correction factor is applied to each of the subscriber 
counts, in an attempt to account for the different approaches of the subreddits to the June 2023 Reddit blackout.  
r/PSVR went private while r/psvr2 merely prevented posts; this seems to have resulted in a temporary increase in the
rate of new subscribers for r/psvr2 and a cessation of new subscribers for r/PSVR for about 1 week, which I have attempted
to corret for with the constants corr1 and corr2.

In May 2023, the two estimates from r/PSVR and r/psvr2 were quite close, but have since diverged considerably,
leading to large uncertainty in the estimate.  

However, as of October 18, 2023 the most likely range of unit sales is **732,000-975,000** (68% CI), so a little 
less than 1 million units.  With a small holiday surge, it's fairly likely to cross the 1 million units mark by 
the end of 2023.

The validity of this method will be tested when the next batch of sales figures are released by Sony.

# Use

Download or clone estimatePSVR2sales.py into a local repository.  
Run at command line using `python estimatePSVR2sales.py`.
Estimates will be reported in the console window.

# License

BSD 3-Clause License

# Author

Alex Johnson-Buck (alebuck@umich.edu)
