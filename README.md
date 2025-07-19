# EAPP Python Domain 🐍

[![System Contracts Build](https://img.shields.io/github/actions/workflow/status/50gramx/eapp-system-contracts/protobuf-distribution.yml?label=system-contracts%20CI)](https://github.com/50gramx/eapp-system-contracts/actions/workflows/protobuf-distribution.yml)
[![Latest Release](https://img.shields.io/github/v/release/50gramx/eapp-python-domain?label=latest%20release)](https://github.com/50gramx/eapp-python-domain/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Package Index](https://img.shields.io/badge/index-private%20package%20index-blue)](https://raw.githubusercontent.com/50gramx/eapp-python-domain/master/packages/index.html)

> **Python client library for EAPP (Ethos Apps Platform)** - Auto-generated protobuf client code for seamless integration with EAPP services.

## 📦 Package Index & Downloads

### 🚀 Quick Access
- **[📋 Package Index (HTML Preview)](https://html-preview.github.io/?url=https://github.com/50gramx/eapp-python-domain/blob/master/packages/index.html)** - View all available packages
- **[📋 Raw Package Index](https://raw.githubusercontent.com/50gramx/eapp-python-domain/master/packages/index.html)** - Direct package index
- **[📥 Latest Release](https://github.com/50gramx/eapp-python-domain/releases/latest)** - Download latest version
- **[🏗️ Build Status](https://github.com/50gramx/eapp-system-contracts/actions/workflows/protobuf-distribution.yml)** - Check CI/CD status

### 📦 Available Packages
> **📋 View all available packages and versions in our [Package Index (HTML Preview)](https://html-preview.github.io/?url=https://github.com/50gramx/eapp-python-domain/blob/master/packages/index.html)**

### 🔧 Installation
```bash
# Install from our package index
pip install --index-url https://raw.githubusercontent.com/50gramx/eapp-python-domain/master/packages/index.html eapp-python-domain

# Or install specific version
pip install --index-url https://raw.githubusercontent.com/50gramx/eapp-python-domain/master/packages/index.html eapp-python-domain==0.1.0.1752936352
```

## 📋 Table of Contents

- [Overview](#-overview)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🔧 Usage](#-usage)
- [📚 API Reference](#-api-reference)
- [🔄 Auto-Generation](#-auto-generation)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🌟 Overview

EAPP Python Domain provides **auto-generated Python client code** for all EAPP system contracts. This package is automatically generated from Protocol Buffer definitions and provides type-safe, efficient access to EAPP services.

### 🎯 Key Features

- **🔄 Auto-Generated** - Built from protobuf definitions in [eapp-system-contracts](https://github.com/50gramx/eapp-system-contracts)
- **📦 Type-Safe** - Full type hints and IDE support
- **⚡ High Performance** - Optimized protobuf serialization
- **🔒 Production Ready** - Used in production EAPP services
- **📚 Comprehensive** - Covers all EAPP service contracts

### 🏗️ Service Coverage

| Service Category | Description | Available |
|------------------|-------------|-----------|
| **🔐 Identity** | User authentication & authorization | ✅ |
| **💬 Communication** | Messaging & notifications | ✅ |
| **🧠 Cognitive** | AI & knowledge management | ✅ |
| **🛍️ Commerce** | Transactions & payments | ✅ |
| **🌌 Multiverse** | Space & universe management | ✅ |

## 🚀 Quick Start

### 1. Installation

```bash
# Install from our private package index
pip install --index-url https://raw.githubusercontent.com/50gramx/eapp-python-domain/master/packages/index.html eapp-python-domain

# Or install from PyPI (if published)
pip install eapp-python-domain
```

### 2. Basic Usage

```python
from eapp_python_domain.ethos import user_pb2, account_pb2

# Create a user
user = user_pb2.User()
user.id = "user123"
user.name = "John Doe"
user.email = "john@example.com"

# Create an account
account = account_pb2.Account()
account.id = "acc123"
account.user_id = user.id
account.status = account_pb2.AccountStatus.ACTIVE

print(f"User: {user.name} ({user.email})")
print(f"Account: {account.id} - Status: {account.status}")
```

### 3. Service Integration

```python
import grpc
from eapp_python_domain.ethos import account_service_pb2, account_service_pb2_grpc

# Connect to EAPP service
channel = grpc.insecure_channel('localhost:50051')
stub = account_service_pb2_grpc.AccountServiceStub(channel)

# Create account request
request = account_service_pb2.CreateAccountRequest()
request.user_id = "user123"
request.account_type = account_service_pb2.AccountType.PERSONAL

# Call service
response = stub.CreateAccount(request)
print(f"Created account: {response.account.id}")
```

## 📦 Installation

### Requirements

- **Python**: 3.7+
- **Dependencies**: 
  - `protobuf>=3.21.0`
  - `grpcio>=1.50.0`

### Installation Methods

#### 1. Private Package Index (Recommended)
```bash
pip install --index-url https://raw.githubusercontent.com/50gramx/eapp-python-domain/master/packages/index.html eapp-python-domain
```

#### 2. From Source
```bash
git clone https://github.com/50gramx/eapp-python-domain.git
cd eapp-python-domain
pip install -e .
```

#### 3. Development Installation
```bash
git clone https://github.com/50gramx/eapp-python-domain.git
cd eapp-python-domain
pip install -e ".[dev]"
```

## 🔧 Usage

### Importing Modules

```python
# Core entities
from eapp_python_domain.ethos import user_pb2
from eapp_python_domain.ethos import account_pb2
from eapp_python_domain.ethos import space_pb2

# Service stubs
from eapp_python_domain.ethos import account_service_pb2_grpc
from eapp_python_domain.ethos import user_service_pb2_grpc
from eapp_python_domain.ethos import space_service_pb2_grpc
```

### Working with Messages

```python
from eapp_python_domain.ethos import user_pb2

# Create messages
user = user_pb2.User(
    id="user123",
    name="John Doe",
    email="john@example.com",
    status=user_pb2.UserStatus.ACTIVE
)

# Serialize to bytes
user_bytes = user.SerializeToString()

# Deserialize from bytes
user_from_bytes = user_pb2.User()
user_from_bytes.ParseFromString(user_bytes)

# Convert to/from JSON
user_json = user.to_json()
user_from_json = user_pb2.User.from_json(user_json)
```

### gRPC Service Calls

```python
import grpc
from eapp_python_domain.ethos import account_service_pb2, account_service_pb2_grpc

async def get_user_accounts(user_id: str):
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = account_service_pb2_grpc.AccountServiceStub(channel)
        
        request = account_service_pb2.GetUserAccountsRequest(user_id=user_id)
        response = await stub.GetUserAccounts(request)
        
        return response.accounts
```

## 📚 API Reference

### Core Entities

#### User
```python
from eapp_python_domain.ethos import user_pb2

user = user_pb2.User(
    id="string",           # Unique user identifier
    name="string",         # Display name
    email="string",        # Email address
    status=user_pb2.UserStatus.ACTIVE,  # User status
    created_at="timestamp", # Creation timestamp
    updated_at="timestamp"  # Last update timestamp
)
```

#### Account
```python
from eapp_python_domain.ethos import account_pb2

account = account_pb2.Account(
    id="string",           # Unique account identifier
    user_id="string",      # Associated user ID
    type=account_pb2.AccountType.PERSONAL,  # Account type
    status=account_pb2.AccountStatus.ACTIVE, # Account status
    created_at="timestamp" # Creation timestamp
)
```

#### Space
```python
from eapp_python_domain.ethos import space_pb2

space = space_pb2.Space(
    id="string",           # Unique space identifier
    name="string",         # Space name
    description="string",  # Space description
    owner_id="string",     # Owner user ID
    type=space_pb2.SpaceType.PUBLIC,  # Space type
    created_at="timestamp" # Creation timestamp
)
```

### Service Stubs

#### AccountService
```python
from eapp_python_domain.ethos import account_service_pb2_grpc

# Available methods:
# - CreateAccount(request)
# - GetAccount(request)
# - UpdateAccount(request)
# - DeleteAccount(request)
# - GetUserAccounts(request)
```

#### UserService
```python
from eapp_python_domain.ethos import user_service_pb2_grpc

# Available methods:
# - CreateUser(request)
# - GetUser(request)
# - UpdateUser(request)
# - DeleteUser(request)
# - ListUsers(request)
```

## 🔄 Auto-Generation

This package is **automatically generated** from protobuf definitions in the [eapp-system-contracts](https://github.com/50gramx/eapp-system-contracts) repository.

### Generation Process

1. **Protobuf Changes** - Updates to `.proto` files in system-contracts
2. **CI/CD Trigger** - GitHub Actions workflow automatically triggers
3. **Code Generation** - `protoc` generates Python code from `.proto` files
4. **Package Building** - Creates Python wheel and source distribution
5. **Release Creation** - Creates GitHub release with new version
6. **Index Update** - Updates package index with new release

### Versioning

- **Auto-generated versions** - Based on timestamp: `0.1.0.{timestamp}`
- **Release frequency** - On every protobuf change
- **Backward compatibility** - Maintained within major versions

## 🤝 Contributing

### For Python-Specific Changes

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### For Protobuf Changes

1. **Update** protobuf definitions in [eapp-system-contracts](https://github.com/50gramx/eapp-system-contracts)
2. **Push** to trigger auto-generation
3. **Review** generated Python code
4. **Test** with your changes

### Development Setup

```bash
# Clone repository
git clone https://github.com/50gramx/eapp-python-domain.git
cd eapp-python-domain

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest tests/

# Run linting
flake8 src/
black src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Quick Links

- **📦 Package Index**: [View Packages](https://raw.githubusercontent.com/50gramx/eapp-python-domain/master/packages/index.html)
- **🏗️ System Contracts**: [eapp-system-contracts](https://github.com/50gramx/eapp-system-contracts)
- **🐛 Issues**: [GitHub Issues](https://github.com/50gramx/eapp-python-domain/issues)
- **📖 Documentation**: [API Docs](https://github.com/50gramx/eapp-python-domain/wiki)
- **💬 Discussions**: [GitHub Discussions](https://github.com/50gramx/eapp-python-domain/discussions)

---

<div align="center">
  <p><strong>Auto-generated Python client for EAPP System Contracts</strong></p>
  <p><em>Built with ❤️ by the EAPP Team</em></p>
</div>
