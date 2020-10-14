from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/wp-login.php", {"username":"nabor", "password":"education"})

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    # @task
    # def index(self):
    #     self.client.get("/?p=1") # Realiza um get na url <HOST_DO_WORDPRESS>/?p=1


    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
