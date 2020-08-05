import argparse
import re
from collections import Counter

# 公共前缀
prefix = ['job:php', ]
# 不同部分替换为
re_replace = re.compile(r'(([a-z0-9\-]{36})|([A-Z0-9])+|\d+|android|ios)')


def init():
    parser = argparse.ArgumentParser(description="analysis redis key, and find the same key")
    parser.add_argument('file', default=None, type=str, help="filename")
    return parser.parse_args()


def read_file(filename):
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                continue
            yield line

def decimal_format(size, multiple=1024):
    if size < 0:
        raise ValueError('size must be non-negative')
    suffix = ['KB', 'MB', 'GB', 'TB', ]
    for suf in suffix:
        size /= multiple
        if size < multiple:
            return '{0:.3f} {1}'.format(size, suf)
    raise ValueError('size too large')


def replace(s):
    for pre in prefix:
        if s.startswith(pre):
            return pre + ':*'
    return re_replace.sub('*', s)


if __name__ == '__main__':
    args = init()
    counter = Counter()
    count = 0
    for ll in read_file(args.file):
        if count == 0 and ll.startswith('database,'):
            count += 1
            continue
        data = ll.split(',')
        key = replace(data[2])
        counter[key] += int(data[3])

    new_dict = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    for (k, v) in new_dict:
        print('%s => %s' % (k, decimal_format(v)))
