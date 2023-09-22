from pydantic import BaseModel, Field, ValidationError, validator, Extra
from typing import List, Union
import re
import pydantic

import Extract

class ExtraAllowModel(BaseModel):
    class Config:
        extra = 'allow'  # 允许额外字段

# 定义实例化组件数据模型
class Instance_Signal(ExtraAllowModel):
    instance_name: str 

    @pydantic.field_validator('instance_name')
    def validate_instance_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('信号的instance_name必须由字母开头且只包含数字、字母和下划线.')
        return value
    
class Instance_Field(ExtraAllowModel):
    instance_name: str 

    @pydantic.field_validator('instance_name')
    def validate_instance_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('域的instance_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Instance_Reg(ExtraAllowModel):
    instance_name: str 

    @pydantic.field_validator('instance_name')
    def validate_instance_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('寄存器的instance_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Instance_Mem(ExtraAllowModel):
    instance_name: str 

    @pydantic.field_validator('instance_name')
    def validate_instance_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('内存的instance_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Instance_Regfile(ExtraAllowModel):
    instance_name: str 

    @pydantic.field_validator('instance_name')
    def validate_instance_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('寄存器组的instance_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Instance_Addrmap(ExtraAllowModel):
    instance_name: str 

    @pydantic.field_validator('instance_name')
    def validate_instance_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('地址映射的instance_name必须由字母开头且只包含数字、字母和下划线.')
        return value

# 枚举类型成员 
class Enum_Member(ExtraAllowModel):
    key: str 

    @pydantic.field_validator('key')
    def validate_key(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('枚举类型的成员key必须由字母开头且只包含数字、字母和下划线.')
        return value


# 定义组件数据模型
class Enum(ExtraAllowModel):
    enum_name: str 

    member: List[Enum_Member] = []
    @pydantic.field_validator('enum_name')
    def validate_enum_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('enum_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Constraint(ExtraAllowModel):
    constraint_name: str 

    @pydantic.field_validator('constraint_name')
    def validate_constraint_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('constraint_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Signal(ExtraAllowModel):
    signal_name: str 

    instance: List[Instance_Signal] = []
    @pydantic.field_validator('signal_name')
    def validate_signal_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('signal_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class MyField(ExtraAllowModel):
    field_name: str 
    constraint: List[Constraint] = []

    instance: List[Instance_Field] = []
    @pydantic.field_validator('field_name')
    def validate_field_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('field_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Reg(ExtraAllowModel):
    reg_name: str
    enum: List[Enum] = []
    field: List[MyField] = []

    instance: List[Instance_Reg] = []
    @pydantic.field_validator('reg_name')
    def validate_reg_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('reg_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Mem(ExtraAllowModel):
    mem_name: str
    reg: List[Reg] = []

    instance: List[Instance_Mem] = []
    @pydantic.field_validator('mem_name')
    def validate_mem_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('mem_name必须由字母开头且只包含数字、字母和下划线.')
        return value    

class Regfile(ExtraAllowModel):
    regfile_name: str
    enum: List[Enum] = []
    signal: List[Signal] = []
    reg: List[Reg] = []
    mem: List[Mem] = []

    instance: List[Instance_Regfile] = []
    @pydantic.field_validator('regfile_name')
    def validate_regfile_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('regfile_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Addrmap(ExtraAllowModel):
    addrmap_name: str
    enum: List[Enum] = []
    signal: List[Signal] = []
    reg: List[Reg] = []
    mem: List[Mem] = []
    regfile: List[Regfile] = []
    addrmap: List['Addrmap'] = []

    instance: List[Instance_Addrmap] = []
    @pydantic.field_validator('addrmap_name')
    def validate_addrmap_name(cls, value):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value):
            raise ValueError('addrmap_name必须由字母开头且只包含数字、字母和下划线.')
        return value

class Mock(ExtraAllowModel):
    enum: List[Enum] = []
    signal: List[Signal] = []
    reg: List[Reg] = []
    mem: List[Mem] = []
    regfile: List[Regfile] = []
    addrmap: List[Addrmap] = []

class Data(ExtraAllowModel):
    mock: List[Mock] = []



try:
    check_data = Data(**Extract.extract_data).model_dump() #输出检测后的数据（字典）
    print(check_data)
except ValidationError as e:
    for error in e.errors():
        err_path = '.'.join(str(loc) for loc in error['loc'])
        err_msg = error['msg']
        print(f"路径 '{err_path}' 的错误信息：{err_msg}")


