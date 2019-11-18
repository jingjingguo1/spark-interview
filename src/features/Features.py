from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import StandardScaler
from pyspark.ml.feature import VectorAssembler

class features:

	def __init__(raw_data_path, feature_data_path):
		self.raw_data_path = raw_data_path
		self.feature_data_path = feature_data_path
		self.data = spark.read.csv(self.raw_data_path)
		self.column_names = self.data.columns

	def encode_data(self):
		cat_column_names = [col[0] for col in self.data.dtypes if col[1]=='string'] 
		
		cols = self.column_names
		for col in cat_column_names:
			indexer = StringIndexer(inputCol=col, outputCol="tmp")
			self.data = indexer.fit(self.data)\
								  .transform(self.data)\
								  .drop(col)\
								  .withColumnRenamed('tmp',col)\
								  .select(cols)
		return self.data

	def scale_data(self):
		# self.data = encode_data()
		num_column_names = [col[0] for col in self.data.dtypes if col[1]=='double']

		for col in num_column_names:
			scaler = StandardScaler(inputCol=col, \
									outputCol="scaled", \
									withStd=True, \
									withMean=False)

			scaled_data = scaler.fit(self.data)\
								.tranform(self.data)\
								.withColumnRenamed(col,"to_drop")\
								.withColumnRenamed('scaled',col)\
								.drop('to_drop')
		return self.data

	def get_label_features(self):
		self.data = encode_data()
		self.data = scale_data()

		assembler = VectorAssembler(inputCols=self.column_names[1:11], outputCol="features")
		lable_features = assembler.transform(self.data)

		return label_features.select('label', 'features')


	def save_label_featutures(self):
		spark.write.format('libsvm').save(self.feature_data_path+"label_features_dataframe")
		return "Success!"

