import time
import pyautogui
import pyperclip

def copy_content_from_word():
    # Simulate keyboard shortcuts to copy content from MS Word
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy

def paste_content_to_powerpoint():
    # Simulate keyboard shortcuts to paste content into MS PowerPoint
    pyautogui.hotkey('ctrl', 'v')  # Paste

def copy_content_from_google_docs():
    # Simulate keyboard shortcuts to copy content from Google Docs
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy

def paste_content_to_google_slides():
    # Simulate keyboard shortcuts to paste content into Google Slides
    pyautogui.hotkey('ctrl', 'v')  # Paste

def main():
    print("Copy content from MS Word or Google Docs...")
    time.sleep(2)  # Wait for user to focus on the desired document

    copy_content_from_word()  # Call the appropriate copy function

    print("Paste content to MS PowerPoint or Google Slides...")
    time.sleep(2)  # Wait for user to focus on the destination document

    paste_content_to_powerpoint()  # Call the appropriate paste function

if __name__ == '__main__':
    main()
