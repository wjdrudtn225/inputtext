from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("test1")
sc = SparkContext(conf=conf)

inputRDD = sc.textFile("testfile")
pair = inputRDD.map(lambda x: (x.split(" ")[0], x))
result = pair.filter(lambda x: len(x[1]) < 10)

for line in result.take(5):
        print(line)

