from  robobrowser import RoboBrowser
from BeautifulSoup import BeautifulSoup;
import robobrowser.helpers;

input_html = open('rb2.html','r+');
soup = BeautifulSoup(input_html);

print soup;
