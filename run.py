from transformers import pipeline, utils
from sentence_transformers import SentenceTransformer
import time
import objsize
from utils import hw_info, get_size

def load_model(model, task=None):
    if task:
        return pipeline(model=model, task=task).model
    else:
        return SentenceTransformer(model)

if __name__ == "__main__":
    utils.logging.set_verbosity_error()

    report = f'{"="*20} Loading time benchmark {"="*20}\n'

    start_time = time.time()
    model = load_model(model='microsoft/resnet-50', task='image-classification')
    report += f'Classification model (resnet-50): {time.time() - start_time:.3f}s ({get_size(objsize.get_deep_size(model))})\n'

    start_time = time.time()
    model = load_model(model='hustvl/yolos-tiny', task='object-detection')
    report += f'Detection model (yolos-tiny): {time.time() - start_time:.3f}s ({get_size(objsize.get_deep_size(model))})\n'

    start_time = time.time()
    model = load_model('clip-ViT-B-32')
    report += f'CLIP (clip-ViT-B-32): {time.time() - start_time:.3f}s ({get_size(objsize.get_deep_size(model))})\n'

    report += hw_info()

    f = open("report.txt", "w")
    f.write(report)
    f.close()
