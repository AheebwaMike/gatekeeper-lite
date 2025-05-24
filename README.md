# Gatekeeper App - User Registration System

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A secure Python-based user registration system with validation, password hashing, and subscription management.

## Features

- ✔️ User name validation (2+ chars, no special chars except _)
- 🔒 Password management (auto-generation or manual with strict rules)
- 📅 Date of birth verification (DD/MM/YYYY format, 18+ only)
- 💳 Subscription system with payment options
- ⚙️ Configuration management via INI files
- 🔐 SHA-256 password hashing for security

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AheebwaMike/gatekeeper-app.git
   cd gatekeeper-app
2. Run the application
   ```bash
   python main.py
### Usage
Follow the interactive prompts to:
1. Enter your name (validated)
2. Set or generate a password
3. Provide your date of birth
4. Choose subscription options
Your details will be securely stored in database.json and settings saved in settings.ini.

### Code Structure
gatekeeper-app/
├── main.py            # Main application logic 
├── app_utils.py       # Validation and utility functions 
├── database.json      # User data storage (created if doesn't exist) 
├── settings.ini       # Application configuration 
└── README.md          # This file 

### SKills Demonstrated
## 1. Core Programming
- File I/O operations (JSON, INI)
- Regular expressions
- Data validation
- Error handling
- Modular code organization
## 2. Security
- Password hashing (SHA-256)
- Input sanitization
- Secure password generation
- Age verification
## 3. Software Practices
- Configuration management
- User interaction flows
- Persistent data storage
- Separation of concerns

