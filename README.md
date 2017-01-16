# GTX Compressor  （直压上云技术预览版）

Powered by GTXLab of Genetalks.

下载： https://github.com/Genetalks/gtz/archive/0.1_tech_preview.zip

##系统简介
GTX Compressor是Genetalks公司GTX Lab实验室开发的面向大型数据（数GB甚至数TB数据，尤其是生物信息数据）上云，而量身定制的复杂通用数据压缩打包系统，可以对任意基因测序数据以及数据目录进行高压缩率的快速打包，形成单个压缩数据文件，以方便存储档与远程传输、校验。区别于以往的压缩工具，GT Compressor系统着力于**高压缩率，高速率，方便的数据抽取**。

GTX Compressor可以在AWS C4.8xlarge机器（或同配置服务器），**以超过114MB/s的速度，将接近200GB大小的33个质量数的FASTQ文件（NA12878_1.fastq），在29分钟内压缩到原大小的13%**，而对于X10等只有**7个质量数的FASTQ数据，其压缩率更可以达到5.5%**。

**GTX Compressor提供“直压上云”功能**。考虑商业使用时，用户不仅需要将测序产生的海量数据存储于本地，更迫切地寻求将数据快速稳定传输至云端的能力。 GTX Compressor的数据压缩引擎允许用户直接将fastq文件压缩存储到亚马逊AWS平台或者阿里云OSS平台，并保持与本地压缩相同的压缩速度与压缩效率。普通100Mbits Intenet线路，可以在短短30分钟内稳定地将200GB Fastq文件的直压上云。

## 系统亮点

该数据打包压缩系统的特点：
- **高压缩比：**采用Context Model压缩技术，配合多种优化的预测模型，平衡系统并发度与内存资源消耗后，能达到极高的压缩率。对FASTQ文件，压缩率最高可达5.58%。
- **高性能：** GTX compressor充分发挥了CPU的并发性以及新型Haswell CPU体系结构与AVX2、BMI2等指令集的计算能力，使得在普通服务器上的压缩速度，最高能够以接近114MB/s的输入流量输入数据并压缩完毕。 
- **高速直压上云：** GTX compressor支持直压上云和从云端直接解压下载功能。普通的20核服务器，通过百兆Intenet线路，可以在短短30分钟内稳定地将200GB Fastq文件的直压上云。 



## 系统环境要求
64位 Linux 系统（CentOS 6.5以上或Ubuntu 12.04以上，推荐Ububtu 14.04及以上64位操作系统)
4核以上，最小8GB内存的主机系统（若要达到最大并发性，推荐32核 64GB内存，或与AWS C4.8xlarge机器相同配置）

## 安装说明
本系统采用开包即用的打包原则，不依赖当前系统其他任何库。

下载包内包含ubuntu版本和centos版本的两个tar.gz的包。选择对应tar.gz的包，解压后，gtz命令就在当前解压的gtz_0.1_ubuntu_tech_preview目录或gtz_0.1_centos_tech_preview目录中，直接使用即可。


## 命令行说明

执行 ./gtz -h，输出命令行帮助说明。


```
USAGE: 
./gtz  [-f] [--endpoint <string>] [--timeout <string>]
          [--secret-access-key <string>] [--access-key-id <string>] [-b
          <string>] [-s <string>] [-t] [-n <string>] [-l <string>] [-i]
          [-d] [--delete] [-a] [-g <number>] [-o <string>] [--] [--version]
          [-h] <file names> ...

  
```

通用选项说明：
- -h：输出以上命令行帮助信息
- \-\-version：输出gt_compress程序的版本号
- \-\-access-key-id       :   指定云平台用户ID
- \-\-secret-access-key： 指定云平台用户密钥
- \-\-endpoint             ：  指定阿里云OSS平台的访问域名和数据中心

压缩选项说明：
- -f,  \-\-force              ：  强制删除容器内的object
- \-\-timeout               ：  指定上传超时阀值
- -i：压缩时增加索引，主要用于在压缩文件中快速检索fastq文件的某段内容，该选项会降低压缩速度
- -a：追加模式，本次压缩的内容会追加到压缩文件中
- -g：分组加速压缩，分组越多，需要的cpu和内存越多，压缩速度越快。不指定该值时，程序会根据cpu和内存自动选择最优值
- -o：指定压缩文件名，不指定时，默认为out.gtz
- file_name：需要压缩的文件或目录, 若不指定，则从标准输入中读入数据


解压选项说明：
- -d,\-\-decode             :  解压模式
- -f, \-\-force              ：  强制删除容器内的object
- \-\-timeout               ：  指定下载超时阀值
- -t,\-\-terminal            :   解压数据输出至标准输出
- -i,\-\-index                 :   解压模式下，启用索引功能
- -l, \-\-line                   :   指定需检索的起始行，起始行在fastq中的位置为（该值-1)*4
- -n, \-\-number           :   指定需要检索输出的行数，输出的行数为该值*4，负数为向后检索
- -o：指定输出文件名，使用-n或-l时需要指定该选项，否则不需要该选项
- file_name：需要压缩的文件, 若不指定，则从标准输入中读入数据


### 示例：
配置环境变量：
export access_key_id=xxxxxx
export secret_access_key=xxxxxx
export endpoint=xxxxxx   （该环境变量只有上传至OSS时才需设置）


#### 直压阿里OSS：

./gtz  -o oss://gt-compress/source.gtz   source.fastq
或者
zcat source.fastq.gz  |  ./gtz  -o oss://gt-compress/source.gtz

####直压AWS S3：
./gtz  -o s3://gt-compress/source.gtz   source.fastq
或者：
zcat source.fastq.gz  |  ./gtz  -o s3://gt-compress/source.gtz

#### 压缩到本地
./gtz  -o gt-compress/source.gtz   source.fastq
或者
zcat source.fastq.gz  |  ./gtz  -o gt-compress/source.gtz



## 联系我们

使用中有任何问题请联系： gen.li@genetalks.com
