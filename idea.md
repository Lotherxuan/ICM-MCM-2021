f搜集数据：https://firms.modaps.eosdis.nasa.gov/download/

选择VIIRS-NPP

在https://www.openstreetmap.org/和[Geofabrik下载](https://download.geofabrik.de/)上导出维多利亚州的边界数据

https://gadm.org/download_country_v3.html下载澳洲行政区划数据

排除掉维多利亚州之外（用shapely形状的方法）的fire event

置信度较低的也排除掉

连接9年的数据

给出总数据的热力图，也可以给出分开数据的热力图

用k均值回归将数据减少到100个，给出均值回归后数据的热点图

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



每一个fire event 点到每一个SSA无人机的信号率  考虑一个距离衰减因子（在训练模型的时候只用一个平方反比） 和地形衰减因子 求和（火情监控指数）

假设：EOC是均匀且具有合适密度的分布 能确保任意中继无人机的覆盖情况都能将信息传递到EOC

每一个SSA无人机到每一个中继无人机的信息传递

中继无人机网络中的

先简要介绍三层网络的模型，用无人机图片，再继续深入介绍

以下内容不知道属于假设还是建模相关的定义，但这些定义跟建模有比较紧密的关系：

人（消防员）：并不直接在模型中出现，我们是使用无人机（两种）来辅助监控火情，传递无人机监控信息以及报告来自前线人员可穿戴设备采集的信息，辅助EOC下达命令（写英语时参见题目） 关于人的信息只写这一次，后面就不提人了

EOC：EOC和各种中介设备具有合适的密度和分布，使得传递到了中继无人机的信息能直接地或间接地通过中介设备（比如基站之类）传递到EOC   

（我们希望达到这样一个效果，所以构建了一个密铺的模型）

起飞充电和降落：起飞降落和充电分开考虑。假设里面写：无人机基地具有合适的数量和地理分布，使得所有无人机在其巡航范围内都能找到无人机基地进行起飞降落和充电。在模型中写：根据充电时间和电池大小等相关因素，添加对无人机总数量的修正因子 起飞降落也可以不写到假设中

SSA无人机：检测fire event point（写模型一定要出来火灾的频率的大小，就跟点题一样）

写进假设里面：对模型的抽象的时候考虑的，聚类到100个区域，然后用区域质心点表示，论文中要说明该做法的合理性，用热力图佐证，抽样具有统计学意义，用kmeans理论予以说明

上下行带宽足够大

关于模型：暂时是一个主体为两层的模型

第一层模型：输入是100个fire event point的坐标和累积frp的值以及SSA无人机数量（代码中） 论文中我们写成火情点坐标和火情大小和火情频率，输出是所有SSA无人机的坐标和火情的覆盖率

分析第一层模型 分析模拟退火的目标函数，比如说贡献率什么 关于普通模型的数量和覆盖率的关系比较我们第一层模型数量和覆盖率的关系 在提出预算方面比较我们模型中不同数量和覆盖率的关系

第二层模型：输入是第一层模型输出的SSA的数量以及位置坐标



经都L纬度B

2无人机巡航模型

2.1建立模型

在这个模型中我们主要考虑SSA无人机对fire event point的监控作用。我们使用一个两层的网络

$D=(V_F,V_U,E_{UF})$来刻画我们的模型，其中$V_F=\{V_{F_1},V_{F_2},...,V_{F_{100}}\}$是在先前的数据处理中我们通过聚类得到的100个fire event point，我们用这100个fire event point刻画火灾的整体情况。对于每一个$V_{F_i}=(L_{F_i},B_{F_i},b_{F_i},m_{F_i},s_{F_i})$，$L_{F_i}$表示fire event point的经度，$B_{F_i}$表示fire event point的纬度，$b_{F_i}$表示过去8年中发生大规模火灾的频率，$m_{F_i}$表示过去8年中发生中等规模火灾的频率，$s_{F_i}$表示过去8年中发生小规模火灾的频率。我们用$V_U=\{V_{U_1},V_{U_2},...,V_{U_n}\}$来刻画SSA无人机的位置分布情况，,其中${U_n}$是SSA无人机的总数量，对于每一个$V_{U_i}=(L_{U_i},B_{U_i})$，$L_{U_i}$表示无人机的经度，$B_{U_i}$表示无人机的纬度。$E_{UF}=\{(V_{F_i},B_{F_i})|V_{F_i}\in V_F,B_{F_i}\in B_F\}$表示网络中一个fire event point和一个SSA无人机的连接关系。

模型的输入是$V_F$和$U_n$，我们希望通过运行合适的算法找到一组$V_U$，使得$E_{UF}$在以下两个评估指标上取得较好的效果：$n_s$

coverage rate$Cover=\frac{}{}$我们定义以SSA无人机位置为圆心，30km为半径的圆的范围，是一个无人机的可达范围，在一个无人机的可达范围内的所有fire event point都是可覆盖的，可覆盖意味该点处的火灾是可监控的，在或长或短的时间内。若一个fire event point没有在任何一个无人机的覆盖范围内，该point就是未覆盖的。覆盖率是可覆盖的point数量与所有point数量的比值，覆盖率刻画了在较长的时间尺度上对于火情的监控情况

无人机巡航图

未监控指数

un

无人机范围内不同距离的多个fire event point的图

在上一个指标coverage rate中我们提到了fire event point是否是被覆盖的，但进一步来讲在同一个SSA无人机的覆盖范围内，由于SSA在不同的位置具有不同的出现概率，故对于不同位置的fire event具有不同的检查效应。距离SSA无人机巡航中心越近的fire event point在发生火灾时更有可能被监控到。而且考虑到发生火灾时可能有多个SSA无人机同时监测到火情，其中第一个检测到火情的SSA无人机具有最大的效果，我们使用调和平均式，以反映出距离最近的无人机对于监控该fire point有格外高的贡献率。

FDRI(fire dectection risk index)

2.2训练模型

We use simulated annealing to search for a comparetively good placement of SSA UAVs. Simulated Annealing is easy to implementand while still is very usefull when coming with very hard computational optimization problems. There is no doubt that the process of searching for a favorable placement of SSA UAVs can be extremely hard to find a precise optimum. We can suppose that it is even impossible to apply a exact algorithm in this problem. We ues $R_{F_i}$ to serve as objective function which depicts not only how many fire event points are in the range of SSA UAVs, but also how likely it is that a bush fire will be monitored and managed in time and effectively. Just like other normal  simulated annealing algorithm, we gradually lower the temperature $T$ and deploy random disturbances in the positions of SSA UAVs, aiming to avoid being trapped in local minima. The detailed implementation of our SA algorithm is described as followed.

$$
R_{F_i}=\begin{cases}
\frac{1}{\sum_{R_i}^{d_{F_i,U_j}\leq 30} \frac{1}{d_{F_i,U_j}}}\times \frac{1}{30}, & C_{F_i}=1 \\
1 ,& C_{F_i}=0
\end{cases}
$$



SSA UAV

receviers  UAV

2.3结果分析

和遗传算法 粒子群算法相比收敛速度快



大中小火火情系数$\mu_b$,$\mu_m$,$\mu_s$

地球半径$R=6371.0km$

$F_i$和$U_i$之间的距离$d_{F_i,U_i}=R\times \arccos[\cos B_{F_i}\times \cos B_{U_i}\times \cos({L_{F_i}-L_{U_j})+sinB_{F_i}\times sinB_{U_j}}]$

$C_{F_i}$表示$F_i$是否被覆盖
$$
C_{F_i}=\begin{cases}

1 & \exists U_j,d_{F_i,U_j}\leq R_u \\
0 & others
\end{cases}
$$

覆盖率
$$
C=\frac{\sum_{i=1}^{100}C_{F_i}}{U_n}
$$
某一个fire event point的未监控指数
$$
R_{F_i}=\begin{cases}
\frac{1}{\sum_{R_i}^{d_{F_i,U_j}\leq 30} \frac{1}{d_{F_i,U_j}}}\times \frac{1}{30}, & C_{F_i}=1 \\
1 ,& C_{F_i}=0
\end{cases}
$$

所有fire event point的未监控指数
$$
R=\sum_{i=1}^{100}\times R_{F_i} \times (b_{F_i}\times \mu_b+m_{F_i}\times \mu_m+s_{F_i}\times \mu_s)
$$


discusssion

conclusion

优点和缺点

| 7    | 8    | 9    | 10   | 11   |      |
| ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |

100 0.98

strength:在模拟退火算法中我们利用了启发式的信息（[metaheuristic information](https://en.wikipedia.org/wiki/Metaheuristic)），可以在较短的搜索空间(search space)中找到一个近似的全局最优解(approximate [global optimization](https://en.wikipedia.org/wiki/Global_optimization))

weakness: 由于采取了智能搜索算法（Intelligent search algorithm），在每次重新统计fire event point的频率和大小后，都需要重新运行算法来得到模型结果。

second: 我们用模拟退火算法来寻找一种合适SSA 无人机的位置组合方案。我们希望在该方案下我们能用尽可能少的SSA无人机数量，通过合理有效率地布置SSA无人机的位置以使得所有的fire event point都处于有效地监控之下。我们充分利用了模拟退火算法的性质，避免了组合优化问题(Combinatorial Optimization Problem)中的高时间复杂度(Time complexity)，并取得了不错的效果。