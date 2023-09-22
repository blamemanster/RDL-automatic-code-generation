import yaml

'''yaml文件的读取和写入'''

# 读取YAML文件
def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# 写入YAML文件
def write_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

# 示例YAML文件路径
file_path = "reg.yaml"

# 读取YAML文件
data = read_yaml_file(file_path)
print(data)

# 修改数据
data[0]['reg_name'] = 'r1'
data[1]['desc'] = 'test2'

# 写入YAML文件
write_yaml_file(data, file_path)