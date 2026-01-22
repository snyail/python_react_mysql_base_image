import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .exception.exception import NotExistDatabaseUrlException

class MysqlEngine():
    def __init__(self):
        def __is_exists_environ_key(key: str) -> bool:
            '''
            環境変数にkeyを配列に持つ値が存在するか確認する

            param: string key 探索対象のkey名
            return: boolean -- 存在/存在なし（true/false)
            '''
            return os.getenv(key) != None
        if __is_exists_environ_key("DATABASE_URL") is None:
            raise NotExistDatabaseUrlException()
        else:
            database_url = os.getenv("DATABASE_URL")

        self.mysql_engine = create_engine(
            database_url,
            pool_pre_ping=True,
        )

        self.session_local = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.mysql_engine,
        )

    def get_db_access(self) -> Session:
        db_handler = self.session_local()

        try:
            yield db_handler
        finally:
            db_handler.close()