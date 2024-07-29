import subprocess
import os
import time

# IDM的完整路径，根据你的安装位置进行调整
idm_path = 'D:\\Program File\\Download tools\\IDM\\IDMan.exe'

# 要下载的网页URL
url = 'https://tonviewer.com/EQD0vdSA_NedR9uvbgN9EikRX-suesDxGeFg69XQMavfLqIw?section=holders'

# 获取当前脚本运行的目录
current_directory = os.getcwd()

print(current_directory)

file_name = '001.html'

download_path = os.path.join(current_directory, file_name)

# 调用IDM下载文件
subprocess.Popen([idm_path, '/d', url, '/p', current_directory, '/f', file_name, '/n', '/q'])

print("下载命令已发送到IDM。")

def wait_for_download_complete(path, timeout=300):
    start_time = time.time()
    while time.time() - start_time < timeout:
        # 检查文件是否存在
        if os.path.exists(path):
            size1 = os.path.getsize(path)
            time.sleep(1)  # 等待一秒再次检查文件大小
            size2 = os.path.getsize(path)
            if size1 == size2:  # 如果文件大小在一秒钟内没有变化，假设下载完成
                return True
        else:
            time.sleep(1)  # 如果文件尚不存在，等待一秒再检查
    return False


if wait_for_download_complete(download_path):
    print("下载完成")
else:
    print("下载未在预定时间内完成")