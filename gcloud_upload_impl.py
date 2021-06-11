#from dotenv import load_dotenv
import ntpath 
#load_dotenv()
import json,os
from gcloud_api_upload import file_upload_gcloud,get_bucket
def file_name(filepath):
    file_name= ntpath.basename(filepath)
    return file_name
 
def file_extension(filepath):
   split_up = os.path.splitext(filepath)
   file_extension = split_up[1]
   return(file_extension) 

    
if __name__=="__main__":
   bucket_name = os.environ.get("BUCKET_NAME")
   print("bucket name=",bucket_name)
   file="sample.msg"
   json_file="gcloud.json"
   bucket=get_bucket("textsmind.appspot.com",json_file)
   if bucket:
        return_msg=file_upload_gcloud(file,bucket,"msg")
   print(return_msg)