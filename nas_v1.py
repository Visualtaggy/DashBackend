import os
import psutil

def get_directory_size(path):
    total_size = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_directory_size(entry.path)
    return total_size

def convert_bytes_to_gb(size_in_bytes):
    return size_in_bytes / (1024 ** 3)

def calculate_storage_utilization(path):
    total_space = psutil.disk_usage(path).total
    used_space = get_directory_size(path)
    free_space = total_space - used_space
    utilization_percent = (used_space / total_space) * 100

    return convert_bytes_to_gb(total_space), convert_bytes_to_gb(used_space), convert_bytes_to_gb(free_space), utilization_percent

if __name__ == "__main__":
    nas_path = r"\\ubisoft.org\projects\Crest\PUN\versions1"

    if os.path.exists(nas_path):
        total_space_gb, used_space_gb, free_space_gb, utilization_percent = calculate_storage_utilization(nas_path)
        print("NAS Path:", nas_path)
        print("Total Storage: {:.2f} GB".format(total_space_gb))
        print("Used Storage: {:.2f} GB".format(used_space_gb))
        print("Free Storage: {:.2f} GB".format(free_space_gb))
        print("Storage Utilization: {:.2f}%".format(utilization_percent))
    else:
        print("Error: The specified path does not exist.")
