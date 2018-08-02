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
Cookie: UM_distinctid=164d5d1212b397-0c676fcecd50d9-5e442e19-15f900-164d5d1212c31c; 
PHPSESSID=1kcsf3rsc422a31mm8779jtfd3; 
CNZZDATA3875484=cnzz_eid%3D1648041560-1532595546-http%253A%252F%252Fc.biancheng.net%252F%26ntime%3D1532595546; 
td_cookie=1763870692

username=test
&password=1234
&submit=%E7%99%BB%C2%A0%C2%A0%C2%A0%C2%A0%E5%BD%95

username=123&password=123&submit=%E7%99%BB%C2%A0%C2%A0%C2%A0%C2%A0%E5%BD%95
'''
fd = {'username': 'niejn', 'password': 'cxf8922470', 'submit': '%E7%99%BB%C2%A0%C2%A0%C2%A0%C2%A0%E5%BD%95'}
sel = response.xpath('//form[@id="reg-login-form"]//input')
{'username':'niejn', 'password':'cxf8922470', 'submit':'%E7%99%BB%C2%A0%C2%A0%C2%A0%C2%A0%E5%BD%95'}
from scrapy.http import FormRequest
request = FormRequest.from_response(response, formdata=fd)
fetch(request)
'''
UM_distinctid=164d5d1212b397-0c676fcecd50d9-5e442e19-15f900-164d5d1212c31c; 
PHPSESSID=1kcsf3rsc422a31mm8779jtfd3; 
td_cookie=1825436122; 
CNZZDATA3875484=cnzz_eid%3D1648041560-1532595546-http%253A%252F%252Fc.biancheng.net%252F%26ntime%3D1532658097;
 username=niejn; userdata=d1barWcIB1rNLK%2FuHIvPQVLhQqDnOWxG2EbW7J3Sjnu4UyOawGZ224Bd9sHqW6Zt67Ex7mCQCqBEKEelvQ_7_0; 
 userdataencode=7df0BAMX%2FEg%2FFRA8fM3j0De%2F9iLS1xwTMe5fRaYdaG6baHUKYAY
 
 
'''

'''
Cookie: 
td_cookie=1827088135; 
UM_distinctid=164d5d1212b397-0c676fcecd50d9-5e442e19-15f900-164d5d1212c31c; 
CNZZDATA4153548=cnzz_eid%3D1734078255-1532590687-%26ntime%3D1532654657; 
CNZZDATA3875484=cnzz_eid%3D1089615187-1532655279-http%253A%252F%252Fc.biancheng.net%252F%26ntime%3D1532655279; 
username=niejn; 
userdata=d1barWcIB1rNLK%2FuHIvPQVLhQqDnOWxG2EbW7J3Sjnu4UyOawGZ224Bd9sHqW6Zt67Ex7mCQCqBEKEelvQ_7_0; 
userdataencode=7df0BAMX%2FEg%2FFRA8fM3j0De%2F9iLS1xwTMe5fRaYdaG6baHUKYAY
'''
'''
td_cookie=1828635565; 
td_cookie=1828181516; 
UM_distinctid=164d5d1212b397-0c676fcecd50d9-5e442e19-15f900-164d5d1212c31c; 
CNZZDATA3875484=cnzz_eid%3D1089615187-1532655279-http%253A%252F%252Fc.biancheng.net%252F%26ntime%3D1532655279; 
username=niejn; 
userdata=d1barWcIB1rNLK%2FuHIvPQVLhQqDnOWxG2EbW7J3Sjnu4UyOawGZ224Bd9sHqW6Zt67Ex7mCQCqBEKEelvQ_7_0; 
userdataencode=7df0BAMX%2FEg%2FFRA8fM3j0De%2F9iLS1xwTMe5fRaYdaG6baHUKYAY; 
CNZZDATA4153548=cnzz_eid%3D1734078255-1532590687-%26ntime%3D1532658914
'''
cookies ={
        'td_cookie':1828635565,
        'UM_distinctid':'164d5d1212b397-0c676fcecd50d9-5e442e19-15f900-164d5d1212c31c',
        'CNZZDATA4153548':'NZZDATA4153548=cnzz_eid%3D1734078255-1532590687-%26ntime%3D1532658914',
        'CNZZDATA3875484':'cnzz_eid%3D1089615187-1532655279-http%253A%252F%252Fc.biancheng.net%252F%26ntime%3D1532655279',
         'username':'niejn',
        'userdata':'d1barWcIB1rNLK%2FuHIvPQVLhQqDnOWxG2EbW7J3Sjnu4UyOawGZ224Bd9sHqW6Zt67Ex7mCQCqBEKEelvQ_7_0',
        'userdataencode':'7df0BAMX%2FEg%2FFRA8fM3j0De%2F9iLS1xwTMe5fRaYdaG6baHUKYAY',

          }

'''
td_cookie=1827088135; 
CNZZDATA4153548=cnzz_eid%3D1734078255-1532590687-%26ntime%3D1532654657; 
CNZZDATA3875484=cnzz_eid%3D1089615187-1532655279-http%253A%252F%252Fc.biancheng.net%252F%26ntime%3D1532655279; 
userdata=d1barWcIB1rNLK%2FuHIvPQVLhQqDnOWxG2EbW7J3Sjnu4UyOawGZ224Bd9sHqW6Zt67Ex7mCQCqBEKEelvQ_7_0; 
username=niejn; userdataencode=7df0BAMX%2FEg%2FFRA8fM3j0De%2F9iLS1xwTMe5fRaYdaG6baHUKYAY; 
UM_distinctid=164d5d1212b397-0c676fcecd50d9-5e442e19-15f900-164d5d1212c31c
'''
request_with_cookies = Request(url="http://c.biancheng.net/cpp/biancheng/view/2995.html", cookies=cookies,
                               headers={'Referer':'http://c.biancheng.net/cpp/biancheng/cpp/rumen/'})



#
# Just remove all pipelines from main settings and use this inside spider.
#
# This will define the pipeline to user per spider


# class testSpider(InitSpider):
#     name = 'test'
#     custom_settings = {
#         'ITEM_PIPELINES': {
#             'app.MyPipeline': 400
#         }
#     }