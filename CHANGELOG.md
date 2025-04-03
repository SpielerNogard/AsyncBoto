# Changelog

<!--next-version-placeholder-->

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