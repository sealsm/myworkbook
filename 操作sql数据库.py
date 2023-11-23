#coding:utf-8
'''
mysql数据库常用操作-操作数据库文件
'''
import mysql.connector
from mysql.connector import Error

# 连接MySQL数据库函数：
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f"The error '{e}' occurred.")

    return connection

# 调用函数执行连接
connection = create_connection('localhost','root','toor','reader')

# 写操作函数：
def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('query executed successfully')
        cursor.close()
    except Error as e:
        print(f'The Error {e} occurred.')

# 读操作函数：
def execute_read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'The Error {e} occurred.')
    cursor.close()

# 调用写函数建表
create_user_table = '''
create table if not exists users(
id int auto_increment,
name text not null,
age int,
gender text,
primary key(id)
)engine = InnoDB
'''
#execute_query(connection, create_user_table)


# 调用写函数插入记录：注意`user`, `name`, `age`, `gender`，不适用引号包裹，而是键盘左上角的撇号
insert_user = '''
insert into
`users` (`name`, `age`, `gender`)
values
('zhangsan',23,'male'),
('lisi',24,'female'),
('wangwu',25,'male');
'''
#execute_query(connection,insert_user)


# 调用读函数查询记录
select_users = 'select * from users'
users = execute_read_query(connection,select_users)
for user in users:
    print(user)

# 关闭连接
if connection.is_connected():
    connection.close()
    print('connection closed')
