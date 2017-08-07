import requests
import sys

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","Upgrade-Insecure-Requests":"1","Connection":"close","User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36","Referer":"https://www.overleaf.com/teams/","Accept-Language":"en-US,en;q=0.8"}
cookies = {"wl_editor_position":"60.3877945669143%2525","__utmz":"256011733.1501268381.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)","hide_help_ride":"true","__cfduid":"dfa94658f4a2fb632886b66b56cef45a61501268382","mp_super_properties":"%7B%22all%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A//www.google.com/%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22Anonymous%22%3A%20false%2C%22Subdomain%22%3A%20%22writelatex%22%2C%22Product%22%3A%20%22UserVoice%22%2C%22distinct_id%22%3A%20%22413847013@writelatex%22%2C%22mp_name_tag%22%3A%20%22413847013@writelatex%22%7D%2C%22events%22%3A%20%7B%7D%2C%22funnels%22%3A%20%7B%7D%7D","__atuvc":"1%7C28%2C0%7C29%2C0%7C30%2C11%7C31","_gat":"1","_ga":"GA1.2.1015104215.1499969912","_write_latex_session":"RS90S0dWQ3ptS1AyVkZVejFXOGZBdmFSLzRVcytqbGJObGM4L3IwMWdYS25aQnFFdGxRYXJLc3poTGxkQ0czRXVISHdqVnZFbnZNSXRkM0ZpSFFTVGcrZVFPYWV6ZlVhTWFMS3JGNmZNeHd6VVQ1WFB3ZDAzQmlBUVMwRVQ2RVdrOGhaWDEyaU9KR052ZUNyQkRiOTZsZFVKVzh6alJzUkdhQit6WldmQU12cEE5a3ZjTTlkaHhtWWlOVXF3cXhKK1crVUlHdjhNVUtSOWhxVmIyWDdjMXIyVDJiY0E0OC9xLzRGL0RPTGZlTVFYUDF4UkNuMVZvK0ROUmNRdHZoOFJsWWViVmloaWkvQnBOcGIxN082OHJLalJXYitGSTd5eVMrc21JbHZRODVLNXZ1cjhJU3ZMSDh6SWpwdFg4U0MtLXA4cHY4Um9GQTlGQ0lDeUhQTHNTd1E9PQ%3D%3D--d753ece74077d876f6ebe80cfb0a663cb0acecfc","__utma":"256011733.1015104215.1499969912.1501268381.1501274785.2","_gid":"GA1.2.2113141071.1501425638"}

short_extensions = ['css','png','jpg','gif','txt','js','swf','bmp']
large_extensions = ['aif','aiff','css','au','avi','bin','bmp','cab','carb','cct','cdf','class','css','doc',' dcr',' dtd',' gcf',' gff',' gif',' grv',' hdml',' hqx',' ico',' ini',' jpeg',' jpg',' js',' mov',' mp3',' nc',' pct',' ppc',' pws',' swa',' swf',' txt',' vbs',' w32',' wav',' wbmp',' wml',' wmlc',' wmls',' wmlsc',' xsd',' zip']

auth = requests.Session()
results=[]
possible_result=[]
urls = sys.argv[1]
try:
	with open(urls,'r') as f:
		for j in f.readlines():
			j=j.strip('\n')
			j=j.strip('\r')
			url = j 
			#print url
			unsession = requests.get(url)
			session = auth.get(url, headers=headers, cookies=cookies)
			print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
			print '[+] Authenticated Detail [+]  '+'\n'
			print 'URL : '+session.url
			print 'Status Code : '+str(session.status_code)
			print 'Content Length: '+str(len(session.content))
			print '\n'
			print '[+] UnAuthenticated Details [+]  '+'\n'
			print 'URL : '+unsession.url
			print 'Status Code : '+str(unsession.status_code)
			print 'Content Length : '+str(len(unsession.content))+'\n'
			print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
			if unsession.history:
				for resp in unsession.history:
					print 'Redirected From : '+resp.url
					print 'With Status Code : '+str(resp.status_code)
					print '\n'
				print '\n~~~~~ATTACK~~~~~\n'
			for i in short_extensions:
				i = i.strip('\n')
				i = i.strip('\r')
				i = 'testsheet.'+i
				newurl=url+i
				newsession = auth.get(newurl, headers=headers, cookies=cookies)
				print 'Trying ... -> '+str(newurl)+'\n'
				conditionContent = str(len(newsession.content)+100) # To Avoid False Positivie

				#print conditionContent
				if len(newsession.content) == len(session.content) | (newsession.status_code) == (session.status_code):
					print '100% Cache at : '+newurl+str(newsession.status_code)+', Length:'+str(len(newsession.content))+'\n'
					results.append(newurl)
				elif len(session.content) > len(newsession.content) & (newsession.status_code) == (session.status_code):
					if conditionContent >= len(session.content):
						print 'Possible Cache at : '+newurl+str(newsession.status_code)+', Length:'+str(len(newsession.content))+'\n'
						possible_result.append(newurl)
				else:
					print 'Not Possible , Status code : '+str(newsession.status_code)+', Length:'+str(len(newsession.content))+'\n'

except KeyboardInterrupt as e:
	print 'Error occured : '+str(e)+'\n'
	pass

print '[+] Results '+str(len(results))+'\n'
print results

print '[+] Possible Results '+str(len(possible_result))+'\n'
print possible_result
