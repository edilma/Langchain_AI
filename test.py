topic_list = [
    "nasa", "local government", "engineering", 
    "employee satisfaction", "federal government"
]




topic_dict = {i.split(': ')[0]: int(i.split(': ')[1]) for i in response.split(sep='\n')}

topic_dict = 

if topic_dict['nasa'] == 1:
    print("ALERT: New NASA story!")

