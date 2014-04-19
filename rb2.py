import re
from robobrowser import RoboBrowser
# Browse to Rap Genius
browser = RoboBrowser(history=True)
s = browser.open('http://www.glassdoor.com/Reviews/Employee-Review-Adobe-RVW3950149.htm')

print browser;
f=open("rb2.html","w+");
f.write(str(browser.response.text));

