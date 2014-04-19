from robobrowser import RoboBrowser;
import BeautifulSoup;
"""
Take HTML file as input
return well indented HTML file using freeformatter.com
"""
input_html = open('rb2.html','r+');
browser = RoboBrowser(history=True);
main_url = 'http://www.freeformatter.com/html-formatter.html';
browser.open(main_url);
#print browser.find();
#print browser.response.text;
forms = browser.get_forms();
form_counter = 1;
#for f in forms:
# print f,'\n',++form_counter;
"""
<RoboForm action=, inputstring=, inputurl=, indent=3spaces, forcenewwindow=false> 
"""
form = browser.get_form(action='/html-formatter.html');
#print form;
form['inputstring'] = input_html;
form['forcenewwindow'] = 'false';
browser.submit_form(form);
#print browser;
resp = browser.response.content;
output_file = open('rb3.html','w+');
output_file.write(resp);

