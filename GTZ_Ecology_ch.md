# GTX.Zip 生态圈工具集   
## 目录
- [1、BWA for GTZ](#bwa)  
 
-----------------------------------------
## 1、BWA for GTZ <span id="bwa"></span>  

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -sSL https://gtz.io/bwagtz_latest.run -o /tmp/bwagtz.run && sudo sh /tmp/bwagtz.run`  
	##### 方式二  
	下载安装文件：[-GTX.Zip bwa-gtz-]( https://gtz.io/bwagtz_latest.run )  
	在安装文件目录下运行命令  
	`sudo sh bwagtz_lastest.run`  
	根据提示完成安装  
	
- **使用说明**

	GTX.Zip对bwa的支持包中，包含bwa-gtz和bwa-opt-gtz, 两个版本均基于bwa的0.7.17版本。
	其中：两个版本都添加了对gtz文件的直接读取能力，各项功能与bwa主代码功能完全一致。
	bwa-opt-gtz还对bwa的查表结构进行了深度优化，在完全不改变其比对结果的情况下，能够节省超过1/3的比对时间。由于查表数据结构发生了一些变化，因此，bwa-opt-gtz不兼容原bwa产生的index文件数据，请按照bwa标准步骤，先重新生成index文件，然后在使用bwa-opt-gtz进行比对。

	bwa-gtz对比bwa-opt-gtz差异如下：

	(1) bwa-gtz可以直接使用官网bwa所制作的index，性能与官网bwa一致

	(2) bwa-opt-gtz不能直接使用官网bwa制作的index，index需要使用bwa-opt-gtz重新制作，但在性能上会比官网bwa提升1/3
	

	#### 使用举例

	#### bwa-gtz

	`export GTZ_RBIN_PATH=/path/rbin`
	
	`bwa-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -o aln-pe.sam`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快bwa-gtz处理速度。因为，当bwa-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件，则会通过网络下载，下载过程将消耗时间。</font>
	

	#### bwa-opt-gtz

	##### 步骤一：重新制作index（必须）

	`bwa-opt-gtz index ref.fa`

	##### 步骤二：执行比对

	`export GTZ_RBIN_PATH=/path/rbin`
	
	`bwa-opt-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	
- **性能**

	
	在服务器资源足够的情形下，bwa-opt-gtz性能会比官网bwa好1/3，以下是同环境下的一组测试数据(指定线程数为4):
	
	#####	测试命令
	
	`bwa mem ref.fa read1.fq.gz read2.fq.gz -t 4 -o aln-pe.sam`
	
	`bwa-gtz mem ref.fa read1.fq.gz.gtz read2.fq.gz.gtz -t 4 -o aln-pe.sam`
	
	`bwa-opt-gtz mem ref.fa read1.fq.gz.gtz read2.fq.gz.gtz -t 4 -o aln-pe.sam`
	
	#####	测试环境
	
	服务器配置：48核CPU,128G内存; 文件大小: read1.fq.gz(1.5G), read1.fq.gz(1.6G), read1.fq.gz(1G), read1.fq.gz(1.1G)
	
	#####	性能数据
	
	软件  |bwa|bwa-gtz|bwa-opt-gtz
	---|:---:|:--:|---:
 	时间消耗|82m48.506s|80m10.062s|58m28.795s
	内存消耗|-|-|-
	



