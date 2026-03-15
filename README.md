# AWS Serverless Portfolio

This repository contains hands-on AWS projects designed to demonstrate practical cloud architecture skills using serverless technologies.

The goal of this portfolio is to showcase real AWS architecture patterns including authentication, API design, serverless compute, data storage, and monitoring.

---

# Architecture Overview

This portfolio demonstrates a fully serverless architecture on AWS.

Main services used:

* Amazon S3 (Static website hosting)
* Amazon CloudFront (CDN)
* Amazon Cognito (Authentication)
* Amazon API Gateway (Secure API layer)
* AWS Lambda (Serverless compute)
* Amazon DynamoDB (NoSQL database)
* Amazon CloudWatch (Monitoring and observability)

Architecture flow:

User
↓
CloudFront
↓
S3 (Static Frontend)
↓
Amazon Cognito Authentication
↓
API Gateway (JWT Authorizer)
↓
Lambda
↓
DynamoDB

Monitoring:

Lambda / API Gateway / DynamoDB
↓
CloudWatch Metrics
↓
CloudWatch Logs
↓
CloudWatch Alarms

---

# Portfolio Projects

## Project #1 — Static Website Hosting

A globally distributed static website hosted on AWS.

Services used:

* Amazon S3
* Amazon CloudFront
* Route53
* AWS Certificate Manager (ACM)

Key concepts:

* Static site hosting
* CDN distribution
* HTTPS configuration
* Custom domain setup

---

## Project #2 — Serverless Contact Form

A contact form implemented using a serverless backend.

Services used:

* Amazon API Gateway
* AWS Lambda
* Amazon SES

Key concepts:

* API design
* Serverless backend
* Email integration

---

## Project #3 — Portfolio CRUD API

A serverless backend API for managing portfolio data.

Services used:

* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB

Key concepts:

* REST API design
* CRUD operations
* NoSQL data modeling

---

## Project #4 — Authenticated Admin Dashboard

A secure admin dashboard that allows authenticated users to manage portfolio items.

Services used:

* Amazon Cognito (Hosted UI authentication)
* Amazon API Gateway (JWT Authorizer)
* AWS Lambda
* Amazon DynamoDB

Features:

* Cognito login
* JWT-based authentication
* Secure API access
* CRUD operations
* Logout functionality

Security flow:

1. User logs in via Cognito Hosted UI
2. Cognito issues a JWT token
3. The frontend includes the token in API requests
4. API Gateway validates the JWT
5. Authorized requests reach Lambda functions

Unauthenticated requests are blocked by API Gateway authorization.

---

## Project #5 — Serverless Monitoring System

A monitoring system for serverless workloads using Amazon CloudWatch.

Services used:

* Amazon CloudWatch Metrics
* Amazon CloudWatch Logs
* Amazon CloudWatch Alarms

Monitoring features:

* API Gateway request monitoring
* Lambda execution metrics
* Log collection and analysis
* CloudWatch alarms for abnormal behavior

This project demonstrates operational visibility and monitoring for serverless architectures.

---

# Technologies Used

AWS S3
AWS CloudFront
Amazon Cognito
Amazon API Gateway
AWS Lambda
Amazon DynamoDB
Amazon CloudWatch
JavaScript

---

# Key Concepts Demonstrated

Serverless architecture
Authentication with Cognito
JWT authorization
REST API design
NoSQL database integration
Cloud monitoring and observability
Secure API access patterns

---

# Author

AWS Certified Solutions Architect – Associate
PMP / PMI-ACP Certified Project Manager

Currently building hands-on AWS architectures while transitioning into a cloud engineering role.
