import random
import time
from src.system_info import SystemInfo
from colorama import Fore


class MemoryBenchmark:
    """Класс для тестирования производительности памяти."""
    @staticmethod
    def memory_benchmark():
        SystemInfo.print_info("Running memory performance test...", Fore.MAGENTA)
        start_time = time.time()
        large_data = [random.random() for _ in range(10**7)]
        SystemInfo.print_info(f"Array created in {time.time() - start_time:.2f} seconds", Fore.MAGENTA)

