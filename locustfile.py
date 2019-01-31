from locust import HttpLocust, TaskSet, task


class UserActions(TaskSet):


	def on_start(self):
		self.login()


	def login(self):
		# login to the application
		response = self.client.get('/login/')
		csrftoken = response.cookies['csrftoken']
		self.client.post('/login/', {'username': '60004160040', 'password': 'demopass'}, headers={'X-CSRFToken': csrftoken})


	@task(1)
	def index(self):
		self.client.get('/')


	for i in range(4):
		@task(2)
		def first_page(self):
			self.client.get('/analytics/')



class ApplicationUser(HttpLocust):
	task_set = UserActions
	min_wait = 0
	max_wait = 0