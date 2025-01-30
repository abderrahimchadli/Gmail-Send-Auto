# Gmail-Send-Auto

**Developer**: Abderrahim Chadli

Gmail-Send-Auto is a Python-based application designed to automate the process of sending emails through Gmail. It utilizes Selenium to interact with the Gmail web interface, allowing for automated email dispatch without relying on the Gmail API.

## Features

- **Automated Email Sending**: Leverages Selenium to compose and send emails via Gmail's web interface.
- **Cross-Platform Compatibility**: Includes scripts tailored for both Windows and Linux environments.
- **Customizable Email Content**: Allows users to define the subject and body of the email.

## Project Structure

The repository is organized as follows:

- `chromedriver.exe`: ChromeDriver executable for Windows systems.
- `finalscript.py`: Main script for automating email sending.
- `linux.py`: Script tailored for Linux systems.
- `mailsend.py`: Contains functions related to email composition and sending.
- `selisend.py`: Utilizes Selenium for browser automation to send emails.
- Additional Python scripts (`ftest2.py`, `gmailsend.py`, `googlesend.py`, `ts.py`, `tsf.py`): Various scripts exploring different methods of sending emails.

## Prerequisites

- **Python**: Ensure Python is installed on your system.
- **Google Chrome**: Required for Selenium to interact with the Gmail web interface.
- **ChromeDriver**: Compatible with your version of Google Chrome. For Linux users, download the appropriate version from the [official ChromeDriver site](https://sites.google.com/chromium.org/driver/).

## Installation

To set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abderrahimchadli/Gmail-Send-Auto.git
   cd Gmail-Send-Auto
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install selenium
   ```

4. **Configure ChromeDriver**:

   - **Windows**: Ensure `chromedriver.exe` is in the project directory.
   - **Linux**: Download the appropriate `chromedriver` version and place it in the project directory or a directory included in your system's `PATH`.

## Usage

1. **Prepare the Script**:

   - Open `finalscript.py` (or `linux.py` for Linux users) in a text editor.
   - Update the script with your Gmail credentials and the desired email content.

2. **Run the Script**:

   ```bash
   python finalscript.py
   ```

   The script will launch Google Chrome, log into your Gmail account, compose the email, and send it to the specified recipient.

## Security Considerations

- **Google Account Security**: Be aware that using automated scripts to log into your Gmail account may trigger security alerts or temporary account locks. It's advisable to use an application-specific password and ensure your account has appropriate security settings.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Abderrahim Chadli
---

