from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import StandardScaler
from pyspark.ml.feature import VectorAssembler

from pyspark.sql.types import StructType, StructField, DoubleType, StringType

class Features:
	assembled_data_schema = StructType([StructField('user_id',StringType(),True), \
										StructField('feature_1',DoubleType(),True), \
										StructField('feature_2',StringType(),True), \
										StructField('feature_3',DoubleType(),True), \
										StructField('feature_4',DoubleType(),True), \
										StructField('feature_5',DoubleType(),True), \
										StructField('feature_6',DoubleType(),True), \
										StructField('feature_7',DoubleType(),True), \
										StructField('feature_8',DoubleType(),True), \
										StructField('feature_9',DoubleType(),True), \
										StructField('feature_10',DoubleType(),True), \
										StructField('label',DoubleType(),False)
										])

	def __init__(self, assembled_data_path):
		self.assembled_data_path = assembled_data_path
		self.data = spark.read.csv(self.assembled_data_path, schema=self.assembled_data_schema)
		self.column_names = self.data.columns

	def encode_data(self):
		cat_column_names = [col[0] for col in self.data.drop('user_id').dtypes if col[1]=='string'] 
		
		cols = self.column_names
		for col in cat_column_names:
			indexer = StringIndexer(inputCol=col, outputCol="tmp")
			self.data = indexer.fit(self.data)\
								  .transform(self.data)\
								  .drop(col)\
								  .withColumnRenamed('tmp',col)\
								  .select(cols)
		return self.data

	def get_label_features(self):
		self.data = self.encode_data()

		assembler = VectorAssembler(inputCols=self.column_names[1:11], outputCol="features")
		self.data = assembler.transform(self.data)

		return self.data.select('label', 'features')

	def get_scaled_label_features(self):
		self.data = self.get_label_features()
		scaler = StandardScaler(inputCol='features', \
								outputCol="scaled", \
								withStd=True, \
								withMean=False)

		self.data = scaler.fit(self.data)\
						  .transform(self.data)\
						  .withColumnRenamed('features',"to_drop")\
						  .withColumnRenamed('scaled','features')\
						  .drop('to_drop')
		return self.data



#=========main function========
from pyspark import SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")


from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
if __name__ == "__main__":

	data_path = "./data/"
	model_path = "./model/"

	featurized_data = Features(data_path+"assembled").get_scaled_label_features()
	featurized_data.show(1)

	train, test = featurized_data.randomSplit([0.7,0.3])

	blor = LogisticRegression(labelCol='label', featuresCol='features')
	model = blor.fit(train)
	# model.write().overwrite().save(model_path)
	model.transform(test).select('label', 'prediction').show(10)
	
	evaluator = BinaryClassificationEvaluator()\
				.setMetricName('areaUnderROC')\
				.setRawPredictionCol('prediction')\
				.setLabelCol('label')
	print "Model Coefficients are: " + str(model.coefficients)
	print "Model Intercept is: "+ str(model.intercept)
	print "Test set Area Under the Curve (AUC) is " + str(evaluator.evaluate(model.transform(test)))

spark.stop()


