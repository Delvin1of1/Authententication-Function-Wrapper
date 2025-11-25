def check_user_credentials():
    username = input("Please Enter your Username: ")
    password = input("Please Enter your Password: ")

    stored_username = "Easy Money Sniper"
    stored_password = "IGOTGAME12"

    return username==stored_username and password==stored_password

def send_email(to,subject,message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not check_user_credentials():
                print("Authentication failed. Email NOT sent.")
                return
            
            print(f"Sending email to: {to}")
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@send_email(
        to="niikawei@gmail.com",
        subject="Log in Attempt",
        message="Your Log in was successful"
)
def log_in():
    print(f"Welcome To Your Dashboard")

log_in()
            
