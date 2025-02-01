++++++++++++++++++
7:40 AM 11.4.2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 


GCF: Google Cloud Run Functions:
--------------------------------

@ Developing Cloud Run Functions and Deploying them from Local/Locally:


folder Structure:
    
involved services:
  GCF, GR, GArtFactReg, Gbuild, GCS, SA, Logs    
    
web page: http https://us-central1-woven-name-434311-i8.cloudfunctions.net/http-trigger-func?number=2

json string - payload --


gun - payload - material - machine - encode - to - machine - json - udf - data packets - 

reach - decode 

[1.a] [1.c] [1.b] 

endpoint - dataflow - workernodes - ip - 


[1] encoded - decoded 


nulls - 

paypal - null - 
big issue --




              
    
    



Attempts to retrieve the JSON payload sent in the HTTP request body.


{"name":"raja"}

ImmutableMultiDict([('number', '10')])
pubsub - msg - json payload


bigquery table: 

json payload 

bqtowebpage - GCF - Development:

Programme1:

import functions_framework

@functions_framework.http
def bq_table_data(request):
    """HTTP Cloud Function that returns the square of a given integer number.""" 
    
    # Check for 'number' in JSON body or query parameters
    request_json = request.get_json(silent=True) 
    request_args = request.args 

    # Try to get 'number' from JSON or query parameters
    if request_json and 'table_id' in request_json:
        table_id = request_json['table_id']
    elif request_args and 'table_id' in request_args:
        table_id = request_args['table_id']
    else:
        return "Please provide a valid table_id as 'table_id' parameter.", 400

    # Check if the number is an integer and calculate its square
    try:
        table_id = table_id 
        print(table_id)
        return 'sucess'
    except ValueError:
        return "The 'table_id' parameter should be a valid table_id.", 400



Programme2:


from google.cloud import bigquery

# Initialize a BigQuery client
client = bigquery.Client()

def print_top_records(table_name):
    """
    Prints the top 3 records of a given BigQuery table.
    
    Args:
    table_name (str): The fully-qualified name of the table (e.g., "project.dataset.table").
    """
    query = f"SELECT * FROM {table_name} LIMIT 3"
    
    try:
        # Execute the query
        query_job = client.query(query)
        
        # Fetch and print the results
        results = query_job.result()
        print(f"Top 3 records from table '{table_name}':")
        
        for row in results:
            print(dict(row))
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
print_top_records('your_project.your_dataset.your_table')


Programme3:

import functions_framework
from google.cloud import bigquery

@functions_framework.http
def bq_table_data(request):
    """HTTP Cloud Function that fetches and displays top 3 records from a specified BigQuery table as HTML."""
    
    # Check for 'table_id' in JSON body or query parameters
    request_json = request.get_json(silent=True)
    request_args = request.args

    # Retrieve table_id from JSON or query parameters
    if request_json and 'table_id' in request_json:
        table_id = request_json['table_id']
    elif request_args and 'table_id' in request_args:
        table_id = request_args['table_id']
    else:
        return "Please provide a valid table_id as 'table_id' parameter.", 400

    query = f"SELECT * FROM {table_id} LIMIT 1"
    
    try:
        # Initialize a BigQuery client
        client = bigquery.Client()
        # Execute the query
        query_job = client.query(query)
        
        # Fetch the results
        results = query_job.result()
        
        # Process the result row
        row = next(results)
        data = {
            "Customer_id": row["Customer_id"],
            "date": row["date"].strftime('%Y-%m-%d'),
            "time": row["time"],
            "order_id": row["order_id"],
            "items": row["items"],
            "amount": row["amount"],
            "mode": row["mode"],
            "restaurant": row["restaurnt"],
            "status": row["Status"],
            "ratings": row["ratings"],
            "feedback": row["feedback"]
        }
        
        # HTML Template for displaying data
        html_content = f"""
        <html>
            <head>
                <title>Order Details</title>
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    table {{ width: 50%; margin: 20px auto; border-collapse: collapse; }}
                    th, td {{ padding: 10px; border: 1px solid #ddd; text-align: left; }}
                    th {{ background-color: #f2f2f2; }}
                </style>
            </head>
            <body>
                <h2 style="text-align:center;">Order Details</h2>
                <table>
                    <tr><th>Customer ID</th><td>{data["Customer_id"]}</td></tr>
                    <tr><th>Date</th><td>{data["date"]}</td></tr>
                    <tr><th>Time</th><td>{data["time"]}</td></tr>
                    <tr><th>Order ID</th><td>{data["order_id"]}</td></tr>
                    <tr><th>Items</th><td>{data["items"]}</td></tr>
                    <tr><th>Amount</th><td>${data["amount"]}</td></tr>
                    <tr><th>Mode</th><td>{data["mode"]}</td></tr>
                    <tr><th>Restaurant</th><td>{data["restaurant"]}</td></tr>
                    <tr><th>Status</th><td>{data["status"]}</td></tr>
                    <tr><th>Ratings</th><td>{data["ratings"]}</td></tr>
                    <tr><th>Feedback</th><td>{data["feedback"]}</td></tr>
                </table>
            </body>
        </html>
        """
        
        # Return HTML response
        return html_content, 200, {'Content-Type': 'text/html'}

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while processing the request.", 500



bigquery - table - google sheet -- 6.15 - refresh -- clarity

