import json
from tasks.serializers import NeoSerializer

def conversion(data):
    json_data = data
    #json_string = json.dumps(data)
    #with open("example.json", "w"):
        #json.dump(data, "example.json")
    #with open('example.json') as F:
        #json_data = json.load(F)
   
    first_dict = {k:v for (k,v) in json_data.items() if k == 'element_count' }
    secound_list = [v for (k,v) in json_data.items() if k == 'near_earth_objects' ]
    third_list = []
    fourth_list = []
    keys = ['id', 'neo_reference_id', 'name','nasa_jpl_url', 'is_potentially_hazardous_asteroid']
    q = len(keys)
    for element in secound_list:
        for key, value in element.items():
            foo = value
            for bar in foo:
                for key , value in bar.items():
                    if key in keys:
                        third_list.append(value)
    multiple_lists = [third_list[i * q:(i + 1) * q] for i in range((len(third_list) + q - 1) // q )]
    list_of_dictiories = [] 
    for item in multiple_lists:
        rtmp =  dict(zip(keys, item))
        list_of_dictiories.append(rtmp)
    return list_of_dictiories
      

# list contains a dictionary with a single key which value is a list and this list contains a dictionary :[{x:[{key:value}]}] 
#x = json_data.keys()
# print(first_dict)
#with open('request.data') as F:
#  print(list_of_dictiories )
# with open("example.json", "w") as outfile:
 # json.dump(dic_exm, outfile)
 # NeoSerializer(list_of_dictiories) 
 # conversion(data)


   
        
        
            
                
                     
                     





            
            
 
    
    
    
    
        
       
        
            
             
             

  



    

        
 