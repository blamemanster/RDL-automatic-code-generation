import yaml
import json

# 读取 JSON 文件
with open('mock.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# 转换为 YAML
yaml_data = yaml.dump(json_data, allow_unicode=True, sort_keys=False)

# 写入 YAML 文件
with open('output.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml_file.write(yaml_data)