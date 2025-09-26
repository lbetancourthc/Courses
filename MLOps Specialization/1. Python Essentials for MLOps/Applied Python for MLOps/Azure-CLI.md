# Azure CLI

## Installing Azure CLI

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

Checking some useful commands:

Installation directory:
```bash
which az
```

Version:
```bash
az --version
```

Current extension list:
```bash
az extension list
```

### Install Azure ML Studio CLI and Python

Add Azure ML Studio extension:
```bash
az extension add -n ml -y
```

Veridy the extension installed:
```bash
az extension list
```

Azure ML Studio help:
```bash
az ml --help
```

Login to Azure:
```bash
az login
```

check account list:
```bash
az account list -o table
```

Create and activate Python `venv`:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install AZ ML:
```bash
pip install azureml-core
```

