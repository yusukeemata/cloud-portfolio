# Cloud Portfolio – Serverless CRUD Application

This project is a serverless portfolio management application built on AWS.

It allows administrators to create and manage portfolio projects using a simple web interface.

## Overview

The application uses a static frontend and a serverless backend.

- The frontend is built with HTML and JavaScript
- The backend uses Amazon API Gateway, AWS Lambda, and Amazon DynamoDB
- The backend infrastructure can also be deployed with AWS CloudFormation

## Architecture

AWS services used in this project:

- Amazon S3
- Amazon CloudFront
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Route 53
- AWS Certificate Manager (ACM)
- AWS CloudFormation

## Features

- Public portfolio page
- Admin page for CRUD operations
- Create new portfolio items
- Read all items
- Read a single item
- Update existing items
- Delete items
- Custom API domain
- Infrastructure as Code with CloudFormation

## Repository Structure

```text
cloud-portfolio
│
├─ README.md
│
├─ frontend
│  ├─ projects.html
│  └─ admin.html
│
└─ infrastructure
   └─ template.yaml
```

## Frontend

The frontend is stored in the `frontend` directory.

- `projects.html`
  - Public portfolio page
  - Displays portfolio items from the API

- `admin.html`
  - Admin page
  - Supports create, update, and delete operations

## Backend

The backend is built with:

- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB

Main API routes:

```text
POST   /items
GET    /items
GET    /items/{id}
PUT    /items/{id}
DELETE /items/{id}
```

## Infrastructure as Code

The CloudFormation template is stored here:

```text
infrastructure/template.yaml
```

This template deploys the backend resources, including:

- DynamoDB table
- Lambda function
- IAM role
- HTTP API
- API routes
- Lambda invoke permissions

## Live URLs

Public page:

```text
https://yusuke-cloud.org/projects.html
```

Admin page:

```text
https://yusuke-cloud.org/admin.html
```

Custom API domain:

```text
https://api.yusuke-cloud.org/items
```

## What I Learned

Through this project, I practiced:

- Building a serverless CRUD API on AWS
- Connecting a static frontend to a backend API
- Using DynamoDB as a NoSQL database
- Creating a custom domain for API Gateway with Route 53 and ACM
- Reproducing backend infrastructure using CloudFormation
- Organizing a cloud project in GitHub

## Future Improvements

- Add authentication for the admin page
- Restrict public write access
- Improve UI/UX further
- Add monitoring and alarms
- Extend CloudFormation to include more resources

## Author

Yusuke Emata
