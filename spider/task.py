import requests
from logging import getLogger

from spider.db import MongoDB

# from spider.log import get_logger

# logger = get_logger('FileLogger')
logger = getLogger(__file__)


class TechCrunchSpider(object):

    def __init__(self):
        self.url = 'https://techcrunch.com/wp-json/tc/v1/crunchbase/unicorns?'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        self.params = {
            'cachePrevention': 0
        }

    def get_unicorns(self) -> dict:
        """
        获取接口返回的数据
        :return: 数据
        """
        try:
            response = requests.get(url=self.url, headers=self.headers, params=self.params, timeout=5)
            if response.status_code == 200 and len(response.content):
                logger.info('接口请求成功')
                return response.json()
            else:
                raise Exception(f'请求异常：{response.status_code} {len(response.content)}')
        except Exception as e:
            logger.error(e)

    def save_unicorns(self) -> None:
        unicorns = self.get_unicorns()
        with MongoDB(host='localhost', port=27017, db_name='techcrunch', collection_name='unicorns') as db:
            if not db.find_one({'meta.updated_at': unicorns['meta']['updated_at']}):
                db.insert_one(unicorns)
                logger.info('数据写入成功')
            else:
                logger.info('数据已存在, 无需重复写入')


if __name__ == '__main__':
    # Just for test
    spider = TechCrunchSpider()
    spider.save_unicorns()
