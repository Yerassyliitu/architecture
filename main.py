import multiprocessing

from colorama import Fore
from src.cpu_benchmark import CPUBenchmark
from src.disk_benchmark import DiskBenchmark
from src.memory_benchmark import MemoryBenchmark
from src.system_info import SystemInfo


class BenchmarkRunner:
    """Класс для запуска всех тестов."""
    def __init__(self, duration=5, num_processes=None):
        self.cpu_benchmark = CPUBenchmark(duration, num_processes)

    def start(self, operation_based=True):
        SystemInfo.print_info("CPU Information:", Fore.GREEN)
        SystemInfo.get_cpu_info()
        SystemInfo.print_info("\nMemory Information:", Fore.GREEN)
        SystemInfo.get_memory_info()
        MemoryBenchmark.memory_benchmark()
        DiskBenchmark.disk_benchmark(file_size_mb=100)
        SystemInfo.print_info("\nCPU Benchmark:", Fore.GREEN)
        self.cpu_benchmark.run_benchmark(operation_based=operation_based)
        SystemInfo.print_info("\nReal-time CPU Usage:", Fore.GREEN)
        self.cpu_benchmark.get_real_time_cpu_usage(interval=1, duration=5)


if __name__ == "__main__":
    multiprocessing.freeze_support()

    benchmark_runner = BenchmarkRunner(duration=5, num_processes=4)
    benchmark_runner.start(operation_based=True)