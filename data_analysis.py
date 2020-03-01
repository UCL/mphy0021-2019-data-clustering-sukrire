import json

with open('cities.json') as json_file:
    data1   = json.load(json_file)

with open('libraries.json') as json_file:
    data2 = json.load(json_file)
    
def combine_func(file1,file2):
    combine_list=[]
    for i in range(len(file1)):
        dict1 = {**file1[i]}
        
    for i in range(len(file2)):
        dict2 = {**file2[i]}
        
        combine_dict = {**dict1,**dict2}
        combine_list.append(combine_dict)
        
    return combine_list
        

with open('combined.json', 'w', encoding='utf-8') as f:
    json.dump(combine_func(data1,data2), f, ensure_ascii=False, indent=4)
