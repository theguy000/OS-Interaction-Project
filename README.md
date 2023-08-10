### OS Interaction Project

---

#### Introduction

This project consists of scripts to interact with the operating system and perform specific actions depending on whether the system is running Windows or Linux. It simply performs random mouse movements and stops when you press **ESC**

#### Requirements

- Python 3.x
- Libraries: `pyautogui`, `random`, `time`, `pynput` (for Linux), `msvcrt` (for Windows)

#### Installation

1. Clone the repository or download the project files.
2. Install the required Python libraries(for linux only):
   ```bash
   pip install pyautogui pynput
   ```

#### Usage

To run the project, execute the `main.py` file:

```bash
python main.py
```

The script will detect the operating system and run the corresponding code:
- On Windows: The script will perform random mouse movements on the screen.
- On Linux: The script will monitor keyboard events and listen for the escape key.

#### Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request, or open an issue to discuss your ideas.

#### License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to modify or add any sections as needed. If you'd like to download this README as a file, let me know, and I can provide it in the desired format!
