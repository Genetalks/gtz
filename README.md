# GTX.Zip Professional Version

Powered by GTXLab of Genetalks.  
- One-click installation:  
	`sudo curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`

- GTX.Zip Professional download URL:https://gtz.io/gtz_latest.run

[中文说明](https://github.com/Genetalks/gtz/blob/master/README_chs.md "Markdown").

## System Overview

GTX.Zip is a professional fastq/bam compressor and also can be used as a universal data compression software, developed by GTXLab of Genetalks Inc. GTX.Zip can rapidly compress any DNA sequencing files and directories with very high compression rate, and generate a single compressed data files, thus facilitating the data storage, distribution and transmission. Different from other compression tools, GTX.Zip system focuses on **high compression rate, high speed, and convenient data extraction**. 

There are three different versions of GTX.Zip for different users:
- **GTX.Zip Professional**：Companies, Institutions and individual users that with large local sequencing data
- **GTX.Zip Enterprise**：Large-scale enterprises and data centers that with PB-level sequencing data and require distributed compression by their own computing clusters
- **GTX.Zip Cloud**：Companies that with low efficiency of sequencing data distribution and storage





## System Highlights

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

- **Software Ecology**: GTX.Zip provides command line and GUI decompression software for Linux, Mac OSX and Windows. It also provides SDK interfaces in languages such as Python, C, C++, etc. which is convenient for third-party developers to read and write gtz file (GTX.Zip compression format) directly. For example, gtz version of bcl2fastq, fastp and BWA are supported by community now. More software will be released soon.  
## Nirvana Plan
As an enterprise-level software, GTX.Zip has developed a nirvana program for high-availability requirements to ensure that users can decompress compressed data into original data under the extreme condition. The nirvana plan's dual availability protection strategy is as follows:
-  GTX.Zip is multi-site hosted. http://gtz.io website, GitHub and other sites will permanently host all versions of GTX.Zip, to make sure that it is available to the entire network all the time and free of charge at any time.
-  To ensure that compressed data can be restored to original file under any conditions, pre-embedded micro decompression programs could be extract from compressed data first, and then be used to decompress the file.



## GTX.Zip Professional
- GTX.Zip Professional is a stand-alone version which supports local compression service. GTX.Zip Professional runs by command lines for compression and decompression of local genomic data.

## System Environment Requirements
- **64-bit Linux system (CentOS 6.5 or above, or Ubuntu 12.04 or above)**                                                                                                                            
- To achieve good performance, the computing server with **32-core 64GB** memory is recommended (**at least 4-core and 8GB memory**), or that has the same configuration with the **AWS C4.8xlarge** machine)

## Quick Start	

1. **Install GTX.Zip**
   - Method 1(recommended)
   
	`sudo curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`
	
   - Method 2：
   
	Download from:
	
    	https://gtz.io/gtz_latest.run
	
	Change permissions:
	
    	chmod +x ./gtz_latest.run
	
	Install:
	
    	./gtz_latest.run
2. **Make index to enable high rate compression**
   Take the human sample species as an example, make the index file (bin file) required for GTX.Zip high rate compression
   
   - Download the 1th rbin file (1 is the number of the human RBIN file in the appendix list) and gtz_index will save it to the default path (~/.config/gtz):
   
      `gtz_index download 1`
      
      or
      
      You can download rbin file from  here ( [Homo_sapiens rbin file](https://gtzdata.oss-cn-hangzhou.aliyuncs.com/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin) )

   - Make the index bin file ( may need 100GB free disk space, and >28GB memory, and 10 sec)
   
     `gtz_index makeindex ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin`

3. **Compress sample fastq file**

    `gtz  sample.fq -o  sample.fq.gtz --bin-file  ~/.config/gtz/Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin` 
 
    sample.fq can be downloaded from https://gtz.io/sample.fq. (1GB fastq file, extracted from a real WES data produced by Novaseq)
  
    [^] Notice: gtz can also directly compress fastq.gz file.


## Installation Instruction	
- Method 1 (recommended):  
	`sudo curl -sSL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`

- Method 2:  
	Download the [gtz_latest.run](https://gtz.io/gtz_latest.run), and then execute the it. 


## Guidelines Of gtz:
```  
usage: gtz [-h] [-o OUT] [-b INDEX_BIN] [-d DECOMPRESS] [-O OUT_DIR]  

-h, --help                                      show this help message and exit  
-o OUT, --out OUT                               specify the GTZ file name after compression  
-b BIN_FILE, --bin-file BIN_FILE                specify the bin file name for high compression  
-d DECOMPRESS, --decompress DECOMPRESS          decompress  
-O OUT_DIR, --out-dir OUT_DIR                   specify the save path of the extracted file 
-c, --stdout                                    decompress to terminal
-gz, --fastq-to-fastq-gz                        decompress fastq to fastq.gz, it's valid only for FASTQ
-r RBIN_PATH, --rbin-path RBIN_PATH             specify the path where the rbin file resides  
-p PARALLEL_NUM,--parallel			specify parallel number for compression or decompression, 
						default equal CPU logical cores
-f, --force                                     force overwrite of output file  
-e, --no-keep                                   don't keep input files  
-v, --version                                   display version number  
```

## Guidelines Of gtz_index：  
```
gtz_index <command> [options]
-	list					show species which current support
-	download <index> <path_to>		download species reference sequence rbin file , path_to is not necessary.
-	makeindex <rbin_path>			making reference sequence  
```

## For Example:
### Compress  
1:Compress the sample.fq to the current directory.Without the specified bin file, GTZ will automatically recognize the species to compress.  
	`gtz sample.fq -o sample.fq.gtz `   

2:Compress the file sample.fq into the out folder of the current directory.Without the specified bin file, GTZ will automatically recognize the species to compress.  
	`gtz sample.fq -o ./out/sample.fq.gtz `   

3.GTZ performs high compression by specifying bin files in the Homo folder under the current directory.  
	`gtz sample.fq -o sample.fq.gtz --index-bin ./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin`  

### Decompress
1.Deompress the file sample.fq to the current directory.If there is no species rbin file under "\~/.config/ gtz/", GTZ will be automatically downloaded from the Cloud to "\~/.config/ gtz /".  
	`gtz -d sample.fq.gtz` 

2.Specify the directory of the rbin path “~/Homo” for decompress sample.fq.gtz.  
	`gtz -d sample.fq.gtz --index-path ~/Homo` 

3.Decompress sample.fq.gtz to the Homo folder in the current path  
	`gtz -d sample.fq.gtz --out-dir ./Homo`  

## gtz_index
Interaction mode:  
	`gtz_index`  
Show supported species and you can gradually create bin files through human-machine interaction mode.  

Manual mode  
1:Show supported species list，the index number is the input of the gtz_index download command.  
	`gtz_index list`  
2:Download the rbin file in the species list with No.1 index  
	`gtz_index download 1`  
3:Make BIN,rec file by specifying the rbin file". /Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin "  
	`gtz_index makeindex ./Homo/Homo_sapiens_bcacac9064331276504f27c6cf40e580.rbin`


## Nirvana Plan  
Let’s start Nirvana plan!At first, we have a gtz file named sample.fq.gtz.  
Step 1:  
Run the following command to extract the embeded programe gtz_reborn to current directory:  
	`sed -e 's/\[GTZ_REBORN_BEGIN\]/\n&/;' sample.fq.gtz | sed -n '/\[GTZ_REBORN_BEGIN\]/,/\[GTZ_REBORN_END\]/p' | sed -e 's/.*\[GTZ_REBORN_BEGIN\]//g' -e 's/\[GTZ_REBORN_END\].*//g' | tar -zxvf -`

Step2:  
If sample.fq.gtz is a high compression file, download the corresponding fasta file according to the prompt, and then extract the file.  
If sample.fq.gtz is not a high compression file, the FASTQ file can be extracted directly  
	`./gtz_reborn -d sample.fq.gtz`

## Note:
- **bin files**:Genome reference index files which used for compression.The default file storage path is "~/.config/gtz/"
- **rbin files**:Compact genome reference files which used for decompression.The default file storage path is "~/.config/gtz/"
- **gtz_index**:An installation tool of GTX.Zip Professional which used to view species list, download rbin files and generate bin files. 

## Rbin files Download 

No. | Species | Official Url
----|-------- | -------------
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

## Change Log

### v1.0
base revision

### v1.1
add function:
-c, --stdout                   decompress to terminal
-gz, --fastq-to-fastq-gz       decompress fastq to fastq.gz, it's valid only for FASTQ

## Contact Us

If you have any questions, feel free to contact: contact@gtz.io, or commit an issus on Github.

