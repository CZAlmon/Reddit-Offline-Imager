# Reddit-Offline-Imager
Given a hard coded list of subreddit names, this program will use praw, selenium, and phantom.js to screenshot the top 25 subreddit submissions to view later.


This version works 100%. I have not encountered any bugs as of yet. This file will download screenshots of each subreddit submission. 

One thing about this is if the submission is flagged as 'NSFW' then a page warning you of this fact will be screenshot instead of the submission webpage. UPDATED (7/29/15): Using Firefox instead of PhantomJS I was able to add another picture after I try to 'submit' the Over 18 button. This should allow me to see the reddit page that was posted and contains the comments/user content
