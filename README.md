# Gatekeeper App - User Registration System (Simulation)

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Connect with Me
Let's connect! Find me on:

[![GitHub](https://img.shields.io/badge/GitHub-AheebwaMike-181717?style=for-the-badge&logo=github)](https://github.com/AheebwaMike)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-AheebwaMichael-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/AheebwaMichael)
[![Instagram](https://img.shields.io/badge/Instagram-Michael_Aheebwa-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/michael_aheebwa?igsh=MW5kYm5tYjk2OTgzdA==)
[![SoloLearn](https://img.shields.io/badge/SoloLearn-Drichlet-149EF2?style=for-the-badge&logo=sololearn)](https://www.sololearn.com/profile/aheebwamike](https://www.sololearn.com/en/profile/33968466))

## About This Python Program
A secure Python-based user registration system with validation, password hashing, and subscription management.

## Features

- User name validation (2+ characters, no special characters except _)
- Password management (auto-generation or manual entry with strict validation rules)
- Date of birth verification (DD/MM/YYYY format, 18+ only)
- Subscription system with payment options
- Configuration management via INI files
- SHA-256 password hashing for security

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AheebwaMike/gatekeeper-lite.git
   cd gatekeeper-lite
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

### Skills Demonstrated

#### 1. Core Programming
- File I/O operations (JSON, INI)
- Regular expressions
- Data validation
- Error handling
- Modular code organization

#### 2. Security
- Password hashing (SHA-256)
- Input sanitization
- Secure password generation
- Age verification

#### 3. Software Practices
- Configuration management
- User interaction flows
- Persistent data storage
- Separation of concerns

## Why I Built This
This project is part of my self-teaching journey in Python. It combines practical coding with real-world concepts such as:
- Configuration files (.ini, .json)
- Data validation
- Simulated user authentication and logging workflows

Feel free to use this project to learn, expand, or adapt it for your own work.

## Feedback and Contributions
Suggestions and contributions are welcome.

Open an issue or fork the project and share your ideas.

## License
MIT License — feel free to use, modify, and share. Please give credit where it is due.

