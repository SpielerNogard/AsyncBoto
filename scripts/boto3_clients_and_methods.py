import argparse
import boto3
import boto3.session
from botocore.exceptions import ClientError
import os
from bullet import Check, colors
from bullet import styles

this_dir = os.path.dirname(os.path.abspath(__file__))

def get_clients_and_methods():
    """
    Get a list of all available AWS services and their methods.
    """
    session = boto3.session.Session()
    available_services = session.get_available_services()
    available_services.sort()

    clients_and_methods = {}

    for service_name in available_services:
        try:
            client = session.client(service_name, region_name="us-east-1")
            methods = [
                method
                for method in dir(client)
                if not method.startswith("_") and callable(getattr(client, method))
            ]
            methods.sort()
            clients_and_methods[service_name] = methods
        except ClientError as e:
            print(f"Error initializing client for {service_name}: {str(e)}")

    return clients_and_methods



def generate_boto3_clients_todo_markdown(output_file=os.path.join(this_dir, '..', 'docs',"implementation_status")):
    """
    Generate a markdown TODO list with methods and their subtasks.
    """
    os.makedirs(output_file, exist_ok=True)

    session = boto3.session.Session()
    available_services = session.get_available_services()
    available_services.sort()

    for service_name in available_services:
        markdown_content = f"# {service_name}\n\n"

        try:
            client = session.client(service_name, region_name="us-east-1")
            methods = [
                method
                for method in dir(client)
                if not method.startswith("_") and callable(getattr(client, method))
            ]
            methods.sort()

            for method in methods:
                markdown_content += f"# {method}\n"
                markdown_content += f"  - ❌ Written\n"
                markdown_content += f"  - ❌ Tested\n"
                markdown_content += f"  - ❌ Confirmed in Cloud\n"

        except (ClientError, Exception) as e:
            markdown_content += f"- ❌ Error initializing client: {str(e)}\n"

        markdown_content += "\n"

        with open(os.path.join(output_file, f'{service_name}.md'),"w") as f:
            f.write(markdown_content)

    print(f"TODO list with subtasks generated in {output_file}")

if __name__ == "__main__":


    generate_boto3_clients_todo_markdown()