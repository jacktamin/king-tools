class Sort_dic:
    
    def __init__(self):
        pass
        

    @staticmethod
    def sort_values(dic,rev=False,sort_by= 'values'):
        if sort_by == 'values':
   
            sv = sorted(dic.values(),reverse=rev)
            new_dic = {}
            for num in sv :
                for k,v in dic.items():
                    if num == v:
                        new_dic[k] = v

            return new_dic
        
        elif sort_by == 'keys':
            sk = sorted(dic.keys(),reverse=rev)
            new_dic = {}
            for num in sk :
                for k,v in dic.items():
                    if k==num:
                        new_dic[k] = v
            return new_dic
            