import os
import random

"""
These are for overlap and num_file should not be 1

for i in range(100):
    mode = "full_overlap"
    num_file = random.randint(2, 23)
    compressed_size = random.randint(1111, 10000)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ --compressed-size={compressed_size} > zips/overlap{order}_{num_file}_{compressed_size}.zip".format(
        mode=mode, num_file=num_file, compressed_size=compressed_size, order=i
    )
    os.system(command)
"""

"""
These are for sm

for i in range(100):
    mode = "quoted_overlap"
    num_file = random.randint(100, 252)
    compressed_size = random.randint(20000, 21000)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --compressed-size={compressed_size} > zips/zbsm{order}_{num_file}_{compressed_size}.zip".format(
        mode=mode, num_file=num_file, compressed_size=compressed_size, order=i
    )
    os.system(command)
"""

"""
These are for lg

for i in range(10):
    mode = "quoted_overlap"
    num_file = random.randint(60000, 65534)
    max_uncompressed_size = random.randint(4000000000, 4292788525)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --max-uncompressed-size={max_uncompressed_size} > zips/zblg{order}_{num_file}.zip".format(
        mode=mode, num_file=num_file, max_uncompressed_size=max_uncompressed_size, order=i
    )
    os.system(command)
"""

"""
These are for xl:

for i in range(10):
    mode = "quoted_overlap"
    num_file = random.randint(100000, 190023)
    compressed_size = random.randint(10000000, 22982788)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --compressed-size={compressed_size} --zip64 > zips/zbxl{order}_{num_file}_{compressed_size}.zip".format(
        mode=mode, num_file=num_file, compressed_size=compressed_size, order=i
    )
    os.system(command)
"""

"""
These are for bz2

for i in range(100):
    mode = "quoted_overlap"
    num_file = random.randint(1000, 1809)
    max_uncompressed_size = random.randint(4000000000,4294967294)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --max-uncompressed-size={max_uncompressed_size} --extra=9999> zips/zbbz2{order}_{num_file}.zip".format(
        mode=mode, num_file=num_file, max_uncompressed_size=max_uncompressed_size, order=i
    )
    os.system(command)
"""

"""
These are for sm.extra

for i in range(100):
    mode = "quoted_overlap"
    num_file = random.randint(100, 252)
    compressed_size = random.randint(20000, 21000)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --compressed-size={compressed_size} --extra=9999 > zips/zbsm.extra{order}_{num_file}_{compressed_size}.zip".format(
        mode=mode, num_file=num_file, compressed_size=compressed_size, order=i
    )
    os.system(command)
"""

"""
These are for lg.extra

for i in range(10):
    mode = "quoted_overlap"
    num_file = random.randint(60000, 65534)
    max_uncompressed_size = random.randint(4000000000, 4292788525)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --max-uncompressed-size={max_uncompressed_size} --extra=9999> zips/zblg.extra{order}_{num_file}.zip".format(
        mode=mode, num_file=num_file, max_uncompressed_size=max_uncompressed_size, order=i
    )
    os.system(command)
"""

"""
These are for xl.extra
"""
for i in range(10):
    mode = "quoted_overlap"
    num_file = random.randint(100000, 190023)
    compressed_size = random.randint(10000000, 22982788)
    command = "python3 zipbomb --mode={mode} --num-files={num_file} --compressed-size={compressed_size} --zip64 --extra=9999> zips/zbxl.extra{order}_{num_file}_{compressed_size}.zip".format(
        mode=mode, num_file=num_file, compressed_size=compressed_size, order=i
    )
    os.system(command)


