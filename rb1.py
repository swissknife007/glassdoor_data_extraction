import re
from robobrowser import RoboBrowser
# Browse to Rap Genius
browser = RoboBrowser(history=True)
browser.open('http://rapgenius.com/')

    # Search for Queen
form = browser.get_form(action='/search')
form # <RoboForm q=>
form['q'].value = 'queen'
browser.submit_form(form)
# Look up the first song
songs = browser.select('.song_name')
browser.follow_link(songs[0])
lyrics = browser.select('.lyrics')
print lyrics[0].text      # \n[Intro]\nIs this the real life...
