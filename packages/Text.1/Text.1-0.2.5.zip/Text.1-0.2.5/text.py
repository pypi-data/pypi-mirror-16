def wo(lists,indent = False,num = 0):
    for l in lists:
        if isinstance(l,list):
            wo(l,indent,num+1)
        else:
            if indent:
                '''for tab in range(num):
                    print('\t',end = '')'''
                print('\t'*num,end = '')
            print(l)
