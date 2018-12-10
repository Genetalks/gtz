# GTX.Zip Professional Version  

**如果我们提供的[-物种列表-](#rbin-download)不在您的需求范围内，请[-联系我们-](#contact-us)，我们将免费为您制作所需物种的rbin跟bin文件。**  

### QQ交流群：934492381
![GTX.Zip QQ groups](https://i.loli.net/2018/12/10/5c0df947eddde.png "GTX.Zip QQ groups")

### 微信交流群:
![GTX.Zip WebChat groups](https://i.loli.net/2018/12/03/5c047b3204fc2.jpg "GTX.Zip WebChat groups")

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
- [Rbin文件下载](#rbin-download)  
- [GTZ生态圈软件](#ecology)  
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
**GTX.Zip Professional**|V1.0.1|本地测序数据量大的基因公司、研究机构及个人用户|[-安装软件-](#install)
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
	

-	**涅槃计划**<span id="nirvana"></span>
	- GTX.Zip作为企业级软件，针对高可用性需求制定了“涅磐计划”，以确保用户在最为极端、无法获得任何GTX.Zip系统支持的情况下，也能将压缩数据解压为原始数据。涅磐计划的双重可用性保护策略如下：  
	**1.GTX.Zip多站托管，确保全网随时可下载：**  
	gtz.io网站与GitHub等多个站点永久托管GTX.Zip所有版本，确保全网不掉线，免费随时可得。  
	**2.内嵌应急解压程序，确保极端情况下仍可还原数据：**  
	压缩数据中预嵌微型程序，支持在极端特殊情况时，先一键抽取出解压程序再直接还原数据。  
	- 具体操作方式请点击[-这里-](#nirvana-example)。  
  
[-回顶-](#index)  
  
--------    
  

	
## 运行环境<span id="environment"></span>
- **64位 Linux 系统（CentOS >= 6.5；Ubuntu >= 12.04， < 18.04)**
- 4核以上，最小8GB内存的主机系统（若要达到最大并发性，推荐32核 64GB内存，或与AWS C4.8xlarge机器相同配置）
  
[-回顶-](#index)  
  
--------    
  

## 安装GTX.Zip Pro<span id="install"></span>  
- **方式一 :**  
运行命令（推荐）  
	`sudo curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`  
- **方式二：**  
下载安装文件：[-GTX.Zip Professional-]( https://gtz.io/gtz_latest.run)  
在安装文件目录下运行命令  
`sudo sh gtz_lastest.run`  
根据提示完成安装  

- **验证安装是否成功**  
运行命令  
`gtz -v`  
出现相应的软件版本信息则说明安装成功
  
[-回顶-](#index)  
  
--------    
  

## 快速上手<span id="quick-start"></span>  
前提：当前机器中已经安装了GTX.Zip Professional软件，如未安装请参考[-安装软件-](#install)

**1、制作参考基因组bin文件**  
 以人类（Homo_sapiens）为样本数据的物种，利用软件包里自带的gtz_index 工具下载rbin文件并制作bin文件  
- 通过工具下载人类rbin文件   
` gtz_index download 1`  
>命令中的“1”为人类物种在gtz_index 列表中的编号，可以通过gtz_index list命令查看物种列表  
- 或者直接下载rbin文件并保存到“\~/.config/gtz”目录  
[-homo_sapiens.rbin-](https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin)
- 下载完毕之后，制作bin文件(需要至少100GB的空闲磁盘空间跟28GB内存空间，耗时10分钟    
`gtz_index makeindex ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin  `    

><font size=1>\*  **bin文件**：高倍压缩时用到的参考序列索引文件。文件默认存放路径为："\~/.config/gtz/"</font>  
><font size=1>\*  **rbin文件**：解压缩时用到的紧致参考序列文件。文件默认存放路径为："\~/.config/gtz/"</font>   

**2、下载待压缩样本**	  
样本下载：[-sample.fq-](https://gtz.io/sample.fq)  
>  <font size=1>\* 样本文件大小2GB , 从Novaseq的WES数据提取</font>
 
**3、开始压缩**	  
 `gtz  sample.fq -o  sample.fq.gtz --bin-file  ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin`  
>  <font size=1>\* GTX.Zip 同时支持压缩fq.gz文件</font>
  
[-回顶-](#index)  
  
--------    
  

## 使用方法<span id="usage"></span>  
### 压缩示例
```
1:将文件sample.fq压缩到当前目录 
    gtz sample.fq 

2:将文件sample.fq压缩到当前目录的out文件夹内  
    gtz sample.fq -o ./out/sample.fq.gtz
    
/***如果没有通过--bin-file参数指定物种的话，则采用自动判断物种模式，自动判断比指定耗时更长 ***/

3:通过指定物种bin文件的方式来进行高倍压缩（Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin为人类的bin文件）   
    gtz sample.fq -o sample.fq.gtz --bin-file ./Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin

```
### 解压示例
```
1:将文件sample.fq解压到当前路径，如果"~/.config/gtz/"下没有对应的rbin文件，程序会自动从云下载至"~/.config/gtz/"   
    gtz -d sample.fq.gtz

2:指定已有的rbin文件所在文件夹 --rbin-path; 
  当rbin文件存在于"~/.config/gtz/"的其它地方，则可以指定rbin所在文件夹的形式进行解压，示例中rbin文件存在于“~/Homo”  
    gtz -d sample.gtz --rbin-path ~/Homo

3:将文件sample.fq.gtz解压至当前路径的Homo文件夹下   
    gtz -d sample.fq.gtz --out-dir ./Homo		
```  
### 主程序gtz 
```  
usage: gtz [-h] [-o OUT] [-b INDEX_BIN] [-d DECOMPRESS] [-O OUT_DIR]  

-h, --help                                                    显示帮助信息  
-o OUT, --out OUT                                             指定GTZ压缩文件的输出路径  
-b BIN_FILE, --bin-file BIN_FILE                              通过指定所需物种bin文件进行高倍率压缩  
-d DECOMPRESS, --decompress DECOMPRESS                        解压缩GTZ文件  
-O OUT_DIR, --out-dir OUT_DIR                                 指定解压后文件的保存路径  
-c, --stdout                                                  解压到终端
-z, --fastq-to-fastq-gz                                       将FASTQ解压成GZ格式，该选项只对FASTQ有效，非FASTQ会忽略该选项
-r RBIN_PATH, --rbin-path RBIN_PATH                           通过指定rbin文件解压  
-p PARALLEL_NUM,--parallel				      指定并行压缩/解压的线程数，默认等于CPU逻辑核数
-f, --force                                                   输出覆盖同名文件  
-e, --erase                                                   删除源文件  
-v, --version                                                 显示版本号  
```


### gtz_index
```
-交互模式：
 显示当前支持的物种列表，并且通过人机交互的模式逐步制作成BIN文件  
    gtz_index

-手动模式：  
1:显示当前支持的物种列表，其中index编号为gtz_index download 命令的输入，下载对应物种的rbin文件  
    gtz_index list  

2:下载编号为1的Homo(人类)物种的rbin文件  
    gtz_index download 1

3:通过指定rbin文件 “./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin"制作Homo_sapiens物种的bin、rec文件  
    gtz_index makeindex ./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin
		
```


### gtz_index工具
```
gtz_index <command> [options]  
Command:  
   list                                                         查看现在支持的所有物种信息  
   download <index> <path_to>                                   下载紧致参考序列rbin文件  
   makeindex <rbin_path>                                        制作参考序列索引bin文件  
```  
  
[-回顶-](#index)  
  
--------    
### 涅槃计划<span id="nirvana-example"></span>  
```
假定gtz文件名为: sample.fq.gtz

步骤一:  
    运行以下命令提取解压缩内嵌程序gtz_reborn到当前目录下会生成可执行文件gtz_reborn  
    sed -e 's/\[GTZ_REBORN_BEGIN\]/\n&/;' sample.fq.gtz | sed -n '/\[GTZ_REBORN_BEGIN\]/,/\[GTZ_REBORN_END\]/p' | sed -e 's/.*\[GTZ_REBORN_BEGIN\]//g' -e 's/\[GTZ_REBORN_END\].*//g' | tar -zxvf -

步骤二:  
    运行:  
    `./gtz_reborn -d sample.fq.gtz`  
	情形一: 如果sample.fq.gtz是高倍率压缩文件，需要按提示下载对应的fasta文件，然后再解压  
	情形二: 如果sample.fq.gtz不是高倍压缩文件，则该命令可以直接解压出原始的fastq文件  
```
  
## Rbin下载列表<span id="rbin-download"></span>

当前支持物种的rbin文件下载地址列表：

No. | 物种 | 官方链接
----|---- | --------
1|Homo sapiens|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin
2|Triticum aestivum|Https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Triticum_aestivum_8e2da4d2c18d5fadd1d3cd0c15e918d0.rbin
3|Arabidopsis thaliana|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Arabidopsis_thaliana_3dcb9b7a5a8b46c8ebbdbbdb3e0fa233.rbin
4|Mus musculus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Mus_musculus_def651daa3884affc85be8a74f7ba67e.rbin
5|Rattus norvegicus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Rattus_norvegicus_6cb6204aeddde515414059bcc3f048af.rbin
6|Oryza sativa Japonica Group|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Oryza_sativa_Japonica_Group_90b8919fd938ce2eb40a83da674d8b3f.rbin
7|Zea mays|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Zea_mays_898a827cde37664a7c0ac710d79b333f.rbin
8|Ailuropoda melanoleuca|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Ailuropoda_melanoleuca_9d59370cb06760b671353b20224ec2de.rbin
9|Apis mellifera|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Apis_mellifera_10a768025aad33307a53bc077b60e4c8.rbin
10|Bombyx mori|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Bombyx_mori_3ad2e80daa1d88f3339ac968e97f72eb.rbin
11|Bos taurus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Bos_taurus_2726c844c35a2576a513a0b578955a70.rbin
12|Brassica napus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Brassica_napus_39b086ee1025ab9d96e59639c4ce87f7.rbin
13|Caenorhabditis elegans|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Caenorhabditis_elegans_2fa2b1575d9e722f076bafcf3b755fed.rbin
14|Canis lupus familiaris|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Canis_lupus_familiaris_ddd3c39e58079f740ae2d21613f923ba.rbin
15|Capra hircus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Capra_hircus_d58b5bac5ee5baf3cb4873be119d86fe.rbin
16|Capsicum annuum|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Capsicum_annuum_9d1dac11540dbee75ea81868a5c52cc3.rbin
17|Chlorocebus sabaeus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Chlorocebus_sabaeus_6c0f80b3ca9404dc83ddffdad72c206b.rbin
18|Citrus sinensis|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Citrus_sinensis_704f1f26af39ba2e78d562e85ce974c4.rbin
19|Danio rerio|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Danio_rerio_7b1f24b449248a08ddab86d19b686818.rbin
20|Drosophila elegans|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Drosophila_elegans_ac9318016d83e7234b35aee177545225.rbin
21|Felis catus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Felis_catus_9af1182789a93a7b7c00eb657928a270.rbin
22|Glycine max|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Glycine_max_8761f4855d9396ff38f5a6201edc6080.rbin
23|Gossypium hirsutum|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Gossypium_hirsutum_3f2a7ca4b7cc58f57022c24f1cc24094.rbin
24|Macaca mulatta|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Macaca_mulatta_e75fcb8d26d9a316f1da1983b584b142.rbin
25|Manihot esculenta|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Manihot_esculenta_45e8f4480f267cf82f51f08af5dd1fa8.rbin
26|Medicago truncatula|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Medicago_truncatula_4b0ad793b3a8a7bcc1c1bcb0dee5c3c9.rbin
27|Momordica charantia|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Momordica_charantia_30f2c8beae3bb8d7beb990c522ae454d.rbin
28|Nicotiana tabacum|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Nicotiana_tabacum_c8d4659974cfc88753b60684aadb9ca3.rbin
29|Oryctolagus cuniculus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Oryctolagus_cuniculus_2d37f28080f4caff68fd164c567f18be.rbin
30|Populus trichocarpa|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Populus_trichocarpa_72f0a29abc20570aa3691445160b584c.rbin
31|Prunus persica|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Prunus_persica_cb65aac20158fa3e8075963e8ff45cfa.rbin
32|Raphanus sativus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Raphanus_sativus_fc9dc14c13511a3cd8ed2377d2c8f472.rbin
33|Sesamum indicum|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Sesamum_indicum_18e9ca5868589ab3851ee39536577784.rbin
34|Solanum tuberosum|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Solanum_tuberosum_11117f289d350ac2727d5136941986f0.rbin
35|Sorghum bicolor|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Sorghum_bicolor_ad3fb597e71a3d3cc1a50606865207a5.rbin
36|Sus scrofa|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Sus_scrofa_fa17a95f7b8532dfb932210977bebc77.rbin  
37|Homo sapiens meth|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Homo_sapiens_meth_d497f0f9f716dff930ae92146c950576.rbin
38|Mus musculus meth|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Mus_musculus_meth_42a6bd57204889412125be9111bca783.rbin  
39|Equus caballus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Equus_caballus_48fb76cc859b80aff9818361dce3e735.rbin  

**如果以上物种不在您的需求范围内，请[-联系我们-](#contact-us)，我们将免费为您制作所需物种的rbin跟bin文件。**  
  
[-回顶-](#index)  
  
--------    
  
  
  
## GTZ生态圈软件<span id="ecology"></span>  
- [1、BWA for GTZ](#bwa)  
- [2、BOWTIE for GTZ](#bowtie)  
- [3、BOWTIE2 for GTZ](#bowtie2) 
- [4、TOPHAT for GTZ](#tophat) 
- [5、HISAT2 for GTZ](#hisat2) 
- [6、MEGAHIT for GTZ](#megahit) 
- [7、FASTQC for GTZ](#fastqc) 


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

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bwa-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -o aln-pe.sam`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快bwa-gtz处理速度。因为，当bwa-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件，则会通过网络下载，下载过程将消耗时间。</font>
	

	#### bwa-opt-gtz

	##### 步骤一：重新制作index（必须）

	`bwa-opt-gtz index ref.fa`

	##### 步骤二：执行比对

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bwa-opt-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	
- **性能**

	
	在服务器资源足够的情形下，bwa-opt-gtz性能会比官网bwa好1/3，以下是同环境下的一组测试数据(指定线程数为4):
	
	#####	测试命令
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
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
	
## 2、BOWTIE for GTZ <span id="bowtie"></span>  

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -sSL https://gtz.io/bowtiegtz_latest.run -o /tmp/bowtiegtz.run && sudo sh /tmp/bowtiegtz.run`  
	##### 方式二  
	下载安装文件：[-GTX.Zip bowtie-gtz-]( https://gtz.io/bowtiegtz_latest.run )  
	在安装文件目录下运行命令  
	`sudo sh bowtiegtz_latest.run`  
	根据提示完成安装  
	
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

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bowtie-gtz -S ref_index reads.fq.gtz eg.sam`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快bowtie-gtz处理速度。因为，当bowtie-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	

	
- **性能**

	
	
 	
 	
## 3、BOWTIE2 for GTZ <span id="bowtie2"></span>  

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -sSL https://gtz.io/bowtie2gtz_latest.run -o /tmp/bowtie2gtz.run && sudo sh /tmp/bowtie2gtz.run`  
	##### 方式二  
	下载安装文件：[-GTX.Zip bowtie2-gtz-]( https://gtz.io/bowtie2gtz_latest.run )  
	在安装文件目录下运行命令  
	`sudo sh bowtie2gtz_latest.run`  
	根据提示完成安装  
	
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

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bowtie2-gtz -x ref_index -1 reads_1.fq.gtz -2 reads_2.fq.gtz -S eg2.sam -p 4 --reorder`

	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快bowtie2-gtz处理速度。因为，当bowtie2-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	

	
- **性能**

	
	#####	测试命令
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
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
	
 
## ４、TOPHAT for GTZ <span id="tophat"></span>  

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -sSL https://gtz.io/tophatgtz_latest.run -o /tmp/tophatgtz.run && sudo sh /tmp/tophatgtz.run`  
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
	
## 5、HISAT2 for GTZ <span id="hisat2"></span> 

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -sSL https://gtz.io/hisat2gtz_latest.run -o /tmp/hisat2gtz.run && sudo sh /tmp/hisat2gtz.run`  
	##### 方式二  
	下载安装文件：[-GTX.Zip hisat2-gtz-]( https://gtz.io/hisat2gtz_latest.run )  
	在安装文件目录下运行命令  
		`sudo sh hisat2gtz_latest.run`  
	根据提示完成安装

- **使用说明**

    安装完成后，会在安装目录生成hisat2-gtz、hisat2-build等执行程序和相关脚本。
    如果安装时"create a soft link to /usr/bin"选择y，则在任意目录可以直接运行hisat2-gtz和hisat2-build执行程序；否则需要切换到安装目录，以./hisat2-gtz方式运行。
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
	
	
## 6、MEGAHIT for GTZ <span id="megahit"></span>  

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -sSL https://gtz.io/megahitgtz_latest.run -o /tmp/megahitgtz.run && sudo sh /tmp/megahitgtz.run`  
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
	
## 7、FASTQC for GTZ <span id="fastqc"></span> 

- **安装方法**

	##### 方式一  
	运行命令（推荐）  
		`sudo curl -sSL https://gtz.io/fastqc_gtz_latest.run -o /tmp/fastqc2gtz.run && sudo sh /tmp/fastqc2gtz.run`  
	##### 方式二  
	下载安装文件：[-GTX.Zip fastqc-gtz-]( https://gtz.io/fastqc_gtz_latest.run )  
	在安装文件目录下运行命令  
		`sudo sh fastqc_gtz_latest.run`  
	根据提示完成安装

- **使用说明**

    安装完成后，会在安装目录生成fastqc-gtz等执行程序和相关脚本。
    如果安装时"create a soft link to /usr/bin"选择y，则在任意目录可以直接运行fastqc-gtz执行程序；否则需要切换到安装目录，以./fastqc-gtz方式运行。
    GTX.Zip对fastqc的支持包中，基于fastqc（0.11.8）版本，其中：添加了对gtz文件的直接读取能力，各项功能与fastqc主代码功能完全一致。

	#### 使用举例

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`fastqc-gtz -t 1 reads_1.fq.gtz -o ~/result_directory`
	
	>  <font size=1>\* 该例子中通过环境变量GTZ_RBIN_PATH指定了rbin文件所在路径，这里"export GTZ_RBIN_PATH=/path/rbin/"不是必须的，但如果您知道rbin所在路径，建议您指定，这样可以加快fastqc-gtz处理速度。因为，当fastqc-gtz需要rbin文件，且在默认路径~/.config/gtz下找不到该rbin文件时，则会通过网络下载，下载过程将消耗时间。</font>
	
	
	
  
[-回顶-](#index)  
  
--------    
  
  
## 版本日志<span id="change-log"></span>

#### 1.2.2 - 2018/11/09
主要优化索引文件的加载速度，压缩速度会有明显的提升  

#### 1.2.1
解决压缩完成后做校验时，GTZ有时会比较慢的问题

解决用-c做解压时，-e不工作的问题

#### 1.2
解决GTZ有时加载慢的问题

解决输入ctrl+c，GTZ有时不能退出的问题  

#### 1.1

增加功能:

-c/--stdout                   解压到终端

-z/--fastq-to-fastq-gz        将FASTQ解压成GZ格式，该选项只对FASTQ有效，非FASTQ会忽略该选项
#### 1.0

基础修订
  
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
- [14、如果你们公司不做这个项目了，我们压缩完的文件怎么办?](#14)  
- [15、是否有工具软件能够支持GTX.Zip的压缩格式作为输入?](#15)  
- [16、GTX.Zip Pro是否支持所有下机数据格式？比如fasta](#16)  
- [17、是否允许将GTX.Zip Pro二次打包进其他软件的商业发布中？](#17)  
- [18、怎样让GTX.Zip Pro增加高倍压缩所需的新物种的参考基因组信息？](#18)  
- [19、bwa-gtz计算gtz压缩格式的性能与官方bwa相比会有差异么？](#19)  
- [20、尝试用GTX.Zip对bam文件进行压缩，但文件大小几乎没变。](#20)    


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

**14、如果你们公司不做这个项目了，我们压缩完的文件怎么办？**<span id="14"></span>  
  >首先我们不会不做这个项目，其次GTX.Zip作为企业级软件，针对高可用性需求制定了“涅磐计划”，以确保用户在最为极端、无法获得任何GTX.Zip系统支持的情况下，也能将压缩数据解压为原始数据。涅磐计划的双重可用性保护策略如下：  
  >- 1）GTX.Zip多站托管，确保全网随时可下载：gtz.io网站与GitHub等多个站点永久托管GTX.Zip所有版本，确保全网不掉线，免费随时可得；  
  >- 2）内嵌应急解压程序，确保极端情况下仍可还原数据：压缩数据中预嵌微型程序，支持在极端特殊情况时，先一键抽取出解压程序再直接还原数据。  
  >- 3）详情请参考[-涅槃计划-](#nirvana)  
  
**15、是否有工具软件能够支持GTX.Zip的压缩格式作为输入？**<span id="15"></span>  
  >我们提供直接读写gtz格式的上下游工具软件（比如，bcl2fastq, fastp, bwa 等）和各种程序语言的API接口（Perl/Python/C/C++）。 
  >详细内容可以参考[-GTZ生态圈软件-](ecology).
  
**16、GTX.Zip Pro是否支持所有下机数据格式？比如fasta**<span id="16"></span>  
  >全部支持，只是fastq格式压缩效果最好。  
   
**17、是否允许将GTX.Zip Pro二次打包进其他软件的商业发布中？**<span id="17"></span>  
  >不允许直接将 GTZ-Perfessional版本 二次 打包进 其他商业发布系统中。但如果由此需求的客户，请联系 ：contact@gtz.io , 我们会确认身份后，跟您签署一份合作协议，并为您发布一份专有重打包协议。  
  
**18、怎样让GTX.Zip Pro增加高倍压缩所需的新物种的参考基因组信息？**<span id="18"></span>  
  >邮箱: contact@gtz.io, 或者在GitHub创建一个[新的issue](https://github.com/Genetalks/gtz/issues/new) 或者加入我们的[微信交流群](https://github.com/Genetalks/gtz/)提出需求。  
  >我们将免费制作用户所需的新物种的参考基因组文件。  
  
**19、bwa-gtz计算gtz压缩格式的性能与官方bwa相比会有差异么？**<span id="19"></span>  
  >bwa-gtz做了很好的性能优化，性能上跟官方bwa相同，同时百分之百保证与官方bwa比对结果一致，完全原汁原味。  
  >深度优化的bwa-opt-gtz工具，可以在完全保证比对结果一致的前提下，使每一次bwa运算节约1/3的时间。  。  
  >详细内容可以参考[-BWA for GTZ-](#bwa).  
  
**20、尝试用GTX.Zip对bam文件进行压缩，但文件大小几乎没变。**<span id="20"></span>  
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

