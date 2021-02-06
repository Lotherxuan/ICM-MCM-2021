import geopandas
australia = geopandas.read_file("../data/gadm36_AUS_shp/gadm36_AUS_1.shp")
victoria = australia[9:10]
print(australia)
