# MixedScript
【本仓库放一些平时写的小脚本，有空搬到Gist】

1. 12306查票助手

12306不知道什么时候又更新了（链接里把query改成了queryA）。。写了一爬虫查票，还有个问题没有解决：

'https://kyfw.12306.cn/otn/leftTicket/queryA?purpose_codes=ADULT&leftTicketDTO.train_date=2017-01-04&leftTicketDTO.to_station=HZH&leftTicketDTO.from_station=BJP'

'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2017-01-04&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=HZH&purpose_codes=ADULT'

第一个GET请求无法返回数据。。难道还有针对参数顺序的反爬虫机制？还是见得太少了。。orz



base64加密脚本