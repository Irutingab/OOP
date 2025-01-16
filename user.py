class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_tittle = current_job_title
    def change_password(self, new_password):
        self.password = new_password
    def change_job_tittle(self, new_job_title):
        self.new_job_title = new_job_title
    def get_user_info(self):
        
        print(f"User{self.name} works as {self.current_job_tittle} and you can contact them at {self.email}")
app_user_one=User("nn@gmail.com", "Nana Janashia", "pwd1", "DevOps")

app_user_one.get_user_info()
app_user_one.new_job_title("Software trainer")
app_user_one.get_user_info()