# Deployment Plan for Django Application on AWS

## Database
1. **Amazon RDS**: Amazon RDS offers managed PostgreSQL databases.
2. **Read Replicas**: For handling increased read traffic, read replicas can be configured.
3. **Scalability and Features**: RDS supports vertical scaling, automated backups, high availability, and built-in security features.

## Backend Servers
We will deploy the Django web application on EC2 instances. The architecture will include multiple web servers behind a load balancer to handle incoming requests. An auto-scaling group will manage the scaling of instances based on metrics like CPU usage.

For access, a DNS endpoint will be set up in Route 53. A CNAME record will be configured to point to the load balancer, allowing easy access to the web server APIs.

## Code Deployment to Servers
Before merging any pull request into the main branch, all tests must pass. Once code is pushed to the main branch, an AWS CodePipeline will be triggered.

**CodePipeline Setup**:
1. **Source**: Connect the pipeline to the GitHub repository, branch, and trigger details.
2. **Build**: Use AWS CodeBuild to compile and test the project.
3. **Deploy**: Use AWS CodeDeploy to deploy the application to EC2 instances behind the load balancer.

## Data Ingestion
All text files for data ingestion will be uploaded to an S3 bucket. There are several ways to trigger data ingestion:

1. **Using API**:
   - Create an asynchronous API to process files in a specified S3 bucket and path (provided as query parameters).
   - The API triggers a worker via a message broker to handle the upload asynchronously and notify the user via a callback API.

2. **Using S3 and EC2**:
   - Upon file upload to S3, a Lambda function triggers and sends a message to the message broker.
   - A worker listening to the message broker processes the upload asynchronously.

3. **Using S3 and Lambda**:
   - Utilize an S3 trigger to invoke a Lambda function that handles data uploads to the PostgreSQL database.
   - Note: This method does not use Django-based code, which can affect maintainability, as updates to the model code require changes in both Lambda and EC2.

## Monitoring and Logging
**Amazon CloudWatch**:
1. **Alerts**: Set up alerts for various resources such as EC2, RDS, message broker, Lambda, etc.
2. **Logs**: Use CloudWatch Logs to store logs from EC2 instances. To improve log searching, include request IDs in all logs. Each request will have an associated request ID, which will be included in all related logs for easier tracking.

This approach ensures a scalable, reliable, and maintainable deployment of the Django application and its associated services in the cloud using AWS.
