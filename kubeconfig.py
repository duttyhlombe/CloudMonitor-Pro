from kubernetes import client, config
import os

# Ensure the KUBECONFIG environment variable is set
os.environ['KUBECONFIG'] = r'C:\Users\User\.kube'

try:
    # Load the kubeconfig file
    config.load_kube_config()

    # Create a Kubernetes API client
    api_instance = client.CoreV1Api()

    # List all namespaces
    namespaces = api_instance.list_namespace()
    for ns in namespaces.items:
        print(ns.metadata.name)
except Exception as e:
    print(f"An error occurred: {e}")