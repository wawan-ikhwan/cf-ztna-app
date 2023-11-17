# cf-ztna-app

This project is a FastAPI application for listing devices in the Cloudflare Zero Trust Network Access (ZTNA).

## Table of Contents

- [Introduction](#introduction)
- [Feature](#feature)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The cf-ztna-app is a FastAPI application designed to retrieve and list devices in the Cloudflare Zero Trust Network Access (ZTNA).

## Feature

- **List Devices:** Retrieve and display the devices connected to the Zero Trust Network.

## Getting Started

### Prerequisites

Ensure you have the following prerequisites installed:

- Python 3
- [virtualenv](https://virtualenv.pypa.io/) (optional but recommended)

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/wawan-ikhwan/cf-ztna-app.git
cd cf-ztna-app
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```
