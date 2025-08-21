# 🎉 Automated Birthday Wisher

An automated Python script that sends personalized birthday wishes via email.  
This project reads birthday information from a CSV file, matches today’s date, selects a random pre-written letter template, and sends the message to the birthday person automatically.

## ✨ Features
- Reads birthdays from a `birthdays.csv` file.  
- Picks a random birthday message template from the `letter_templates` folder.  
- Automatically replaces `[NAME]` with the person’s real name.  
- Sends the greeting via Gmail SMTP.  
- Can be scheduled to run daily (using `cron` or Task Scheduler).

## 📂 Project Structure
-Automated-Birthday-Wisher/
-├── main.py                # Main Python script
-├── birthdays.csv          # List of birthdays (name, email, year, month, day)
-├── letter_templates/      # Folder containing pre-written birthday messages
-│    ├── letter_1.txt
-│    ├── letter_2.txt
-│    ├── letter_3.txt
-│    └── letter_4.txt
-└── README.md              # Project documentation

## 📊 Example `birthdays.csv`
```csv
name,email,year,month,day
Mom,mom22@gmail.com,1971,8,21
Dad,dad223@gmail.com,1970,11,18
##Clone the Repository
git clone https://github.com/yourusername/Automated-Birthday-Wisher.git
cd Automated-Birthday-Wisher

##Install Dependencies
pip install pandas

