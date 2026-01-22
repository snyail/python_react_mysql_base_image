from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from core.db.engine import MysqlEngine

mysql_engine = MysqlEngine()

app = FastAPI()

@app.get("/health")
def health(db: Session = Depends(mysql_engine.get_db_access)):
    return {
        "status": "ok",
        "db_type": str(type(db))
    }