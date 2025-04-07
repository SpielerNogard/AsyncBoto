# Usage

```python
from async_boto.core.session import AsyncAWSSession
from async_boto.clients.dynamodb import AsyncDynamoDBClient, ListTablesRequest, ListTablesResponse
import asyncio
session = AsyncAWSSession()
client = AsyncDynamoDBClient(aws_session=session)

resp:ListTablesResponse = asyncio.run(client.list_tables(request=ListTablesRequest()))
resp.TableNames
```
