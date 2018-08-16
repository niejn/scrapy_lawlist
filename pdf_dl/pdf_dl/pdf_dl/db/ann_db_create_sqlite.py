from sqlalchemy import create_engine, Column, Integer, Sequence, DateTime, String, Numeric, func, Text
from sqlalchemy.ext.declarative import declarative_base


# source = 'sqlite:///ann_spiders.sqlite'
# engine = create_engine(source,echo=True)  # 生产库
Base = declarative_base()

class Announcement(Base):

    __tablename__ = 'announcement'
    id = Column(Integer, comment='id', primary_key=True, autoincrement=True)
    title = Column(String(100), comment='公告名称')
    last_modified_date = Column(DateTime(timezone=True), server_default=func.now())
    pub_date = Column(Integer, comment='公告发布日期')
    exchange =  Column(String(40), comment='交易所')
    pub_id = Column(String(40), comment='公告编号')
    body_text = Column(Text(), comment='公告正文')
    url = Column(Text(), comment='网页地址')


class VisitedURL(Base):
    __tablename__ = 'visitedurl'
    id = Column(Integer, comment='id', primary_key=True, autoincrement=True)
    last_modified_date = Column(DateTime(timezone=True), server_default=func.now())
    url = Column(Text(), comment='网页地址')
    # exchange =  Column(String(40), comment='交易所')

# Base.metadata.create_all(bind=engine, checkfirst=True, )

def creat_db(source_path='ann_spiders.sqlite'):
    global Base
    source = 'sqlite:///{path}'.format(path=source_path)
    engine = create_engine(source, echo=True)  # 生产库
    Base.metadata.create_all(bind=engine, checkfirst=True, )
    return


def main():
    # global Base
    # Base.metadata.create_all(bind=engine, checkfirst=True, )
    creat_db()
    return

if __name__ == '__main__':
    main()

