def multi_find(s,sub):
    return_list=[]
    loc_int=0
    while True:
        found_int=s.find(sub,loc_int)
        if found_int!=-1:
            ret_list.append(found_int)
            loc_int=found_int+1
        else:
            break
    return return_list
