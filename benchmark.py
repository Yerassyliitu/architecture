import os
import psutil
import time
import multiprocessing
import random
from colorama import init, Fore, Style


init(autoreset=True)


class CPUBenchmark:
    def __init__(self, duration=5, num_processes=None):
        self.duration = duration
        self.num_processes = num_processes or multiprocessing.cpu_count()

    def print_info(self, message, color=Fore.WHITE):
        print(f"{color}{message}{Style.RESET_ALL}")

    def get_cpu_info(self):
        physical_cores = psutil.cpu_count(logical=False)
        logical_cores = psutil.cpu_count(logical=True)
        frequency = psutil.cpu_freq().current if psutil.cpu_freq() else "Unknown"

        self.print_info(f"Physical cores: {Fore.CYAN}{physical_cores}", Fore.CYAN)
        self.print_info(f"Logical cores: {Fore.CYAN}{logical_cores}", Fore.CYAN)
        self.print_info(f"CPU frequency: {Fore.CYAN}{frequency} MHz", Fore.CYAN)

    def get_memory_info(self):
        memory = psutil.virtual_memory()
        total_memory = memory.total / (1024 ** 3)
        available_memory = memory.available / (1024 ** 3)

        self.print_info(f"Total memory: {Fore.GREEN}{total_memory:.2f} GB", Fore.GREEN)
        self.print_info(f"Available memory: {Fore.GREEN}{available_memory:.2f} GB", Fore.GREEN)

    def memory_benchmark(self):
        """Memory performance test by creating a large array of data."""
        self.print_info("Running memory performance test...", Fore.MAGENTA)
        start_time = time.time()
        large_data = [random.random() for _ in range(10**7)]
        self.print_info(f"Array created in {time.time() - start_time:.2f} seconds", Fore.MAGENTA)

    def disk_benchmark(self, file_size_mb=100):
        """Disk performance test by measuring write and read speeds."""
        self.print_info("Running disk performance test...", Fore.BLUE)
        data = os.urandom(file_size_mb * 1024 * 1024)  # Generate 100 MB of random data
        file_path = "test_disk_benchmark.tmp"
        
        # Write test
        start_time = time.time()
        with open(file_path, "wb") as f:
            f.write(data)
        write_time = time.time() - start_time
        self.print_info(f"Wrote {file_size_mb} MB file in {write_time:.2f} seconds", Fore.YELLOW)

        # Read test
        start_time = time.time()
        with open(file_path, "rb") as f:
            _ = f.read()
        read_time = time.time() - start_time
        self.print_info(f"Read {file_size_mb} MB file in {read_time:.2f} seconds", Fore.YELLOW)

        # Remove file
        os.remove(file_path)

    def get_real_time_cpu_usage(self, interval=1, duration=5):
        self.print_info(f"Monitoring CPU usage for {duration} seconds...", Fore.YELLOW)
        for i in range(int(duration / interval)):
            usage = psutil.cpu_percent(interval=interval)
            self.print_info(f"[{i+1}/{int(duration / interval)}] CPU usage: {Fore.MAGENTA}{usage}%", Fore.YELLOW)

    @staticmethod
    def compute_operations(num_operations=10**7):
        result = 0
        for _ in range(num_operations):
            result += 1
        return result

    def run_benchmark(self, operation_based=True):
        if operation_based:
            self.print_info("Running operation-based performance test...", Fore.BLUE)
        else:
            self.print_info(f"Running time-based performance test: {self.duration} seconds...", Fore.BLUE)

        start_time = time.time()
        processes = []

        for _ in range(self.num_processes):
            if operation_based:
                process = multiprocessing.Process(target=self.compute_operations)
            else:
                process = multiprocessing.Process(target=self.run_timed_test)
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.print_info(f"Elapsed time: {Fore.CYAN}{elapsed_time:.2f} seconds", Fore.CYAN)

    def run_timed_test(self):
        end_time = time.time() + self.duration
        result = 0
        while time.time() < end_time:
            result += 1

    def start(self, operation_based=True):
        self.print_info("CPU Information:", Fore.GREEN)
        self.get_cpu_info()
        self.print_info("\nMemory Information:", Fore.GREEN)
        self.get_memory_info()
        self.memory_benchmark()
        self.disk_benchmark(file_size_mb=100)
        self.print_info("\nCPU Benchmark:", Fore.GREEN)
        self.run_benchmark(operation_based=operation_based)
        self.print_info("\nReal-time CPU Usage:", Fore.GREEN)
        self.get_real_time_cpu_usage(interval=1, duration=5)


if __name__ == "__main__":
    multiprocessing.freeze_support()

    benchmark = CPUBenchmark(duration=5, num_processes=4)
    benchmark.start(operation_based=True)
