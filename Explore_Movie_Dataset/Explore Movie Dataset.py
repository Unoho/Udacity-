
# coding: utf-8

# ## 探索电影数据集
# 
# 在这个项目中，你将尝试使用所学的知识，使用 `NumPy`、`Pandas`、`matplotlib`、`seaborn` 库中的函数，来对电影数据集进行探索。
# 
# 下载数据集：
# [TMDb电影数据](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/explore+dataset/tmdb-movies.csv)
# 

# 
# 数据集各列名称的含义：
# <table>
# <thead><tr><th>列名称</th><th>id</th><th>imdb_id</th><th>popularity</th><th>budget</th><th>revenue</th><th>original_title</th><th>cast</th><th>homepage</th><th>director</th><th>tagline</th><th>keywords</th><th>overview</th><th>runtime</th><th>genres</th><th>production_companies</th><th>release_date</th><th>vote_count</th><th>vote_average</th><th>release_year</th><th>budget_adj</th><th>revenue_adj</th></tr></thead><tbody>
#  <tr><td>含义</td><td>编号</td><td>IMDB 编号</td><td>知名度</td><td>预算</td><td>票房</td><td>名称</td><td>主演</td><td>网站</td><td>导演</td><td>宣传词</td><td>关键词</td><td>简介</td><td>时常</td><td>类别</td><td>发行公司</td><td>发行日期</td><td>投票总数</td><td>投票均值</td><td>发行年份</td><td>预算（调整后）</td><td>票房（调整后）</td></tr>
# </tbody></table>
# 

# **请注意，你需要提交该报告导出的 `.html`、`.ipynb` 以及 `.py` 文件。**

# 
# 
# ---
# 
# ---
# 
# ## 第一节 数据的导入与处理
# 
# 在这一部分，你需要编写代码，使用 Pandas 读取数据，并进行预处理。

# 
# **任务1.1：** 导入库以及数据
# 
# 1. 载入需要的库 `NumPy`、`Pandas`、`matplotlib`、`seaborn`。
# 2. 利用 `Pandas` 库，读取 `tmdb-movies.csv` 中的数据，保存为 `movie_data`。
# 
# 提示：记得使用 notebook 中的魔法指令 `%matplotlib inline`，否则会导致你接下来无法打印出图像。

# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().magic('matplotlib inline')


# ---
# 
# **任务1.2: ** 了解数据
# 
# 你会接触到各种各样的数据表，因此在读取之后，我们有必要通过一些简单的方法，来了解我们数据表是什么样子的。
# 
# 1. 获取数据表的行列，并打印。
# 2. 使用 `.head()`、`.tail()`、`.sample()` 方法，观察、了解数据表的情况。
# 3. 使用 `.dtypes` 属性，来查看各列数据的数据类型。
# 4. 使用 `isnull()` 配合 `.any()` 等方法，来查看各列是否存在空值。
# 5. 使用 `.describe()` 方法，看看数据表中数值型的数据是怎么分布的。
# 
# 

# In[1]:


#读取tmdb_movies.csv文件，保存为movie_data
movie_data = pd.read_csv(r'C:\Users\Administrator\python\AIPND_CN_P2_Explore_Movie_Dataset-master\AIPND_CN_P2_Explore_Movie_Dataset-master\tmdb-movies.csv')


# In[2]:


#利用shape函数返回数据的维度
movie_data.shape


# In[3]:


#利用head()函数显示前5行数据
movie_data.head()


# In[4]:


利用tail()函数显示后五行数据
movie_data.tail()


# In[5]:


#利用sample函数随机显示3行数据
movie_data.sample(n=3)


# In[6]:


#利用dtypes函数显示各列的数据类型
movie_data.dtypes


# In[7]:


#利用isnull()和any()函数检查各列是否有NULL值
movie_data.isnull().any()


# In[8]:


#利用describe()函数了解调整后预算的数据分布
movie_data['budget_adj'].describe()


# In[9]:


#利用describe()函数了解所有数据分布
movie_data.describe()


# ---
# 
# **任务1.3: ** 清理数据
# 
# 在真实的工作场景中，数据处理往往是最为费时费力的环节。但是幸运的是，我们提供给大家的 tmdb 数据集非常的「干净」，不需要大家做特别多的数据清洗以及处理工作。在这一步中，你的核心的工作主要是对数据表中的空值进行处理。你可以使用 `.fillna()` 来填补空值，当然也可以使用 `.dropna()` 来丢弃数据表中包含空值的某些行或者列。
# 
# 任务：使用适当的方法来清理空值，并将得到的数据保存。

# In[10]:


#因为imdb_id存在控空值，并且已经有id了，可drop将imdb_id列删除
movie_data.drop(['imdb_id'],axis = 1 ,inplace = True)


# In[11]:


#后期按类别和导演进行统计，为不影响数据统计，将类别和导演为空值的行删除
movie_data.dropna(subset = ['director','genres'],inplace = True)


# In[12]:


#检查导演列是否还有空值
movie_data['director'].isnull().value_counts()


# In[13]:


#检查类别列是否还有空值
movie_data['genres'].isnull().value_counts()


# In[14]:


#用fillna()将其他空值以‘Not given’填充
movie_data.fillna('Not given',inplace =True)


# In[15]:


#再次检查全部数据是否还有空值
movie_data.isnull().any()


# ---
# 
# ---
# 
# ## 第二节 根据指定要求读取数据
# 
# 
# 相比 Excel 等数据分析软件，Pandas 的一大特长在于，能够轻松地基于复杂的逻辑选择合适的数据。因此，如何根据指定的要求，从数据表当获取适当的数据，是使用 Pandas 中非常重要的技能，也是本节重点考察大家的内容。
# 
# 

# ---
# 
# **任务2.1: ** 简单读取
# 
# 1. 读取数据表中名为 `id`、`popularity`、`budget`、`runtime`、`vote_average` 列的数据。
# 2. 读取数据表中前1～20行以及48、49行的数据。
# 3. 读取数据表中第50～60行的 `popularity` 那一列的数据。
# 
# 要求：每一个语句只能用一行代码实现。

# In[16]:


#读取数据表中名为 id、popularity、budget、runtime、vote_average 列的数据。
movie_data[['id','popularity','budget','runtime','vote_average']]


# In[22]:


np.r_[movie_data.iloc[0:20],movie_data.iloc[47:49]]


# In[18]:


#读取数据表中前1～20行以及48、49行的数据。
movie_data.iloc[list(range(20)) + list([47,48])]


# In[23]:


#读取数据表中第50～60行的 popularity 那一列的数据。
movie_data.loc[range(49,60),['popularity']]


# ---
# 
# **任务2.2: **逻辑读取（Logical Indexing）
# 
# 1. 读取数据表中 **`popularity` 大于5** 的所有数据。
# 2. 读取数据表中 **`popularity` 大于5** 的所有数据且**发行年份在1996年之后**的所有数据。
# 
# 提示：Pandas 中的逻辑运算符如 `&`、`|`，分别代表`且`以及`或`。
# 
# 要求：请使用 Logical Indexing实现。

# In[24]:


#读取数据表中 popularity 大于5 的所有数据。
movie_data[movie_data['popularity']>5]


# In[25]:


#读取数据表中 popularity 大于5 的所有数据且发行年份在1996年之后的所有数据。
movie_data[(movie_data['popularity']>5) & (movie_data['release_year']>1996)]


# ---
# 
# **任务2.3: **分组读取
# 
# 1. 对 `release_year` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `revenue` 的均值。
# 2. 对 `director` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `popularity` 的均值，从高到低排列。
# 
# 要求：使用 `Groupby` 命令实现。

# In[95]:


#对 release_year 进行分组，使用 .agg 获得 revenue 的均值。
movie_data.groupby('release_year')['revenue'].agg({'revenue_mean':'mean'})


# In[28]:


#对 director 进行分组，使用 .agg 获得 popularity 的均值，从高到低排列。
movie_data.groupby('director')['popularity'].agg({'popularity_mean':'mean'}).sort_values(by='popularity_mean',ascending = False)


# ---
# 
# ---
# 
# ## 第三节 绘图与可视化
# 
# 接着你要尝试对你的数据进行图像的绘制以及可视化。这一节最重要的是，你能够选择合适的图像，对特定的可视化目标进行可视化。所谓可视化的目标，是你希望从可视化的过程中，观察到怎样的信息以及变化。例如，观察票房随着时间的变化、哪个导演最受欢迎等。
# 
# <table>
# <thead><tr><th>可视化的目标</th><th>可以使用的图像</th></tr></thead><tbody>
#  <tr><td>表示某一属性数据的分布</td><td>饼图、直方图、散点图</td></tr>
#  <tr><td>表示某一属性数据随着某一个变量变化</td><td>条形图、折线图、热力图</td></tr>
#  <tr><td>比较多个属性的数据之间的关系</td><td>散点图、小提琴图、堆积条形图、堆积折线图</td></tr>
# </tbody></table>
# 
# 在这个部分，你需要根据题目中问题，选择适当的可视化图像进行绘制，并进行相应的分析。对于选做题，他们具有一定的难度，你可以尝试挑战一下～

# **任务3.1：**对 `popularity` 最高的20名电影绘制其 `popularity` 值。

# In[36]:


top20_popularity = movie_data.sort_values(by = 'popularity',ascending = True)[-20:]
base_color = sb.color_palette()[0]
index = np.arange(0,40,2)
bar_width = 1
plt.barh(index,top20_popularity['popularity'],bar_width,align = 'center',color = base_color)
plt.ylabel('Movie name')
plt.xlabel('Popularity')
plt.title('Top 20 popularity movies')
plt.yticks(index + bar_width/4,top20_popularity['original_title'])
plt.xticks(np.arange(8,top20_popularity['popularity'].max() + 2,6))


# In[35]:


movie_data.sort_values('popularity',ascending = False).head(20).plot(kind ='barh',y='popularity',x='original_title',legend=False)
plt.xlabel('popularity')
plt.title('Top 20 popularity movies')


# ---
# **任务3.2：**分析电影净利润（票房-成本）随着年份变化的情况，并简单进行分析。

# In[37]:


#计算利润添加到最后一列，命名为Profit
movie_data['Profit']= movie_data['revenue_adj'] - movie_data['budget_adj']


# In[38]:


movie_data.head


# In[39]:


movie_data['Profit'].describe()


# In[44]:


#计算每一年所有电影的总利润和平均利润
total_Profit_per_year = movie_data.groupby(['release_year'])['Profit'].sum()
average_Profit_per_year = movie_data.groupby(['release_year'])['Profit'].mean()


# In[47]:


plt.figure(figsize = [10,5])
#在左边生成每年电影合计收益在连续年份上的折线图
plt.subplot(1,2,1)
plt.errorbar(data = movie_data,x=total_Profit_per_year.index,y=total_Profit_per_year)
plt.xlabel('release year')
plt.ylabel('totlal profit')
#在左边生成每年电影平均收益在连续年份上的折线图
plt.subplot(1,2,2)
plt.errorbar(data = movie_data,x=average_Profit_per_year.index,y=average_Profit_per_year)
plt.xlabel('release year')
plt.ylabel('average profit')



# 任务小结：
# 1.左图中，每年的电影总利润在在1960至2015年间，总体呈持续上升趋势,2015年的总利润高达176亿美元,相比较于1960年增长了9555.98%。在图中有一些小的低点，这些低点多是受当时经济环境的影响，例如1973至1975年的下折，当时正在经历第一次石油危机，以及199年的亚洲经融风暴和2007年的次贷危机。
# 2.右图中，1960年至1978年每年电影的平均票房利润是上升状态，但1978年以后平均票房利润呈现持续走低趋势，给人的感觉是1978年以后电影的总量在增加，电影的利润差别较大，即使总利润是上升的，但数量的增加、电影质量的层次不齐和利润额的较大区别，拉低了平均利润。

# ---
# 
# **[选做]任务3.3：**选择最多产的10位导演（电影数量最多的），绘制他们排行前3的三部电影的票房情况，并简要进行分析。

# In[48]:


#根据director,revenue对movie_data分别进行升序和降序排序
movie_data.sort_values(['director','revenue'],ascending=[1,0],inplace=True)
#获得电影数量最多的前10位导演的姓名
top10_movies_countby_director = movie_data.groupby(['director'])['id'].count().sort_values(ascending = False)[0:10]
#在movie_data中筛选出前电影数量最多的前10位导演的数据
top10_movies_countby_director_data = movie_data[movie_data['director'].isin(top10_movies_countby_director.index)]
#获得每位导演排名票房排名前3的电影数据
top3_in_top10_movies_countby_director = top10_movies_countby_director_data.groupby(['director']).head(3)


# In[58]:


#计算电影量最多的前10名导演分别最卖座的三部电影的票房平均值并排序,此排序用于确定barplot中图例的顺序
mean_top3_in_top10_movies_countby_director=top3_in_top10_movies_countby_director.groupby(['director'])['revenue'].mean().sort_values(ascending = False)
mean_top3_in_top10_movies_countby_director


# In[49]:


top3_in_top10_movies_countby_director


# In[67]:


plt.figure(figsize = [20,15])
g=sb.barplot(y='original_title',x='revenue',hue='director',data=top3_in_top10_movies_countby_director,hue_order=mean_top3_in_top10_movies_countby_director.index)


# 任务小结：通过柱形图可以看出，三部电影平均票房最高的是Steven Spielberg,同时他导演的侏罗纪公园、ET外星人、夺宝奇兵也是总票房的前三名,是历史上最卖座的三部电影;Ron Howard 和Ridley Scott的三部电影平均票房排名第二、第三，他们的达芬奇密码和火星救援分别位居总票房的第四、第五。

# ---
# 
# **[选做]任务3.4：**分析1968年~2015年六月电影的数量的变化。

# In[68]:


#获得上映时间在1968年~2015年六月电影的数据
date_interval_movie_data = movie_data[(movie_data['release_date']>= '1/1/1968') & (movie_data['release_date']<= '6/30/2015')]
#分年度统计在1968年~2015年六月电影的数量并按年度排序
date_interval_movie_data = date_interval_movie_data.groupby(['release_year'])['release_year'].count().sort_index(ascending = True)
#计算逐年电影上映总量的增长率
growth_rate=pd.DataFrame((np.array(date_interval_movie_data[1:])-np.array(date_interval_movie_data[:-1]))/np.array(date_interval_movie_data[:-1]),columns=['rate_of_increase'])
growth_rate['release_year'] = date_interval_movie_data.index[1:]


# In[69]:


#计算逐年电影上映总量的增长量
growth_num=pd.DataFrame((np.array(date_interval_movie_data[1:])-np.array(date_interval_movie_data[:-1])),columns=['num_of_increase'])
growth_num['release_year'] = date_interval_movie_data.index[1:]


# In[70]:


plt.figure(figsize = [20,5])
#生成1960年至2015年6月上映电影总数的折线图
plt.subplot(1,3,1)
plt.errorbar(x=date_interval_movie_data.index,y=date_interval_movie_data)
plt.xlabel('Release year')
plt.ylabel('Total number of films released')

#生成1960年至2015年6月上映电影总数增量的折线图
plt.subplot(1,3,2)
plt.errorbar(data = growth_num,x='release_year',y='num_of_increase')
plt.xlabel('Release year')
plt.ylabel('Growth number of films released')

#生成1960年至2015年6月上映电影总数增长率的折线图
plt.subplot(1,3,3)
plt.errorbar(data = growth_rate,x='release_year',y='rate_of_increase')
plt.xlabel('Release year')
plt.ylabel('Growth rate of films released')


# 任务小结：1960年至2015年6月间电影发行量呈现持续上升态势，即使在其中有些时间点的发行量出现了下降，但是从1975年进入当代电影开始，电影发行量就在持续攀升；2015年因为只有半年数据，所以从图形来看出现了大幅下滑；电影增量最大的一年出现在2013年，达到73部，电影增长率最大的时间是在1973年，电影减产率最大的则是在头一年即1972年。

# ---
# 
# **[选做]任务3.5：**分析1968年~2015年六月电影 `Comedy` 和 `Drama` 两类电影的数量的变化。

# In[71]:


#筛选1968年~2015年六月电影
date_interval_movie_data_2 = movie_data[(movie_data['release_date']>= '1/1/1968') & (movie_data['release_date']<= '6/30/2015')]
# 筛选Comedy 和 Drama 两类电影
withcomedy_date_interval_movie_data_2 = date_interval_movie_data_2[(date_interval_movie_data_2['genres'].str.contains('Comedy'))]
withdrama_date_interval_movie_data_2 = date_interval_movie_data_2[(date_interval_movie_data_2['genres'].str.contains('Drama'))]


# In[72]:


#统计不同类型各年度的电影数量
comedy = withcomedy_date_interval_movie_data_2.groupby(['release_year'])['genres'].count()
drama = withdrama_date_interval_movie_data_2.groupby(['release_year'])['genres'].count()


# In[73]:


comedy = pd.DataFrame(comedy)
drama= pd.DataFrame(drama)


# In[74]:


#修改列名
comedy = comedy.rename(columns={'genres':'release number'})
drama = drama.rename(columns={'genres':'release number'})


# In[ ]:


comdey


# In[75]:


plt.figure(figsize = [20,5])
#生成1968年至2015年6月两类电影数量的折线图
plt.errorbar(data = comedy , x=comedy.index,y='release number',label ='comedy')
plt.errorbar(data = drama , x=drama.index,y='release number',label ='drama')
plt.xlabel('Release year')
plt.ylabel('number of films released')
plt.xticks(np.arange(1960,2018,5))
plt.legend(loc = 'upper left')


# 任务小结：总体来看，剧情片比喜剧片的出片量更多、增长速度更快，只是在1984年至1990年之间以及1994年喜剧片短暂的超越了剧情片，反映了市场对剧情片更加偏爱。

# 注意: 当你写完了所有的代码，并且回答了所有的问题。你就可以把你的 iPython Notebook 导出成 HTML 文件。你可以在菜单栏，这样导出**File -> Download as -> HTML (.html)、Python (.py)** 把导出的 HTML、python文件 和这个 iPython notebook 一起提交给审阅者。
