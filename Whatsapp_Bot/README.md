# WhatsApp Bot

## Introduction
WhatsApp Bot is a Python script designed to automate the scheduling and sending of messages on WhatsApp. The script utilizes the existing browser session for WhatsApp Web, allowing users to send messages at a specified time.

## Features
- Schedule messages to be sent at a later time.
- Utilizes the existing WhatsApp Web session for convenience.
- Easy-to-use command-line interface.

## Prerequisites
Before running the script, make sure you have the following installed:
- Python 3.x
- Web browser with an existing WhatsApp Web session

## Getting Started
1. Clone the repository:

    ```bash
    git clone https://github.com/vbvsk/VK_Python_Projects.git
    ```

2. Navigate to the project directory:

    ```bash
    cd VK_Python_Projects/Whatsapp_Bot
    ```

3. Run the Python script:

    ```bash
    python3 WA_Bot.py
    ```

4. Enter the required details when prompted:
    - Mobile number (e.g., +91 9999988888)
    - Message you want to send (e.g., Hare Krishna)
    - Hour (e.g., 1)
    - Minute (e.g., 55)

    The script will inform you that WhatsApp will open in an existing browser session, and the message will be delivered after the specified delay.

## Example
```bash
enter mobile number: +91 9999988888
enter message u want to send: Hare Krishna
enter hour: 1
enter minute: 55
In 53 Seconds WhatsApp will open, and after 15 Seconds, the message will be Delivered!
Opening in an existing browser session.

