# The purpose of this script is to export IAM policies to a CSV file
import boto3
import csv


# Create  IAM client
client = boto3.client('iam')

def iAMPolicy():
  # get all policies
  all_policies = client.list_policies()['Policies']
  
  # set up csv file
  csv_filename = "I_AM_Policies.csv"
  headers = ['PolicyName', 'PolicyId', 'ARN']
  
  # write headers in csv file
  with open(csv_filename, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    
    # Write each policy to a row
    for policy in all_policies:
      row = [policy["PolicyName"], policy["PolicyId"], policy["ARN"]]
      writer.writerow(row)
      
  # ensure csv file created
  print(f"Your {csv_filename} has been successfully created!")
  
# call the iam_policy function
iAMPolicy()
