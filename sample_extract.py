#!/usr/bin/env python

# pip install google-play-scraper
from google_play_scraper import Sort, reviews
import pandas as pd
import parse


# get meta data, like review count, download counts and then tweak the later section for actual data extraction. 

# result = app(
#     'com.adswipe.jobswipe',
#     lang='en', # defaults to 'en'
#     country='us' # defaults to 'us'
# )

apps = ["https://play.google.com/store/apps/details?id=com.adswipe.jobswipe&hl=en_US&gl=US",
        "https://play.google.com/store/apps/details?id=com.jobget&hl=en_US&gl=US",
        "https://play.google.com/store/apps/details?id=com.harri.candidate&hl=en_US&gl=US",
        "https://play.google.com/store/apps/details?id=com.poachedjobs.mobile&hl=en_US&gl=US ",
        "https://play.google.com/store/apps/details?id=com.snagajob.jobseeker&hl=en_US&gl=US"]

for app_link in apps:
    app_id = parse("https://play.google.com/store/apps/details?id={}&hl=en_US&gl=US", app_link)
    result, continuation_token = reviews(
        app_id.fixed,
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=10000, # defaults to 100
        filter_score_with=None # defaults to None(means all score)
    )
    df_result = pd.DataFrame(result)
    df_result.to_csv("./data/submission_"+app_id.fixed.split(".")[-1]+".csv", index=False)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

# result, _ = reviews(
#     'com.adswipe.jobswipe',
#     continuation_token=continuation_token # defaults to None(load from the beginning)
# )




