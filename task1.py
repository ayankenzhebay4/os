class VirtualMachine:
    def __init__(self, id, name, cpu, memory, storage):
        self.id = id
        self.name = name
        self.total_cpu = cpu
        self.total_memory = memory
        self.total_storage = storage
        self.available_cpu = cpu
        self.available_memory = memory
        self.available_storage = storage
        self.running_apps = []

    def run_app(self, app, cpu, memory, storage):
        if self.available_cpu >= cpu and self.available_memory >= memory and self.available_storage >= storage:
            self.available_cpu -= cpu
            self.available_memory -= memory
            self.available_storage -= storage
            self.running_apps.append((app, cpu, memory, storage))
            print(f"Running {app} on {self.name}")
        else:
            print(f"Not enough resources to run {app} on {self.name}")

    def stop_app(self, app, cpu, memory, storage):
        if (app, cpu, memory, storage) in self.running_apps:
            self.available_cpu += cpu
            self.available_memory += memory
            self.available_storage += storage
            self.running_apps.remove((app, cpu, memory, storage))
            print(f"Stopped {app} on {self.name}. Freed up CPU: {cpu}, Memory: {memory}, Storage: {storage}")
        else:
            print(f"{app} is not running on {self.name}")

    def show_specs(self):
        print(f"VM Name: {self.name}, CPU: {self.available_cpu}/{self.total_cpu}, Memory: {self.available_memory}/{self.total_memory}, Storage: {self.available_storage}/{self.total_storage}")
