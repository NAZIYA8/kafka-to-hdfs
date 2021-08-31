# kafka-to-hdfs

# TASK:
# KAFKA STORING REAL TIME DATA ON HDFS.
    Write the producer and consumer code for fetching real time data with kafka.

VERSIONS:
hadoop 3.3.1
kafka_2.13-2.8.0
pydoop 2.0.0
kafka-python-2.0.2

Step1:
Start the zookeeper. 
    sudo systemctl start zookeeper
Start Kafka.
    sudo systemctl start kafka
Check the status if it is active.
    sudo systemctl status kafka

Step2:
    Create a producer.py and consumer.py file and write the code.
    
Step3:
Install the necessary modules and now execute the consumer.py in the terminal using the following command. 
$ python3 consumer.py
This will create kafka_stock_data directory in the hdfs and will also copy the empty data.txt file into the kafka_stock_data directory.

Step4:
Now run the producer.py file and then we will get the output in the consumer.py file and the program will start to write the data into the hdfs.

This is how we can store real time data into the hdfs.

