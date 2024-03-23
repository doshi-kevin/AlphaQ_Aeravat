import os
import time
import pyautogui

def capture_screenshots(num_images=5, interval_seconds=0.5, output_folder="images"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for count in range(1, num_images + 1):
        # Capture screen
        screen = pyautogui.screenshot()
        screenshot_path = os.path.join(output_folder, f"screenshot_{count}.png")
        screen.save(screenshot_path)
        print(f"Saved screenshot {count} as {screenshot_path}")

        # Wait for specified interval
        time.sleep(interval_seconds)

if __name__ == "__main__":
    capture_screenshots()
