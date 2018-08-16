from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine = create_engine('oracle://test2:test2@10.21.68.211:1521/hsfa?charset=utf8',echo=True)
source = 'oracle://sc:sc2017@10.21.69.198:1521/riskdb?charset=utf8'
source = 'oracle://test2:test2@10.21.68.211:1521/hsfa?charset=utf8'
engine = create_engine(source,echo=True)  # 生产库


from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import *
from sqlalchemy.sql import select
import sqlalchemy as sa


Base = declarative_base()

class AccountSummary(Base):

    __tablename__ = 'r_g_kn_account_summary'

    id = Column(Integer, Sequence('{table_name}_id'.format(table_name=__tablename__), start=1, increment=1), comment='id', primary_key=True, autoincrement=True)
    last_modified_date = Column(DateTime(timezone=True), server_default=func.now())
    holding_date = Column(Integer, comment='日期')
    client_id = Column(String(40), comment='客户号')
    balance_b_f = Column(Numeric(20, 2), comment='上次结算资金')
    delivery_fee = Column(Numeric(20, 2), comment='交割手续费')
    margin_occupied = Column(Numeric(20, 2), comment='保证金占用')
    deposit_withdrawal = Column(Numeric(20, 2), comment='出入金')
    fund_avail = Column(Numeric(20, 2), comment='可用资金')
    realized_p_l = Column(Numeric(20, 2), comment='平仓盈亏')
    delivery_fee = Column(Numeric(20, 2), comment='手续费')
    mtm_p_l = Column(Numeric(20, 2), comment='持仓盈亏')
    balance_c_f = Column(Numeric(20, 2), comment='期末结存')
    risk_degree = Column(Numeric(12, 4), comment='风险度')
    currency = Column(String(40), comment='Currency', default='CNY')






Base.metadata.create_all(bind=engine, checkfirst=True, )
