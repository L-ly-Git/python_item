import requests
import prettytable as pt
import json

#获取关键参数，城市编号，出发时间
with open("data.json", 'r', encoding='utf-8') as f:
    datas = f.read()
citys = json.loads(datas)

from_station = input("请输入出发城市:")
to_station = input("请输入到达城市:")
train_date = input("请输入出发时间(YYYY-MM-DD): ")

#确定请求链接
url = f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={train_date}&leftTicketDTO.from_station={citys[from_station]}&leftTicketDTO.to_station={citys[to_station]}&purpose_codes=ADULT'
# url = 'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date=2026-08-10&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
print(train_date,citys[from_station],citys[to_station])
#模拟浏览器
headers = {
    'Cookie':'_uab_collina=178634047275356895353026; JSESSIONID=094769EFAEF28F97A8A2DB55DC24E00B; SF_cookie_2=34555212; BIGipServerotn=2880570378.38945.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=1005060362.50215.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2026-08-10; _jc_save_toDate=2026-08-10; _jc_save_wfdc_flag=dc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.7271 SLBChan/112 SLBVPV/64-bit'
}
response = requests.get(url=url,headers=headers)

print(response)

#实例化pt对象
tb = pt.PrettyTable()
tb.field_names=[
'序号',
'车次',
'出发时间',
'到达时间',
'耗时',
'特等座',
'一等座',
'二等座',
'硬卧',
'硬座',
'无座',
'软卧'
]
post = 1
for item in response.json()['data']['result']:
    arr = item.split('|')
    num = arr[3] #车次
    start_time = arr[8] #出发时间
    end_time = arr[9] #到达时间
    use_time = arr[10] #耗时
    topGrade = arr[32] #特等座
    firstGrade = arr[31] #一等座
    secondGrade = arr[30] #二等座
    hard_sleeper = arr[28] #硬卧u
    hard_seat = arr[29] #硬座
    no_seat = arr[26] #无座
    soft_sleeper = arr[23] #软卧u

    # dit = {
    #     '车次':num,
    #     '出发时间':start_time,
    #     '到达时间':end_time,
    #     '耗时':use_time,
    #     '特等座':topGrade,
    #     '一等座':firstGrade,
    #     '二等座':secondGrade,
    #     '硬卧':hard_sleeper,
    #     '硬座':hard_seat,
    #     '无座':no_seat,
    #     '软卧':soft_sleeper
    # }

    tb.add_row([post,num,start_time,end_time,use_time,topGrade,firstGrade,secondGrade,hard_sleeper,hard_seat,
                no_seat,soft_sleeper])
    post+=1
"""
    #获取索引
    a = 0
    for i in arr:
        print(i,a,sep='--')
        a+=1
    # break 
"""

print(tb)