# GTX.Zip Compressor Compressor Professional Version

Powered by GTXLab of Genetalks.

- One-click installation:
	**sudo curl -sSL https://gtzdata.oss-cn-hangzhou.aliyuncs.com/install_gtz_latest.run -o /tmp/install_gtz_latest.run && sudo sh /tmp/install_gtz_latest.run**

[中文说明](https://github.com/Genetalks/gtz/blob/master/README_chs.md "Markdown").

## System Overview

GTX.Zip is a professional fastq/bam compressor and also can be used as a universal data compression software, developed by GTXLab of Genetalks Inc. GTX.Zip can rapidly compress any DNA sequencing files and directories with very high compression rate, and generate a single compressed data files, thus facilitating the data storage, distribution and transmission. Different from other compression tools, GTX.Zip system focuses on **high compression rate, high speed, and convenient data extraction**. 

There are three different versions of GTX.Zip for different users:
- **GTX.Zip Professional**：Companies, Institutions and individual users that with large local sequencing data
- **GTX.Zip Enterprise**：Large-scale enterprises and data centers that with PB-level sequencing data and require distributed compression by their own computing clusters
- **GTX.Zip Cloud**：Companies that with low efficiency of sequencing data distribution and storage


## Nirvana plan
As an enterprise-level software, GTX.Zip has developed a nirvana program for high-availability requirements to ensure that users can decompress compressed data into original data under the extreme condition. The nirvana plan's dual availability protection strategy is as follows:
-  GTX.Zip is multi-site hosted. http://gtz.io website, GitHub and other sites will permanently host all versions of GTX.Zip, to make sure that it is available to the entire network all the time and free of charge at any time.
-  To ensure that compressed data can be restored to original file under any conditions, pre-embedded micro decompression programs could be extract from compressed data first, and then be used to decompress the file.


## System highlights

GTX.Zip compressor system features:
- **High compression ratio**: The system implements Context Model compression technology, with a variety of optimized predicting model, and balancing the system concurrent and memory resources consumption, thus achieving a extreme high compression rate. For FASTQ files, GTX.Zip is capable to compress the original fastq file to 2.53%. The compression rate of GTX.Zip is about 3-6 times of gzip compressor which could save up to 80% storage space and transfer costs.

 Data List|Compression rate of GTX.Zip|Compression rate of Fastq.gz
 ---|:--:|---:
 Nova_wes_1.fq|2.53%|17.15%
 Nova_wes_2.fq|3.45%|18.34%
 nova_wgs_1.fq|3.18%|17.55%
 nova_wgs_2.fq|3.93%|18.66%
 nova_rna_1.fq|4.56%|17.70%
 nova_rna_2.fq|5.39%|18.94%

- **High performance**: GTX.Zip fully exploits the concurrency of the CPU, the new Haswell CPU architecture, and the computing power of the new instructions such as AVX2, BMI2, which makes GTX.Zip gain high compression speed even on a ordinary computing server, with the throughput of 1100MB/s for a single compression node. GTX.Zip Enterprise supports large-scale distributed compression.

- **Safety Guarantee**: Thanks to its high speed, during the process of GTX.Zip compression, the data decompression and restore test is performed. The compression process will be done only after the data has been confirmed exactly the same as the source data. MD5 validation is performed to ensure data integrity as well.

- **Software ecology**: GTX.Zip provides command line and GUI decompression software for Linux, Mac OSX and Windows. It also provides SDK interfaces in languages such as Python, C, C++, etc. which is convenient for third-party developers to read and write gtz file (GTX.Zip compression format) directly. For example, gtz version of bcl2fastq, fastp and BWA are supported by community now. More software will be released soon.

## Note:
- **bin files**:Genome reference index files which used for compression.Size range: 5.3~37G.Human: 14G
- **rbin files**:Compact genome reference files which used for decompression.Size range: 0.041G~3.6G.  Human: 0.7G
- **gtz_index**:An installation tool of GTX.Zip Professional which used to view species list, download rbin files and generate bin files. 
- **BIN,RBIN**:The default file storage path is "~/.config/gtz/"

## GTX.Zip Professional version
- GTX.Zip Professional is a stand-alone version which supports local compression service. GTX.Zip Professional runs by command lines for compression and decompression of local genomic data.

## System environment requirements
- **64-bit Linux system (CentOS 6.5 or above, or Ubuntu 12.04 or above)**                                                                                                                            
- To achieve good performance, the computing server with **32-core 64GB** memory is recommended (**at least 4-core and 8GB memory**), or that has the same configuration with the **AWS C4.8xlarge** machine)

## Installation Instruction  
	sudo curl -sSL https://gtzdata.oss-cn-hangzhou.aliyuncs.com/install_gtz_latest.run -o /tmp/install_gtz_latest.run && sudo sh /tmp/install_gtz_latest.run


## Guidelines of gtz:
usage: gtz [-h] [-o OUT] [-b INDEX_BIN] [-d DECOMPRESS] [-O OUT_DIR]

-	 -h, --help&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;show this help message and exit
-	 -o OUT,--out OUT&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specify the GTZ file name after compression
-	 -b BIN_FILE,--bin-file BIN_FILE&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specify the BIN file for high compression
-	 -d DECOMPRESS, --decompress DECOMPRESS&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;decompress
-	 -O OUT_DIR,--out-dir OUT_DIR&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specify the save path of the extracted file
-	 -r RBIN_PATH,--rbin-path RBIN_PATH&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specify the path where the RBIN file resides
-	 -f, --force&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;force overwrite of output file
-	 -k, --keep&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;keep (don't delete) input files
-	 -v, --version&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;display version number

## Guidelines f gtz_index：
gtz_index <command> [options]
-	list&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;show species which current support
-	download <index> <path_to>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;download species reference sequence rbin file , path_to is not necessary.
-	make <rbin_path>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;making reference sequence

## For Example:
### compress
    1 ./gtz Arab_E822-R02-I_good_1.fq -o Arab_E822-R02-I_good_1.fq.gz.gtz 
    Compress the file arab_e822-r02-i_good_1.fq to the current directory.Without the specified BIN file, GTZ will automatically recognize the species to compress.

    2./gtz Arab_E822-R02-I_good_1.fq -o ./out/Arab_E822-R02-I_good_1.fq.gz.gtz 
    Compress the file arab_e822-r02-i_good_1.fq into the out folder of the current directory.Without the specified BIN file, GTZ will automatically recognize the species to compress.

    3./gtz Arab_E822-R02-I_good_1.fq -o Arab_E822-R02-I_good_1.fq.gz.gtz --bin-file ./Arab/Arabidopsis_thaliana_3dcb9b7a5a8b46c8ebbdbbdb3e0fa233.bin
    GTZ performs high compression by specifying BIN files in the Arab folder under the current directory.

### Decompress
    1./gtz -d Arab_E822-R02-I_good_1.fq.gz.gtz
    Deompress the file arab_e822-r02-i_good_1.fq to the current directory.If there is no species RBIN file under "~/.config/ gtz/", GTZ will be automatically downloaded from the Cloud to "~/.config/ gtz /".

    2./gtz -d Arab_E822-R02-I_good_1.fq.gz.gtz --rbin-path ~/Arab
    Specify the directory of the rbin path “~/Ara” for decompress Arab_E822-R02-I_good_1.fq.gz.gtz.

    3./gtz -d Arab_E822-R02-I_good_1.fq.gz.gtz -outdir ./Arab
    Decompress Arab_e822-r02-i_good_1.fq.gz.gtz to the Arab folder in the current path

## gtz_index
    Interaction mode:
	./gtz_index
	Show supported species and you can gradually create bin files through human-machine interaction mode.

	Manual mode
	1./gtz_index list
	Show supported species list，the index number is the input of the gtz_index download command.

	2./gtz_index download 3
	Download the RBIN file in the species list with No.3 index .

	3、./gtz_index makeindex ./Arab/Arabidopsis_thaliana_3dcb9b7a5a8b46c8ebbdbbdb3e0fa233.rbin
	Make BIN,rec file by specifying the rbin file". / Arab/Arabidopsis_thaliana_3dcb9b7a5a8b46c8ebbdbbdb3e0fa233 rbin "

## Nirvana plan
	Let’s start Nirvana plan!At first, we have a gtz file named nova_rna_1.fq.gtz.
	Step 1:
	Run the following command to extract the embeded programe gtz_reborn to current directory:
	sed -e 's/\[GTZ_REBORN_BEGIN\]/\n&/;' nova_rna_1_head.fq.gtz　| sed -n '/\[GTZ_REBORN_BEGIN\]/,/\[GTZ_REBORN_END\]/p' | sed -e 's/.*\[GTZ_REBORN_BEGIN\]//g' -e 's/\[GTZ_REBORN_END\].*//g' | tar -zxvf -
	Step2:
	Run ./gtz_reborn -d nova_rna_1.fq.gtz
	If nova_rna_1.fq.gtz is a high compression file, download the corresponding fasta file according to the prompt, and then extract the file.
	If nova_rna_1.fq.gtz is not a high compression file, the FASTQ file can be extracted directly

## contact us

	If you have any questions, feel free to contact: gtz@genetalks.com, or commit an issus on Github.

