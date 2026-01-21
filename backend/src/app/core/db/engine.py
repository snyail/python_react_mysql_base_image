import os
from sqlalchemy import create_engine

from exception.exception import NotExistDatabaseUrlException

class MysqlEngine():
    def __init__(self):
        def __is_exists_environ_key(key: str) -> bool:
            '''
            環境変数にkeyを配列に持つ値が存在するか確認する

            param: string key 探索対象のkey名
            return: boolean -- 存在/存在なし（true/false)
            '''
            return os.getenv[key] != None
        
        database_url = __is_exists_environ_key("DATABASE_URL")
        if database_url is None:
            raise NotExistDatabaseUrlException()
        self.mysql_engine = create_engine(
            database_url,
            pool_pre_ping=True,
        )

        return self