# python test.py
# python3 test.py



import bddjr_scls_data
import json

ls = [
    '你说的对::',
    '但是《别针社区》是由一群scratcher自主研发的一款全新开放scratch社区。',
    '社区发生在一个被称作「ClipCC」的JavaScript世界，',
    '在这里，',
    '被神选中的人将被授予「绒布球」，',
    '导引西蒙司机之力。',
    '你将扮演一位名为别针用户的神秘角色，',
    '在自由的编写scratch/扩展中邂逅性格各异、能力独特的开发者们，',
    '和他们一起击败难题，',
    '找回失散的爱好',
    '——同时，',
    '逐步发掘「别急」的真相。'
]

print('in')
print(json.dumps( ls, indent='  ', ensure_ascii=False ))

print()

print('data')
data = bddjr_scls_data.list_to_data(ls)
print(data)

print()

print('out')
data_ls = bddjr_scls_data.data_to_list(data)
print(json.dumps( data_ls, indent='  ', ensure_ascii=False ))
