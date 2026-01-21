class MyException(Exception):
    def __init__(self, arg = None):
        self.arg = arg

class NotExistDatabaseUrlException(MyException):
    def __str__(self):
        return (
            "環境変数にデータベース接続用のURLが存在しません、環境変数を見直してください"
        )
