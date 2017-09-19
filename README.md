# Ridibooks CMS SDK
[![Packagist](https://img.shields.io/packagist/v/ridibooks/cms-sdk.svg)](https://packagist.org/packages/ridibooks/cms-sdk)

## Introduction
CMS SDK provides common resources used in RIDI CMS
- RPC Client code to communicate with CMS auth server
- Common twig templates

This library uses [Apache Thrift](https://thrift.apache.org) for a RPC implementation.

## Hierarchy
```
cms-sdk
├── src
│   ├── (...)          # Wrapping classes which uses thrift client inside.
│   │
│   └── Thrift
│        ├── (...)     # PHP codes generated by Thrift source.
│        └── *.thrift  # Thrift source to communicate with CMS Auth server.
│
├── views
│   └── *.twig         # Common twig templates
...
```

## Dependencies
To make RPC client, you should install Apache Thrift.
```
# In OSX, you can install easily with homebrew.
brew install thrift
```

## Generate code
To generate thrift code, please run:
```
make thrift
```

## Usage
- [PHP](./lib/php/README.md)
- [Node.js](./lib/nodejs/README.md)
