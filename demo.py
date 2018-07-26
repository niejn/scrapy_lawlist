# from scrapy import responset
from scrapy.utils import response
from scrapy.linkextractors import LinkExtractor

le = LinkExtractor(restrict_css='div.lawbox')
le = LinkExtractor(restrict_css='div.lawbox')
le.extract_links(response)
law_list = response.css('div.lawbox')
law_list.xpath('./ul/li/a/text()').extract_first()
law_list.css('ul li a::text').extract()
print(law_list.xpath('./ul/li/a/@title'))
print(law_list.css('ul li a::attr(href)').extract())
print(law_list.css('ul li a::attr(title)').extract())

# le = LinkExtractor(restrict_css='ul.pager li.next') contains(@id, 'result_') 下页>
le = LinkExtractor(restrict_css="div.page-no[text()='下页']")
# le = LinkExtractor(restrict_css='div.page-no[text=\'下页\>\']')
# response.css('.listWidget').xpath('.//*[contains(text(), "All versions")]').extract()
# le = LinkExtractor(restrict_xpaths='//div[@class="page-no"]/a[text()="下页>"]')
# response.css('span[property="city"]::text').extract_first()
'''
POST /login.php HTTP/1.1
Host: vip.biancheng.net
Connection: keep-alive
Content-Length: 77
Cache-Control: max-age=0
Origin: http://vip.biancheng.net
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://vip.biancheng.net/login.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=164d5d1212b397-0c676fcecd50d9-5e442e19-15f900-164d5d1212c31c; PHPSESSID=1kcsf3rsc422a31mm8779jtfd3; CNZZDATA3875484=cnzz_eid%3D1648041560-1532595546-http%253A%252F%252Fc.biancheng.net%252F%26ntime%3D1532595546; td_cookie=1763870692

username=test&password=1234&submit=%E7%99%BB%C2%A0%C2%A0%C2%A0%C2%A0%E5%BD%95
'''