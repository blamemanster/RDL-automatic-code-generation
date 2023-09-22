import yaml, json

# def extract_data(data):
#     template = ""
#     for item in data:
#         template += extract_reg(item.get('reg', []))
#         template += extract_regfile(item.get('regfile', []))
#         template += extract_mem(item.get('mem', []))
#         template += extract_addrmap(item.get('addrmap', []))
#     return template

# def extract_addrmap(addrmap_data):
#     template = ""
#     for addrmap in addrmap_data:
#         addrmap_name = addrmap.get('addrmap_name', '')
#         template += f"  addrmap {addrmap_name} {{\n"
#         template += extract_reg(addrmap.get('reg', []))
#         template += extract_regfile(addrmap.get('regfile', []))
#         template += extract_mem(addrmap.get('mem', []))
#         template += extract_addrmap(addrmap.get('addrmap', []))
#         template += "   }\n"
#     return template

# def extract_regfile(regfile_data):
#     template = ""
#     for regfile in regfile_data:
#         regfile_name = regfile.get('regfile_name', '')
#         template += f"  regfile {regfile_name} {{\n"
#         template += extract_reg(regfile.get('reg', []))
#         template += extract_mem(regfile.get('mem', []))
#         template += "  }\n"
#     return template

# def extract_reg(reg_data):
#     template = ""
#     for reg in reg_data:
#         reg_name = reg.get('reg_name', '')
#         template += f"  reg {reg_name} {{\n"
#         template += extract_field(reg.get('field', []))
#         template += "   }\n"
#     return template

# def extract_field(field_data):
#     template = ""
#     for field in field_data:
#         field_name = field.get('field_name', '')
#         name = field.get('name', '')
#         swwe_l = field.get('swwe_l', '')
#         encode = field.get('encode', '')
#         template += f"    field {field_name} {{\n"
#         template += f"      name = '{name}';\n"
#         template += f"      swwe_l = '{swwe_l}';\n"
#         template += f"      encode = '{encode}';\n"
#         template += "    }\n"
#     return template

# def extract_mem(mem_data):
#     template = ""
#     for mem in mem_data:
#         mem_name = mem.get('mem_name', '')
#         sw = mem.get('sw', '')
#         template += f"  mem {mem_name} {{\n"
#         template += f"    sw = '{sw}';\n"
#         template += "  }\n"
#     return template

# 将嵌套列表的字典中的空值''转换成None
def replace_empty_with_none(obj):
    if isinstance(obj, dict):
        return {k: replace_empty_with_none(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_empty_with_none(item) for item in obj]
    elif obj == '':
        return None
    else:
        return obj


# 读取YAML文件
with open('output.yaml', 'r', encoding='utf-8') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)
print(yaml_data)

extract_data = replace_empty_with_none(yaml_data)
print(extract_data)

# # 提取数据并生成模板
# template = extract_data(yaml_data['mock'])

# # 输出模板到文件
# with open('output.rdl', 'w', encoding='utf-8') as output_file:
#     output_file.write(template)