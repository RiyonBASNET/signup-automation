# Signup Automation Script

## 1. Overview

This Python script automates the signup process on: https://authorized-partner.vercel.app/

The automation covers:

- Opening the landing page
- Clicking "Get Started" to reach signup page
- Agreeing to Terms of Service
- Filling all required form fields:
  - First Name
  - Last Name
  - Email
  - Phone Number
  - Password
  - Confirm Password
- Submitting the signup form
- Stopping at the Email Verification Code page (OTP is not automated for security reasons)

## 2. Prerequisites / Environment

- Python 3.8+
- Google Chrome (latest stable version)
- ChromeDriver matching Google Chrome version
- Selenium 4.x

Install Selenium via pip

- pip install selenium

### ChromeDriver Setup

- Download ChromeDriver matching your installed Google Chrome version
- Place 'chromedriver.exe' in the project root directory OR add it to the system PATH

## 3. How to Run the Script

1. Clone the repository:
   git clone https://github.com/RiyonBASNET/signup-automation.git
   cd signup-automation

2. Activate virtual environment (optional but recommended)
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the script
   python signup_automation_script.py

- The browser will open automatically
- It will navigate through the signup form
- It will stop at the Email Verification Code

## 4. Test Data Used

- First Name : Test
- Last Name : User
- Email : test.user@gmail.com (test email)
- Phone Number : 9818181818 (dummy number)
- Password : R@M1bahadur

## 5. OTP Handling

- The signup flow requires email verification after Account Setup
- OTP is sent to the registered email address
- Automating OTP entry is intentionally skipped due to security and privacy constraints
- The automation validates successful completion of Account Setup by confirming navigation to Email Varification page
