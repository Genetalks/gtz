# GTX.Zip Professional Version

Powered by GTXLab of Genetalks.

- 一键安装命令:  
	`curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`

- GTX.Zip 专业版本下载链接:https://gtz.io/gtz_latest.run

[English Manual](https://github.com/Genetalks/gtz/blob/master/README.md "Markdown").

## 系统简介

GTX.Zip是面向基因行业，结合行业数据特征，对基因测序数据进行定向优化，支持所有文件格式的高倍无损压缩系统。**该系统具有业界最高无损压缩倍率和速度，能以1100MB/s的极致速度，将基因测序数据压缩至原大小的2%。该系统采用高效“多流数据”存储结构，可对测序数据文件及文件目录进行高倍率快速压缩和打包，并支持随机寻址等高级功能，赋能用户对海量基因数据进行方便快捷的存储、传输、分发和提取**。

目前 GTX.Zip Professional, GTX.Zip Enterprise, GTX.Zip Cloud三个产品已正式面世，分别适用于以下客户：
- 	**GTX.Zip Professional**:本地测序数据量大的基因公司、研究机构及个人用户
- 	**GTX.Zip Enterprise**:拥有PB级本地测序数据，需要通过自有计算集群对数据进行分布式压缩的大型企业和数据中心
- 	**GTX.Zip Cloud**:云端测序数据分发、存储效率低的企业

## 涅槃计划
GTX.Zip作为企业级软件，针对高可用性需求制定了“涅磐计划”，以确保用户在最为极端、无法获得任何GTX.Zip系统支持的情况下，也能将压缩数据解压为原始数据。涅磐计划的双重可用性保护策略如下：
-	GTX.Zip多站托管，确保全网随时可下载：gtz.io网站与GitHub等多个站点永久托管GTX.Zip所有版本，确保全网不掉线，免费随时可得。
-	内嵌应急解压程序，确保极端情况下仍可还原数据：压缩数据中预嵌微型程序，支持在极端特殊情况时，先一键抽取出解压程序再直接还原数据。
		
## 技术亮点	
-	**高倍无损**  
	- GTX.Zip 采用全球领先的基因数据无损压缩算法，能够将FASTQ文件压缩低至原大小的2%，可以直接重压缩fastq.gz 至原大小的1/6。

数据集名称|GTX.Zip—压缩率|Gzip—压缩率
---|:--:|---:
Nova_wes_1.fq|2.53%|17.15%
Nova_wes_2.fq|3.45%|18.34%
nova_wgs_1.fq|3.18%|17.55%
nova_wgs_2.fq|3.93%|18.66%
nova_rna_1.fq|4.56%|17.70%
nova_rna_2.fq|5.39%|18.94%

-	**极速如飞**  
	- GTX.Zip 充分利用了CPU的并发性、新的Haswell CPU体系结构，以及新的指令(如AVX2、BMI2)，使得即使在普通计算服务器上，GTX.Zip的压缩速度也是飞快的，GTX.Zip Professional单机压缩速度高达1100MB/s，GTX.Zip Enterprise更支持企业所需的大规模分布式压缩。

-	**安全无忧**
	- GTX.Zip 采用业内首屈一指的企业级数据安全策略,是目前业界唯一能够确保数据解压100%一致还原的系统。除了常规的分块MD5校验，还凭借其强大的计算效率,在压缩的同时进行解压还原验证，只有当解压还原后的数据与源数据完全一致时，才落地压缩文件，做到数据万无一失。

-	**生态完整**
	- GTX.Zip 提供 Linux 、Mac OSX以及Windows等全平台命令行以及图形化解压工具。并提供Python、C、C++等语言的SDK接口，方便第三方开发者接入数据的读写处理。目前已免费提供能支持直接读写gtz格式（GTX.Zip压缩文件）的 bcl2fastq, fastp和BWA等常用测序分析软件，更多支持软件将陆续发布，欢迎垂询。
	
## 名词解析
**BIN文件**:压缩时用到的参考序列索引文件。文件默认存放路径为："~/.config/gtz/"

**RBIN文件**:解压缩时用到的紧致参考序列文件。文件默认存放路径为："~/.config/gtz/"

**gtz_index**:GTX.Zip Professional 安装目录下的工具软件，可以用来查看支持物种列表、下载rbin、制作bin。


## GTX.Zip Professional产品
GTX.Zip Professional为用户提供便捷的单机版压缩服务，可以灵活地使用默认或指定参考基因组对本地基因组数据文件进行压缩、解压操作。
	
	
## 系统环境要求
- **64位 Linux 系统（CentOS 6.5以上或Ubuntu 12.04以上，推荐Ububtu 14.04及以上64位操作系统)**
- 4核以上，最小8GB内存的主机系统（若要达到最大并发性，推荐32核 64GB内存，或与AWS C4.8xlarge机器相同配置）


## 安装说明	
方式一（推荐）：
	`curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`

方式二：
	下载文件gtz_latest.run，然后执行它。
	
### gtz的用法
usage: gtz [-h] [-o OUT] [-b INDEX_BIN] [-d DECOMPRESS] [-O OUT_DIR]  

-h, --help&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;显示帮助信息  
-o OUT, --out OUT&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;指定GTZ压缩文件的输出路径  
-b BIN_FILE, --bin-file BIN_FILE&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;通过指定所需物种BIN文件进行高倍率压缩  
-d DECOMPRESS, --decompress DECOMPRESS&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;解压缩GTZ文件  
-O OUT_DIR, --out-dir OUT_DIR&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;指定解压后文件的保存路径  
-r RBIN_PATH, --rbin-path RBIN_PATH&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;通过指定RBIN文件解压  
-f, --force&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;输出覆盖同名文件  
-k, --keep&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;保留源文件  
-v, --version&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;显示版本号  



### gtz_index的用法：
gtz_index <command> [options]  
Command:  
- list&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;查看现在支持的所有物种信息  
- download <index> <path_to>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;下载紧致参考序列rbin文件  
- make <rbin_path>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;制作参考序列索引bin文件  
         
## 示例：	         
### 压缩举例:
1:将文件Arab_E822-R02-I_good_1.fq压缩到当前目录  
	`./gtz Arab_E822-R02-I_good_1.fq -o Arab_E822-R02-I_good_1.fq.gz.gtz`

2:将文件Arab_E822-R02-I_good_1.fq压缩到当前目录的out文件夹内,以上两种情况没有指定bin，会根据程序自动识别物种功能去压缩,以下为指定物种的使用方式--index-bin  
	`./gtz Arab_E822-R02-I_good_1.fq -o ./out/Arab_E822-R02-I_good_1.fq.gz.gtz`

3:GTZ通过指定当前目录下Arab文件夹中BIN文件的方式来进行高倍压缩   
	`./gtz Arab_E822-R02-I_good_1.fq -o Arab_E822-R02-I_good_1.fq.gz.gtz --index-bin ./Arab/Arabidopsis_thaliana_3dcb9b7a5a8b46c8ebbdbbdb3e0fa233.bin`

### 解压举例
1:将文件Arab_E822-R02-I_good_1.fq解压到当前路径，如果"\~/.config/gtz/"下没有对应的rbin文件，程序会自动从云下载至"\~/.config/gtz/"   
	`./gtz -d Arab_E822-R02-I_good_1.fq.gz.gtz`

2:指定已有的rbin文件所在文件夹 --index-path; 当rbin文件存在于"\~/.config/gtz/"的其它地方，则可以指定rbin所在文件夹的形式进行解压，目前rbin文件存在于“\~/Arab”  
	`./gtz -d Arab_E822-R02-I_good_1.fq.gz.gtz --index-path ~/Arab`

3:将文件Arab_E822-R02-I_good_1.fq.gz.gtz解压至当前路径的Arab文件夹下   
	`./gtz -d Arab_E822-R02-I_good_1.fq.gz.gtz -outdir ./Arab`		
			
### gtz_index举例
-	交互模式：
		显示当前支持的物种列表，并且通过人机交互的模式逐步制作成BIN文件  
		`./gtz_index`

-	手动模式：
	1:显示当前支持的物种列表，其中index编号为gtz_index download 命令的输入，下载对应物种的rbin文件  
		`./gtz_index list`  

	2:下载编号为3的Arab物种的rbin文件  
		`./gtz_index download 3`
		

	3:通过指定rbin文件 “./Arab/Arabidopsis_thaliana_3dcb9b7a5a8b46c8ebbdbbdb3e0fa233.rbin"制作Arabidopsis_thaliana物种的bin、rec文件  
		`./gtz_index makeindex ./Arab/Arabidopsis_thaliana_3dcb9b7a5a8b46c8ebbdbbdb3e0fa233.rbin`
		

## 涅槃计划
gtz文件名为: nova_rna_1.fq.gtz

步骤一:  
	运行以下命令提取解压缩内嵌程序gtz_reborn到当前目录下会生成可执行文件gtz_reborn  
	`sed -e 's/\[GTZ_REBORN_BEGIN\]/\n&/;' nova_rna_1_head.fq.gtz　|　sed -n '/\[GTZ_REBORN_BEGIN\]/,/\[GTZ_REBORN_END\]/p' |sed -e 's/.*\[GTZ_REBORN_BEGIN\]//g' -e 's/\[GTZ_REBORN_END\].*//g' | tar -zxvf -`

步骤二:  
	运行:  
	`./gtz_reborn -d nova_rna_1.fq.gtz`  
	情形一: 如果nova_rna_1.fq.gtz是高倍率压缩文件，需要按提示下载对应的fasta文件，然后再解压  
	情形二: 如果nova_rna_1.fq.gtz不是高倍压缩文件，则该命令可以直接解压出原始的fastq文件  

	
## 联系我们
	使用中有任何问题请联系: contact@gtz.io 
