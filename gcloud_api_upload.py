from google.cloud import storage


def get_bucket(bucket_name,json_file):
    client = storage.Client.from_service_account_json(json_credentials_path=json_file)
    bucket = client.get_bucket(bucket_name)
    return(bucket)
    
def file_upload_gcloud(filename,bucket,file_extension):  
    # Get bucket name from environment variable in app.yaml file
    try:   
         
        # declare your file name in GCP
        filename_gcp = filename
        print("gcp name",filename_gcp)
        blob = bucket.blob(filename_gcp)
      
        if file_extension =='msg':
           blob.upload_from_filename(filename)
           
           return 'UPLOAD COMPLETE:msg format'
      
        elif file_extension =='json':
           blob.upload_from_string(
             data=json.dumps(filename),
             content_type='application/json'
             )
           
           return 'UPLOAD COMPLETE:json format'
   
    except Exception as ex:
       logging.error('Error while uploading file logs: %s', ex)
       return "Upload Unsuccessful:Error"
      
   