import psutil
import time
import multiprocessing
from colorama import Fore

from src.system_info import SystemInfo


class CPUBenchmark:
    """Класс для тестирования производительности CPU."""
    def __init__(self, duration=5, num_processes=None):
        self.duration = duration
        self.num_processes = num_processes or multiprocessing.cpu_count()

    @staticmethod
    def compute_operations(num_operations=10**7):
        result = 0
        for _ in range(num_operations):
            result += 1
        return result

    def run_benchmark(self, operation_based=True):
        SystemInfo.print_info(
            "Running operation-based performance test..." if operation_based else
            f"Running time-based performance test: {self.duration} seconds...",
            Fore.BLUE
        )

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
        SystemInfo.print_info(f"Elapsed time: {Fore.CYAN}{elapsed_time:.2f} seconds", Fore.CYAN)

    def run_timed_test(self):
        end_time = time.time() + self.duration
        result = 0
        while time.time() < end_time:
            result += 1

    @staticmethod
    def get_real_time_cpu_usage(interval=1, duration=5):
        SystemInfo.print_info(f"Monitoring CPU usage for {duration} seconds...", Fore.YELLOW)
        for i in range(int(duration / interval)):
            usage = psutil.cpu_percent(interval=interval)
            SystemInfo.print_info(f"[{i+1}/{int(duration / interval)}] CPU usage: {Fore.MAGENTA}{usage}%", Fore.YELLOW)
