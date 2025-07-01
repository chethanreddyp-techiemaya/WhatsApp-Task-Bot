import time
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from airtable import add_task_to_airtable


def parse_task_command(message):
    """
    Example command:
    /Task Task-Title | 2025-07-01 | John Doe | https://link-to-attachment.com/file.png
    """
    pattern = r"Task\s+(.+?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.+?)\s*\|\s*(\S+)"
    match = re.match(pattern, message)
    if match:
        task, deadline, assign_to, attachment = match.groups()
        return task.strip(), deadline.strip(), assign_to.strip(), attachment.strip()
    return None


def main():
    # Open WhatsApp Web
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com")
    print("Scan the QR code to log in to WhatsApp Web...")

    # Wait for QR scan
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "canvas[aria-label='Scan me!']")
            time.sleep(2)
        finally:
            break

    print("Logged in! Listening for tasks...")

    last_message = ""
    while True:
        try:
            # Find the last message in the currently open chat
            messages = driver.find_elements(By.CSS_SELECTOR, "div.message-in, div.message-out")
            if messages:
                last = messages[-1]
                message_text = last.text
                if message_text != last_message:
                    last_message = message_text
                    # Check if it's a task command
                    #print(message_text)
                    if message_text.startswith("Task"):
                        parsed = parse_task_command(message_text)
                        print(parsed)
                        if parsed:
                            task, deadline, assign_to, attachment = parsed
                            #print(task,deadline)
                            add_task_to_airtable(task, deadline, assign_to, attachment)
                            print(f"Task added: {task} | {deadline} | {assign_to} | {attachment}")
                        else:
                            print("Invalid task command format.")
            time.sleep(3)
        except Exception as e:
            print("Error:", e)
            time.sleep(5)


if __name__ == "__main__":
    main()
