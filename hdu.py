#coding=utf-8
#!/usr/bin/python
import re;
import urllib;
import urllib2;

def get_html(opener,pid):
	url = "http://acm.hdu.edu.cn/showproblem.php?pid=" + pid;
	headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'};
	req = urllib2.Request(url = url, headers = headers);
	html = opener.open(req).read().decode('gbk').encode('utf8');
	return html;



if __name__ == '__main__':
	opener = urllib2.build_opener();
	#a,b = input("input pid range(Separated by ','):");
	a,b = 1000,1000;
	map = {};
	for i in range(a,b + 1):
		html = get_html(opener, str(i));
		