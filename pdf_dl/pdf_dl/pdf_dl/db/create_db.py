from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
                        DateTime, ForeignKey, Boolean, create_engine, func, text, Sequence)
from sqlalchemy.sql import insert
'''table = Table(
            table_name,
            metadata,
            Column('id', Integer, Sequence(table_name + '_id'), comment='id号', primary_key=True),
            Column('last_modified_date', DateTime, nullable=False),
            autoload=True
        )'''

'''
class AnnSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pub_date = scrapy.Field()
    exchange = scrapy.Field()
    pub_id = scrapy.Field()
    body_text = scrapy.Field()
    update_time = scrapy.Field()
    url = scrapy.Field()
'''

class DataAccessLayer:
    connection = None
    engine = None
    conn_string = 'sqlite:///exchange_v1.sqlite'
    metadata = MetaData()
    ranks = Table('RANKS',
                  metadata,
                  Column('ID', Integer, Sequence('RANKS_ID'), comment='id号', primary_key=True, autoincrement=True),
                  Column('EXCHANGE', String(50), comment='交易所名称'),
                  Column('RANK', Integer(), comment='名次'),
                  Column('CJ1', Integer(), comment='成交量'),
                  Column('CJ2', Integer(), comment='持买单量'),
                  Column('CJ3', Integer(), comment='持卖单量'),
                  Column('PARTICIPANTABBR3',  String(50), comment='期货公司会员简称3'),
                  Column('PARTICIPANTABBR2',  String(50), comment='期货公司会员简称2'),
                  Column('PARTICIPANTABBR1',  String(50), comment='期货公司会员简称1'),
                  Column('CJ3_CHG', Integer(), comment='比上交易日增减3'),
                  Column('CJ2_CHG', Integer(), comment='比上交易日增减2'),
                  Column('CJ1_CHG', Integer(), comment='比上交易日增减1'),
                  Column('INSTRUMENTID', String(50), comment='合约代码'),
                  Column('PRODUCTNAME', String(50), comment='合约品种'),
                  Column('PRODUCTSORTNO', Integer(), comment='productsortno'),
                  Column('PARTICIPANTID1', Integer(), comment='期货公司代码1'),
                  Column('PARTICIPANTID2', Integer(), comment='期货公司代码2'),
                  Column('PARTICIPANTID3', Integer(), comment='期货公司代码3'),
                  Column('UTC_DATE', DateTime(timezone=True), server_default=func.current_timestamp()),
                  Column('REPORT_DATE', DateTime,),
                  Column('VARIETY', Boolean(), comment='variety or instrument'),
                  )


    def db_init(self, conn_string=None):
        self.engine = create_engine(conn_string or self.conn_string ,echo=True)
        # self.engine.execute('''
        #     DROP TABLE IF EXISTS {name}'''.format(name='RANKS'))
        ans = self.metadata.create_all(self.engine)
        print(ans)
        # self.connection = self.engine.connect()

# new_table = Table(
#     'new_table',
#     metadata,
#     Column('id', Integer, Sequence('id_seq'), comment='id号',primary_key=True),
#     Column('time',DateTime,default=datetime.now()),
#     comment = '测试',
# )

source = 'sqlite:///exchange1.sqlite'
source = 'oracle://test2:test2@10.21.68.211:1521/hsfa?charset=utf8'
dal = DataAccessLayer()
dal.db_init(source)

