# GTX.Zip Professional Version（最新版本 GTZ 2.1.4）

<table style="width:100%">
<tr>
	<td>
		<h3>QQ 交流群: 934492381 </h3>
		<img src="https://i.loli.net/2018/12/10/5c0df947eddde.png" alt="GTX.Zip QQ groups"/>
	</td>
	<td>
		<h3>微信交流群:</h3>
		<img src="https://i.loli.net/2018/12/10/5c0e0afa8d12d.jpg" alt="GTX.Zip WebChat groups"/>
	</td>
</tr>
</table>
Powered by GTXLab of Genetalks.

[-English Manual-](https://github.com/Genetalks/gtz/blob/master/README.md "Markdown").

## 目录<span id="index"></span>
- [简介](#intro)  
- [产品系列](#product)  
- [生物信息分析软件支持情况](#support)
- [特性](#feature)    
- [运行环境](#environment)  
- [安装软件](#install)
- [快速上手](#quick-start)
- [使用方法](#usage) 
- [GTZ生态圈软件](#ecology)  
- [解压SDK](#decompress-sdk)  
- [版本日志](#change-log)  
- [常见问题](#faq)  
- [联系我们](#contact-us)


## 简介<span id="intro"></span>

GTX.Zip（简称GTZ）是面向基因行业，结合行业数据特征，对基因测序数据进行定向优化，支持所有文件格式的高倍无损压缩系统。**该系统具有业界最高无损压缩倍率和速度，能以1100MB/s的极致速度，将基因测序数据压缩至原大小的2%。该系统可对测序数据文件及文件目录进行高倍率快速压缩和打包，赋能用户对海量基因数据进行方便快捷的存储、传输、分发和提取**。  
  
**[安装 GTX.Zip Professional](#install)** , 提供单机版压缩，可以灵活地使用默认或指定参考基因组对本地基因组数据文件进行压缩、解压操作。
  
[-回顶-](#index)  
  
--------    
  

## 产品系列<span id="product"></span>
  
产品名称 | 版本 | 描述 | 获得方式
----|---- | -------- | --------
**GTX.Zip Professional**|V2.0.0|本地测序数据量大的基因公司、研究机构及个人用户|[-安装软件-](#install)
**GTX.Zip Enterprise**|V1.0.1|拥有PB级本地测序数据，需要通过自有计算集群对数据进行分布式压缩的大型企业和数据中心|[-联系我们-](#contact-us)
**GTX.Zip Cloud**|V1.0.1|云端测序数据分发、存储占比高的企业| http://gtz.io
  
[-回顶-](#index)  
  
--------    
  

## 生物信息分析软件支持情况<span id="support"></span>
- **[BWA 0.7 for GTX.Zip](#bwa)** 是基于官方BWA 0.7开发的比对分析软件，可以直接读取gtz压缩格式的数据，其中包含 bwa 0.7 版本和 bwa-opt 0.7版本。其中  bwa-opt 是深度优化版本，比标准 bwa快 30%左右，并且比对结果完全一致。  
- **[BOWTIE](#bowtie)/[BOWTIE2](#bowtie2) for GTX.Zip** 是将短序列与参考基因组进行比对的工具，它的运行速度快并且内存利用率高，同时可以直接读取gtz压缩格式的数据，使用方式跟官方BOWTIE/BOWTIE2保持一致。其中BOWTIE for GTX.Zip是基于官方BOWTIE 1.2.2版本开发的，BOWTIE2 for GTX.Zip是基于官方BOWTIE2 2.3.4.3版本开发的。  
  
[-回顶-](#index)  
  
--------    
  
	
## 特性<span id="feature"></span>

-	**高倍无损**  
	- GTX.Zip 采用全球领先的基因数据无损压缩算法，能够将FASTQ文件压缩低至原大小的2%，可以直接将fastq.gz 压缩至原大小的1/6。

数据集名称|GTX.Zip—压缩率|GZip—压缩率
---|:--:|---:
Nova_wes_1.fq|2.53%|17.15%
Nova_wes_2.fq|3.45%|18.34%
nova_wgs_1.fq|3.18%|17.55%
nova_wgs_2.fq|3.93%|18.66%
nova_rna_1.fq|4.56%|17.70%
nova_rna_2.fq|5.39%|18.94%  
>\*数据集为Novaseq的wes、wgs、rna测序数据。

-	**极速如飞**  
	- GTX.Zip 充分利用了CPU的并发性、新的Haswell CPU体系结构，以及新的指令(如AVX2、BMI2)，使得即使在普通计算服务器上，GTX.Zip的压缩速度也是飞快的，GTX.Zip Professional单机压缩速度高达1100MB/s，GTX.Zip Enterprise更支持企业所需的大规模分布式压缩。

-	**安全无忧**
	- GTX.Zip 采用业内首屈一指的企业级数据安全策略,是目前业界唯一能够确保数据解压100%一致还原的系统。除了常规的分块MD5校验，还凭借其强大的计算效率,在压缩的同时进行解压还原验证，只有当解压还原后的数据与源数据完全一致时，才落地压缩文件，做到数据万无一失。

-	**生态完整**
	- GTX.Zip 提供 Linux 、Mac OSX以及Windows等全平台命令行以及图形化解压工具。并提供Python、C、C++等语言的SDK接口，方便第三方开发者接入数据的读写处理。目前已免费提供能支持直接读写gtz格式（GTX.Zip压缩文件）的 bcl2fastq, fastp和BWA等常用测序分析软件。  
	- 详情请见[-GTZ生态圈软件-](#ecology)。  
  
[-回顶-](#index)  
  
--------    
  
	
## 运行环境 <span id="environment"></span>
- **64位 Linux 系统（CentOS >= 6.1；Ubuntu >= 12.04， < 18.04)**

- **64位 Windows 系统(win7,win10)**

  
[-回顶-](#index)  
  
--------    
  

## 安装Linux  GTX.Zip Pro<span id="install"></span>  
- **方式一 通过命令行直接安装（建议安装方式）**

如果安装后只希望给当前用户使用，请执行

`curl -SL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sh /tmp/gtz.run && source ~/.bashrc`  

如果安装后希望所有用户都能使用，请执行

`sudo curl -SL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`



- **方式二 先下载软件然后安装**  

首先从[-GTX.Zip Professional-]( https://gtz.io/gtz_latest.run )下载软件。

如果安装后只希望给当前用户使用，请执行

`sh gtz_latest.run && source ~/.bashrc`

如果安装后希望所有用户都能使用，请执行

`sudo sh gtz_latest.run`

- **验证安装是否成功**

运行以下命令，出现相应的软件版本信息则说明安装成功  

`gtz --version`  


## 安装Windows  GTX.Zip Pro<span id="install"></span>  
- **安装**

	安装包下载链接    https://gtz.io/gtz-2.1.4-x64-setup.exe


	双击gtz-X.X.X-x64-setup.exe ，开始安装：
	<tr>
		<td>
			<img src="https://i.loli.net/2019/10/14/NPD3ATahG1jXKIW.jpg">
		</td>
	<tr>

	选择安装目录：
	<tr>
		<td>
			<img src="https://i.loli.net/2019/10/14/b8dj1Btm9QCS3DN.jpg">
		</td>
	<tr>

	选 “是”，完成PATH环境变量配置，就可以在任意路径执行gtz程序：
	<tr>
		<td>
			<img src="https://i.loli.net/2019/10/14/8dpKYlsmA5zoEaC.jpg">
		</td>
	<tr>

	安装完成：
	<tr>
		<td>
			<img src="https://i.loli.net/2019/10/14/lW4A8F9ysEIp5vz.jpg">
		</td>
	<tr>
	
	安装完成之后，打开cmd命令窗口，查看是否已经安装成功；并通过输入命令行进行使用：
	<tr>
		<td>
			<img src="https://i.loli.net/2020/01/22/Ps7S1ty5ckmQ4W6.jpg">
		</td>
	<tr>

- **卸载**

	在windows 系统快捷菜单栏，选择Uninstall GTZ：

	<tr>
		<td>
			<img src="https://i.loli.net/2019/10/14/KQ1bq4SXHkMLFEf.jpg">
		</td>
	<tr>

	或者进入程序安装目录，运行Uninstall GTX.exe 完成卸载
	<tr>
		<td>
			<img src="https://i.loli.net/2019/10/14/ONTe7m1iP8HaJ4g.jpg">
		</td>
	<tr>
		
## 安装MacOS  GTX.Zip Pro<span id="install"></span>  
- **安装**		
	
	安装包下载链接    https://gtz.io/gtz-2.1.4-x64-setup.pkg

	双击 gtz-2.1.4-x64-setup.pkg ，开始安装：
	<tr>
		<td>
			<img src="https://i.loli.net/2020/03/15/Qtrm5Okf2CWVjYX.png">
		</td>
	<tr>
	点击 “Continue”：
		
	<tr>
		<td>
			<img src="https://i.loli.net/2020/03/15/zTXxWAPgdC795tG.png">
		</td>
	<tr>
	软件许可协议，点击 “Continue”：
		
	<tr>
		<td>
			<img src="https://i.loli.net/2020/03/15/KRF4DBsE9PvknVl.png">
		</td>
	<tr>
	点击 “Agree” 以继续安装：
	
	<tr>
		<td>
			<img src="https://i.loli.net/2020/03/15/G7ahPbvCWoD5g9e.png">
		</td>
	<tr>
	安装类型，点“Install ”:
		
	<tr>
		<td>
			<img src="https://i.loli.net/2020/03/15/oVZYgs9K4dqithS.png">
		</td>
	<tr>
	然后输入您的用户名以及密码，点“Install Software”：
	
	<tr>
		<td>
			<img src="https://i.loli.net/2020/03/15/KncSw9Xpob5hdLE.png">
		</td>
	<tr>
	安装成功，点“Close”
		
- **验证安装是否成功**

	打开终端，运行以下命令，出现相应的软件版本信息则说明安装成功；安装成功后，您可以在终端下，通过命令行使用gtz程序：
	<tr>
		<td>
			<img src="https://i.loli.net/2020/03/15/WK8D7QrwfCgykc9.png">
		</td>
	<tr>

[-回顶-](#index)  
  
--------    
  

## 快速上手 (Linux)<span id="quick-start"></span>  
前提：当前机器中已经安装了GTX.Zip Professional软件，如未安装请参考[-安装软件-](#install)


**1、下载待压缩样本**	  
样本下载：[-sample.fq-](https://gtz.io/sample.fq)  
>  <font size=1>\* 样本文件大小2GB , 从Novaseq的WES数据提取</font>

参考基因组下载: [-GCF_000001405.37_GRCh38.p11_genomic.fna.gz-](https://gtz.io/GCF_000001405.37_GRCh38.p11_genomic.fna.gz)
 
**2、开始压缩**	  

 `gtz sample.fq --ref GCF_000001405.37_GRCh38.p11_genomic.fna.gz`  
>  <font size=1>\* GTX.Zip 同时支持压缩fq.gz文件</font>

**3、解压还原**

`gtz -d sample.fq.gtz`

## 快速上手 (Windows)<span id="quick-start"></span>  
前提：当前机器中已经安装了GTX.Zip Professional软件，如未安装请参考[-安装软件-](#install)


**1、下载待压缩样本**	  
样本下载：[-sample.fq-](https://gtz.io/sample.fq)  
>  <font size=1>\* 样本文件大小2GB , 从Novaseq的WES数据提取</font>

参考基因组下载: [-GCF_000001405.37_GRCh38.p11_genomic.fna.gz-](https://gtz.io/GCF_000001405.37_GRCh38.p11_genomic.fna.gz)

**2、打开Windows命令行窗口**

`gtz --version`

<tr>
	<td>
		<img src="https://i.loli.net/2019/10/15/L7UtBzQ5GClM9bI.jpg">
	</td>
<tr>
	
**3、开始压缩**	  

 `gtz sample.fq --ref GCF_000001405.37_GRCh38.p11_genomic.fna.gz`  
>  <font size=1>\* GTX.Zip 同时支持压缩fq.gz文件</font>

<tr>
	<td>
		<img src="https://i.loli.net/2019/10/15/5iPBzuGnRhsoFAw.jpg">
	</td>
<tr>

**4、解压还原**

`gtz -d sample.fq.gtz`

<tr>
	<td>
		<img src="https://i.loli.net/2019/10/15/oik1C4E6plLnwPh.jpg">
	</td>
<tr>

[-回顶-](#index)  
  
--------    
  

## 使用方法<span id="usage"></span>  
### 功能说明

<table style="width:100%">
<tr>
	<td>
		<img src="https://i.loli.net/2019/08/21/KDQmz387AldYHvF.png">
	</td>
<tr>
<tr>
<tr>
	<td>
		<img src="https://i.loli.net/2019/08/21/IzUtNb6YXFqOdrJ.png">
	</td>
<tr>
<tr>
<tr>
	<td>
		<img src="https://i.loli.net/2019/08/21/qQHvu3ib75WTcIZ.png">
	</td>
<tr>
<tr>
<tr>
	<td>
		<img src="https://i.loli.net/2019/08/21/pDsleVQB2SC5kL9.png">
	</td>
<tr>
<tr>
<tr>
	<td>
		<img src="https://i.loli.net/2019/08/21/fXIBUgvHdN3Tatr.png">
	</td>
</tr>
</table>

### 使用实例

#### 一、压缩fastq/fastq.gz（高倍压缩）

##### 1、默认压缩方式

`gtz /data/nova.fastq.gz --ref /fasta/genomic.fna(.gz)`

--ref参数用于指定nova.fastq.gz对应物种的参考基因组fasta文件，fasta文件也支持gz格式。注意：压缩完成后的文件，解压时不再需要fasta文件

##### 2、指定输出文件名

`gtz /data/nova.fastq.gz --ref /fasta/genomic.fna -o /out/nova.gtz`

-o参数指定输出文件名，注意是小写字母o

##### 3、压缩完成后解压校验

`gtz /data/nova.fastq.gz --ref /fasta/genomic.fna --verify`

数据压缩完成后再解压一次，当压缩后文件用于存档时可以加--verify参数，但是gtz压缩时对每个块都有校验，平时使用不需要加该参数

##### 4、快速压缩

`gtz /data/nova.fastq.gz --ref /fasta/genomic.fna -l 1`

-l参数指定压缩level，1-5是快速压缩模式，目前1-5使用的压缩算法是同一个，这里主要是为了以后的扩展，同样6-9使用的压缩算法也是同一个，也是为了以后的扩展，6目前是默认的压缩级别，即最高压缩算法

##### 5、限定压缩资源

`gtz /data/nova.fastq.gz --ref /fasta/genomic.fna -p 4`

-p参数指定压缩时所使用的线程数，这里-p 4表示整个压缩过程只会使用4个线程，该功能在计算资源不够的时候非常实用

##### 6、修改默认缓存路径

`gtz /data/nova.fastq.gz --ref /fasta/genomic.fna --cache-path /path/cache/`

--cache-path参数可以修改gtz默认缓存路径。当使用了--ref指定了fasta时，gtz会将fasta转换为相应的二进制文件，然后将其缓存到默认路径（/home/user/.config/gtz），以便在下次压缩指定了相同的fasta时，gtz可以直接从缓存路径读取数据，这种处理相对较快。如果有要需要时（譬如/home/user空间不够）可以使用该参数

##### 7、不打包fasta文件

`gtz /data/nova.fastq.gz --ref /fasta/genomic.fna --donot-pack-ref`

使用--donot-pack-ref选项，生成的目标gtz文件会更小，但是解压时需要指定对应的fasta。我们不建议使用这个选项，因为不加这个选项相比加这个选项，压缩率影响很小，但如果使用此选项，则在解压缩时需要指定相应的fasta

#### 二、压缩bam

##### 1、默认压缩方式

`gtz /data/nova.bam --ref /fasta/genomic.fna(.gz)`

--ref参数用于指定nova.bam对应物种的参考基因组fasta文件，fasta文件也支持gz格式。注意：压缩完成后的文件，解压时不再需要fasta文件

###### 压缩bam时必须指定bam文件对应的fasta文件，其他压缩方式与fastq压缩方式一致

#### 三、普通压缩

##### 1、 压缩fastq/fastq.gz

`gtz /data/nova.fastq.gz`

不使用--ref指定fasta时，gtz对该fastq文件进行普通压缩，普通压缩压缩率相比高倍压缩大部分情况下会低很多。

##### 2、 压缩非fastq/fastq.gz/bam文件

`gtz /data/test.video`

gtz可以压缩任何文件

#### 四、 解压

##### 1、 解压带fasta压缩的fastq.gtz文件，不需要fasta

`gtz -d nova.fastq.gtz`

默认情况下解压带fasta压缩的gtz文件，不需要fasta文件，这是gtz2.0.0的特性

##### 2、 解压带fasta压缩的fastq.gtz文件，需要指定fasta

`gtz -d nova.fastq.gtz --ref /fasta/genomic.fna(.gz)`

如果压缩带了fasta，且使用了--donot-pack-ref参数，那么解压时需要指定压缩时所使用的fasta

##### 3、 解压bam.gtz文件

`gtz -d nova.bam.gtz`

`gtz -d nova.bam.gtz --bam-to-sam`

默认情况下bam.gtz解压成bam文件，如果需要解压成sam文件，需要带参数--bam-to-sam。如果该bam.gtz解压需要指定fasta可以通过--ref指定，参考fastq的解压即可

##### 4、 解压到终端

`gtz -d nova.fastq.gtz -c 2>/dev/null`

-c参数表示解压到终端。2>/dev/null表示将其他打印去除，只打印解压出来的fastq的内容

##### 5、解压到指定路径

`gtz -d nova.fastq.gtz -O /path/out/`

-O参数指定解压文件的输出目录，注意是大小字母O

##### 6、限定解压资源

`gtz -d nova.fastq.gtz -p 4`

-p参数同样适用解压，这里-p 4表示解压时只使用4个线程

##### 7、解压低版本带bin压缩的gtz文件

`gtz -d nova.fastq.old.gtz -r Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin`

-r参数用于兼容比2.0.0低的gtz版本，2.0.0版本可以解压老版本压缩任意gtz文件。当老版本gtz压缩fastq文，使用了-b参数指定了对应的bin文件时，那么2.0.0版本可以用-r指定对应的rbin文件解压老版本的gtz的该文件


### 参数说明
```
--ref <string>
    @ 用于压缩时: 指定压缩数据对应的Fasta文件（支持gz格式）
    @ 用于解压时: 如果压缩通过--ref指定了Fasta，并且使用了参数--donot-pack-ref，那么解压时会需要通过--ref指定对应的Fasta
-z,  --fastq-to-fastq-gz
    @ 压缩不使用
    @ 用于解压时: 将fastq解压成fastq.gz，只对fastq有效
--bam-to-sam
　　 @ 压缩不使用
   　@ 用于解压时：将bam.gtz解压成sam文件，如果不指定该参数，则解压成bam格式文件
--cache-path <string>
    @ 用于压缩时: 当通过--ref指定了fasta时，GTZ会将该fasta转换为对应的二进制文件，然后缓存至默认路径，这样当同一个fasta被使用时，
                 GTZ直接从缓存路径读取，这样会非常迅速。默认的缓存路径是~/.config/gtz，你可以通过--cache-path指定另外的路径
    @ 用于解压时: 与压缩使用方式一致
--donot-pack-ref
    @ 用于压缩时: 这个选项不建议使用。默认情况下，当压缩使用fasta时，GTZ会从巧妙地从fasta中提取必要信息然后压缩至GTZ文件，这样解压时
                 不再需要fasta信息，不使用该参数对压缩率影响很小。一旦使用该参数解压时会需要通过--ref指定压缩时所使用的fasta
    @ 解压不使用
--verify
    @ 用于压缩时: 压缩完成后，使用该参数后GTZ会再次对生成的GTZ文件解压一次，这样保证生成的GTZ一定能解压。通常情况下，这个参数是不需要的，
                 因为gtz压缩时保证了数据的正确性。当然如果压缩用于存档，你也可以使用该参数
    @ 解压不使用
-l <number>,  --level <number>
    @ 用于压缩时: [1-5]是快速压缩模式，目前1-5使用的压缩算法相同，这里预留是为了后面的扩展；6是默认的压缩级别；[6-9]是最高压缩，目前6-9
                 压缩算法也相同，保留同样是为了以后扩展
    @ 用于解压时: 当解压fastq格式的gtz文件时，如果要解压成fastq.gz格式，可以通过该参数调整fastq.gz的压缩level，level的范围为[0-9]，不指定时为4
-r <string>,  --rbin-path <string>
    @ 压缩不使用
    @ 用于解压时: 该参数对2.0.0不需要。该参数只是为了保证2.0.0能解压更低版本，使用了bin压缩出来的GTZ数据，解压这种数据时通过该参数指定rbin
                 文件或者rbin所在的路径
-O <string>,  --out-dir <string>
    @ 压缩不使用
    @ 用于解压时: 指定解压文件的保存路径
-f,  --force
    @ 用于压缩时: 强制覆盖输出问题
    @ 用于解压时: 与压缩使用方式一致
-c,  --stdout
    @ 压缩不使用
    @ 用于解压时: 解压到终端
-d,  --decompress
    @ 压缩不使用
    @ 用于解压时: 指定要解压的GTZ文件
-p <number>,  --parallel <number>
    @ 用于压缩时: 指定并发线程，不指定时等于cpu的核数
    @ 用于解压时: 与压缩使用方式一致
-o <string>,  --out <string>
    @ 用于压缩时: 指定压缩后输出的GTZ文件名
    @ 解压不使用
-e,  --no-keep
    @ 用于压缩时: 不保存原始文件
    @ 解压不使用
--version
    显示版本信息并退出
-h,  --help
    显示帮助信息并退出
	
```  

  
## GTZ生态圈软件<span id="ecology"></span>  
- [1、BWA for GTZ](#bwa)
- [2、BCL2FASTQ for GTZ](#bcl2fastq)
- [3、STAR for GTZ](#star)
- [4、BOWTIE for GTZ](#bowtie)  
- [5、BOWTIE2 for GTZ](#bowtie2) 
- [6、TOPHAT for GTZ](#tophat) 
- [7、HISAT2 for GTZ](#hisat2) 
- [8、MEGAHIT for GTZ](#megahit) 
- [9、FASTQC for GTZ](#fastqc) 
- [10、FASTP for GTZ](#fastp)
- [11、MINIMAP2 for GTZ](#minimap2)
- [12、WTDBG2 for GTZ](#wtdbg2)


## 1、BWA for GTZ <span id="bwa"></span>  (支持最新的gtz版本)

- **安装方法**

	##### 方式一 通过命令行直接安装（建议安装方式）

	如果安装后只希望给当前用户使用，请执行

	`curl -SL https://gtz.io/bwagtz_latest.run -o /tmp/bwagtz.run && sh /tmp/bwagtz.run && source ~/.bashrc`

	如果安装后希望所有用户都能使用，请执行

	`sudo curl -SL https://gtz.io/bwagtz_latest.run -o /tmp/bwagtz.run && sudo sh /tmp/bwagtz.run`



	##### 方式二 先下载软件然后安装

	首先从[-GTX.Zip Professional-]( https://gtz.io/bwagtz_latest.run )下载软件。

	如果安装后只希望给当前用户使用，请执行

	`sh bwagtz_latest.run && source ~/.bashrc`
	
	如果安装后希望所有用户都能使用，请执行

	`sudo sh bwagtz_latest.run`

	安装完成后在任意目录可以执行bwa-gtz和bwa-opt-gtz
	
- **使用说明**

	GTX.Zip对bwa的支持包中，包含bwa-gtz和bwa-opt-gtz, 两个版本均基于bwa的0.7.17版本。
	其中：两个版本都添加了对gtz文件的直接读取能力，各项功能与bwa主代码功能完全一致。
	bwa-opt-gtz还对bwa的查表结构进行了深度优化，在完全不改变其比对结果的情况下，能够节省超过1/3的比对时间。由于查表数据结构发生了一些变化，因此，bwa-opt-gtz不兼容原bwa产生的index文件数据，请按照bwa标准步骤，先重新生成index文件，然后在使用bwa-opt-gtz进行比对。

	bwa-gtz对比bwa-opt-gtz差异如下：

	(1) bwa-gtz可以直接使用官网bwa所制作的index，性能与官网bwa一致

	(2) bwa-opt-gtz不能直接使用官网bwa制作的index，index需要使用bwa-opt-gtz重新制作，但在性能上会比官网bwa提升1/3
	

	#### 使用举例

	#### bwa-gtz
	
	##### 步骤一：如果解压read.gtz不需要reference则跳过该步骤，否则通过以下方式指定对应reference

	`export GTZ_RBIN_PATH=/path/rbin/` （适用于gtx1.x.x版本，指定解压时rbin文件所在路径，建议指定；但不是必须的，没指定时gtz会自动下载，会消耗一定的时间）

	`export GTZ_RBIN_PATH=/path/fasta/xxx.fa`  （适用于gtx2.x.x版本，指定解压时对应的fasta文件，必须）
	
	##### 步骤二：执行比对
	
	`bwa-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -o aln-pe.sam`
	

	#### bwa-opt-gtz

	##### 步骤一：重新制作index（必须）

	`bwa-opt-gtz index ref.fa`

	##### 步骤二：执行比对，如果解压需要指定reference，可参考bwa-gtz使用举例步骤一
	
	`bwa-opt-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	
- **性能**

	
	在服务器资源足够的情形下，bwa-opt-gtz性能会比官网bwa好1/3，以下是同环境下的一组测试数据(指定线程数为4):
	
	#####	测试命令
	
	`bwa mem ref.fa read1.fq.gz read2.fq.gz -t 4 -o aln-pe.sam`
	
	`bwa-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	`bwa-opt-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	#####	测试环境
	
	服务器配置：16核CPU,64G内存; 文件大小: read1.fq.gz(1.8G), read2.fq.gz(1.8G), read1.fq.gtz(0.3G), read2.fq.gtz(0.3G)
	
	#####	性能数据
	
	软件  |bwa|bwa-gtz|bwa-opt-gtz
	:---:|:---:|:--:|:---:
 	时间消耗|50m14.06s|51m37.67s|39m18.86s
	内存消耗|5.888G|10.56G|19.84G
	
## 2、BCL2FASTQ for GTZ <span id="bcl2fastq"></span>　(目前只支持版本号小于2.x.x的gtz压缩包)

- **安装方法**
    
    ##### 方式一: 给当前用户安装，不需要sudo权限
    运行命令（推荐） 
    
    `curl -SL https://gtz.io/bcl2fastq_gtz_latest.run -o /tmp/bcl2fastqgtz.run && sh /tmp/bcl2fastqgtz.run`  
	
    首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录，然后在任意目录可以执行bcl2fastq-gtz
    
    ###### 或者
    下载安装文件：[-GTX.Zip bcl2fastq-gtz-]( https://gtz.io/bcl2fastq_gtz_latest.run )，然后安装
    
    `sh bcl2fastq_gtz_latest.run`
	
    同样，首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录
        
    ##### 方式二：给所有用户安装，需要sudo权限
    运行命令（推荐）  
    
	`sudo curl -SL https://gtz.io/bcl2fastq_gtz_latest.run -o /tmp/bcl2fastqgtz.run && sudo sh /tmp/bcl2fastqgtz.run`  
	
    ###### 或者
    先下载安装文件：[-GTX.Zip bcl2fastq-gtz-]( https://gtz.io/bcl2fastq_gtz_latest.run )，然后安装  
    
	`sudo sh bcl2fastq_gtz_latest.run`
	
	安装完成后，在任意目录可以执行bcl2fastq-gtz


- **使用说明**


    GTX.Zip对bcl2fastq的支持包中，基于bcl2fastq的v2.20.0.422版本。
    
    默认输出gtz格式，命令加--no-bgtzf-compression参数时，输出gz格式
    
    #### 示例1. 默认情况，输出结果文件为gtz格式，走普通压缩 
	
	`bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`

	#### 示例2. 输出结果文件为gtz格式，走高倍压缩，通过--bin_file指定bin文件
	
	`bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* --bin_file Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`
           
    #### 示例3. 输出结果文件为gz格式，运行时加--no-bgtzf-compression参数
        
    `bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* --no-bgtzf-compression >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`

- **性能**

	
	#####	测试命令

	`bcl2fastq -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`

	`bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`


	#####	测试环境

	服务器配置：16核CPU,64G内存; 文件大小: ./data/BaseCalls总计40G

	#####	性能数据

	bcl2fastq输出目标文件夹总大小40G，bcl2fastq-gtz输出目标文件夹总大小16G
	
	
	
## 3、STAR for GTZ <span id="star"></span> (目前只支持版本号小于2.x.x的gtz压缩包)

  官网STAR直接支持GTZ格式，在安装gtz和STAR之后，
 
- **步骤一** 用STAR制作索引文件

    `STAR --runMode genomeGenerate --genomeDir /path/to/genomeDir --genomeFastaFiles /path/xxx.fasta`

    详细可参考官网文档： https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf

- **步骤二** 执行对比操作

    对比过程使用实例如下：

    ##### 方式一

    `export GTZ_RBIN_PATH=/path/rbin/`

    `STAR --genomeDir /path/to/genomeDir --readFilesIn read1.fq.gtz read2.fq.gtz --readFilesCommand gtz -c -d`

    >  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须，但如果您知道rbin所在路径，建议您指定，这样可以加快gtz处理速度。因为，当gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>

    ##### 方式二

    `STAR --genomeDir /path/to/genomeDir --readFilesIn read1.fq.gtz read2.fq.gtz --readFilesCommand gtz -r /path/to/gtz_rbin_dir/ -c -d`

    >  <font size=1>\* 该例子中通过-r指定rbin文件所在目录，效果与方式一相同</font>

	
## 4、BOWTIE for GTZ <span id="bowtie"></span>  (支持最新的gtz版本)

- **安装方法**

	##### 方式一 通过命令行直接安装（建议安装方式）

	如果安装后只希望给当前用户使用，请执行

	`curl -SL https://gtz.io/bowtiegtz_latest.run -o /tmp/bowtiegtz.run && sh /tmp/bowtiegtz.run && source ~/.bashrc`

	如果安装后希望所有用户都能使用，请执行

	`sudo curl -SL https://gtz.io/bowtiegtz_latest.run -o /tmp/bowtiegtz.run && sudo sh /tmp/bowtiegtz.run`



	##### 方式二 先下载软件然后安装

	首先从[-GTX.Zip Professional-]( https://gtz.io/bowtiegtz_latest.run )下载软件。

	如果安装后只希望给当前用户使用，请执行

	`sh bowtiegtz_latest.run && source ~/.bashrc`
	
	如果安装后希望所有用户都能使用，请执行

	`sudo sh bowtiegtz_latest.run`

	安装完成后在任意目录可以执行bowtie-build-gtz，bowtie-gtz和bowtie-inspect-gtz
	
- **使用说明**

    安装完成后，会生成bowtie-gtz、bowtie-build-gtz、bowtie-inspect-gtz三个执行程序。
    如果安装时"create a soft link to /usr/bin"选择y，则在任意目录可以直接运行以上执行程序；否则需要切换到安装目录，以./bowtie-gtz方式运行
    
	GTX.Zip对bowtie的支持包中，基于bowtie的1.2.2版本。
	其中：添加了对gtz文件的直接读取能力，各项功能与bowtie主代码功能完全一致。
	bowtie-gtz可以直接使用官网bowtie制作的index，您可以用bowtie-build或者bowtie-build-gtz制作index，当然bowtie-inspect-gtz和bowtie-inspect功能也完全一致。

	#### 使用举例


	##### 步骤一：制作index

	`bowtie-build-gtz ref.fa ref_index`

	##### 步骤二：执行比对

	###### 1) 如果解压reads.fq.gtz不需要reference则跳过该步骤，否则通过以下方式指定对应reference

	`export GTZ_RBIN_PATH=/path/rbin/` （适用于gtx1.x.x版本，指定解压时rbin文件所在路径，建议指定；但不是必须的，没指定时gtz会自动下载，会消耗一定的时间）

	`export GTZ_RBIN_PATH=/path/fasta/xxx.fa`  （适用于gtx2.x.x版本，指定解压时对应的fasta文件，必须）
	
	###### 2) 执行命令
	
	`bowtie-gtz -S ref_index reads.fq.gtz eg.sam`

	

	
- **性能**

 	
 	
## 5、BOWTIE2 for GTZ <span id="bowtie2"></span>   (支持最新的gtz版本)

- **安装方法**

	##### 方式一 通过命令行直接安装（建议安装方式）

	如果安装后只希望给当前用户使用，请执行

	`curl -SL https://gtz.io/bowtie2gtz_latest.run -o /tmp/bowtie2gtz.run && sh /tmp/bowtie2gtz.run && source ~/.bashrc`
git config --global user.email
	如果安装后希望所有用户都能使用，请执行

	`sudo curl -SL https://gtz.io/bowtie2gtz_latest.run -o /tmp/bowtie2gtz.run && sudo sh /tmp/bowtie2gtz.run`



	##### 方式二 先下载软件然后安装

	首先从[-GTX.Zip Professional-]( https://gtz.io/bowtie2gtz_latest.run )下载软件。

	如果安装后只希望给当前用户使用，请执行

	`sh bowtie2gtz_latest.run && source ~/.bashrc`
	
	如果安装后希望所有用户都能使用，请执行

	`sudo sh bowtie2gtz_latest.run`

	安装完成后在任意目录可以执行bowtie2-build-gtz，bowtie2-gtz和bowtie2-inspect-gtz
	
- **使用说明**

    安装完成后，会生成bowtie2-gtz、bowtie2-build-gtz、bowtie2-inspect-gtz三个执行程序。
    如果安装时"create a soft link to /usr/bin"选择y，则在任意目录可以直接运行以上执行程序；否则需要切换到安装目录，以./bowtie2-gtz方式运行
    
	GTX.Zip对bowtie2的支持包中，基于bowtie2的2.3.4.3版本。
	其中：添加了对gtz文件的直接读取能力，各项功能与bowtie2主代码功能完全一致。
	bowtie2-gtz可以直接使用官网bowtie2制作的index，您可以用bowtie2-build或者bowtie2-build-gtz制作index，当然bowtie2-inspect-gtz和bowtie2-inspect功能也完全一致。

	#### 使用举例


	##### 步骤一：制作index

	`bowtie2-build-gtz ref.fa ref_index`

	##### 步骤二：执行比对

	###### 1) 如果解压reads_1.fq.gtz和reads_2.fq.gtz不需要reference则跳过该步骤，否则通过以下方式指定对应reference

	`export GTZ_RBIN_PATH=/path/rbin/` （适用于gtx1.x.x版本，指定解压时rbin文件所在路径，建议指定；但不是必须的，没指定时gtz会自动下载，会消耗一定的时间）

	`export GTZ_RBIN_PATH=/path/fasta/xxx.fa`  （适用于gtx2.x.x版本，指定解压时对应的fasta文件，必须）
	
	###### 2) 执行命令
	
	`bowtie2-gtz -x ref_index -1 reads_1.fq.gtz -2 reads_2.fq.gtz -S eg2.sam -p 4 --reorder`
	

	
- **性能**

	
	#####	测试命令
	
	`bowtie2 -x ref_index -1 reads_1.fq.gz -2 reads_2.fq.gz -S eg2.sam -p 4 --reorder`
	
	`bowtie2-gtz -x ref_index -1 reads_1.fq.gtz -2 reads_2.fq.gtz -S eg2.sam -p 4 --reorder`
	
	#####	测试环境
	
	服务器配置：16核CPU,64G内存; 文件大小: read1.fq.gz(1.55G), read2.fq.gz(1.78G), read1.fq.gtz(0.43G), read2.fq.gtz(0.61G)
	
	#####	性能数据
	
	软件  |bowtie2|bowtie2-gtz
	:---:|:---:|:--:
	CPU消耗(平均值)|400|445
	内存消耗(平均值)|0.19G|12.92G
 	时间消耗|63m41.06s|61m56.67s
	
 
## 6、TOPHAT for GTZ <span id="tophat"></span>  (目前只支持版本号小于2.x.x的gtz压缩包)

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -SL https://gtz.io/tophatgtz_latest.run -o /tmp/tophatgtz.run && sudo sh /tmp/tophatgtz.run`  
	##### 方式二  
	下载安装文件：[-GTX.Zip tophat-gtz-]( https://gtz.io/tophatgtz_latest.run )  
	在安装文件目录下运行命令  
	`sudo sh tophatgtz_latest.run`  
	根据提示完成安装
	
- **使用说明**

    安装完成后可以直接运行tophat-gtz，不需要其他依赖（如果环境没有安装bowtie/bowtie2，安装tophat时会自动安装）
    
    如果安装时"create a soft link to /usr/bin"选择y，则在任意目录可以直接运行tophat-gtz；否则需要切换到安装目录，以./tophat-gtz方式运行
    
    GTX.Zip对tophat的支持包中，基于tophat v2.1.2版本，其中：添加了对gtz文件的直接读取能力，各项功能与tophat主代码功能完全一致。

	#### 使用举例


	##### 步骤一：使用bowtie/bowtie2(bowtie2-gtz)制作index

	`bowtie2-build ref.fa ref_index`
	
	>  <font size=1>\* 注意：这里建议使用bowtie2/bowtie2-gtz制作index，因为对于bowtie，tophat只能使用bowtie1.1.2及以前的版本</font>

	##### 步骤二：执行比对

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`tophat-gtz -o report_dir ref_index reads_1.fq.gtz reads_2.fq.gtz`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快tophat-gtz处理速度。因为，当tophat-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	
	
- **性能**

	
	#####	测试命令
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`tophat -o report_dir -p 4 ref_index reads_1.fq.gz reads_2.fq.gz`
	
	`tophat-gtz -o report_dir -p 4 ref_index reads_1.fq.gtz reads_2.fq.gtz`
	
	
	#####	测试环境
	
	服务器配置：16核CPU,64G内存; 文件大小: read1.fq.gz(1.55G), read2.fq.gz(1.78G), read1.fq.gtz(0.43G), read2.fq.gtz(0.61G)
	
	#####	性能数据
	
	软件  |tophat|tophat-gtz
	:---:|:---:|:--:
 	时间消耗|133m12.61s|134m43.02s
	
## 7、HISAT2 for GTZ <span id="hisat2"></span> (目前只支持版本号小于2.x.x的gtz压缩包)

- **安装方法**

	##### 方式一: 给当前用户安装，不需要sudo权限
	
   	 运行命令（推荐）
	 
	`curl -SL https://gtz.io/hisat2gtz_latest.run -o /tmp/hisat2gtz.run && sh /tmp/hisat2gtz.run`  
	
	首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录，然后在任意目录可以执行hisat2-gtz和hisat2-build。
	
	###### 或者
	
	下载安装文件：[-GTX.Zip hisat2-gtz-]( https://gtz.io/hisat2gtz_latest.run )，然后安装：
	
	`sh hisat2gtz_latest.run`
	
	同样，首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录。

	##### 方式二：给所有用户安装，需要sudo权限
	
	运行命令（推荐）
	
	`sudo curl -SL https://gtz.io/hisat2gtz_latest.run -o /tmp/hisat2gtz.run && sudo sh /tmp/hisat2gtz.run`  
    	
	###### 或者
	
	下载安装文件：[-GTX.Zip hisat2-gtz-]( https://gtz.io/hisat2gtz_latest.run )，然后安装：

	`sudo sh hisat2gtz_latest.run` 
	
	根据提示完成安装

- **使用说明**

    安装完成后，会在安装目录生成hisat2-gtz、hisat2-build等执行程序和相关脚本。

    GTX.Zip对hisat2的支持包中，基于hisat2（2.1.0）版本，其中：添加了对gtz文件的直接读取能力，各项功能与hisat2主代码功能完全一致。

	#### 使用举例


	##### 步骤一：使用hisat2-build制作index

	`hisat2-build -p 4 ~/GCF_000001405.37_GRCh38.p11_genomic.fna  genome`
	

	##### 步骤二：执行比对

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`hisat2-gtz -x genome -1　reads_1.fq.gtz -2 reads_2.fq.gtz -S result.sam`
	
	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快hisat2-gtz处理速度。因为，当hisat2-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	
- **性能**
	#####	测试命令
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`hisat2 -x genome -1 reads_1.fq.gz -2 reads_2.fq.gz -S gz.sam -p 16 --reorder`
	
	`hisat2-gtz -x genome -1 reads_1.fq.gtz -2 reads_2.fq.gtz -S gtz.sam -p 16 --reorder`
	
	
	#####	测试环境
	
	服务器配置：16核CPU,64G内存; 测试文件大小: read1.fq.gz(7.3G), read2.fq.gz(7.3G), read1.fq.gtz(1.6G), read2.fq.gtz(1.8G)
	
	#####	性能数据
	
	软件  |hisat2|hisat2-gtz
	:---:|:---:|:--:
 	时间消耗|8m25.845s|10m47.930s	
	
	
## 8、MEGAHIT for GTZ <span id="megahit"></span>  (目前只支持版本号小于2.x.x的gtz压缩包)

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -SL https://gtz.io/megahitgtz_latest.run -o /tmp/megahitgtz.run && sudo sh /tmp/megahitgtz.run`  
	##### 方式二  
	下载安装文件：[-GTX.Zip megahit-gtz-]( https://gtz.io/megahitgtz_latest.run )  
	在安装文件目录下运行命令  
	`sudo sh megahitgtz_latest.run`  
	根据提示完成安装
	
- **使用说明**

    安装完成后会生成megahit-gtz（及megahit_asm_core、megahit_sdbg_build、megahit_toolkit）
    
    如果安装时"create a soft link to /usr/bin"选择y，则在任意目录可以直接运行megahit-gtz；否则需要切换到安装目录，以./megahit-gtz方式运行
    
    GTX.Zip对megahit的支持包中，基于MEGAHIT v1.1.3版本，其中：添加了对gtz文件的直接读取能力，各项功能与megahit主代码功能完全一致。

	#### 使用举例

    ##### 示例一: 支持fq

    `megahit-gtz -1 pe1.fq -2 pe2.fq -o out`
    

    ##### 示例二: 支持gtz
    
    `export GTZ_RBIN_PATH=/path/rbin/`
    
    `megahit-gtz -1 pe1.fq.gtz -2 pe2.fq.gtz -o out`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快megahit-gtz处理速度。因为，当megahit-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	
	
- **性能**

	
	#####	测试命令
	
	`megahit -t 16 -o out -1 pe1.fq.gz -2 pe2.fq.gz`
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`megahit-gtz -t 16 -o out -1 pe1.fq.gtz -2 pe2.fq.gtz`
	
	
	#####	测试环境
	
	服务器配置：16核CPU,64G内存; 文件大小: read1.fq.gz(1.55G), read2.fq.gz(1.78G), read1.fq.gtz(0.43G), read2.fq.gtz(0.61G)
	
	#####	性能数据
	
	软件  |megahit|megahit-gtz
	:---:|:---:|:--:
 	时间消耗|67m38.381s|66m44.151s
	
## 9、FASTQC for GTZ <span id="fastqc"></span> (目前只支持版本号小于2.x.x的gtz压缩包)

- **安装方法**

	##### 方式一  
	给当前用户安装，不需要sudo权限
	运行命令（推荐）
	
	`curl -SL https://gtz.io/fastqc_gtz_latest.run -o /tmp/fastqc2gtz.run &&  sh /tmp/fastqc2gtz.run`  
	
	首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录，然后在任意目录可以执行fastqc-gtz

	或者:
	
	下载安装文件：[-GTX.Zip fastqc-gtz-]( https://gtz.io/fastqc_gtz_latest.run )
	
	然后安装:
	
	`sh fastqc_gtz_latest.run`  
	
	根据提示完成安装。同样，首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录
	
	##### 方式二  
	给所有用户安装，需要sudo权限
	
	运行命令（推荐）
	
	`sudo curl -SL https://gtz.io/fastqc_gtz_latest.run -o /tmp/fastqc2gtz.run && sudo sh /tmp/fastqc2gtz.run`
	
	或者:
	
	下载安装文件：[-GTX.Zip fastqc-gtz-]( https://gtz.io/fastqc_gtz_latest.run )  
	
	然后安装:
	
	`sudo sh fastqc_gtz_latest.run`  
	
	安装完成后，在任意目录可以执行fastqc-gtz。
- **使用说明**

    安装完成后，会在安装目录生成fastqc-gtz等执行程序和相关脚本。
    GTX.Zip对fastqc的支持包，基于fastqc（0.11.8）版本，其中：添加了对gtz文件的直接读取能力，各项功能与fastqc主代码功能完全一致。

	#### 使用举例

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`fastqc-gtz -t 1 reads_1.fq.gtz -o ~/result_directory`
	
	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快fastqc-gtz处理速度。因为，当fastqc-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	
	
## 10、FASTP for GTZ <span id="fastp"></span>　(支持最新的gtz版本)

- **安装方法**
    
	##### 方式一 通过命令行直接安装（建议安装方式）

	如果安装后只希望给当前用户使用，请执行

	`curl -SL https://gtz.io/fastpgtz_latest.run -o /tmp/fastpgtz.run && sh /tmp/fastpgtz.run && source ~/.bashrc`

	如果安装后希望所有用户都能使用，请执行

	`sudo curl -SL https://gtz.io/fastpgtz_latest.run -o /tmp/fastpgtz.run && sudo sh /tmp/fastpgtz.run`



	##### 方式二 先下载软件然后安装

	首先从[-GTX.Zip Professional-]( https://gtz.io/fastpgtz_latest.run )下载软件。

	如果安装后只希望给当前用户使用，请执行

	`sh fastpgtz_latest.run && source ~/.bashrc`
	
	如果安装后希望所有用户都能使用，请执行

	`sudo sh fastpgtz_latest.run`

	安装完成后在任意目录可以执行fastp-gtz


- **使用说明**


    GTX.Zip对fastp的支持包中，基于fastp的0.19.5版本。
    输入和输出均支持gtz和非gtz格式文件，当输出文件名以.gtz结尾时，fastp-gtz会对输出文件进行gtz压缩
    
    #### 1. 输入不是gtz格式
        
	示例：

	输出gtz格式:  
	
	`fastp-gtz -i in.fq -o out.fq.gtz --ref in.fq.species.fasta`

	输出非gtz格式: 
	
	`fastp-gtz -i in.fq -o out.fq`

	关于--ref使用可以参考下面的章节说明
    
    #### 2. 输入是gtz格式
    
	示例：

	步骤一：如果解压in.R1.fq.gtz和in.R2.fq.gtz不需要reference则跳过该步骤，否则通过以下方式指定对应reference

	`export GTZ_RBIN_PATH=/path/rbin/` （适用于gtx1.x.x版本，指定解压时rbin文件所在路径，建议指定；但不是必须的，没指定时gtz会自动下载，会消耗一定的时间）

	`export GTZ_RBIN_PATH=/path/fasta/xxx.fa`  （适用于gtx2.x.x版本，指定解压时对应的fasta文件，必须）

	步骤二：执行分析

	`fastp-gtz -i in.R1.fq.gtz -I in.R2.fq.gtz -o out.R1.fq.gtz -O out.R2.fq.gtz --ref in.fq.species.fasta` 
	
	其他使用方式：

	`fastp-gtz -i in.R1.fq.gtz -I in.R2.fq.gtz -o out.R1.fq.gtz -O out.R2.fq.gtz --ref in.fq.species.fasta　--donot_pack_ref　--cache_path /cache/path/`
	
	命令说明：
	
	-ref
	
	  该参数建议指定，但不是必须的，用于指定双端读入文件所属物种对应的fasta文件，指定时fastp-gtz会高倍率压缩输出结果文件，详细可阅读工作原理
	  
	--donot_pack_ref
	
	  带该参数说明生成的out.fq.gtz在解压时需要指定reference文件，在这里即对应in.fq.species.fasta
	  
	--cache_path
	
	  默认的cache路径是~/.config/gtz，你也可以通过该参数用于指定其他路径

  ###### 工作原理：

	当输入为gtz文件时，fastp-gtz可以简单描述为四个过程：
	
	    (A)读入in.gtz -> (B)解压成in.fq -> (C)处理数据 -> (D)压缩成in.gtz

	说明：
	##### 1) 过程B

	   i. 如果过程A中in.gtz是gtz 1.x.x的高倍率压缩文件版本，则过程B需要对应的rbin文件， 这时有两种工作方式：
	   
	   方式一： 
	       您本地有该rbin文件，并通过以下环境变量指定了该文件所在路径:    
	       
		   export GTZ_RBIN_PATH=/path/rbin
	       那么程序会使用本地的rbin文件完成步骤B
	       
	   方式二：
	       您本地没有该rbin文件，或者有但没有通过环境变量指定，这种情形下程序会自动从网络下载该rbin，当然该过程将消耗一定的时间
	       
	       
	   ii. 如果过程A中in.gtz是gtz 2.x.x的高倍率压缩文件版本，则过程B也有两种工作方式：
	   
	   方式一:
	   　　in.gtz的生成使用了--donot-pack-ref，那么过程B需要通过以下环境变量指定压缩时所使用的fasta文件:
	     
	     	export GTZ_RBIN_PATH=/path/fasta/xxx.fa
	   方式二：
	   
	       in.gtz的生成没有使用--donot-pack-ref，那么过程B不需要额外的参数
	       

	##### 2) 过程C

	    fastp-gtz分析数据

	##### 3) 过程D

	   方式一：
	   
	       没有通过--ref指定fasta文件，那么out.R1.fq.gtz和out.R2.fq.gtz的生成均采用普通压缩
	       
	   方式二：
	   
	   　　通过--ref指定了fasta文件，则fastp-gtz采用高倍率压缩输出out.R1.fq.gtz和out.R2.fq.gtz
           
        
- **性能**

	
	#####	测试命令

	`fastp -i in.R1.fq.gz -I in.R2.fq.gz -o out.R1.fq.gz -O out.R2.fq.gz`

	`fastp-gtz -i in.R1.fq.gtz -I in.R2.fq.gtz -o out.R1.fq.gtz -O out.R2.fq.gtz --ref in.fq.species.fasta`


	#####	测试环境

	服务器配置：16核CPU,64G内存; 文件大小: in.R1.fq.gz(1.55G), in.R2.fq.gz(1.78G), in.R1.fq.gtz(0.43G), in.R2.fq.gtz(0.61G)

	#####	性能数据

	fastp输出文件out.R1.fq.gz和out.R2.fq.gz总大小为3.3G， fastp-gtz输出文件out.R1.fq.gtz和out.R2.fq.gtz总大小为1G
	
## 11、MINIMAP2 for GTZ <span id="minimap2"></span>　(目前只支持版本号小于2.x.x的gtz压缩包)

- **安装方法**
    
    ##### 方式一: 给当前用户安装，不需要sudo权限
    运行命令（推荐） 
    
    `curl -SL https://gtz.io/minimap2_gtz_latest.run -o /tmp/minimap2_gtz_latest.run && sh /tmp/minimap2_gtz_latest.run`  
	
    首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录，然后在任意目录可以执行minimap2-gtz
    
    ###### 或者
    下载安装文件：[-GTX.Zip minimap2-gtz-]( https://gtz.io/minimap2_gtz_latest.run )，然后安装
    
    `sh minimap2_gtz_latest.run`
	
    同样，首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录
        
    ##### 方式二：给所有用户安装，需要sudo权限
    运行命令（推荐）  
    
	`sudo curl -SL https://gtz.io/minimap2_gtz_latest.run -o /tmp/minimap2_gtz_latest.run && sudo sh /tmp/minimap2_gtz_latest.run`  
	
    ###### 或者
    先下载安装文件：[-GTX.Zip minimap2-gtz-]( https://gtz.io/minimap2_gtz_latest.run )，然后安装  
    
	`sudo sh minimap2_gtz_latest.run`
	
	安装完成后，在任意目录可以执行minimap2-gtz


- **使用说明**	
	安装完成后会生成minimap2-gtz。
	
	#### 使用举例
  	  	`export GTZ_RBIN_PATH=/path/rbin/`
    		`minimap2-gtz -ax asm20 ref.fa pacbio-ccs.fq.gtz > aln.sam`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快minimap2-gtz处理速度。因为，当minimap2-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	
	
- **性能**

	#### 测试命令
	
	`minimap2 -t 16 -a Arab.mmi Arab_E822-R02-I_good_1.fq.gz > Arab_p.sam`
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`minimap2-gtz -t 16 -a Arab.mmi Arab_E822-R02-I_good_1.fq.gz.gtz > Arab_gtz_p.sam`
		
	
	#### 测试环境
	
	服务器配置：16核CPU,64G内存;
	
	#### 性能数据
	
	软件  |minimap2|minimap2-gtz
	:---:|:---:|:--:
 	时间消耗|2m57s|3m57.151s
	
## 12、WTDBG2 for GTZ <span id="wtdbg2"></span>　(目前只支持版本号小于2.x.x的gtz压缩包)

- **安装方法**
    
    ##### 方式一: 给当前用户安装，不需要sudo权限
    运行命令（推荐） 
    
    `curl -SL https://gtz.io/wtdbg2_gtz_latest.run -o /tmp/wtdbg2_gtz_latest.run && sh /tmp/wtdbg2_gtz_latest.run`  
	
    首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录，然后在任意目录可以执行wtdbg2-gtz
    
    ###### 或者
    下载安装文件：[-GTX.Zip wtdbg2-gtz-]( https://gtz.io/wtdbg2_gtz_latest.run )，然后安装
    
    `sh wtdbg2_gtz_latest.run`
	
    同样，首次安装后，需要执行一次source ~/.bashrc或者退出去后重新登录
        
    ##### 方式二：给所有用户安装，需要sudo权限
    运行命令（推荐）  
    
    `sudo curl -SL https://gtz.io/wtdbg2_gtz_latest.run -o /tmp/wtdbg2_gtz_latest.run && sudo sh /tmp/wtdbg2_gtz_latest.run`  
	
    ###### 或者
    先下载安装文件：[-GTX.Zip wtdbg2-gtz-]( https://gtz.io/wtdbg2_gtz_latest.run )，然后安装  
    
    `sudo sh wtdbg2_gtz_latest.run`
	
    安装完成后，在任意目录可以执行wtdbg2-gtz


- **使用说明**	
	安装完成后会生成wtdbg2-gtz。
	
	#### 使用举例
  	`export GTZ_RBIN_PATH=/path/rbin/`

	`wtdbg2-gtz -x rs -g 4.6m -t 16 -i  ~/source_dir/wtdbg2_test2.fastq.gtz -fo prefix`

	`wtpoa-cns -t 16 -i prefix.ctg.lay.gz -fo prefix.ctg.fa`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快wtdbg2-gtz处理速度。因为，当wtdbg2-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	
	

	
  
[-回顶-](#index)  
  
--------    

## 解压sdk<span id="decompress-sdk"></span>

#### 解压sdk已保持与gtz最新版本同步，能解压最新版本gtz生成的压缩包

- [1、decompress sdk for perl](#sdk-perl)
- [2、decompress sdk for python](#sdk-python)
- [3、decompress sdk for R](#sdk-r)
- [4、decompress sdk for c](#sdk-c)
- [5、decompress sdk for java](#sdk-java)

## 1、decompress sdk for perl  <span id="sdk-perl"></span>

- **安装方法**

`curl -SL https://gtz.io/sdk/gtz_perl_sdk-2.1.0-linux-x86_64.tar.gz -o gtz_perl_sdk-2.1.0-linux-x86_64.tar.gz`

`tar -xvf gtz_perl_sdk-2.1.0-linux-x86_64.tar.gz`

`cd gtz_perl_sdk-2.1.0-linux-x86_64`

`# 拷贝gtz_api.h到/usr/include，拷贝libgtz.so到/usr/lib或者/usr/lib64(centos)`

`sudo make install`

`cd ./IO-GTZ`

`# 如果没有安装perl的ExtUtils::MakeMaker模块,请先执行cpan install ExtUtils::MakeMaker命令安装`

`perl Makefile.PL`

`make`

`sudo make install`


- **校验安装**

`cd gtz_perl_sdk-2.1.0-linux-x86_64`

`perl example.pl`

如果能正常显示fastq内容，说明安装成功，在自己流程中要使用perl sdk时，可以参考example.pl内容

- **运行环境**

perl >= 5.09


## 2、decompress sdk for python  <span id="sdk-python"></span>

- **安装方法**

`curl -SL https://gtz.io/sdk/gtz_python_sdk-2.1.0-linux-x86_64.tar.gz -o gtz_python_sdk-2.1.0-linux-x86_64.tar.gz`

`tar -xvf gtz_python_sdk-2.1.0-linux-x86_64.tar.gz`

`cd gtz_python_sdk-2.1.0-linux-x86_64`

#### python2
`sudo pip install gtz-2.0.1-py2-none-any.whl`

#### python3
`sudo pip3 install gtz-2.0.1-py3-none-any.whl`

- **校验安装**

`cd gtz_python_sdk-2.1.0-linux-x86_64`

`python example.py`

如果能正常显示fastq内容，说明安装成功，在自己流程中要使用python sdk时，可以参考example.py内容

- **运行环境**

python2 >= 2.6, python3 >=3.5

## 3、decompress sdk for R  <span id="sdk-r"></span>

- **安装方法**

`curl -SL https://gtz.io/sdk/gtz_r_sdk-2.1.0-linux-x86_64.tar.gz -o gtz_r_sdk-2.1.0-linux-x86_64.tar.gz`

`tar -xvf gtz_r_sdk-2.1.0-linux-x86_64.tar.gz`

`cd gtz_r_sdk-2.1.0-linux-x86_64`

`# 拷贝gtz_api.h到/usr/include，拷贝libgtz.so到/usr/lib或者/usr/lib64(centos)`

`sudo make install`

`# 安装R Rcpp包`

`R -e "install.packages(\"Rcpp\", repos=\"https://mirrors.tuna.tsinghua.edu.cn/CRAN/\")"`

`R CMD INSTALL --preclean gtz`


- **校验安装**

`cd gtz_r_sdk-2.1.0-linux-x86_64`

`Rscript ./example.r`


如果能正常显示fastq内容，说明安装成功，在自己流程中要使用r sdk时，可以参考example.r内容

## 4、decompress sdk for c  <span id="sdk-c"></span>

- **安装方法**

`curl -SL https://gtz.io/sdk/gtz_c_sdk-2.1.0-linux-x86_64.tar.gz -o gtz_c_sdk-2.1.0-linux-x86_64.tar.gz`

`tar -xvf gtz_c_sdk-2.1.0-linux-x86_64.tar.gz`

`cd gtz_c_sdk-2.1.0-linux-x86_64`

`sudo make install`


- **校验安装**

`cd gtz_c_sdk-2.1.0-linux-x86_64`

`make example`

`./example`

如果能正常显示fastq内容，说明安装成功，在自己流程中要使用c sdk时，可以参考example.c内容

- **运行环境**

## 5、decompress sdk for java  <span id="sdk-java"></span>

- **安装方法**

`curl -SL https://gtz.io/sdk/gtz_java_sdk-2.1.0-linux-x86_64.tar.gz -o gtz_java_sdk-2.1.0-linux-x86_64.tar.gz`

`tar -xvf gtz_java_sdk-2.1.0-linux-x86_64.tar.gz`

`cd gtz_java_sdk-2.1.0-linux-x86_64`

#### 步骤一：

首先将libgtzjava.so拷贝到java.path.library所指向的路径

#### 步骤二：

将io文件夹拷贝到工程目录，或者将gtz_sdk.tar拷贝到工程目录


- **校验安装**

`cd gtz_java_sdk-2.1.0-linux-x86_64`

`javac example.java`

`java example`

如果能正常显示fastq内容，说明安装成功，在自己流程中要使用java sdk时，可以参考example.java内容

[-回顶-](#index)  

--------    

  
## 版本日志<span id="change-log"></span>

目前最新版本：gtz-2.1.3 [2020/03/16]

历史版本见：	[-版本日志-](https://github.com/Genetalks/gtz/blob/master/Changelog_chs.md "Markdown")
  
[-回顶-](#index)  
  
--------    
  
## 常见问题<span id="faq"></span>  
- [1、GTX.Zip Pro的压缩性能怎么样？](#1)  
- [2、GTX.Zip Pro可以压缩哪些文件？](#2)  
- [3、GTX.Zip Pro收费模式是怎样的？](#3)  
- [4、免费的话，那你们如何盈利？](#4)  
- [5、为什么GTX.Zip Pro采用免费但不开源的模式？](#5)  
- [6、GTX.Zip Pro是否支持STDIN 和 STDOUT?](#6)  
- [7、GTX.Zip Pro为什么要求每半年更新一次？](#7)  
- [8、怎么并行跑多个压缩任务](#8)  
- [9、当fq.gz被GTX.Zip Pro压缩成fq.gz.gtz 后再解压回fq.gz，为什么前后两个gz文件的md5值不一致呢？](#9)  
- [10、GTX.Zip Pro目前支持多少个物种的智能选择压缩？](#10)  
- [11、GTX.Zip Pro软件包里的bin，rbin文件是做什么的？](#11)  
- [12、有参与无参压缩模式相比有什么不同，GTX.Zip Pro采用的哪种模式？](#12)  
- [13、为什么有些物种的数据文件的压缩率没有达到官宣中的级别？](#13)  
- [14、是否有工具软件能够支持GTX.Zip的压缩格式作为输入?](#14)  
- [15、GTX.Zip Pro是否支持所有下机数据格式？比如fasta](#15)  
- [16、是否允许将GTX.Zip Pro二次打包进其他软件的商业发布中？](#16)  
- [17、怎样让GTX.Zip Pro增加高倍压缩所需的新物种的参考基因组信息？](#17)  
- [18、bwa-gtz计算gtz压缩格式的性能与官方bwa相比会有差异么？](#18)  
- [19、尝试用GTX.Zip对bam文件进行压缩，但文件大小几乎没变。](#19)    


 <!--- [15、为什么不允许我们自己生成rbin文件以增加物种支持？](#15)-->  
 
-----------------------------------------
**1、GTX.Zip Pro的压缩性能怎么样？**<span id="1"></span>  
  >GTX.Zip Pro采用全球领先的基因数据无损压缩算法，能够将FASTQ文件压缩低至原大小的2%，可以直接将fastq.gz 压缩至原大小的1/6；GTX.Zip Pro单机压缩速度高达1100MB/s。  
  
**2、GTX.Zip Pro可以压缩哪些文件？**<span id="2"></span>  
  >GTX.Zip Pro不仅支持fastq及fastq.gz格式的高倍率压缩，还支持所有格式的文件压缩。  

**3、GTX.Zip Pro目前收费吗？**<span id="3"></span>  
  >GTX.Zip Pro是免费的，而且永久免费。  
  
**4、免费的话，那你们如何盈利？**<span id="4"></span>  
  >GTX.Zip Pro是公司为了向行业展现我们的技术能力所推出的免费产品，公司还有其他的黑科技付费产品，比如能提供测序数据计算加速服务的基因超算工作站（GTX.One）等，通过免费产品建立跟客户的信任关系，寻求更深度的商业合作。  
  
**5、为什么GTX.Zip Pro采用免费但不开源的模式？**<span id="5"></span>  
  >为了更加便于维护和持续优化GTX.Zip Pro这款企业级产品，目前采用闭源开发模式。将来时机成熟时，我们会将GTX.Zip的解压端开源给社区以方便与其他开源软件相融合。  

**6、GTX.Zip Pro是否支持STDIN 和 STDOUT?**<span id="6"></span>  
  >GTX.Zip Pro V1.01版本仅支持STDOUT，STDIN将在未来版本中支持。  

**7、GTX.Zip Pro为什么要求每 半年更新一次？**<span id="7"></span>  
  >GTX.Zip Pro将永远向后兼容所有以前版本，但同时也在增添更多功能，未来的持续改进包括：继续优化压缩率和压缩速度、采用更加紧致的索引文件、支持BAM文件压缩、支持BCL目录压缩等，通过强制更新，以期望大家手里的客户端可以跟上GTZ升级的步伐，已达到最佳的使用体验，切实帮助整个产业减小数据传、存成本。此外，6个月时间的选择也期望尽量减小对大家的运维时间上的打断，有更好的使用体验。  
    
  >如果使用场景中有绝不允许任何更新的情况，请联系我们，可以获得企业版或商讨其他解决方案。    
  >邮箱: contact@gtz.io, 或者在GitHub创建一个[新的issue](https://github.com/Genetalks/gtz/issues/new) 。

**8、怎么并行跑多个压缩任务？**<span id="8"></span>  
  >如果需要并行跑多个压缩任务可以联系我们获得GTX.Zip Enterprise版，该版本可以在企业内部组建分布式计算集群，从而获得高并发高性能的压缩性能。  
 
**9、当fq.gz被GTX.Zip Pro压缩成fq.gz.gtz后再解压回fq.gz，为什么前后两个gz文件的md5值不一致呢？**<span id="9"></span>  
  >GTX.Zip Pro对gz数据进行了重压缩工作，即将gz文件解压成fq（fastq）文件后再将fq文件压缩成gtz；当gtz文件解压成gz文件时会先解压成fq文件后，再压缩成gz格式。  
  >因此，问题中的两个gz文件其实是两个不同的文件，所以md5不同，但是里面的fq文件相同且fq文件的md5值是一样的。  
  
**10、GTX.Zip Pro目前支持多少个物种的智能选择压缩？**<span id="10"></span>  
  >39个物种，点击[-这里-](https://github.com/Genetalks/gtz/blob/master/README_chs.md#rbin-download)查看列表:。    
  >如果您希望将某个物种加入支持列表，请联系邮箱: contact@gtz.io, 或者在GitHub创建一个[新的issue](https://github.com/Genetalks/gtz/issues/new)。  
  
**11、GTX.Zip Pro软件包里的bin，rbin文件是做什么的？**<span id="11"></span>  
  >bin文件是高倍压缩时用到的指定物种的参考序列索引文件；   
  >rbin文件是解压缩时用到的指定物种的紧致参考序列文件。  
  
**12、有参与无参压缩模式相比有什么不同，GTX.Zip Pro采用的哪种模式？**<span id="12"></span>  
  >有参考基因组的压缩模式指压缩和解压时需要提前制作好的参考基因组的索引文件，无参则指压缩时不需要索引文件。  
  >因为参考基因组的存在，有参比无参能提供更优的压缩率，通常是无参大小的50%。有些无参压缩算法为了向有参靠拢提高压缩率，会在压缩过程中利用待压缩文件中的序列组装出一个文件特异性的“参考基因组”。这种方式不仅会牺牲大量计算时间，导致压缩时间过长，还会浪费计算资源，因为每个文件都需要重新组装。  
  >GTX.Zip Pro默认采用有参压缩模式，以提供最佳空间和时间上的性能，当遇到无参考基因组时，将改用次优的无参模式。    
  
**13、为什么有些物种的数据文件的压缩率没有达到官宣中的级别？**<span id="13"></span>  
  >通常这是因为这些物种暂时不在GTX.Zip Pro支持的列表范围内。GTX.Zip Pro默认采用基于参考基因组的压缩模式以提供最优压缩率，但是当物种不在支持列表范围内，GTX.Zip Pro会自动改用无参考基因组的次优倍率压缩模式，无参的压缩率通常逊于有参压缩率。  
  
  >如果遇到此情况，请您能及时跟我们联系，制作您需要的物种bin文件。  
  >邮箱: contact@gtz.io, 或者在GitHub创建一个[新的issue](https://github.com/Genetalks/gtz/issues/new)。    
  
**14、是否有工具软件能够支持GTX.Zip的压缩格式作为输入？**<span id="15"></span>  
  >我们提供直接读写gtz格式的上下游工具软件（比如，bcl2fastq, fastp, bwa 等）和各种程序语言的API接口（Perl/Python/C/C++）。 
  >详细内容可以参考[-GTZ生态圈软件-](ecology).
  
**15、GTX.Zip Pro是否支持所有下机数据格式？比如fasta**<span id="16"></span>  
  >全部支持，只是fastq格式压缩效果最好。  
   
**16、是否允许将GTX.Zip Pro二次打包进其他软件的商业发布中？**<span id="17"></span>  
  >不允许直接将 GTZ-Perfessional版本 二次 打包进 其他商业发布系统中。但如果由此需求的客户，请联系 ：contact@gtz.io , 我们会确认身份后，跟您签署一份合作协议，并为您发布一份专有重打包协议。  
  
**17、怎样让GTX.Zip Pro增加高倍压缩所需的新物种的参考基因组信息？**<span id="18"></span>  
  >邮箱: contact@gtz.io, 或者在GitHub创建一个[新的issue](https://github.com/Genetalks/gtz/issues/new) 或者加入我们的[微信交流群](https://github.com/Genetalks/gtz/)提出需求。  
  >我们将免费制作用户所需的新物种的参考基因组文件。  
  
**18、bwa-gtz计算gtz压缩格式的性能与官方bwa相比会有差异么？**<span id="19"></span>  
  >bwa-gtz做了很好的性能优化，性能上跟官方bwa相同，同时百分之百保证与官方bwa比对结果一致，完全原汁原味。  
  >深度优化的bwa-opt-gtz工具，可以在完全保证比对结果一致的前提下，使每一次bwa运算节约1/3的时间。  。  
  >详细内容可以参考[-BWA for GTZ-](#bwa).  
  
**19、尝试用GTX.Zip对bam文件进行压缩，但文件大小几乎没变。**<span id="20"></span>  
  >暂时不支持bam文件的高倍压缩，
  >因为bam文件已经是压缩过的，所以常规压缩模式下bam文件的大小也不会有太多变化。
  >如有相关的功能更新，会第一时间在交流群里通知大家。
 
<!--**15、为什么不允许我们自己生成rbin文件以增加物种支持？**<span id="15"></span>  -->  
  
[-回顶-](#index)  
  
--------    
  
## 联系我们<span id="contact-us"></span>  
使用中有任何问题请：  
邮件至: contact@gtz.io OR [创建一个新的issue](https://github.com/Genetalks/gtz/issues/new)。  
  
[-回顶-](#index)  
  
--------    
  
## License<span id="license"></span>  

详情请查看 [LICENSE](https://github.com/Genetalks/gtz/blob/master/License.md) .  
  
[-回顶-](#index)  
  
--------    

