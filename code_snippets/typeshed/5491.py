import gzip
import tarfile


open('t', 'w').close()
with gzip.GzipFile('out.tar.gz', 'wb') as gzipf:
    with tarfile.open(fileobj=gzipf, mode='w') as tf:
        tf.add('t')
