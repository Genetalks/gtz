# GTX.Zip Professional Version   

### If the species you need is not in our [species list](#rbin-download), please [contact us](#contact-us) !  
### QQ group(s): 934492381 

### WeChat group(s):
![GTX.Zip WebChat groups](https://i.loli.net/2018/11/12/5be8d03268263.jpg "GTX.Zip WebChat groups")

Powered by GTXLab of Genetalks.  

[中文说明](https://github.com/Genetalks/gtz/blob/master/README_chs.md "Markdown").
## Index<span id="index"></span>
- [What is GTX.Zip?](#intro)  
- [Product series](#product)  
- [Supported Bioinformatic Analysis Softwares](#supported-softwares)  
- [Feature](#feature)    
- [Environment Requirements](#environment)  
- [How to Install?](#install)
- [Let's Do It!](#quick-start)
- [Usage](#usage)
- [For Example](#example)   
- [Species rbin Downloads](#rbin-download)  
- [GTZ Ecology Softwares](#ecology)  
- [Change Log](#change-log) 
- [FAQ](#faq)  
- [Contact Us](#contact-us)  
- [License](#license)    

## What is GTX.Zip？<span id="intro"></span>

GTX.Zip(or GTZ for short) is a professional fastq/bam compressor and also can be used as a universal data compression software, developed by GTXLab of Genetalks Inc. GTX.Zip can rapidly compress any DNA sequencing files and directories with very high compression rate, and generate a single compressed data files, thus facilitating the data storage, distribution and transmission. Different from other compression tools, GTX.Zip system focuses on **high compression rate, high speed, and convenient data extraction**. 
- **[GTX.Zip Professional](#install)** is a stand-alone version which supports local compression service. GTX.Zip Professional runs by command lines for compression and decompression of local genomic data.If you want get other GTX.Zip product, come [here](#product).  
  
[-Back to Top-](#index)  
  
--------    
  
## Products<span id="product"></span>
  
Product | Version | Description | How to Get
----|---- | -------- | --------
**GTX.Zip Professional**|V1.0.1|Companies, Institutions and individual users that with large local sequencing data|[Install](#install)
**GTX.Zip Enterprise**|V1.0.1|Large-scale enterprises and data centers that with PB-level sequencing data and require distributed compression by their own computing clusters|[Contact Us](#contact-us)
**GTX.Zip Cloud**|V1.0.1|Companies that with large amounts of sequencing data distribution and storage in the cloud| http://gtz.io
  
[-Back to Top-](#index)  
  
--------  
  
## Supported Bioinformatic Analysis Softwares<span id="supported-softwares"></span>
  
[BWA 0.7 for GTX.Zip](#bwa) is the  the most widely used software package for mapping DNA sequences that can input XXX.gtz file. It consists of two softwares : bwa 0.7 and bwa-opt 0.7.   
bwa-opt 0.7 is the optimized version that is about 30% faster than standard bwa, and its mapping results are completely consistent with those of standard bwa.       
  
[-Back to Top-](#index)  
  
--------  

## Feature<span id="feature"></span>

GTX.Zip compressor system features:
- **High Compression Ratio**: The system implements Context Model compression technology, with a variety of optimized predicting model, and balancing the system concurrent and memory resources consumption, thus achieving a extreme high compression rate. For FASTQ files, GTX.Zip is capable to compress the original fastq file to 2.53%. The compression rate of GTX.Zip is about 3-6 times of gzip compressor which could save up to 80% storage space and transfer costs.

 Data List|Compression rate of GTX.Zip|Compression rate of Fastq.gz
 ---|:--:|---:
 Nova_wes_1.fq|2.53%|17.15%
 Nova_wes_2.fq|3.45%|18.34%
 nova_wgs_1.fq|3.18%|17.55%
 nova_wgs_2.fq|3.93%|18.66%
 nova_rna_1.fq|4.56%|17.70%
 nova_rna_2.fq|5.39%|18.94%

- **High Performance**: GTX.Zip fully exploits the concurrency of the CPU, the new Haswell CPU architecture, and the computing power of the new instructions such as AVX2, BMI2, which makes GTX.Zip gain high compression speed even on a ordinary computing server, with the throughput of 1100MB/s for a single compression node. GTX.Zip Enterprise supports large-scale distributed compression.

- **Safety Guarantee**: Thanks to its high speed, during the process of GTX.Zip compression, the data decompression and restore test is performed. The compression process will be done only after the data has been confirmed exactly the same as the source data. MD5 validation is performed to ensure data integrity as well.

- **Software Ecology**: GTX.Zip provides command line and GUI decompression software for Linux, Mac OSX and Windows. It also provides SDK interfaces in languages such as Python, C, C++, etc. which is convenient for third-party developers to read and write gtz file (GTX.Zip compression format) directly. For example, gtz version of bcl2fastq, fastp and BWA are supported by community now.   
If you want to get these softwares, please go to [-GTZ Ecology Softwares-](#ecology).    
- **Nirvana Plan**:   
As an enterprise-level software, GTX.Zip has developed a nirvana program for high-availability requirements to ensure that users can decompress compressed data into original data under the extreme condition. The nirvana plan's dual availability protection strategy is as follows:
	-  GTX.Zip is multi-site hosted. http://gtz.io website, GitHub and other sites will permanently host all versions of GTX.Zip, to make sure that it is available to the entire network all the time and free of charge at any time.
	-  To ensure that compressed data can be restored to original file under any conditions, pre-embedded micro decompression programs could be extract from compressed data first, and then be used to decompress the file.
	-  Please click [-here-](nirvana-example) for usage.   
    
[-Back to Top-](#index)  
  
--------  

## System Environment Requirements<span id="environment"></span>
- **64-bit Linux system (CentOS >= 6.5；Ubuntu >= 12.04， < 18.04)**                                                                                                                            
- To achieve good performance, the computing server with **32-core 64GB** memory is recommended (**at least 4-core and 8GB memory**), or that has the same configuration with the **AWS C4.8xlarge** machine)
  
## How to Install？ <span id="install"></span>	
- **For installation you can (recommended)**  

	`sudo curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`
	
- **Or**  
	Download the [gtz_latest.run](https://gtz.io/gtz_latest.run), and then execute it.   
  
- **Verify installation**    
	run  
	
	`gtz -v`  
	
	If software version information appears, the installation is successful.    
	  
	    
[-Back to Top-](#index)  
  
--------  

## Quick Start <span id="quick-start"></span>	
GTX.Zip Professional needs to be installed on the current machine. If not, please see [-How to Install-](#install) .

1. **Make bin file to enable high rate compression**
   Take the human sample species as an example, make the index file (*bin* file) required for GTX.Zip high rate compression
   
   - Download the 1th *rbin* file ("1" is the number of the human *rbin* file in the gtx_index list) and gtz_index will save it to the default path (~/.config/gtz):
   
      `gtz_index download 1`
      
      or
      
      You can download *rbin* file from  here ( [Homo_sapiens rbin file](https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin) )

   - Make the *bin* file ( may need 100GB free disk space, and >28GB memory, and 10 mins)
   
     `gtz_index makeindex ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin`  
     
     ><font size=1>\*  **bin file**：The index file used for hight compression.The default file path is："\~/.config/gtz/"</font>    
     ><font size=1>\*  **rbin file**：The compact index file used for decompression.The default file  path is："\~/.config/gtz/"</font>  

2. **Compress sample fastq file**

    `gtz  sample.fq -o  sample.fq.gtz --bin-file  ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin` 
 
    sample.fq can be downloaded from https://gtz.io/sample.fq. (2GB fastq file, extracted from a real WES data produced by Novaseq)  
    > \*gtz can also directly compress fastq.gz file.
  
      
[-Back to Top-](#index)  
  
--------  
## Usage <span id="usage"></span>    
### gtz:
```  
usage: gtz [-h] [-o OUT] [-b INDEX_BIN] [-d DECOMPRESS] [-O OUT_DIR]  

-h, --help                                      show this help message and exit  
-o OUT, --out OUT                               specify the GTZ file name after compression  
-b BIN_FILE, --bin-file BIN_FILE                specify the bin file name for high compression  
-d DECOMPRESS, --decompress DECOMPRESS          decompress  
-O OUT_DIR, --out-dir OUT_DIR                   specify the save path of the extracted file 
-c, --stdout                                    decompress to terminal
-z, --fastq-to-fastq-gz                         decompress fastq to fastq.gz, it's valid only for FASTQ
-r RBIN_PATH, --rbin-path RBIN_PATH             specify the path where the rbin file resides  
-p PARALLEL_NUM,--parallel			specify parallel number for compression or decompression, 
						default equal CPU logical cores
-f, --force                                     force overwrite of output file  
-e, --no-keep                                   don't keep input files  
-v, --version                                   display version number  
```

### gtz_index：  
```
gtz_index <command> [options]
	list					show species which current support
	download <index> <path_to>		download species reference sequence rbin file , path_to is not necessary.  
	makeindex <rbin_path>			making reference sequence  
```

### Nirvana Plan<span id="nirvana-example"></span>  
Let’s start Nirvana plan!
At first, we have a gtz file named sample.fq.gtz.    
```
Step 1:  
Run the following command to extract the embeded programe gtz_reborn to current directory:  
	sed -e 's/\[GTZ_REBORN_BEGIN\]/\n&/;' sample.fq.gtz | sed -n '/\[GTZ_REBORN_BEGIN\]/,/\[GTZ_REBORN_END\]/p' | sed -e 's/.*\[GTZ_REBORN_BEGIN\]//g' -e 's/\[GTZ_REBORN_END\].*//g' | tar -zxvf -

Step2:  
If sample.fq.gtz is a high compression file, download the corresponding fasta file according to the prompt, and then extract the file.  
If sample.fq.gtz is not a high compression file, the FASTQ file can be extracted directly  
	./gtz_reborn -d sample.fq.gtz  
	
```  
    
[-Back to Top-](#index)  
  
--------  

## For Example: <span id="example"></span>
### Compress  
```
1:Compress the sample.fq to the current directory.
	gtz sample.fq    

2:Compress the file sample.fq into the out folder of the current directory.
	gtz sample.fq -o ./out/sample.fq.gtz    

***If the species is not specified by the '--bin-file' , GTZ will automatically recognize the species to compress.  ***  

3.GTZ performs high compression by specifying bin files in the Homo folder under the current directory.  
	gtz sample.fq --bin-file ./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin  
```

### Decompress  
```
1.Deompress the file sample.fq to the current directory.If there is no species rbin file under "\~/.config/ gtz/", GTZ will be automatically downloaded from the Cloud to "\~/.config/ gtz /".  
	gtz -d sample.fq.gtz 

2.Specify the directory of the rbin path “~/Homo” for decompress sample.fq.gtz.  
	gtz -d sample.fq.gtz --rbin-path ~/Homo 

3.Decompress sample.fq.gtz to the Homo folder in the current path  
	gtz -d sample.fq.gtz --out-dir ./Homo    
```

## gtz_index  
```
Interaction mode:  
	gtz_index  
	
Show supported species and you can gradually create bin files through human-machine interaction mode.  

Manual mode  
1:Show supported species list，the index number is the input of the gtz_index download command.  
	gtz_index list  
	
2:Download the rbin file in the species list with No.1 index  
	gtz_index download 1  
	
3:Make BIN,rec file by specifying the rbin file". /Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin "  
	gtz_index makeindex ./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin  
	
```


[-Back to Top-](#index)  
  
--------    
  
## Rbin files Download <span id="rbin-download"></span> 

No. | Species | Official Url
----|-------- | -------------
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
37|Homo sapiens methylation|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Homo_sapiens_meth_d497f0f9f716dff930ae92146c950576.rbin
38|Mus musculus methylation|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Mus_musculus_meth_42a6bd57204889412125be9111bca783.rbin  
39|Equus caballus|https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Equus_caballus_48fb76cc859b80aff9818361dce3e735.rbin  

**If the species you need is not in our [species list](#rbin-download) , please [contact us](#contact-us) !**    
  
    
[-Back to Top-](#index)  
  
--------  

## Ecology Softwares<span id="ecology"></span>
## 1、BWA for gtz <span id="bwa"></span>  

- **How to Install?**

	##### For installation you can (recommended)  
	  
	`sudo curl -sSL https://gtz.io/bwagtz_latest.run -o /tmp/bwagtz.run && sudo sh /tmp/bwagtz.run`    
	  
	##### or 
	download installation files：[-GTX.Zip bwa-gtz-]( https://gtz.io/bwagtz_latest.run )  
	Run commands in the installation file directory   
	  
	`sudo sh bwagtz_lastest.run`  
	  
	complete installation according to prompt. 
	
- **How to Use?**

	GTX.Zip's support package for BWA includes bwa-gtz and bwa-opt-gtz, both of which are based on version 0.7.17 of bwa.
	Among them: the two versions have added the ability to read GTZ files directly, and the functions are completely consistent with the main code functions of bwa.
	bwa-opt-gtz also optimizes the structure of BWA lookup table, which can save more than one third of the time without changing the results of comparison. Due to some changes in the data structure of the lookup table, bwa-opt-gtz is incompatible with the index file data generated by the original bwa. According to the standard steps of bwa, first regenerate the index file, and then compare it with bwa-opt-gtz.

	The difference between bwa-gtz and bwa-opt-gtz is as follows:

	(1) bwa-gtz can directly use index produced by official website BWA, and its performance is consistent with official website BWA.

	(2) bwa-opt-gtz can not directly use the index produced by BWA on official website. index needs to be reproduced by bwa-opt-gtz, but its performance will be improved by 1/3 than that of BWA on official website.
	

	#### Use examples

	#### bwa-gtz

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bwa-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -o aln-pe.sam`

	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up the processing of bwa-gtz. Because when bwa-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, and the download process will consume time.</font>
	

	#### bwa-opt-gtz

	##### Step one: Remake index (must)

	`bwa-opt-gtz index ref.fa`

	##### Step two: execution comparison

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bwa-opt-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	
- **performance**

	
	In the case of sufficient server resources, the performance of bwa-opt-gtz is 1/3 better than that of official bwa. The following is a set of test data in the same environment (the number of specified threads is 4):
	
	#####	Test command
	
	`bwa mem ref.fa read1.fq.gz read2.fq.gz -t 4 -o aln-pe.sam`
	
	`bwa-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	`bwa-opt-gtz mem ref.fa read1.fq.gtz read2.fq.gtz -t 4 -o aln-pe.sam`
	
	#####	Test environment
	
	Server configuration: 16 core CPU, 64G memory; file size: read1.fq.gz(1.8G), read2.fq.gz(1.8G), read1.fq.gtz(0.3G), read2.fq.gtz(0.3G)
	
	#####	performance data
	
	Software  |bwa|bwa-gtz|bwa-opt-gtz
	---|:---:|:--:|---:
 	Time consumption|50m14.06s|51m37.67s|39m18.86s
	Memory consumption|5.888G|10.56G|19.84G

  
[-Back to Top-](#index)  
  
--------  
    
## Change Log  


#### 1.2.2 - 2018/11/09
mainly optimize the loading speed of index files, the compression speed will be significantly improved
  
#### 1.2.1
fix : validation maybe be slow sometimes

fix : when decompressed with -c, -e does not work  

#### 1.2
fix : GTZ load slowly sometimes

fix : GTZ cann't be quit by Ctrl+C sometimes  

#### 1.1
add function:

-c/--stdout                   decompress to terminal

-z/--fastq-to-fastq-gz        decompress fastq to fastq.gz, it's valid only for FASTQ

#### 1.0
base revision


    
## FAQ<span id="faq"></span>  
Frequently Asked Questions are intended to help newcomers to understand how we work! [-Click here！-](https://github.com/Genetalks/gtz/blob/master/FAQ_chs.md "Markdown")  

## Contact Us<span id="contact-us"></span> 

If you have any questions, feel free to contact: contact@gtz.io, or  create [a new GitHub issue](https://github.com/Genetalks/gtz/issues/new) .  
  
[-Back to Top-](#index)  
  
--------  
  
## License<span id="license"></span>  

See [LICENSE](https://github.com/Genetalks/gtz/blob/master/License.md) for details.
