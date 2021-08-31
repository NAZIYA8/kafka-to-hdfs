'''
@Author: Naziya
@Date: 2021-08-31
@Last Modified by: Naziya
@Last Modified : 2021-08-31
@Title : Program Aim is to send stock data from producer to consumer
and store it in hdfs
'''

from kafka import KafkaConsumer
import pydoop.hdfs as hdfs
import subprocess

consumer = KafkaConsumer('topic4')
hdfs.mkdir('hdfs://localhost:9000/kafka_stock_data')
file = '/home/naziya/data.txt'
args_list = [ 'hdfs', 'dfs', '-put',file, '/kafka_stock_data']
print('Running system command: {}'.format(' '.join(args_list)))
proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc.communicate()
hdfs_path = 'hdfs://localhost:9000/kafka_stock_data/data.txt'


for message in consumer:
    values = message.value.decode('utf-8')
    with hdfs.open(hdfs_path, 'at') as f:
        f.write(f"{values}\n")