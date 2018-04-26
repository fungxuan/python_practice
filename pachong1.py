import requests
url='http://www.baidu.com'
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
response=requests.get(url,headers=headers)
print(response.text)
#json字符串是字典变量类型的字符串的时候，对应字典中的key部分，注意是用双引号括起来，而不能是单引号，否则也是会导致json.loads出错的。