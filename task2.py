class Hypervisor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.vms = []

    def create_vm(self, vm):
        self.vms.append(vm)
        print(f"Created VM {vm.name} on {self.name}")

    def remove_vm(self, vm):
        self.vms.remove(vm)
        print(f"Removed VM {vm.name} from {self.name}")

    def list_vms(self):
        for vm in self.vms:
            print(f"VM ID: {vm.id}, VM Name: {vm.name}")
