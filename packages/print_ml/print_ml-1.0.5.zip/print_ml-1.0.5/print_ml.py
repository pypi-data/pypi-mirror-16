import sys
'''这是测试函数，可以打印'''
def print_lol(the_list,suojin=False,lv=0,outto=sys.stdout):
    '''参数1是列表值，参数2是缩进开关，参数3是缩进值'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,suojin,lv+1,outto)
        else:
            if suojin:
                for num in range (lv):
                    print('\t',end='',file=outto)
                    
            print(each_item,file=outto)
            
