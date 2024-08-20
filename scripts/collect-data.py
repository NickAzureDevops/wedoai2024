import os
import csv
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.exceptions import AzureDevOpsServiceError

# Azure DevOps configuration
organization_url = 'https://dev.azure.com/nicholaschang'
project = 'wedoai-demo'
pat = os.getenv('AZURE_DEVOPS_PAT')

if not pat:
    raise ValueError("Please set the AZURE_DEVOPS_PAT environment variable")

# Create a connection to the Azure DevOps organization
connection = Connection(base_url=organization_url, creds=BasicAuthentication('', pat))
build_client = connection.clients.get_build_client()
test_client = connection.clients.get_test_client()

local_file_path = 'build_data.csv'

def collect_build_data():
    try:
        build_list = build_client.get_builds(project)
        with open(local_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Build ID', 'Build Number', 'Status', 
                'Number of Tests Run', 'Number of Tests Passed', 'Number of Tests Failed'
            ])
            for build in build_list:
                build_id = build.id
                build_number = build.build_number
                status = build.status
                
                # Fetch test results using the TestClient
                test_results = test_client.get_test_results(project, build_id)
                number_of_tests_run = len(test_results)
                number_of_tests_passed = sum(1 for result in test_results if result.outcome == 'Passed')
                number_of_tests_failed = sum(1 for result in test_results if result.outcome == 'Failed')

                writer.writerow([
                    build_id, build_number, status, 
                    number_of_tests_run, number_of_tests_passed, number_of_tests_failed
                ])
                print(f"Build ID: {build_id}, Build Number: {build_number}, Status: {status}")
    except AzureDevOpsServiceError as e:
        print(f"AzureDevOpsServiceError: {e}")
        raise

# Call the function to collect build data
collect_build_data()