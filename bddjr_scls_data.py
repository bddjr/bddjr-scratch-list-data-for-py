'''
bddjr-scratch-list-data-for-py

Scratch原版可用的列表转变量数据格式。
Use MIT License.

单片数据结构：
<length hex>:<data>
当列表有三项时：
<length hex>:<data><length hex>:<data><length hex>:<data>
以此类推。

'''

#=========================================================

def list_to_data( in_array: list[str] ):
    ret_str_ls = []
    for i in in_array:
        i = str(i) #懒得判断了，因为判断的时候可能也要转为字符串
        ret_str_ls.append( '{0}:{1}'.format(
            hex( len(i) )[ 2: ] ,
            i
        ) )
    return ''.join( ret_str_ls )

#=========================================================

def data_to_list( in_data: str ) -> list[str]:
    d = str( in_data )
    ret_ls = []
    while len(d) >0:
        Index = d.index(':')
        if Index <1:
            raise 'get data error: index error'
        
        Leng = int(
            d[ 0 : Index ] ,
            16
        )

        LastIndex = Index + Leng +1

        ret_ls.append( d[
            Index +1 :
            LastIndex
        ] )

        d = d[ LastIndex : ]
    return ret_ls
