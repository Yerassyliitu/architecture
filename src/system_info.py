import psutil
from colorama import init, Fore, Style


init(autoreset=True)


class SystemInfo:
    """Класс для получения информации о системе."""
    @staticmethod
    def print_info(message, color=Fore.WHITE):
        print(f"{color}{message}{Style.RESET_ALL}")

    @staticmethod
    def get_cpu_info():
        physical_cores = psutil.cpu_count(logical=False)
        logical_cores = psutil.cpu_count(logical=True)
        frequency = psutil.cpu_freq().current if psutil.cpu_freq() else "Unknown"

        SystemInfo.print_info(f"Physical cores: {Fore.CYAN}{physical_cores}", Fore.CYAN)
        SystemInfo.print_info(f"Logical cores: {Fore.CYAN}{logical_cores}", Fore.CYAN)
        SystemInfo.print_info(f"CPU frequency: {Fore.CYAN}{frequency} MHz", Fore.CYAN)

    @staticmethod
    def get_memory_info():
        memory = psutil.virtual_memory()
        total_memory = memory.total / (1024 ** 3)
        available_memory = memory.available / (1024 ** 3)

        SystemInfo.print_info(f"Total memory: {Fore.GREEN}{total_memory:.2f} GB", Fore.GREEN)
        SystemInfo.print_info(f"Available memory: {Fore.GREEN}{available_memory:.2f} GB", Fore.GREEN)
