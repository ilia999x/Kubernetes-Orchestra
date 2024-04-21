import os
import requests
import datetime
import time
from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
v1 = client.CoreV1Api()

def send_message(text):
    # Replace the webhook URL with the URL of your Discord webhook
    webhook_url = "https://discord.com/api/webhooks/1059134064541565038/cmdJckV83a_AlPszGyHOlvktR5i0IzayO2q6AaC1OLIoqifjfFI-xyya_cckdZGDb87q"
    payload = {"content": text}
    requests.post(webhook_url, json=payload)

def report_pod_count():
    # List the pods in the default namespace
    pods = v1.list_namespaced_pod("default")

    # Count the number of pods
    pod_count = len(pods.items)

    # Send a message to the Discord webhook
    text = f"There are currently {pod_count} pods running in the cluster."
    send_message(text)

if __name__ == "__main__":
    # Run the report_pod_count function every hour
    while True:
        report_pod_count()
        time.sleep(3600)