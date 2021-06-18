# Why this project ?
*This project based out of my hunt to grab my bike as soon as available*


Canyon bikes are one of the best bikes especially for mountain biking and Gravel rides. Which is why their bikes sell like hot cakes. Most Canyon bikes are sold within hours it is launched in the website. 

Tired of keeping tracking of the website, i have built this quick alert system which sends me email as soon as the Product the available. 

I scrape through Canyons website with some quick regex (with some help [here](https://stackoverflow.com/questions/67852325/scraping-text-after-a-span-in-with-regex-and-requests)), look for the product status and send an email once available. 


## Scheduling
To run this in background, we need to schedule this in crontab. 

Here is an example. Here i activate my virtual environment and run the script and save the log in a txt file. 

```
55 08 18 6 * cd /home/vra/Projects/canyon/ && /home/vra/Projects/canyon/env/bin/python3 /home/vra/Projects/canyon/canyon/alerts/alerts.py > /tmp/cronlog.txt 2>&1
```


