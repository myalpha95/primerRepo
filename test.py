from google.cloud import storage

gcs_client = storage.Client(project='agr-sendirect-des')
bucket = gcs_client.get_bucket('snd-bpdf')
print(bucket)
blob = bucket.blob('cliente2/')
blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

def main():
  password_id= "wqewqeewqqwe63226123321"
  return password_id
