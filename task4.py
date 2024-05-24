# Run multiple applications on each virtual machine
vm1.run_app("App1", 1, 2, 125)
vm2.run_app("App2", 1, 12, 750)

# Stop the applications to calculate utilization
vm1.stop_app("App1", 1, 2, 125)
vm2.stop_app("App2", 1, 12, 750)

# Calculate resource utilization
def calculate_utilization(total, used):
    return (used / total) * 100

# Utilization for VM1
cpu_util_vm1 = calculate_utilization(vm1.total_cpu, 1)
memory_util_vm1 = calculate_utilization(vm1.total_memory, 2)
storage_util_vm1 = calculate_utilization(vm1.total_storage, 125)

# Utilization for VM2
cpu_util_vm2 = calculate_utilization(vm2.total_cpu, 1)
memory_util_vm2 = calculate_utilization(vm2.total_memory, 12)
storage_util_vm2 = calculate_utilization(vm2.total_storage, 750)

print(f"Resource utilization for VM1 - CPU: {cpu_util_vm1}%, Memory: {memory_util_vm1}%, Storage: {storage_util_vm1}%")
print(f"Resource utilization for VM2 - CPU: {cpu_util_vm2}%, Memory: {memory_util_vm2}%, Storage: {storage_util_vm2}%")
