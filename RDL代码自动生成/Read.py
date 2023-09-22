import yaml

# 读取函数
def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        data = convert_empty_to_none(data)
    return data

# 将字典中值为''转换成值为None的函数
def convert_empty_to_none(data):
    return [{key: None if value == '' else value for key, value in item.items()} for item in data]

# 读取yaml文件中的数据
file_path = 'data/addrmap.yaml'  #  YAML 文件路径
addrmap_dictdata = read_yaml_file(file_path)
print(addrmap_dictdata)

file_path = 'data/regfile.yaml'  
regfile_dictdata = read_yaml_file(file_path)
print(regfile_dictdata)

file_path = 'data/reg.yaml'  
reg_dictdata = read_yaml_file(file_path)
print(reg_dictdata)

file_path = 'data/field.yaml'  
field_dictdata = read_yaml_file(file_path)
print(field_dictdata)

file_path = 'data/counter.yaml'  
counter_dictdata = read_yaml_file(file_path)
print(counter_dictdata)

file_path = 'data/enum_element.yaml'  
enum_dictdata = read_yaml_file(file_path)
print(enum_dictdata)

file_path = 'output.yaml'  
out = read_yaml_file(file_path)
print(out)