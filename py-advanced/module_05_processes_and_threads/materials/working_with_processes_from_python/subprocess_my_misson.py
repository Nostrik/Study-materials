import time
import subprocess


def run():
    start = time.time()
    processes = []
    for p_num in range(1, 10):
        p = subprocess.Popen(
            ['sleep 5', 'echo "My mission is done here!"'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        print(f'Process number {p_num} started. PID {p.pid}')
        processes.append(p)

    for proc in processes:
        proc.wait()
        if b'Done' in proc.stdout.read() and proc.returncode == 0:
            print(f'Process with PID {proc.pid} ended successfully')
    print(f'Done in {time.time() - start}')


if __name__ == '__main__':
    run()
