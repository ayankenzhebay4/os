# Create a hypervisor
hypervisor = Hypervisor(1, "Hypervisor1")

# Create Virtual Machines
vm1 = VirtualMachine(1, "VM1", 2, 8, 500)
vm2 = VirtualMachine(2, "VM2", 4, 16, 1000)

# Add the virtual machines to the hypervisor
hypervisor.create_vm(vm1)
hypervisor.create_vm(vm2)

# List all virtual machines on the hypervisor
hypervisor.list_vms()

# Show the specifications of each virtual machine
vm1.show_specs()
vm2.show_specs()

# Run an application on each virtual machine
vm1.run_app("App1", 1, 2, 125)
vm2.run_app("App2", 1, 12, 750)

# Stop an application on each virtual machine
vm1.stop_app("App1", 1, 2, 125)
vm2.stop_app("App2", 1, 12, 750)

# Show the specifications of each virtual machine after stopping the applications
vm1.show_specs()
vm2.show_specs()
