import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

def get_conn_by_mysql_connector():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="root",
        database="python_use"
    )
    return conn

def get_engine_by_sql_alchemy():
    db_user = 'root'
    db_password = 'root'
    db_host = 'localhost'  # 或 MySQL 服务器的 IP 地址
    db_port = '3306'  # MySQL 的默认端口号为 3306
    db_name = 'python_use'
    engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    return engine


if __name__ == '__main__':

    engine = get_engine_by_sql_alchemy()
    query = "select * from douban_book"
    sql_data = pd.read_sql(query, engine)
    print(sql_data.head())
    # 每次创建新表｜不建议
    # sql_data.to_sql("douban_book_copy", engine,if_exists='replace', index=False)
    # 在已存在表中追加
    sql_data.to_sql("douban_book_copy", engine,if_exists='append', index=False)


