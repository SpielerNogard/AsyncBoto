# Welcome to AsyncBoto

AsyncBoto is a Python library that provides an asynchronous interface similar to the Boto3 library, allowing you to interact with AWS services in a non-blocking manner.
This can be particularly useful for applications that require high concurrency or need to perform multiple AWS operations simultaneously.
This library is built on top of aiohttp and is designed to be easy to use, efficient, and compatible with the latest AWS services.

## Features
- Asynchronous API: Built on top of aiohttp, allowing for non-blocking I/O operations.
- Familiar Interface: Similar to Boto3, making it easy for existing Boto3 users to transition.
- Support for Multiple AWS Services: Interact with various AWS services such as S3, DynamoDB, and more.
- Automatic Retries: Built-in support for automatic retries on failed requests.
- Session Management: Manage AWS sessions and credentials easily.
- Customizable: Easily extendable and customizable to fit your needs.
- Full typing support: Every request/response is fully typed using pydantic models.

## Installation
You can install AsyncBoto using pip:

```bash
pip install asyncboto
```

or using uv
```bash
uv pip install asyncboto
```


For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

