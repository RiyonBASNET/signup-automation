# Signup Automation Script

## 1. Overview

This Python script automates the signup process on: https://authorized-partner.vercel.app/

The automation covers:

- Opening the landing page
- Clicking "Get Started" to reach the signup page
- Agreeing to Terms of Service
- Filling all required form fields:
  - First Name
  - Last Name
  - Email
  - Phone Number
  - Password
  - Confirm Password
- Submitting the signup form
- Stopping when the Email Verification (OTP) section is rendered (OTP is not automated for security reasons)

## 2. Prerequisites / Environment

- Python 3.8+
- Google Chrome (latest stable version)
- ChromeDriver matching Google Chrome version
- Selenium 4.x

Install Selenium via pip:

```bash
 pip install selenium
```

### ChromeDriver Setup

- Download ChromeDriver matching your installed Google Chrome version
- Place `chromedriver.exe` in the project root directory OR add it to the system PATH

## 3. How to Run the Script

1. Clone the repository:

```bash
   git clone https://github.com/RiyonBASNET/signup-automation.git
   cd signup-automation
```

2. Activate virtual environment (optional but recommended)

```bash
   python -m venv venv
   .\venv\Scripts\activate
```

3. Install dependencies

```bash
   pip install -r requirements.txt
```

4. Run the script

```bash
   python signup_automation_script.py
```

- The browser will open automatically
- It will navigate through the signup form
- It will stop when the Email Verification (OTP) section is displayed

## 4. Test Data Used

- First Name : Test
- Last Name : User
- Email : test.user@gmail.com (test email)
- Phone Number : 9818181818 (dummy number)
- Password : Test@1234

## 5. OTP Handling

- The signup flow requires email-based OTP verification after Account Setup
- The OTP is sent to the registered email address
- For this assignment, a dummy/test email address was used, so the received OTP is not accessible
- As a result, OTP verification cannot be completed
- The automation validates successful progression by confirming that the Email Verification (OTP) section is rendered
- Full OTP automation would require access to a test email inbox or a fixed test OTP provided by the system
