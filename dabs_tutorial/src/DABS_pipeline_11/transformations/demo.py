import dlt

@dlt.table
def demo_table_dab_new():
    return spark.createDataFrame([("a", 1), ("b", 2), ("c", 3)])