# import json
# from datetime import datetime
#
# from motor.motor_tornado import MotorDatabase
# from tornado.httpclient import AsyncHTTPClient
#
# url = 'https://techcrunch.com/wp-json/tc/v1/crunchbase/unicorns?cachePrevention=0'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
# }
#
#
# def unicorns_collect(db: MotorDatabase):
#     unicorns = db.unicorns
#     http_client = AsyncHTTPClient(force_instance=True, defaults=headers)
#     while True:
#         try:
#             response = await http_client.fetch(url, validate_cert=False, connect_timeout=10)
#         except Exception as e:
#             print(f'接口请求异常: {e}')
#         else:
#             print(f'接口请求成功: [{response.code} {response.reason}] {int(response.request_time * 1000)}ms')
#             # 获取接口数据并增加文档创建时间戳
#             data = json.loads(response.body)
#             data['meta']['created_at'] = datetime.now()
#             unicorns.insert_one(data)
