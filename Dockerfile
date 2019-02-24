FROM openjdk:8

MAINTAINER Valerio Del Meglio

COPY ./gfg.py /usr/local/bin
COPY ./execute.sh /usr/local/bin

RUN chmod +x /usr/local/bin/execute.sh
RUN  apt-get update \
  && apt-get install -y wget python-pip
RUN pip install awscli
RUN wget http://apache.lauf-forum.at/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
RUN wget http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar
RUN wget http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.3/hadoop-aws-2.7.3.jar
RUN tar -zxf spark-2.4.0-bin-hadoop2.7.tgz -C /usr/local/bin
RUN mv hadoop-aws-2.7.3.jar /usr/local/bin/spark-2.4.0-bin-hadoop2.7/jars
RUN mv aws-java-sdk-1.7.4.jar /usr/local/bin/spark-2.4.0-bin-hadoop2.7/jars

WORKDIR /usr/local/bin

ENV SPARK_HOME=/usr/local/bin/spark-2.4.0-bin-hadoop2.7
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH
ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH


CMD ["sh", "./execute.sh"]
