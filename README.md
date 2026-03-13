# cloud-portfolio
Serverless CRUD portfolio app built on AWS

Cloud Portfolio – Serverless CRUD App

This project is a serverless portfolio management application built on AWS.

Architecture:
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudFormation (Infrastructure as Code)

Features:
- Create portfolio projects
- Update project status (draft / published)
- List all projects via API
- Admin interface for managing projects

Tech Stack:
AWS Lambda (Node.js)
API Gateway
DynamoDB
CloudFormation
HTML + JavaScript frontend

Repository Structure:

frontend/
    admin.html
    projects.html

infrastructure/
    template.yaml

API Endpoint:
/items
