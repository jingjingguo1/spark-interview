from pyspark.sql.functions import regexp_extract
from pyspark.sql.types import StructType, StructField, DoubleType, StringType

class samples:

	schema = [StructField('user_id',StringType(),True), \
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
			  ]

	def __init__(self, path):
		self.path = path


	def json_to_dataframe(self, filename):
		json_schema = StructType([self.schema[i] for i in [0,1,2,3,4,5,6,7,8]])
		csv_data = spark.read.json(self.path+filename, schema=json_schema)
		return csv_data


	def custom_to_dataframe(self, filename):
		# custom_schema = StructType([self.schema[i] for i in [0,9,10]])
		custom_data = spark.read.text(self.path+filename)
		
		r = "user_id=(.+)feature_9=(.+)feature_10=(.+)"
		custom_data = custom_data.select(regexp_extract('value',r,1).alias('user_id'), \
										 regexp_extract('value',r,2).alias('feature_9').cast("double"), \
										 regexp_extract('value',r,3).alias('feature_10').cast("double"))
		return custom_data

	def tsv_to_dataframe(self, filename):
		tsv_schema = StructType([self.schema[i] for i in [0,11]])
		tsv_data = spark.read.csv(self.path+filename, sep="\t", header=False, schema=tsv_schema)
		return tsv_data

	def get_assembled_dataframe(self, json_filename, custom_filename, tsv_filename):
		json_data = self.json_to_dataframe(csv_filename)
		custom_data = self.custom_to_dataframe(custom_filename)
		tsv_data = self.tsv_to_dataframe(tsv_filename)

		assembled_dataframe = json_data.join(custom_data,'user_id').join(tsv_data,'user_id')
		return assembled_dataframe

	def save_assembled_dataframe(self, output_path):
		return "Success!"




