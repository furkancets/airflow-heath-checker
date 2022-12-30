import requests
import json
from webhook.msteams_notif import send_msteams_notif
import subprocess

url = "http://localhost:8080/health"

payload={}
headers = {
  'Cookie': 'session=eyJfcGVybWFuZW50Ijp0cnVlfQ.Y6rxOg.edFsd1MxZsDlyI9z1Ti9QBH0UGc'
}

response = requests.request("GET", url, headers=headers, data=payload)

def webserver():

    if response.status_code == 404:

        #print("airflow webserver down! alert")
        send_msteams_notif(title="AIRFLOW WEB-UI INSTANCE DOWN!", subtitle="START AIRFLOW FROM AMBARI !!! OR LET YOUR SUPERVISOR !!!")

        return False
    
    else:

        return True

def scheduler_with_meta():  

    meta_flow = response.json()["metadatabase"]["status"]

    scheduler_health = response.json()["scheduler"]["status"]

    if (meta_flow == 'healthy') & (scheduler_health == 'healthy'):

        print("dont send send ms teams notif everything ok!")

        return True
    
    elif scheduler_health != 'healthy':

        send_msteams_notif(title="AIRFLOW SCHEDULAR INSTANCE DOWN!", subtitle="AIRFLOW-SCHEDULAR IS BEING RESTARTED !!! PLESAE CHECK MANUALLY FROM AMBARI !!!")

        subprocess.call(['sh', './airflowrestart.sh'])

        return False

    else :
        
        send_msteams_notif(title="AIRFLOW-META INSTANCE DOWN!", subtitle="START AIRFLOW FROM AMBARI !!! OR LET YOUR SUPERVISOR")

if __name__ == "__main__":
    if webserver():
        scheduler_with_meta()
