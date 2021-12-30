Combines multiple csv files with the same file structure into one master file. Headers will not be repeated. 


PROJECT_DIR:
	dataset(folder. name is important)
	csv_conv.py




Save the collection of csv files into the folder 'dataset'.

If you would like to remove columns, specify the what the index (starting at index 0) of the column is in the variable 'cols_to_delete', seperated by commas.

If there are rows with the same index in each file you would like removed, specify what the index (starting at index 0) of the row is in the variable 'rows_to_delete', seperated by commas. If there are rows you would like to delete that have different indexes for each file, you cannot do that in this step.

Specify the name of the .csv file you would like for the resulting file. It will be inserted into the root directory to be copied and saved elsewhere. 