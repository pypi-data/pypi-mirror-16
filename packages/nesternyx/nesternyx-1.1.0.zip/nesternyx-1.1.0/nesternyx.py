"""����"nester.py"ģ�飬�ṩ��һ����Ϊprint_lol()�ĺ�������
��ӡ�б����а����򲻰���Ƕ���б�"""
def print_lol(the_list,level):
    """���������һ��λ�ò�������Ϊ"the_list"�������
    ���κ�Python�б������򲻰���Ƕ���б������ṩ�б�
    �еĸ���������ᣨ�ݹ�أ���ӡ����Ļ�ϣ����Ҹ�ռһ�С�"""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t\n")
            print(each_item)
