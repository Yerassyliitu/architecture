import os
from colorama import Fore
import time
from src.system_info import SystemInfo


class DiskBenchmark:
    """Класс для тестирования производительности диска."""
    @staticmethod
    def disk_benchmark(file_size_mb=100):
        SystemInfo.print_info("Running disk performance test...", Fore.BLUE)
        data = os.urandom(file_size_mb * 1024 * 1024)  # Генерация данных размером 100 MB
        file_path = "test_disk_benchmark.tmp"

        # Тест записи
        start_time = time.time()
        with open(file_path, "wb") as f:
            f.write(data)
        write_time = time.time() - start_time
        SystemInfo.print_info(f"Wrote {file_size_mb} MB file in {write_time:.2f} seconds", Fore.YELLOW)

        # Тест чтения
        start_time = time.time()
        with open(file_path, "rb") as f:
            _ = f.read()
        read_time = time.time() - start_time
        SystemInfo.print_info(f"Read {file_size_mb} MB file in {read_time:.2f} seconds", Fore.YELLOW)

        # Удаление файла
        os.remove(file_path)