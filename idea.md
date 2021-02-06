搜集数据：https://firms.modaps.eosdis.nasa.gov/download/

选择VIIRS-NPP

在https://www.openstreetmap.org/和[Geofabrik下载](https://download.geofabrik.de/)上导出维多利亚州的边界数据

https://gadm.org/download_country_v3.html下载澳洲行政区划数据

排除掉维多利亚州之外（用shapely形状的方法）的fire event

置信度较低的也排除掉

连接9年的数据

给出总数据的热力图，也可以给出分开数据的热力图

用k均值回归将数据减少到100个，给出均值回归后数据的最少值

建模：

不能是0 1判断fire event是否在范围内 要刻划一个通信性能模型 信号随距离衰减的模型

采用强化学习以提升预测能力 再考虑  巨灾模型的经济学模型 第二题 

可视化相关的

地形用梯度数据 等高线数据用于画图



2.6 23:12会议：

重建三维立体地图模型（待完成）

信号强度评估函数

数学公式过少

可视化作图 八年数据绘图和制表

巨灾模型