import yaml
import sqlite3
import os

'''将数据库的表格转换成yaml文件'''

def convert_to_yaml(database, table, output_file):
    # 连接数据库
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # 查询表数据
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    # 构建数据列表
    data = []
    for row in rows:
        data.append(dict(zip([column[0] for column in cursor.description], row)))

    # 获取输出文件的绝对路径
    output_path = os.path.abspath(output_file)

    # 将数据写入YAML文件
    with open(output_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

    # 关闭数据库连接
    cursor.close()
    conn.close()

# 示例数据库和表名
database = "RDL.db"
table = "Table_write_enable"

# 转换为YAML文件
output_file = "data/write_enable.yaml"  # 修改为所需的输出文件路径
convert_to_yaml(database, table, output_file)