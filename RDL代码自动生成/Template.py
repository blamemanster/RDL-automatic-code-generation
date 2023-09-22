"""2023/08/21"""
#定义RDL的模板框架
#首先需要确定框架的样子


####定义模板####
template ="""

{% for en in data_enum %}
{% if en[0]!=None %}
enum {{ en[0] }} {
    {% for element in en[-4] %}
    {{ element }} = {{ en[-3][loop.index0] }} 
    {%- if en[-2][loop.index0]!=None or en[-1][loop.index0]!=None%}{
        name = " {{ en[-2][loop.index0] }} ";
        desc = " {{ en[-1][loop.index0] }} "; 
    }; 
    {% endif %}
    {% endfor %}
}
{% endif %}
{% endfor %}



{% for rg in data_reg %}
{% if rg[-1]==None and rg[-2]==None %}
reg {{ rg[0] }}{
    name = " {{ rg[1] }} ";
    desc = " {{ rg[2] }} ";
    regwidth = {{ rg[3] }};
    accesswidth = {{ rg[4] }};
    errextbus = {{ rg[5] }};
    {% if rg[7]!=None %}intr;{% endif %}
    {% if rg[8]!=None %}halt;{% endif %}
    shared = {{ rg[9] }};
    {% for fld in data_field %}
    {% if rg[0]==fld[-1] %}
    field {{ fld[0] }} {
        name = " {{ fld[1] }} ";
        desc = " {{ fld[2] }} ";
        fieldwidth = {{ fld[3] }};
        defalut = {{ fld[4] }};
        onread = {{ fld[5] }};
        onwrite = {{ fld[6] }};
        {{ fld[7] }} = true;
        swmod = {{ fld[8] }};
        swacc = {{ fld[9] }};
        singlepulse = {{ fld[10] }};
        {{ fld[11] }};
        {{ fld[12] }};
        {{ fld[13] }};
        {{ fld[14] }};
        hw = {{ fld[15] }} ;
        sw = {{ fld[16] }} ;
        {{ fld[17] }};
        {{ fld[18] }};

        encode = {{ fld[19] }};
        precedence = {{ fld[20] }};
        {{ fld[21] }};
        
        {% for cut in data_counter %}
        {% if fld[0]==cut[-1] %}
        counter;
        {{ cut[1] }} = {{ cut[2] }};
        {{ cut[3] }} = {{ cut[4] }};
        incrsaturate = {{ cut[5] }};
        incrthreshold = {{ cut[6] }};
        decrstaturate = {{ cut[7] }};
        decrthreshold = {{ cut[8] }};
        {% endif %}
        {% endfor %}
    };
    {% endif %}
    {% endfor %}
};
{% endif %}
{% endfor %}




{% for regf in data_regfile %}
{% if regf[-1]==None %}
regfile {{ regf[0] }}{
    name = " {{ regf[1] }} ";
    desc = " {{ regf[2] }} ";
    alignment = {{regf[3]}};
    sharedextbus = {{regf[4]}};
    errextbus = {{regf[5]}};
    {% for rg in data_reg %}
    {% if regf[0]==rg[-1] %}
    reg {{ rg[0] }}{
        name = " {{ rg[1] }} ";
        desc = " {{ rg[2] }} ";
        regwidth = {{ rg[3] }};
        accesswidth = {{ rg[4] }};
        errextbus = {{ rg[5] }};
        {% if rg[7]!=None %}intr;{% endif %}
        {% if rg[8]!=None %}halt;{% endif %}
        shared = {{ rg[9] }};
        {% for fld in data_field %}
        {% if rg[0]==fld[-1] %}
        field {{ fld[0] }} {
            name = " {{ fld[1] }} ";
            desc = " {{ fld[2] }} ";
            fieldwidth = {{ fld[3] }};
            defalut = {{ fld[4] }};
            onread = {{ fld[5] }};
            onwrite = {{ fld[6] }};
            {{ fld[7] }} = true;
            swmod = {{ fld[8] }};
            swacc = {{ fld[9] }};
            singlepulse = {{ fld[10] }};
            {{ fld[11] }};
            {{ fld[12] }};
            {{ fld[13] }};
            {{ fld[14] }};
            hw = {{ fld[15] }} ;
            sw = {{ fld[16] }} ;
            {{ fld[17] }};
            {{ fld[18] }};

            encode = {{ fld[19] }};
            precedence = {{ fld[20] }};
            {{ fld[21] }};

            {% for cut in data_counter %}
            {% if fld[0]==cut[-1] %}
            counter;
            {{ cut[1] }} = {{ cut[2] }};
            {{ cut[3] }} = {{ cut[4] }};
            incrsaturate = {{ cut[5] }};
            incrthreshold = {{ cut[6] }};
            decrstaturate = {{ cut[7] }};
            decrthreshold = {{ cut[8] }};
            {% endif %}
            {% endfor %}
        };
        {% endif %}
        {% endfor %}
    };
    {% endif %}
    {% endfor %}
}; 
{% endif %}
{% endfor %}




{% for addr in data_addrmap %}
{% if addr[-1]==None %}
addrmap {{ addr[0] }}{
    name = " {{addr[1]}} ";
    desc = " {{addr[2]}} ";
    alignment = {{addr[3]}};
    sharedextbus = {{addr[4]}};
    errextbus = {{addr[5]}};
    bridge = {{addr[6]}};
    {{addr[7]}};
    addressing = {{addr[8]}};
    {{addr[9]}};
    {{addr[10]}};

    
    
    {% for rg in data_reg %}
    {% if addr[0]==rg[-2] and rg[-1]==None %}
    reg {{ rg[0] }}{
        name = " {{ rg[1] }} ";
        desc = " {{ rg[2] }} ";
        regwidth = {{ rg[3] }};
        accesswidth = {{ rg[4] }};
        errextbus = {{ rg[5] }};
        {% if rg[7]!=None %}intr;{% endif %}
        {% if rg[8]!=None %}halt;{% endif %}
        shared = {{ rg[9] }};
        {% for fld in data_field %}
        {% if rg[0]==fld[-1] %}
        field {{ fld[0] }} {
            name = " {{ fld[1] }} ";
            desc = " {{ fld[2] }} ";
            fieldwidth = {{ fld[3] }};
            defalut = {{ fld[4] }};
            onread = {{ fld[5] }};
            onwrite = {{ fld[6] }};
            {{ fld[7] }} = true;
            swmod = {{ fld[8] }};
            swacc = {{ fld[9] }};
            singlepulse = {{ fld[10] }};
            {{ fld[11] }};
            {{ fld[12] }};
            {{ fld[13] }};
            {{ fld[14] }};
            hw = {{ fld[15] }} ;
            sw = {{ fld[16] }} ;
            {{ fld[17] }};
            {{ fld[18] }};

            encode = {{ fld[19] }};
            precedence = {{ fld[20] }};
            {{ fld[21] }};

            {% for cut in data_counter %}
            {% if fld[0]==cut[-1] %}
            counter;
            {{ cut[1] }} = {{ cut[2] }};
            {{ cut[3] }} = {{ cut[4] }};
            incrsaturate = {{ cut[5] }};
            incrthreshold = {{ cut[6] }};
            decrstaturate = {{ cut[7] }};
            decrthreshold = {{ cut[8] }};
            {% endif %}
            {% endfor %}
        };
        {% endif %}
        {% endfor %}
    };
    {% endif %}
    {% endfor %}

    

    {% for regf in data_regfile %}
    {% if addr[0]==regf[-1] %}
    regfile {{ regf[0] }}{
        name = " {{ regf[1] }} ";
        desc = " {{ regf[2] }} ";
        alignment = {{regf[3]}};
        sharedextbus = {{regf[4]}};
        errextbus = {{regf[5]}};
        {% for rg in data_reg %}
        {% if regf[0]==rg[-1] %}
        reg {{ rg[0] }}{
            name = " {{ rg[1] }} ";
            desc = " {{ rg[2] }} ";
            regwidth = {{ rg[3] }};
            accesswidth = {{ rg[4] }};
            errextbus = {{ rg[5] }};
            {% if rg[7]!=None %}intr;{% endif %}
            {% if rg[8]!=None %}halt;{% endif %}
            shared = {{ rg[9] }};
            {% for fld in data_field %}
            {% if rg[0]==fld[-1] %}
            field {{ fld[0] }} {
                name = " {{ fld[1] }} ";
                desc = " {{ fld[2] }} ";
                fieldwidth = {{ fld[3] }};
                defalut = {{ fld[4] }};
                onread = {{ fld[5] }};
                onwrite = {{ fld[6] }};
                {{ fld[7] }} = true;
                swmod = {{ fld[8] }};
                swacc = {{ fld[9] }};
                singlepulse = {{ fld[10] }};
                {{ fld[11] }};
                {{ fld[12] }};
                {{ fld[13] }};
                {{ fld[14] }};
                hw = {{ fld[15] }} ;
                sw = {{ fld[16] }} ;
                {{ fld[17] }};
                {{ fld[18] }};

                encode = {{ fld[19] }};
                precedence = {{ fld[20] }};
                {{ fld[21] }};

                {% for cut in data_counter %}
                {% if fld[0]==cut[-1] %}
                counter;
                {{ cut[1] }} = {{ cut[2] }};
                {{ cut[3] }} = {{ cut[4] }};
                incrsaturate = {{ cut[5] }};
                incrthreshold = {{ cut[6] }};
                decrstaturate = {{ cut[7] }};
                decrthreshold = {{ cut[8] }};
                {% endif %}
                {% endfor %}
            };
            {% endif %}
            {% endfor %}
        };
        {% endif %}
        {% endfor %}
    }; 
    {% endif %}
    {% endfor %} 



    {% for addr1 in data_addrmap %}
    {% if addr1[-1]==addr[0] %}
    addrmap {{ addr1[0] }}{
        name = " {{addr1[1]}} ";
        desc = " {{addr1[2]}} ";
        alignment = {{addr1[3]}};
        sharedextbus = {{addr1[4]}};
        errextbus = {{addr1[5]}};
        bridge = {{addr1[6]}};
        {{addr1[7]}};
        addressing = {{addr1[8]}};
        {{addr1[9]}};
        {{addr1[10]}};

        {% for rg in data_reg %}
        {% if addr[0]==rg[-2] and rg[-1]==None %}
        reg {{ rg[0] }}{
            name = " {{ rg[1] }} ";
            desc = " {{ rg[2] }} ";
            regwidth = {{ rg[3] }};
            accesswidth = {{ rg[4] }};
            errextbus = {{ rg[5] }};
            {% if rg[7]!=None %}intr;{% endif %}
            {% if rg[8]!=None %}halt;{% endif %}
            shared = {{ rg[9] }};
            {% for fld in data_field %}
            {% if rg[0]==fld[-1] %}
            field {{ fld[0] }} {
                name = " {{ fld[1] }} ";
                desc = " {{ fld[2] }} ";
                fieldwidth = {{ fld[3] }};
                defalut = {{ fld[4] }};
                onread = {{ fld[5] }};
                onwrite = {{ fld[6] }};
                {{ fld[7] }} = true;
                swmod = {{ fld[8] }};
                swacc = {{ fld[9] }};
                singlepulse = {{ fld[10] }};
                {{ fld[11] }};
                {{ fld[12] }};
                {{ fld[13] }};
                {{ fld[14] }};
                hw = {{ fld[15] }} ;
                sw = {{ fld[16] }} ;
                {{ fld[17] }};
                {{ fld[18] }};

                encode = {{ fld[19] }};
                precedence = {{ fld[20] }};
                {{ fld[21] }};

                {% for cut in data_counter %}
                {% if fld[0]==cut[-1] %}
                counter;
                {{ cut[1] }} = {{ cut[2] }};
                {{ cut[3] }} = {{ cut[4] }};
                incrsaturate = {{ cut[5] }};
                incrthreshold = {{ cut[6] }};
                decrstaturate = {{ cut[7] }};
                decrthreshold = {{ cut[8] }};
                {% endif %}
                {% endfor %}
            };
            {% endif %}
            {% endfor %}
        };
        {% endif %}
        {% endfor %}

        {% for regf in data_regfile %}
        {% if addr[0]==regf[-1] %}
        regfile {{ regf[0] }}{
            name = " {{ regf[1] }} ";
            desc = " {{ regf[2] }} ";
            alignment = {{regf[3]}};
            sharedextbus = {{regf[4]}};
            errextbus = {{regf[5]}};
            {% for rg in data_reg %}
            {% if regf[0]==rg[-1] %}
            reg {{ rg[0] }}{
                name = " {{ rg[1] }} ";
                desc = " {{ rg[2] }} ";
                regwidth = {{ rg[3] }};
                accesswidth = {{ rg[4] }};
                errextbus = {{ rg[5] }};
                {% if rg[7]!=None %}intr;{% endif %}
                {% if rg[8]!=None %}halt;{% endif %}
                shared = {{ rg[9] }};
                {% for fld in data_field %}
                {% if rg[0]==fld[-1] %}
                field {{ fld[0] }} {
                    name = " {{ fld[1] }} ";
                    desc = " {{ fld[2] }} ";
                    fieldwidth = {{ fld[3] }};
                    defalut = {{ fld[4] }};
                    onread = {{ fld[5] }};
                    onwrite = {{ fld[6] }};
                    {{ fld[7] }} = true;
                    swmod = {{ fld[8] }};
                    swacc = {{ fld[9] }};
                    singlepulse = {{ fld[10] }};
                    {{ fld[11] }};
                    {{ fld[12] }};
                    {{ fld[13] }};
                    {{ fld[14] }};
                    hw = {{ fld[15] }} ;
                    sw = {{ fld[16] }} ;
                    {{ fld[17] }};
                    {{ fld[18] }};

                    encode = {{ fld[19] }};
                    precedence = {{ fld[20] }};
                    {{ fld[21] }};

                    {% for cut in data_counter %}
                    {% if fld[0]==cut[-1] %}
                    counter;
                    {{ cut[1] }} = {{ cut[2] }};
                    {{ cut[3] }} = {{ cut[4] }};
                    incrsaturate = {{ cut[5] }};
                    incrthreshold = {{ cut[6] }};
                    decrstaturate = {{ cut[7] }};
                    decrthreshold = {{ cut[8] }};
                    {% endif %}
                    {% endfor %}
                };
                {% endif %}
                {% endfor %}
            };
            {% endif %}
            {% endfor %}
        }; 
        {% endif %}
        {% endfor %}  
    };
    {% endif %}
    {% endfor %}

    

};
{% endif %}
{% endfor %}
"""










template2 ="""


{# 定义函数 #}

{% macro extract_enum_member(member_dict) %}
{% for member in member_dict.get('member', []) %}
{{member.get('key', None)}}
{%- if member.get('value', None) != None%} = {{member.get('value', None)}}{% endif %};
{% if member.get('name', None) != None or member.get('desc', None) != None %}{
    name = " {{member.get('name', None)}} ";
    desc = " {{member.get('desc', None)}} ";
};
{% endif %}
{% endfor %}
{% endmacro %}

{% macro extract_enum(enum_dict) %}
{% for enum in enum_dict.get('enum', []) %}
enum {{enum.get('enum_name', None)}} {
    name = " {{enum.get('name', None)}} ";
    desc = " {{enum.get('desc', None)}} ";
    
    {{extract_enum_member(enum)|indent}}
};
{% endfor %}
{% endmacro %}

{#--------------------未完成-------------------#}
{% macro extract_constraint(constraint_dict) %}
{% for constraint in constraint_dict.get('constraint', []) %}
enum {{enum.get('enum_name', None)}} {
    name = " {{enum.get('name', None)}} ";
    desc = " {{enum.get('desc', None)}} ";
    
    {{extract_constraint_member(enum)|indent}}
};
{% endfor %}
{% endmacro %}
{# ---------------------------------------------- #}


{% macro extract_signal_instance(instance_dict) %}
{% for instance in instance_dict.get('instance', []) %}
{{instance_dict.get('signal_name', None)}} {{instance.get('instance_name', None)}};
{% endfor %}
{% endmacro %}

{% macro extract_signal(signal_dict) %}
{% for signal in signal_dict.get('signal', []) %}
signal {{signal.get('signal_name', None)}} {
    name = " {{signal.get('name', None)}} ";
    desc = " {{signal.get('desc', None)}} ";
    signalwidth = {{signal.get('signalwidth', None)}};
    sync = {{signal.get('sync', None)}};
    async = {{signal.get('async', None)}};
    activelow = {{signal.get('activelow', None)}};
    activehigh = {{signal.get('activehigh', None)}};
    cpuif_reset = {{signal.get('cpuif_reset', None)}};
    field_reset = {{signal.get('field_reset', None)}};
};
{{extract_signal_instance(signal)}}
{% endfor %}
{% endmacro %}


{% macro extract_field_instance(instance_dict) %}
{% for instance in instance_dict.get('instance', []) %}
{{instance_dict.get('field_name', None)}} {{instance.get('instance_name', None)}}{{instance_dict.get('fieldwidth', None)}}
{%- if instance.get('initial_value', None) != None %} = {{instance.get('initial_value', None)}}{% endif %};

{% endfor %}
{% endmacro %}

{% macro extract_field(field_dict) %}
{% for field in field_dict.get('field', []) %}
field {{field.get('field_name', None)}} {
    name = " {{field.get('name', None)}} ";
    desc = " {{field.get('desc', None)}} ";
    Default = {{field.get('Default', None)}};
    hw = {{field.get('hw', None)}};
    sw = {{field.get('sw', None)}};
    onread = {{field.get('onread', None)}};
    onwrite = {{field.get('onwrite', None)}};
    swmod = {{field.get('swmod', None)}};
    swacc = {{field.get('swacc', None)}};
    singlepulse = {{field.get('singlepulse', None)}};
    fieldwidth = {{field.get('fieldwidth', None)}};
    fieldwidth_lsb = {{field.get('fieldwidth_lsb', None)}};
    fieldwidth_msb = {{field.get('fieldwidth_msb', None)}};
    incrthreshold = {{field.get('incrthreshold', None)}};
    incrvalue = {{field.get('incrvalue', None)}};
    decrvalue = {{field.get('decrvalue', None)}};
    decrthreshold = {{field.get('decrthreshold', None)}};
    next = {{field.get('next', None)}};
    reset = {{field.get('reset', None)}};
    resetsignal = {{field.get('resetsignal', None)}};
    interruptType = {{field.get('interruptType', None)}};
    intr = {{field.get('intr', None)}};
    nonsticky = {{field.get('nonsticky', None)}};
    sticky = {{field.get('sticky', None)}};
    stickybit = {{field.get('stickybit', None)}};
    partiycheck = {{field.get('partiycheck', None)}};
    precedence = {{field.get('precedence', None)}};
    encode = {{field.get('encode', None)}};


};
{{extract_field_instance(field)}}
{% endfor %}
{% endmacro %}


{% macro extract_reg_instance(instance_dict) %}
{% for instance in instance_dict.get('instance', []) %}
{% if instance.get('instance_type', None) != None %}{{instance.get('instance_type', None)}} {% endif -%}
{{instance_dict.get('reg_name', None)}} {{instance.get('instance_name', None)}}
{%- if instance.get('offset_value', None) != None %} {{instance.get('offset_value', None)}}{% endif %};
{% endfor %}
{% endmacro %}

{% macro extract_reg(reg_dict) %}
{% for reg in reg_dict.get('reg', []) %}
reg {{reg.get('reg_name', None)}} {
    name = " {{reg.get('name', None)}} ";
    desc = " {{reg.get('desc', None)}} ";
    regwidth = {{reg.get('regwidth', None)}};
    reset = {{reg.get('reset', None)}};
    accesswidth = {{reg.get('accesswidth', None)}};
    errextbus = {{reg.get('errextbus', None)}};
    intr = {{reg.get('intr', None)}};
    halt = {{reg.get('halt', None)}};
    shared = {{reg.get('shared', None)}};

    {{extract_enum(reg)|indent}}
    {{extract_signal(reg)|indent}}
    {{extract_field(reg)|indent}}
};
{{extract_reg_instance(reg)}}
{% endfor %}
{% endmacro %}


{% macro extract_regfile_instance(instance_dict) %}
{% for instance in instance_dict.get('instance', []) %}
{% if instance.get('instance_type', None) != None %}{{instance.get('instance_type', None)}} {% endif -%}
{{instance_dict.get('regfile_name', None)}} {{instance.get('instance_name', None)}};
{% endfor %}
{% endmacro %}

{% macro extract_regfile(regfile_dict) %}
{% for regfile in regfile_dict.get('regfile', []) %}
regfile {{regfile.get('regfile_name', None)}} {
    name = " {{regfile.get('name', None)}} ";
    desc = " {{regfile.get('desc', None)}} ";
    alignment = {{regfile.get('alignment', None)}};
    sharedextbus = {{regfile.get('sharedextbus', None)}};
    errextbus = {{regfile.get('errextbus', None)}};

    {{extract_enum(regfile)|indent}}
    {{extract_signal(regfile)|indent}}
    {{extract_reg(regfile)|indent}}
    {{extract_mem(regfile)|indent}}
};
{{extract_regfile_instance(regfile)}}
{% endfor %}
{% endmacro %}


{% macro extract_addrmap_instance(instance_dict) %}
{% for instance in instance_dict.get('instance', []) %}
{{instance_dict.get('addrmap_name', None)}} {{instance.get('instance_name', None)}};
};
{% endfor %}
{% endmacro %}

{% macro extract_addrmap(addrmap_dict) %}
{% for addrmap in addrmap_dict.get('addrmap', []) %}
addrmap {{addrmap.get('addrmap_name', None)}} {
    name = " {{addrmap.get('name', None)}} ";
    desc = " {{addrmap.get('desc', None)}} ";
    alignment = {{addrmap.get('alignment', None)}};
    sharedextbus = {{addrmap.get('sharedextbus', None)}};
    errextbus = {{addrmap.get('errextbus', None)}};
    bridge = {{addrmap.get('bridge', None)}};
    addressing = {{addrmap.get('addressing', None)}};
    bigen_littlen = {{addrmap.get('bigen_littlen', None)}};
    rsvdest_X = {{addrmap.get('rsvdest_X', None)}};
    msb_lsb = {{addrmap.get('msb_lsb', None)}};

    {{extract_enum(addrmap)|indent}}
    {{extract_signal(addrmap)|indent}}
    {{extract_regfile(addrmap)|indent}}
    {{extract_reg(addrmap)|indent}}
    {{extract_mem(addrmap)|indent}}
    {{extract_addrmap(addrmap)|indent}}
};
{{extract_addrmap_instance(addrmap)}}
{% endfor %}
{% endmacro %}


{% macro extract_mem_instance(instance_dict) %}
{% for instance in instance_dict.get('instance', []) %}
{{instance_dict.get('mem_name', None)}} {{instance.get('instance_name', None)}};
};
{% endfor %}
{% endmacro %}

{% macro extract_mem(mem_dict) %}
{% for mem in mem_dict.get('mem', []) %}
mem {{mem.get('mem_name', None)}} {
    name = " {{mem.get('name', None)}} ";
    desc = " {{mem.get('desc', None)}} ";
    mementries = {{mem.get('mementries', None)}};
    memwidth = {{mem.get('memwidth', None)}};
    sw = {{mem.get('sw', None)}};

    {{extract_reg(mem)|indent}}
};
{{extract_mem_instance(mem)}}
{% endfor %}
{% endmacro %}


{# 调用函数 #}
{% for item in data %}
{{extract_enum(item)}}
{{extract_signal(item)}}
{{extract_reg(item)}}
{{extract_regfile(item)}}
{{extract_addrmap(item)}}
{{extract_mem(item)}}
{% endfor %}


"""

