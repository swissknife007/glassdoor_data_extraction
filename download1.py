import urllib2

url_name = "http://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3";
output_file = open('download1.out','w+');
response = urllib2.urlopen(url_name);
html = response.read();
output_file.write(html);
