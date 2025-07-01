# WhatsApp Task Bot

A Python bot that monitors WhatsApp Web for task commands, parses them, and adds to Airtable automatically.

## Overview
This bot uses Selenium to monitor WhatsApp Web for messages starting with `Task`. When detected, it:
1. Parses task details using regex
2. Sends structured data to Airtable
3. Handles attachments and assignments

## Features
- **Task Parsing**: Extracts task details from WhatsApp messages
- **Airtable Integration**: Automatically creates records with attachments
- **Real-time Monitoring**: Listens for new messages continuously
- **Error Handling**: Built-in exception handling for robust operation

## Prerequisites
- Python 3.9+
- WhatsApp Web account
- Airtable account
- Chrome browser

## Local Setup Instructions

### Install Dependencies
```bash
pip install selenium webdriver-manager pyairtable
```
###  Configuration
#### Airtable Setup
1. Create a base in Airtable
2. Create table with these columns:
   - `Task` (Single line text)
   - `Deadline` (Date)
   - `Assign To` (Single line text)
   - `Attachment` (Attachment field)


## Usage
1. Run the bot:
```python
python main.py
```
2. Scan QR code to log in to WhatsApp Web
3. Send task commands in this format:
```text
pip install selenium webdriver-manager pyairtable
```


## Code Structure
### `main.py`
- Handles WhatsApp Web interaction using Selenium
- Monitors messages in real-time
- Uses regex parsing for task extraction
- Main loop with error handling

### `airtable.py`
- Contains Airtable integration logic
- Uses pyAirtable to create records
- Handles attachment URLs
- Environment variable configuration

## Important Notes
1. **Security Warning**: 
   > "Never commit API keys to version control. Use environment variables for production."

2. **QR Code Scanning**:
   > "You have 60 seconds to scan the QR code after starting the bot"

3. **Message Format Requirements**:
   > "Tasks must start with 'Task' and use pipe-separated format with exactly 4 components"

4. **Limitations**:
   - Only monitors the currently open chat
   - Requires stable internet connection
   - Attachment URLs must be directly accessible

## Airtable Setup Guide
1. Create a base with:
   
   **Field Name**
   - Task
   - Deadline
   - Assign To
   - Attachment

2. Get your:
- Base ID from Airtable API docs
- Table ID from table URL
- API key from account settings

## Workflow Diagram
```text
Graph LR

A[WhatsApp Message] --> B(Selenium Monitoring)
B --> C{Starts with 'Task'?}
C -->|Yes| D[Parse Command]
D --> E[Extract Task Details]
E --> F[Add to Airtable]
F --> G[Confirm in Console]
C -->|No| B
```
## Key Features
- **WhatsApp Web Integration:** Monitors WhatsApp Web in real-time using Selenium to detect new messages in the currently open chat.
- **Automated Task Parsing:** Uses regular expressions to extract task details (title, deadline, assignee, and attachment URL) from messages that follow a specific command format.
- **Airtable Connectivity:** Automatically adds parsed tasks as new records in a specified Airtable base, including support for uploading attachments via URLs.
- **Continuous Monitoring:** Runs in a loop to listen for and process new task commands as they arrive, ensuring no tasks are missed.
- **User Feedback:** Provides console output for successful task additions and error messages for invalid formats or exceptions.
- **Customizable and Extensible:** Code is modular, allowing easy adaptation to other messaging platforms or database backends
- **Security Guidance:** Emphasizes the use of environment variables for sensitive Airtable credentials instead of hardcoding.
- **Simple Deployment:** Requires only Python, Chrome, and a few pip-installable packages for rapid setup.




