#!/usr/bin/env  python3
# coding utf-8


DB_FILE= "staff.db"
COLUMNS = ['id','name','age','phone','dept','enrolled_date']

def print_log(msg,log_type='info'):
    if log_type == 'info':
        print(msg)

    elif log_type == "error":
        print("\033[31;1m%s\033[0m" %msg)


def load_db(db_file):
    """
    加载员工 信息 表，并转成制定格式
    :param db_file:
    :return:
    """
    data  = {}
    for i in COLUMNS:
        data[i] = []

    f = open(db_file,"r",encoding='utf8')
    for line in f:
        staff_id,name,age,phone,dept,enrolled_date = line.split(",")
        data['id'].append(staff_id)
        data['name'].append(staff_id)
        data['age'].append(staff_id)
        data['phone'].append(staff_id)
        data['dept'].append(staff_id)
        data['enrolled_date'].append(staff_id)
    # print(data)
    # print_log(data)
    return   data


STAFF_DATA = load_db(DB_FILE)  #程序一起动 就执行

def op_gt(column,condtion_val):
    """

    :param column: eg.age
    :param condtion_val:   aeg.22
    :return:
    """
    for val in  STAFF_DATA[column]:  #  age :[22 ,33 ,44 ]
        if val >condtion_val: # 匹配上了
            print("match",val)
        else:
            print(val,condtion_val)

def op_lt(column,condtion_val):
    pass

def op_eq(column,condtion_val):
    pass

def op_like(column,condtion_val):
    pass


def syntax_where(clause):
    """
    解析where条件 并过滤数据
    :param clause:  ag： age > 22
    :return:
    """
    operators = {
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like,
    }
    # if '>' in clause:
    #     column,operator,condtion = clause.split('>')
    # elif '<' in  clause:
    #     column, operator, condtion = clause.split('<')
    for op_key,op_func in operators.items():
        if op_key in clause:
            print("clasuese",clause)
            column,val = clause.split(op_key)
            op_func(column.strip(),val.strip())  # 真正的数据查询
            break
    else:  # 只有在for执行完 并且没有中间被freak的情况下  才会被执行
        # 没有匹配任何条件公式
        print("语法错误：where条件只能支持[>,<,=,like]")





def syntax_parser(cmd):
    """
    解析语句 并执行
    1
    :param cmd:
    :return:
    """
    # find name,age from  staff_table where age >22
    if cmd.split()[0] in ('find','add','del','update'):
        query_clause,where_clause = cmd.split("where")
        print(query_clause,where_clause)

        syntax_parser(where_clause)

    else:
         print("\033[31:1m语法错误：\033[0m\n[[find\\add\\del\\update][colum1,...] from [staff_table] [where] [column][>,...][condtion]\n")



def main():
    """
    让用户数据语句，并执行
    :return:
    """
    while True:
        cmd = input("[staff_db]:").strip()
        if not cmd:continue

        syntax_parser(cmd)

main() # start  program