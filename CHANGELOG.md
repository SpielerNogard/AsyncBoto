# Changelog

<!--next-version-placeholder-->

## 1.1.14 (2025-04-08)

### Fix

- fix

## 1.1.13 (2025-04-08)

### Fix

- fix

## 1.1.12 (2025-04-08)

### Fix

- fix

## 1.1.11 (2025-04-08)

### Fix

- fix

## 1.1.10 (2025-04-08)

### Fix

- fix

## 1.1.9 (2025-04-08)

### Fix

- fix

## 1.1.8 (2025-04-08)

### Fix

- **PiPy**: use correct tag for github release

## 1.1.7 (2025-04-08)

### Fix

- fix

## 1.1.6 (2025-04-08)

### Fix

- **PiPy**: use latest tag name as release name
- **AsyncBoto**: fixed project description in pyproject.toml and docs

## 1.1.5 (2025-04-08)

### Fix

- fix

## 1.1.4 (2025-04-08)

### Fix

- **PiPy-workflow**: trigger workflow with commitzen

## 1.1.3 (2025-04-08)

### Fix

- **PiPy-worklfow**: only start pipy workflow on commitizen bump

## 1.1.2 (2025-04-08)

### Fix

- fix pipy worklow

## 1.1.1 (2025-04-08)

### Fix

- fix

## 1.1.0 (2025-04-08)

### Feat

- **AsyncBoto**: added Documentation url to pyproject.toml

## 1.0.1 (2025-04-08)

### Fix

- fix pipy workflow

## 1.0.0 (2025-04-08)

### Feat

- **ClientError**: the default error type that is raised is now ClientError

## 0.8.0 (2025-04-07)

### Feat

- **AsyncBoto**: added script for building package documentation

## 0.7.0 (2025-04-07)

### Feat

- **AsyncBoto**: added docs using mkdocs

## 0.6.0 (2025-04-04)

### Feat

- **async_boto.core.session**: first experimental implementation of a session

## 0.5.1 (2025-04-03)

### Refactor

- remove unneeded files

## 0.5.0 (2025-04-03)

### Feat

- **AsyncLambdaClient**: added missing methods and first test
- **lambdaclient**: more methods
- **async_boto.clients.lambda_**: added AsyncLambdaClient

## 0.4.1 (2025-03-24)

### Fix

- fix

## 0.4.0 (2025-03-24)

### Feat

- **devcontainer**: start devcontainters

## 0.3.0 (2025-03-11)

### Feat

- **async_boto.clients**: added AsyncTimestreamQueryClient to the clients
- **async_boto.validation**: added validation models for timestream query

## 0.2.0 (2025-03-10)

### Feat

- **AsyncTimestreamWriteClient**: added async client for interaction with the ingest API of timestream
- **async_boto.validation.timestream_write**: added calidation classes for interaction with timestream write

### Fix

- **BaseClient**: always return response

## 0.1.0 (2025-03-01)

### Feat

- **async_boto/clients/sqs.py**: Added AsyncSQSClient for interaction with SQS

## 0.0.3 (2025-02-28)

### Fix

- **async_boto/__init__.py**: added __version__ to package

## 0.0.2 (2025-02-28)

### Fix

- **.github/workflows/commitizen.yml**: trigger on main push
- **.github/workflows/commitizen.yml**: use commitizen build
- **README.md**: just trigger and test commitizen

## v0.0.1 (29/07/2023)

- First release of `async_boto`!