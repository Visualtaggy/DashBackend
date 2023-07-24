import subprocess
import time

def force_sync_workspace(workspace_path):
    try:
        start_time = time.time()
        p4_sync_command = f"p4 -c {workspace_path} sync -f"
        subprocess.check_output(p4_sync_command, shell=True)
        end_time = time.time()

        sync_time = end_time - start_time
        sync_time_minutes = sync_time / 60  
        average_speed = calculate_average_speed(workspace_path, sync_time)

        print(f"Sync completed in {sync_time_minutes:.2f} minutes.")
        if average_speed is not None:
            print(f"Average sync speed: {average_speed:.2f} MB/s")
        else:
            print("Average sync speed calculation failed.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during sync: {e}")

def calculate_average_speed(workspace_path, sync_time):
    try:
        p4_sizes_command = f"p4 -c {workspace_path} sizes"
        sizes_output = subprocess.check_output(p4_sizes_command, shell=True, stderr=subprocess.STDOUT).decode("utf-8")

        print("Sizes Output:")
        print(sizes_output)

        total_size_bytes = 0
        for line in sizes_output.splitlines():
            _, size_str, _ = line.split()
            total_size_bytes += int(size_str)

        average_speed = total_size_bytes / (sync_time * 60 * 1024 * 1024)  

        return average_speed
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calculating average speed: {e}")
        return None

if __name__ == "__main__":
    workspace_path = "vtyagi_pun-wks-ad018_main_code"  
    force_sync_workspace(workspace_path)
