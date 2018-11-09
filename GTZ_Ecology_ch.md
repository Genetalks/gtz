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

	bwa-gtz基于bwa官网的0.7.17版本所做修改，在bwa基础上支持gtz格式数据，同时其性能比官网bwa提升1/3倍。
	bwa-gtz其他功能和使用方式与官网bwa完全一致，举例如下:
	
	官网bwa

	`bwa mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq nova_wes_2.fq -t 4 -o nova_wes.sam`  

	bwa-gtz
	
	`bwa-gtz mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq nova_wes_2.fq -t 4 -o nova_wes.sam`  
	`bwa-gtz mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq.gtz nova_wes_2.fq.gtz -t 4 -o nova_wes.sam`  
  
	>\*1) bwa-gtz处理gtz格式数据时，我们建议您都可以通过以下环境变量指定rbin文件所在的路径，因为bwa-gtz在处理gtz格式数据
	>时，如果需要rbin文件，它只会去～/.config/gtz路径下搜索对应的rbin文件，在没有找到的情形下再去从网络上拖取对应的rbin
	>文件，下载将消耗一定的时间。  
  >\**环境变量设置**:   
	>    `export GTZ_RBIN_PATH=/path/rbin`  
	>\*2) 使用bwa-gtz时所有index必须重新制作，不能直接使用官网bwa制作的index  
  
- **性能**

	在服务器资源足够的情形下，bwa-gtz性能会比官网bwa好1/3，以下是同环境下的一组测试数据(指定线程数为4):
	
	官网bwa，耗时50分钟  

	`bwa mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq nova_wes_2.fq -t 4 -o nova_wes.sam`  

	bwa-gtz，耗时34分钟  

	`bwa-gtz mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq.gtz nova_wes_2.fq.gtz -t 4 -o nova_wes.sam`  
	
	
- **最佳实践**



