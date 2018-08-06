# GTX Compressor  （技术预览版）

Powered by GTXLab of Genetalks.

技术预览版本下载地址： https://github.com/Genetalks/gtz/archive/0.2.2i_tech_preview.tar.gz 


[English Manual](https://github.com/Genetalks/gtz/blob/master/README.md "Markdown").

## 系统简介

GTX Compressor是Genetalks公司GTX Lab实验室开发的面向大型数据（数GB甚至数TB数据，尤其是生物信息数据）上云，而量身定制的复杂通用数据压缩打包系统，可以对任意基因测序数据以及数据目录进行高压缩率的快速打包，形成单个压缩数据文件，以方便存储档与远程传输、校验。区别于以往的压缩工具，GT Compressor系统着力于 **高压缩率，高速率，方便的数据抽取** 。

GTX Compressor可以在AWS C4.8xlarge机器（或同配置服务器），**以超过114MB/s的速度，将接近200GB大小的33个质量数的FASTQ文件（NA12878_1.fastq），在13分钟内压缩到原大小的19%**，而对于X10等只有 **7个质量数的FASTQ数据，其压缩率更可以达到5.5%** 。

**GTX Compressor提供“上云”功能**。考虑商业使用时，用户不仅需要将测序产生的海量数据存储于本地，更迫切地寻求将数据快速稳定分发传输的能力。GTX Lab实验室已经研发出在普通带宽条件下，提供远距离和超远距离数据传输服务的工具gtransfer，可以便捷地进行端到端或端到云平台的数据传输。

## 系统亮点

该数据打包压缩系统的特点：

- **高压缩比** 采用Context Model压缩技术，配合多种优化的预测模型，平衡系统并发度与内存资源消耗后，能达到极高的压缩率。对FASTQ文件，压缩率最高可达5.58%。

- **高性能：** GTX compressor充分发挥了CPU的并发性以及新型Haswell CPU体系结构与AVX2、BMI2等指令集的计算能力，使得在普通服务器上的压缩速度，最高能够以接近114MB/s的输入流量输入数据并压缩完毕。

- **高速上云：** GTX gtransfer支持在普通带宽条件下，提供远距离和超远距离数据传输服务，可以便捷地进行端到端或端到云平台的数据传输。



## 系统环境要求

- 64位 Linux 系统（CentOS 6.5以上或Ubuntu 12.04以上，推荐Ububtu 14.04及以上64位操作系统)

- 4核以上，最小8GB内存的主机系统（若要达到最大并发性，推荐32核 64GB内存，或与AWS C4.8xlarge机器相同配置）

## 安装说明
本系统采用开包即用的打包原则，不依赖当前系统其他任何库。

下载包内包含ubuntu版本和centos版本的两个tar.gz的包。选择对应tar.gz的包，解压后，gtz命令就在当前解压的gtz_0.2.2i_ubuntu_tech_preview目录或gtz_0.2.2i_centos_tech_preview目录中，直接使用即可。


## 命令行说明

执行 ./gtz -h，输出命令行帮助说明。


```
USAGE: 
./gtz   [--gz]  [--rbin-path] [--outdir] [--list] [-e <string>] [-c] 
          [-d]  [-a] [-o <string>] [--] [--version]
          [-h] <file names> ...

  
```

通用选项说明：

- -h：输出以上命令行帮助信息
- \-\-version：输出gt_compress程序的版本号


压缩选项说明：
- -a：追加模式，本次压缩的内容会追加到压缩文件中
- -o：指定压缩文件名，不指定时，默认为out.gtz
- file_name：需要压缩的文件或目录, 若不指定，则从标准输入中读入数据


解压选项说明：
- -d,\-\-decode             :  解压模式
--gz				 : 解压为gz格式。如果不指定，默认输出为.fastq格式
--rbin-path  : 指定本地解压所需要的rbin文件的路径
--outdir		 : 指定解压输出目录
--list		   : 列出压缩包中所有的压缩文件名，与-d参数一起使用
-e, --extract	   : 解压压缩包中指定的压缩文件，文件名之间用冒号:分割，与-d参数一起使用
- -c,\-\-stdout            :   解压数据输出至标准输出, 只能与 -d 参数一起使用
- file_name：需要压缩的文件, 若不指定，则从标准输入中读入数据


### 示例：


### 压缩举例
	./gtz  -o  output.gtz  source.fastq  									  将原文件source.fastq压缩为output.gtz
	./gtz  -o  output.gtz  source.fastq.gz									将原文件source.fastq.gz压缩为output.gtz
	./gtz  -o  output.gtz  source1.fastq  source2.fastq     将多个原文件source1.fastq,source2.fastq压缩为output.gtz (支持多个文件压缩到一个压缩包)
	./gtz  -o  output.gtz  source_diretory									将目录source_diretory压缩为output.gtz (支持目录压缩到一个压缩包)
	./gtz  -a -o output.gtz source3.fastq                   将文件source3.fastq以追加的方式，压缩到已有的output.gtz中


### 解压举例
	./gtz  -d  output.gtz                                   解压output.gtz，默认输出为fastq格式
	./gtz  -d  output.gtz --gz                              解压output.gtz，输出为fastq.gz格式
	./gtz  -d  output.gtz --outdir  output_path             解压output.gtz到output_path目录中
	./gtz  -d  output.gtz --rbin-path  rbin_path            解压企业版高倍率压缩包output.gtz，指定对应的rbin文件的路径
	./gtz  -d  output.gtz --list														查看压缩包output.gtz里的文件列表	
	
	# -e 代表抽取文件，后面要抽取的文件名称间，用 ":" 隔开
	./gtz -e source.fastq:/A/source2.fastq -d gtz/out.gtz
	
	或者某个文件到管道：
	# -c 代表输出到console， -e 代表抽取其中的某个文件
	./gtz -c -e source.fastq  -d gtz/out.gtz > myfile.txt
	或者
	./gtz -c -e source.fastq  -d gtz/out.gtz | gzip -c > myfastq.gz
	



## 联系我们

使用中有任何问题请联系： gen.li@genetalks.com
