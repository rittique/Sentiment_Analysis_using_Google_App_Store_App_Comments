#!/usr/bin/env python

# pip install google-play-scraper
from google_play_scraper import Sort, reviews #Importing sort and reviews from google_play_scrapper
import pandas as pd #Importing pandas library
import parse #Importing parse libarary, parse is an externaly library which needs to be installed explicitly in 
            #in order to be used as a string parser
from os.path import exists#to get the path to a directory

# get meta data, like review count, download counts and then tweak the later section for actual data extraction. 

# result = app(
#     'com.adswipe.jobswipe',
#     lang='en', # defaults to 'en'
#     country='us' # defaults to 'us'
# )

#List to store the links of each of the apps

apps = ["https://play.google.com/store/apps/details?id=com.adswipe.jobswipe&hl=en_US&gl=US",
        "https://play.google.com/store/apps/details?id=com.jobget&hl=en_US&gl=US",
        "https://play.google.com/store/apps/details?id=com.harri.candidate&hl=en_US&gl=US",
        "https://play.google.com/store/apps/details?id=com.poachedjobs.mobile&hl=en_US&gl=US",
        "https://play.google.com/store/apps/details?id=com.snagajob.jobseeker&hl=en_US&gl=US"]
# A loop to iteration through all the links
for app_link in apps: #app_link holds each of the string links
    # parse.parse() function matches two strings and 
    #using the fixed function it shows the deficit betweent he two strings
    app_id = parse.parse("https://play.google.com/store/apps/details?id={}&hl=en_US&gl=US", app_link) 
    # result is dictonary which holds data that the review function returns 
    result, continuation_token = reviews(
        # app_id.fixed returns a tuple, and we need a string which doesn't have
        # brackets or comas, thus, to remove the unwanted we took a substring
        str(app_id.fixed)[2:-3], 
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=10000, # defaults to 100
        filter_score_with=None # defaults to None(means all score)
    )
    df_result = pd.DataFrame(result) #pandas DataFrame() funciton takes dictionary
    #as an argument and returns a dataframe
    fname = "./data/submission_"+str(app_id.fixed)[2:-3].split(".")[-1]+".csv" 
    # Saving the csv in the prescribed format
    if not exists(fname): 
        #checking if the file already exists
        #if not then saving it
        df_result.to_csv(fname, index=False)
    else:
        pass
    
# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

# result, _ = reviews(
#     'com.adswipe.jobswipe',
#     continuation_token=continuation_token # defaults to None(load from the beginning)
# )




