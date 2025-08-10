# 🕒 Python Reminder App with Notifications and Speech

This is a simple Python desktop application that provides periodic reminders using system notifications and optional text-to-speech. The app uses a GUI built with `tkinter` and supports voice reminders using the `pyttsx3` library.

## ✅ Features

- Set custom reminder interval (in minutes)
- Customize reminder title and message
- Option to enable/disable voice notification
- Simple and user-friendly GUI
- System tray notifications via `plyer`
- Lightweight and easy to use

---

## 🛠️ Requirements

Make sure you have Python 3 installed.

Install dependencies using pip:

```bash
pip install pyttsx3 plyer
```

> Note: On some systems, `pyttsx3` may require additional dependencies for voice output (like `espeak` on Linux or `pywin32` on Windows).

---

## ▶️ How to Run

Save the script as `reminder.py` and run:

```bash
python reminder.py
```

---

## 🧠 How It Works

1. Enter the **interval** in minutes (e.g., `1` for every 1 minute).
2. Customize the **title** and **message** of the reminder.
3. Optionally enable the **voice reminder** checkbox.
4. Click **Start Reminder** – the app minimizes and starts sending reminders periodically.
5. To stop the app, click **Stop Reminder** or close the app window.

---

## 🖼️ GUI Overview

| Field               | Description                           |
|--------------------|---------------------------------------|
| Interval            | Time between reminders in minutes     |
| Title               | Notification title                    |
| Message             | Notification content                  |
| Enable Speaking     | Toggle voice reminder on/off          |
| ❌ Buttons          | Quickly clear any text field          |
| Start Reminder      | Starts the reminder loop              |
| Stop Reminder       | Exits the application                 |

---

## 🌐 Example Use Cases

- Remind yourself to take a break or stretch
- Send a religious or motivational message
- Stay hydrated by getting periodic water reminders
- Customize to act as a productivity tool

---

## 📌 Default Values

When you launch the app, it pre-fills the following defaults:

- **Interval:** `1` minutes (1 minute)
- **Title:** `تدكير`
- **Message:** `صلي على رسول الله`

Feel free to change these as needed.

---

## ⚠️ Notes

- Closing the GUI window **does not** stop the background thread if you’ve clicked "Start Reminder".
- For full control, always use the "Stop Reminder" button to exit.
- On some systems, voice functionality might not work without additional configuration.

---

## 📄 License

This project is open-source and free to use. No license is specified—feel free to modify and adapt it to your needs.
