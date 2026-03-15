# AWS Serverless Architecture Portfolio

Yusuke Emata

This repository contains hands-on AWS projects implementing real serverless architecture patterns on AWS.

The portfolio demonstrates practical cloud architecture including:

* authentication
* secure API design
* serverless compute
* data storage
* monitoring and observability

These projects showcase end-to-end AWS system design using modern serverless services.

---

# Architecture Overview

This portfolio demonstrates a fully serverless architecture on AWS.

Main AWS services used:

* Amazon S3 (Static frontend hosting)
* Amazon CloudFront (Global CDN)
* Amazon Cognito (Authentication)
* Amazon API Gateway (Secure API layer)
* AWS Lambda (Serverless compute)
* Amazon DynamoDB (NoSQL database)
* Amazon CloudWatch (Monitoring)
* Amazon SNS (Alert notifications)

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

Monitoring layer:

Lambda / API Gateway / DynamoDB
↓
CloudWatch Metrics
↓
CloudWatch Logs
↓
CloudWatch Alarms
↓
SNS Notifications

---

# Portfolio Projects

## Project #1 — Static Website Hosting

A globally distributed static website hosted on AWS.

Services used:

* Amazon S3
* Amazon CloudFront
* Amazon Route 53
* AWS Certificate Manager (ACM)

Key concepts demonstrated:

* Static site hosting
* CDN distribution
* HTTPS configuration
* Custom domain setup

Architecture:

User
↓
CloudFront
↓
S3 Static Website
↓
Route53 + ACM

---

## Project #2 — Serverless Contact Form

A contact form implemented using a serverless backend.

Services used:

* Amazon API Gateway
* AWS Lambda
* Amazon SES
* Amazon CloudFront

Key concepts demonstrated:

* API design
* Serverless backend
* Event-driven email workflow
* Integration between frontend and backend services

Architecture:

User
↓
CloudFront
↓
API Gateway
↓
Lambda
↓
SES Email Delivery

---

## Project #3 — Portfolio CRUD API

A serverless backend API for managing portfolio data.

Services used:

* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB

Key concepts demonstrated:

* REST API design
* CRUD operations
* NoSQL data modeling
* Serverless backend architecture

Architecture:

Client
↓
API Gateway
↓
Lambda
↓
DynamoDB

---

## Project #4 — Authenticated Admin Dashboard

A secure admin dashboard that allows authenticated users to manage portfolio items.

Services used:

* Amazon Cognito (Hosted UI authentication)
* Amazon API Gateway (JWT Authorizer)
* AWS Lambda
* Amazon DynamoDB
* Amazon S3
* Amazon CloudFront

Key features:

* Cognito Hosted UI login
* JWT-based authentication
* Secure API authorization
* Protected CRUD operations
* Logout functionality

Security flow:

1. User logs in via Cognito Hosted UI
2. Cognito issues a JWT token
3. The frontend includes the token in API requests
4. API Gateway validates the JWT token
5. Authorized requests reach Lambda functions

Unauthorized requests are blocked by API Gateway authorization.

Architecture:

Admin User
↓
CloudFront
↓
S3 Admin UI
↓
Cognito Hosted UI Authentication
↓
API Gateway (JWT Authorizer)
↓
Lambda
↓
DynamoDB

---

## Project #5 — Serverless Monitoring System

A monitoring system for serverless workloads using Amazon CloudWatch.

Services used:

* Amazon CloudWatch Metrics
* Amazon CloudWatch Logs
* Amazon CloudWatch Alarms
* Amazon SNS

Monitoring features:

* API Gateway request monitoring
* Lambda execution metrics
* Log collection and analysis
* CloudWatch alarms for abnormal behavior
* SNS alert notifications

This project demonstrates operational visibility and monitoring for serverless architectures.

Architecture:

Lambda / API Gateway / DynamoDB
↓
CloudWatch Metrics
↓
CloudWatch Logs
↓
CloudWatch Alarms
↓
SNS Notifications

---

# Technologies Used

AWS Services

* Amazon S3
* Amazon CloudFront
* Amazon Cognito
* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* Amazon CloudWatch
* Amazon SNS
* Amazon SES

Languages / Tools

* JavaScript
* HTML / CSS
* Serverless architecture patterns

---

# Key Concepts Demonstrated

This portfolio highlights several important AWS architecture concepts:

* Serverless architecture design
* Secure authentication with Cognito
* JWT authorization with API Gateway
* REST API design
* NoSQL database integration
* Cloud monitoring and observability
* Secure API access patterns
* End-to-end AWS system integration

---

# Author

Yusuke Emata

AWS Certified Solutions Architect – Associate
PMP / PMI-ACP Certified Project Manager

Focused on designing and implementing serverless architectures on AWS, combining cloud engineering with strong project management experience.

---

# Portfolio Website

You can view the live portfolio here:

https://yusuke-cloud.org
