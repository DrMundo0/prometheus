import multiprocessing as mp

# https://docs.python.org/3.12/library/asyncio-subprocess.html
if __name__ == "__main__":
    mp.set_start_method('spawn')
