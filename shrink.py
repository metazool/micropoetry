import argparse
import os
from gensim.summarization.summarizer import summarize as summarise

def reduce(text):
    shrunk = summarise(text)
    if len(shrunk) > 240:
        return reduce(shrunk)
    return shrunk

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help="text files to summarize")
    args = parser.parse_args()
    lines = []
    for (root, _, files) in os.walk(args.dir):
        for filename in sorted(files, key=lambda f: os.stat(os.path.join(root, f)).st_mtime):
            with open(os.path.join(root, filename), 'r') as text:
                lines.append(reduce(text.read()))
    print('\n'.join(lines))
