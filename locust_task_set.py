from locust import HttpUser, between, task, TaskSet, SequentialTaskSet


class MyTaskSet(TaskSet):
    @task
    def task_one(self):
        return self.client.get("/page/1")

    @task
    def task_two(self):
        return self.client.get("/page/2")


class MySequentialTaskSet(TaskSet):
    @task
    def task_three(self):
        return self.client.get("/page/3")

    @task
    def task_four(self):
        return self.client.get("/page/4")


class MyUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [MyTaskSet]
