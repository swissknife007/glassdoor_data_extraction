from  robobrowser import RoboBrowser;
from bs4 import BeautifulSoup;
import robobrowser.helpers;
import json;
"""
Take HTML file as input
return well indented HTML file using freeformatter.com
"""
input_html = open('sample.html','r+').read();
#print input_html;
#browser = RoboBrowser(history=True);
#main_url = 'http://www.freeformatter.com/html-formatter.html';
#browser.open(main_url);
#print browser.find();
#print browser.response.text;
#forms = browser.get_forms();
#form_counter = 1;
#for f in forms:
# print f,'\n',++form_counter;
"""
<RoboForm action=, inputstring=, inputurl=, indent=3spaces, forcenewwindow=false> 
"""
#form = browser.get_form(action='/html-formatter.html');
#print form;
#form['inputstring'] = input_html;
#form['forcenewwindow'] = 'true';
#browser.submit_form(form);
#print browser;
resp = input_html;
#print resp;
soup = BeautifulSoup(resp);
#soup = soup.prettify();

#print soup;
#print soup.body.div
if soup == None:
	print "None";
	
print soup.find('pre',id='htmlOutput').text;

#print soup;
