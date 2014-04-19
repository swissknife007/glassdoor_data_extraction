from  robobrowser import RoboBrowser;
from bs4 import BeautifulSoup;
import robobrowser.helpers;
import json;
import sys;
"""
Take HTML file as input
return Summary,Employer,Employer,Location,Occupation,Pros,Cons etc

"""

def pre_process(soup):
	if soup == None or soup == []:
		return '';
	#print soup;
	if isinstance(soup,list):
	   return '';
	s = soup.encode('utf-8');
	#print(s);
	l = len(s);
	t='';
	i = 0;
	while(i < l):
		#print t;
		if(s[i] == '<'):
			if(i + 4 <= l):
				if(s[i+1]=='b' and s[i+2]=='r' and s[i+3]=='/' and s[i+4]=='>'):
					t = t + ' ';
					i = i + 5;
					continue;
				
			j = i + 1;
			while(j < l and s[j] != '>'):
				j = j + 1;
			i = j + 1;
		else :
			t = t + s[i]; 
			i = i + 1;
	return t;
    
def process_advice(desc):
	#print desc;
	#return '';
	
	#d = desc.encode('utf-8');
	d = desc;
	needle = 'Advice to Senior Management';
	l = len(needle);
	
	idx = d.find(needle);
	if(idx == -1):
		return 'Neutral';
	else:
		return d[idx + l:];
def process_recommendation(desc):
	d = desc;
	needle1 = 'Yes, I would recommend this company to a friend';
	needle2 = 'No, I would not recommend this company to a friend';
	needle3 = "Neutral";
	idx = d.find(needle1);
	if(idx != -1):
		return d[:idx],needle1;
	idx = d.find(needle2);
	if(idx != -1):
		return d[:idx],needle2;
	return d,needle3;


def process_outlook(desc):
	d = desc;
	needle1 =  "I'm optimistic about the outlook for this company";
	needle2 =  "I'm not optimistic about the outlook for this company";
	needle3 = "Neutral"
	idx = d.find(needle1);
	if(idx != -1):
		return d[:idx],needle1;
	idx = d.find(needle2);
	if(idx != -1):
		return d[:idx],needle2;
	return d,needle3,





file_name = sys.argv[1];     
input_html = open(file_name,'r+').read();

soup = BeautifulSoup(''.join(input_html));
if soup == None:
	print "None";

output_file = open(file_name+".txt",'w+');
output = 'Summary:'+ pre_process(soup.find('span',class_="summary"))+'\n';	
output_file.write((output));
output = 'Employer:'+ pre_process(soup.find('tt',class_="i-emp"))+'\n';
output_file.write((output));
output = 'Location:'+ pre_process(soup.find('div',class_="authorLocation"))+'\n';
output_file.write((output));
output = 'Occupation:'+ pre_process(soup.find('tt',class_="i-occ"))+'\n';
output_file.write((output));
desc = pre_process(soup.find('div',class_="description"));
output = 'Description:'+ desc +'\n';
output_file.write( (output));
output = 'Pros:'+ pre_process(soup.find('p',class_="pro"))+'\n';
output_file.write((output));
output = 'Cons:'+ pre_process( soup.find('p',class_="con"))+'\n';
output_file.write((output));
output = 'Date:'+ pre_process( soup.find('tt',class_="SL_date margBot5"))+'\n';
output_file.write((output));
outlook = process_outlook(desc)[1];
desc = process_outlook(desc)[0];
recommendation = process_recommendation(desc)[1];
desc = process_recommendation(desc)[0];
advice = process_advice(desc);
output = 'Advice to Management:'+ advice +'\n';
output_file.write((output));
output = 'Outlook:'+ outlook +'\n';
output_file.write((output));
output = 'Recommendation:'+ recommendation +'\n';
output_file.write((output));
#print soup;
