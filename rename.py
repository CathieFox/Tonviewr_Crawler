from datetime import datetime



now = datetime.now()

#file  
formatted_date = now.strftime("MARS%m%d%H")



# 构造文件名
file_name_1 = f"{formatted_date}.xlsx"


print (file_name_1)