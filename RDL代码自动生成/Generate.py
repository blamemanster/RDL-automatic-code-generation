"""2023/08/21"""
#定义RDL的模板框架
#首先需要确定框架的样子
from dataclasses import field
from jinja2 import Template
from Template import template2
# from Template import template
import Extract, Check
# from sqlite import regfile_listdata,reg_listdata,field_listdata,addrmap_listdata,counter_listdata,enum_listdata
# from Read import regfile_dictdata,reg_dictdata,field_dictdata,addrmap_dictdata,counter_dictdata,enum_dictdata
import re


# ####创建模板对象####
# template1 = Template(template)


# ####渲染模板#####
# #渲染template1
# result = template1.render( 
# data_addrmap = addrmap_listdata, 
# data_regfile = regfile_listdata, 
# data_reg= reg_listdata,
# data_field = field_listdata,
# data_counter = counter_listdata,
# data_enum = enum_listdata
# )

####创建模板对象####
template1 = Template(template2)


####渲染模板#####
#渲染template1
result = template1.render( 
data = Check.check_data['mock']
)


# 去除带有None和False的行
result_lines = result.split('\n')
result = '\n'.join(line for line in result_lines if not re.search(r'\b(None|False)\b', line))

####美观【用正则去除多余空行】####
#new_result = re.sub(r'\n{2,}', '\n', result)
new_result = re.sub(r'\n\s*\n', '\n', result)


####文件输出####
with open('result1.rdl', 'w', encoding='utf-8') as file:
    file.write(new_result)
print ("模板生成成功")
