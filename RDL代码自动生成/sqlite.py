"""
数据接口，暂时先用数据库
"""
import sqlite3

conn = sqlite3.connect('RDL.db')
#cursor()创建一个游标对象c，用于执行SQL语句和获取结果
c = conn.cursor()

#将列表中''转换成None的函数
def replace_empty_with_none(my_list):
    return [None if item == '' else item for item in my_list]


#获取Table_addrmap中的数据
row_addrmap = c.execute("SELECT addrmap_name, name, desc, alignment, \
                        sharedextbus, errextbus, bridge, bigen_littlen, \
                        addressing, rsvdest_X, msb_lsb, addrmap_name_before \
                        FROM Table_addrmap")

temp_list = [list(row) for row in row_addrmap.fetchall()]
addrmap_listdata = [replace_empty_with_none(row) for row in temp_list]  #将列表中''转换成None
print(addrmap_listdata) #打印列表

#获取Table_regfile中的数据
row_regfile = c.execute("SELECT regfile_name, name, desc, alignment, \
                        sharedextbus, errextbus, instance_type, addrmap_name \
                        FROM Table_regfile")
temp_list = [list(row) for row in row_regfile.fetchall()]
regfile_listdata = [replace_empty_with_none(row) for row in temp_list]
print(regfile_listdata)

#获取Table_reg中的数据
row_reg = c.execute("SELECT reg_name, name, desc, reg_width, \
                    access_width, errextbus, instance_type, intr, \
                    halt, shared, addrmap_name, regfile_name \
                    FROM Table_reg")
temp_list = [list(row) for row in row_reg.fetchall()]
reg_listdata = [replace_empty_with_none(row) for row in temp_list]
print(reg_listdata)

#获取Table_field中的数据
#filed的元素比较多，原理相同
row_field = c.execute("SELECT field_name, name, desc, field_width, \
                      default_value, onread, onwrite, swwe_l, \
                      swmod, swacc, singlepulse, write_enable, \
                      field_logical, hwclr_set, hwenable_mask, hw, sw, \
                      intr_type, sticky_type, encode, precedence, paritycheck, \
                      mem_name, \
                      reg_name \
                      FROM Table_field")
temp_list = [list(row) for row in row_field.fetchall()]
field_listdata = [replace_empty_with_none(row) for row in temp_list]
print(field_listdata)

#获取Table_counter中的数据
row_counter = c.execute("SELECT counter_ID, incrwidth_value, inc_value, decrwidth_value, dec_value, \
                        incrsaturate, incrthreshold, decrstaturate, decrthreshold, \
                        field_name \
                        FROM Table_counter")
temp_list = [list(row) for row in row_counter.fetchall()]
counter_listdata = [replace_empty_with_none(row) for row in temp_list]
print(counter_listdata)


#获取Table_enum中的数据
row_enum = c.execute("SELECT enum_name, key, value, name, desc \
                     FROM Table_enum_element")
temp = {}   #临时字典
for row in row_enum.fetchall():  #获取所有行的数据，row表示其中一行
    key = row[0]    #enum_name作为关键字，区分不同地址映射
    if key in temp:
        temp[key][-4].append(row[-4])
        temp[key][-3].append(row[-3])
        temp[key][-2].append(row[-2])
        temp[key][-1].append(row[-1])   #如果已存在字典中，则需要添加属性
    else:
        temp[key] = list(row[:-4]) + [[row[-4]]] + [[row[-3]]] + [[row[-2]]] + [[row[-1]]]   #不在则新建元素，用列表存储三个属性
temp_list = list(temp.values())  #字典转换成列表
enum_listdata = [replace_empty_with_none(row) for row in temp_list]
print(enum_listdata)




conn.close()

