#Version 0.2.0
#Author: Zach Almon

import urllib.request
import os
import platform
import praw
import time
from selenium import webdriver

#To get Unix and Windows
platformType = platform.system()


def main():

    reddit_url = 'http://www.reddit.com/r/'
    url_part_2 = '/comments/'

    #   reddit_url + 'subreddit' + url_part_2 + 'post.name[3:]' + /?limit=500

    list_of_subreddits = []
    list_of_subreddits.append('askreddit')
    list_of_subreddits.append('todayilearned')
    list_of_subreddits.append('games')
    list_of_subreddits.append('gaming')
    list_of_subreddits.append('worldnews')
    list_of_subreddits.append('news')
    list_of_subreddits.append('science')
    list_of_subreddits.append('upliftingnews')
    list_of_subreddits.append('writingprompts')
    list_of_subreddits.append('pettyrevenge')
    list_of_subreddits.append('books')
    list_of_subreddits.append('tifu')
    list_of_subreddits.append('diy')
    list_of_subreddits.append('buildapc')
    list_of_subreddits.append('python')
    list_of_subreddits.append('c_programming')
    list_of_subreddits.append('skyrim')
    list_of_subreddits.append('civ')
    list_of_subreddits.append('manga')
    list_of_subreddits.append('naruto')
    list_of_subreddits.append('onepiece')
    list_of_subreddits.append('pokemon')

    #praw 'Reddit' Object
    r = praw.Reddit(user_agent='Reddit Webpage Downloader')

    #Directorys

    currentDirectory = os.getcwd()

    if platformType == 'Windows':
        MASTERdirectoryName = currentDirectory + "\\Reddit_Image_Folder"

    else:
        MASTERdirectoryName = currentDirectory + "/Reddit_Image_Folder"
    
    try: 
        os.makedirs(MASTERdirectoryName)
    except OSError:                    
        if not os.path.isdir(MASTERdirectoryName):
            raise

    os.chdir(MASTERdirectoryName)

    list_of_urls = []
    list_of_titles = []

    #Executable path Must be whatever path on your local machine to phantomjs.exe
    #This can be downloaded from the PhantomJS Website.

    #driver = webdriver.PhantomJS(executable_path = currentDirectory + "\\VS\\PhantomJS\\bin\\phantomjs.exe")
    driver = webdriver.Firefox()
    driver.set_window_size(1366, 768)

    #Right now this runs once every hour.
    #The loop may take longer than an hour depending on internet/urllib speed
    #Could adjust frequency by adjusting the time_to_wait line.
    #Number in time_to_wait (5400) is an int in seconds.
    #Right now 7200 - difference makes it wait so that each loop is an 2 hours long
    #You could make it 1800 - difference for 30 minutes, 3600 for an hour, or 5400 for every 1.5 hours.

    while True:

        start_time = time.clock()

        #Time to use as a new directory name. (Year-Month-Day Hour-Minute AM/PM)
        string_time = time.strftime('%Y-%m-%d %I-%M %p', time.localtime())
        
        if platformType == 'Windows':
            new_directory = MASTERdirectoryName + "\\" + string_time

        else:
            new_directory = MASTERdirectoryName + "/" + string_time

        try: 
            os.makedirs(new_directory)
        except OSError:                    
            if not os.path.isdir(new_directory):
                raise

        os.chdir(new_directory)

        list_of_urls = []
        list_of_titles= []
        
        #Loop to Get Lists of URLs and Titles for the Images
        for i in range(len(list_of_subreddits)):

            counter = 0

            print("Downloading Subreddit:", list_of_subreddits[i])

            #"r.get_subreddit(list_of_subreddits[i]).get_top(limit=25)" is an iterator for each of the top submissions
            for post in r.get_subreddit(list_of_subreddits[i]).get_top(limit=25):
                
                counter += 1
                #post.name gives a unique identifer for the URL of a submission
                temp = post.name
                #post.name laways starts with t3_ which is not needed
                temp = temp[3:]
                
                list_of_urls.append(reddit_url + list_of_subreddits[i] + url_part_2 + temp + '/?limit=500')

                list_of_titles.append(list_of_subreddits[i] + ' submission number - ' + str(counter))

        #Reddit Doesn't like when you make requests less than 2 seconds apart. 
        #I give a buffer here from the praw requests to my selenium requests
        time.sleep(15)

        for i in range(len(list_of_urls)):

            print("Downloading webpage %d" % (i), end="", flush=True)
            print("\r", end="", flush=True)

            temp_string = list_of_urls[i]

            time.sleep(3)
            
            driver.get(list_of_urls[i])
            driver.save_screenshot(list_of_titles[i] + '.jpg')

            #driver.find_element_by_name("over18").click()  #Click doesnt work
            driver.find_element_by_name("over18").submit()  #Submit works on Firefox

            driver.save_screenshot(list_of_titles[i] + '_2.jpg')

        

        #Get the time to wait to where from start_time to the next start_time should be exactly 1.5 hours
        end_time = time.clock()
        difference = end_time - start_time
        time_to_wait = 7200 - difference


        #If for some reason the downloading takes longer than 1.5 hours then go ahead and go to next loop otherwise wait
        if int(time_to_wait) < 0:
            pass
        else:
            print('\n\nWaiting %d seconds' % (int(time_to_wait)))
            time.sleep(int(time_to_wait))
    
        


  

main()
