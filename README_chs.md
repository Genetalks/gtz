# GTX.Zip Professional Version

Powered by GTXLab of Genetalks.

[English Manual](https://github.com/Genetalks/gtz/blob/master/README.md "Markdown").

## 目录
- [简介](#intro)  
- [特性](#feature)  
- [运行环境](#environment)  
- [安装软件](#install)
- [快速上手](#quick-start)
- [使用方法](#usage)
- [应用示例](#example)
- [产品系列](#product)
- [rbin下载列表](#rbin-download)

## 简介<span id="intro"></span>

GTX.Zip是面向基因行业，结合行业数据特征，对基因测序数据进行定向优化，支持所有文件格式的高倍无损压缩系统。**该系统具有业界最高无损压缩倍率和速度，能以1100MB/s的极致速度，将基因测序数据压缩至原大小的2%。该系统采用高效“多流数据”存储结构，可对测序数据文件及文件目录进行高倍率快速压缩和打包，并支持随机寻址等高级功能，赋能用户对海量基因数据进行方便快捷的存储、传输、分发和提取**。  


本次发布的是GTX.Zip Professional版本，它可以为用户提供便捷的单机版压缩服务，可以灵活地使用默认或指定参考基因组对本地基因组数据文件进行压缩、解压操作。
	
## 特性<span id="feature"></span>

-	**高倍无损**  
	- GTX.Zip 采用全球领先的基因数据无损压缩算法，能够将FASTQ文件压缩低至原大小的2%，可以直接重压缩fastq.gz 至原大小的1/6。

数据集名称|GTX.Zip—压缩率|GZip—压缩率
---|:--:|---:
Nova_wes_1.fq|2.53%|17.15%
Nova_wes_2.fq|3.45%|18.34%
nova_wgs_1.fq|3.18%|17.55%
nova_wgs_2.fq|3.93%|18.66%
nova_rna_1.fq|4.56%|17.70%
nova_rna_2.fq|5.39%|18.94%  
>\*数据集为Novaseq的wes、wgs、rna测序数据

-	**极速如飞**  
	- GTX.Zip 充分利用了CPU的并发性、新的Haswell CPU体系结构，以及新的指令(如AVX2、BMI2)，使得即使在普通计算服务器上，GTX.Zip的压缩速度也是飞快的，GTX.Zip Professional单机压缩速度高达1100MB/s，GTX.Zip Enterprise更支持企业所需的大规模分布式压缩。

-	**安全无忧**
	- GTX.Zip 采用业内首屈一指的企业级数据安全策略,是目前业界唯一能够确保数据解压100%一致还原的系统。除了常规的分块MD5校验，还凭借其强大的计算效率,在压缩的同时进行解压还原验证，只有当解压还原后的数据与源数据完全一致时，才落地压缩文件，做到数据万无一失。

-	**生态完整**
	- GTX.Zip 提供 Linux 、Mac OSX以及Windows等全平台命令行以及图形化解压工具。并提供Python、C、C++等语言的SDK接口，方便第三方开发者接入数据的读写处理。目前已免费提供能支持直接读写gtz格式（GTX.Zip压缩文件）的 bcl2fastq, fastp和BWA等常用测序分析软件，更多支持软件将陆续发布，欢迎垂询。

## 涅槃计划
GTX.Zip作为企业级软件，针对高可用性需求制定了“涅磐计划”，以确保用户在最为极端、无法获得任何GTX.Zip系统支持的情况下，也能将压缩数据解压为原始数据。涅磐计划的双重可用性保护策略如下：
-	GTX.Zip多站托管，确保全网随时可下载：gtz.io网站与GitHub等多个站点永久托管GTX.Zip所有版本，确保全网不掉线，免费随时可得。
-	内嵌应急解压程序，确保极端情况下仍可还原数据：压缩数据中预嵌微型程序，支持在极端特殊情况时，先一键抽取出解压程序再直接还原数据。

	
## 运行环境<span id="environment"></span>
- **64位 Linux 系统（CentOS 6.5以上或Ubuntu 12.04以上，推荐Ububtu 14.04及以上64位操作系统)**
- 4核以上，最小8GB内存的主机系统（若要达到最大并发性，推荐32核 64GB内存，或与AWS C4.8xlarge机器相同配置）

## 安装软件<span id="install"></span>  
- **方式一 :**  
运行命令（推荐）  
	`sudo curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`  
- **方式二：**  
下载安装文件：[**GTX.Zip Professional **]( https://gtz.io/gtz_latest.run)  
在安装文件目录下运行命令  
`sudo sh gtz_lastest.run`  
根据提示完成安装  

- **验证安装是否成功**  
运行命令  
`gtz -v`  
出现相应的软件版本信息则说明安装成功

## 快速上手<span id="quick-start"></span>  
前提：当前机器中已经安装了GTX.Zip Professional软件，如未安装请参考[安装软件](#install)

**1、制作参考基因组bin文件（定义见附件1）**  
 以人类（Homo_sapiens）为样本数据的物种，利用软件包里自带的gtz_index 工具下载rbin文件并制作bin文件  
- 通过工具下载人类rbin文件并保存到默认路径   
` gtz_index download 1`    
- 或者通过URL下载:[ homo_sapiens.rbin](https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin)
- 下载完毕之后，制作bin文件(需要至少100GB的空闲磁盘空间跟28GB内存空间，耗时10秒钟)    
`gtz_index makeindex ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin  `    

><font size=1>\*  **bin文件**：压缩时用到的参考序列索引文件。文件默认存放路径为："\~/.config/gtz/"</font>  
><font size=1>\*  **rbin文件**：解压缩时用到的紧致参考序列文件。文件默认存放路径为："\~/.config/gtz/"</font>   

**2、下载待压缩样本**	  
样本下载：[sample.fq](https://gtz.io/sample.fq)  
>  <font size=1>\* 样本文件大小1GB , 从Novaseq的WES数据提取</font>
 
**3、开始压缩**	  
 `gtz  sample.fq -o  sample.fq.gtz --bin-file  ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin`  
>  <font size=1>\* gtz也可以直接压缩fq.gz文件</font>

## 使用方法<span id="usage"></span>
### GTX.Zip主程序gtz用法
```  
usage: gtz [-h] [-o OUT] [-b INDEX_BIN] [-d DECOMPRESS] [-O OUT_DIR]  

-h, --help                                                    显示帮助信息  
-o OUT, --out OUT                                             指定GTZ压缩文件的输出路径  
-b BIN_FILE, --bin-file BIN_FILE                              通过指定所需物种bin文件进行高倍率压缩  
-d DECOMPRESS, --decompress DECOMPRESS                        解压缩GTZ文件  
-O OUT_DIR, --out-dir OUT_DIR                                 指定解压后文件的保存路径  
-r RBIN_PATH, --rbin-path RBIN_PATH                           通过指定rbin文件解压  
-p PARALLEL_NUM,--parallel				      指定并行压缩/解压的线程数，默认等于CPU逻辑核数
-f, --force                                                   输出覆盖同名文件  
-e, --no-keep                                                 删除源文件  
-v, --version                                                 显示版本号  
```



### gtz_index工具用法：
```
gtz_index <command> [options]  
Command:  
- list                                                         查看现在支持的所有物种信息  
- download <index> <path_to>                                   下载紧致参考序列rbin文件  
- makeindex <rbin_path>                                        制作参考序列索引bin文件  
```  
         
## 应用示例：<span id="example"></span>	         
### 压缩:
```
1:将文件sample.fq压缩到当前目录 
    `gtz sample.fq -o sample.fq.gtz`

2:将文件sample.fq压缩到当前目录的out文件夹内  
    `gtz sample.fq -o ./out/sample.fq.gtz`
    
/***如果没有通过--index-bin参数指定物种的话，则采用自动判断物种模式，自动判断比指定耗时更长 ***/

3:GTZ通过指定当前目录下Homo文件夹中bin文件的方式来进行高倍压缩   
    `gtz sample.fq -o sample.fq.gtz --index-bin ./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin`

```
### 解压
```
1:将文件sample.fq解压到当前路径，如果"~/.config/gtz/"下没有对应的rbin文件，程序会自动从云下载至"~/.config/gtz/"   
    `gtz -d sample.fq.gtz`

2:指定已有的rbin文件所在文件夹 --index-path; 当rbin文件存在于"~/.config/gtz/"的其它地方，则可以指定rbin所在文件夹的形式进行解压，
示例中rbin文件存在于“\~/Homo”  
    `gtz -d sample.gtz --index-path ~/Homo`

3:将文件sample.fq.gtz解压至当前路径的Homo文件夹下   
    `gtz -d sample.fq.gtz --out-dir ./Homo`		
```  
### gtz_index
```
-交互模式：
 显示当前支持的物种列表，并且通过人机交互的模式逐步制作成BIN文件  
    `gtz_index`

-手动模式：  
1:显示当前支持的物种列表，其中index编号为gtz_index download 命令的输入，下载对应物种的rbin文件  
    `gtz_index list`  

2:下载编号为18的Homo(人类)物种的rbin文件  
    `gtz_index download 18`

3:通过指定rbin文件 “./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin"制作Homo_sapiens物种的bin、rec文件  
    `gtz_index makeindex ./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin`
		
```
### 涅槃计划  
```
假定gtz文件名为: sample.fq.gtz

步骤一:  
    运行以下命令提取解压缩内嵌程序gtz_reborn到当前目录下会生成可执行文件gtz_reborn  
    `sed -e 's/\[GTZ_REBORN_BEGIN\]/\n&/;' sample.fq.gtz | sed -n '/\[GTZ_REBORN_BEGIN\]/,/\[GTZ_REBORN_END\]/p' | sed -e 's/.*\[GTZ_REBORN_BEGIN\]//g' -e 's/\[GTZ_REBORN_END\].*//g' | tar -zxvf -`

步骤二:  
    运行:  
    `./gtz_reborn -d sample.fq.gtz`  
	情形一: 如果sample.fq.gtz是高倍率压缩文件，需要按提示下载对应的fasta文件，然后再解压  
	情形二: 如果sample.fq.gtz不是高倍压缩文件，则该命令可以直接解压出原始的fastq文件  
```


## 产品系列<span id="product"></span>
  
产品名称 | 版本 | 描述 | 获得方式
----|---- | -------- | --------
**GTX.Zip Professional**|V1.0.1|本地测序数据量大的基因公司、研究机构及个人用户|[安装软件](#install)
**GTX.Zip Enterprise**|V1.0.1|拥有PB级本地测序数据，需要通过自有计算集群对数据进行分布式压缩的大型企业和数据中心|[联系我们](https://github.com/Genetalks/gtz/new)
**GTX.Zip Cloud**|V1.0.1|云端测序数据分发、存储效率低的企业| http://gtz.io

## rbin下载列表<span id="rbin-download"></span>

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
3|Populus trichocarpa|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Populus_trichocarpa_72f0a29abc20570aa3691445160b584c.rbin
3|Prunus persica|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Prunus_persica_cb65aac20158fa3e8075963e8ff45cfa.rbin
32|Raphanus sativus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Raphanus_sativus_fc9dc14c13511a3cd8ed2377d2c8f472.rbin
33|Sesamum indicum|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Sesamum_indicum_18e9ca5868589ab3851ee39536577784.rbin
34|Solanum tuberosum|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Solanum_tuberosum_11117f289d350ac2727d5136941986f0.rbin
35|Sorghum bicolor|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Sorghum_bicolor_ad3fb597e71a3d3cc1a50606865207a5.rbin
36|Sus scrofa|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Sus_scrofa_fa17a95f7b8532dfb932210977bebc77.rbin
	
## 联系我们
	使用中有任何问题请联系: contact@gtz.io 
