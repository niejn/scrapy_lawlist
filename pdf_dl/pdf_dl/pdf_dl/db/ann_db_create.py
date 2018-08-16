from sqlalchemy import create_engine, Column, Integer, Sequence, DateTime, String, Numeric, func, Text
from sqlalchemy.ext.declarative import declarative_base


source = 'sqlite:///ann_spiders.sqlite'
engine = create_engine(source,echo=True)  # 生产库
Base = declarative_base()

# class AccountSummary(Base):
#
#     __tablename__ = 'r_g_kn_account_summary'
#
#     id = Column(Integer, Sequence('{table_name}_id'.format(table_name=__tablename__), start=1, increment=1), comment='id', primary_key=True, autoincrement=True)
#     last_modified_date = Column(DateTime(timezone=True), server_default=func.now())
#     holding_date = Column(Integer, comment='日期')
#     client_id = Column(String(40), comment='客户号')
#     balance_b_f = Column(Numeric(20, 2), comment='上次结算资金')
#     delivery_fee = Column(Numeric(20, 2), comment='交割手续费')
#     margin_occupied = Column(Numeric(20, 2), comment='保证金占用')
#     deposit_withdrawal = Column(Numeric(20, 2), comment='出入金')
#     fund_avail = Column(Numeric(20, 2), comment='可用资金')
#     realized_p_l = Column(Numeric(20, 2), comment='平仓盈亏')
#     delivery_fee = Column(Numeric(20, 2), comment='手续费')
#     mtm_p_l = Column(Numeric(20, 2), comment='持仓盈亏')
#     balance_c_f = Column(Numeric(20, 2), comment='期末结存')
#     risk_degree = Column(Numeric(12, 4), comment='风险度')
#     currency = Column(String(40), comment='Currency', default='CNY')


class Announcement(Base):

    __tablename__ = 'announcement'
    id = Column(Integer, Sequence('{table_name}_id'.format(table_name=__tablename__), start=1, increment=1),
                comment='id', primary_key=True, autoincrement=True)
    title = Column(String(100), comment='公告名称')
    last_modified_date = Column(DateTime(timezone=True), server_default=func.now())
    pub_date = Column(Integer, comment='公告发布日期')
    exchange =  Column(String(40), comment='交易所')
    pub_id = Column(String(40), comment='公告编号')
    body_text = Column(Text(), comment='公告正文')
    url = Column(Text(), comment='网页地址')


class VisitedURL(Base):
    __tablename__ = 'visitedurl'
    id = Column(Integer, Sequence('{table_name}_id'.format(table_name=__tablename__), start=1, increment=1),
                comment='id', primary_key=True, autoincrement=True)
    last_modified_date = Column(DateTime(timezone=True), server_default=func.now())
    url = Column(Text(), comment='网页地址')

Base.metadata.create_all(bind=engine, checkfirst=True, )

