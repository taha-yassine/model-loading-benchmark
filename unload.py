from transformers import pipeline
from sentence_transformers import SentenceTransformer
import gc
from threading import Thread
from multiprocessing import Process
import psutil
from utils import get_size
import time

def load_model(model, task=None):
    if task:
        return pipeline(model=model, task=task)
    else:
        return SentenceTransformer(model)
    
def run_job():
    # Load the model into memory
    print('Loading the model...')
    start_time = time.time()
    model = load_model('clip-ViT-B-32')

    print(f'Model loaded ({time.time() - start_time:.3f}s)')

    # Execute a job using the model
    print(f'Memory after loading: {get_size(psutil.Process().memory_info().rss)}')

    # Remove all references to the model
    del model
    gc.collect()

if __name__ == "__main__":

    print(f'{"="*20} Run in subprocess {"="*20}')

    # Create a new subprocess and run the job
    p = Process(target=run_job)

    # Get the memory usage before loading the model
    before_memory = psutil.Process().memory_info().rss
    print(f'Current memory usage: {get_size(before_memory)}')
    # Start subprocess
    p.start()
    # Wait for the subprocess to finish
    p.join()

    # Get the memory usage after deleting the model
    after_memory = psutil.Process().memory_info().rss    
    print(f'Memory after subprocess termination: {get_size(after_memory)}')

    print(f'{"="*20} Run in thread {"="*20}')

    # Create a new thread and run the job
    t = Thread(target=run_job)

    # Get the memory usage before loading the model
    before_memory = psutil.Process().memory_info().rss
    print(f'Current memory usage: {get_size(before_memory)}')
    # Start thread
    t.start()
    # Wait for the thread to finish
    t.join()

    # Get the memory usage after deleting the model
    after_memory = psutil.Process().memory_info().rss    
    print(f'Memory after thread termination: {get_size(after_memory)}')