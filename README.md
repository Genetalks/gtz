# GTX.Zip Professional Version   

[中文说明](https://github.com/Genetalks/gtz/blob/master/README_chs.md "Markdown").
<table style="width:100%">
<tr>
	<td>
		<h3>QQ group(s): 934492381 </h3>
		<img src="https://i.loli.net/2018/12/10/5c0df947eddde.png" alt="GTX.Zip QQ groups"/>
	</td>
	<td>
		<h3>WeChat group(s):</h3>
		<img src="https://i.loli.net/2018/12/10/5c0e0afa8d12d.jpg" alt="GTX.Zip WebChat groups"/>
	</td>
</tr>
</table>


Powered by GTXLab of Genetalks.  


## Index<span id="index"></span>
- [What is GTX.Zip?](#intro)  
- [Product Series](#product-series)  
- [Supported Bioinformatic Analysis Softwares](#supported-softwares)  
- [Feature](#feature)    
- [Environment Requirements](#environment)  
- [How to Install?](#install)
- [Let's Do It!](#quick-start)
- [Usage](#usage)
- [GTZ Ecology Softwares](#ecology)  
- [Change Log](#change-log) 
- [FAQ](#faq)  
- [Contact Us](#contact-us)  
- [License](#license)    

## What is GTX.Zip？<span id="intro"></span>

GTX.Zip(or GTZ for short) is a professional fastq/bam compressor and also can be used as a universal data compression software, developed by GTXLab of Genetalks Inc. GTX.Zip can rapidly compress any DNA sequencing files and directories with very high compression rate, and generate a single compressed data files, thus facilitating the data storage, distribution and transmission. Different from other compression tools, GTX.Zip system focuses on **high compression rate, high speed, and convenient data extraction**. 
- **[GTX.Zip Professional](#install)** is a stand-alone version which supports local compression service. GTX.Zip Professional runs by command lines for compression and decompression of local genomic data.  
  
[-Back to Top-](#index)  
  
--------    
  
## Product Series<span id="product-series"></span>
  
Product | Version | Description | How to Get
----|---- | -------- | --------
**GTX.Zip Professional**|V2.0.0|Companies, Institutions and individual users that with large local sequencing data|[Install](#install)
**GTX.Zip Enterprise**|V1.0.1|Large-scale enterprises and data centers that with PB-level sequencing data and require distributed compression by their own computing clusters|[Contact Us](#contact-us)
**GTX.Zip Cloud**|V1.0.1|Companies that with large amounts of sequencing data distribution and storage in the cloud| http://gtz.io
  
[-Back to Top-](#index)  
  
--------  
  
## Supported Bioinformatic Analysis Softwares<span id="supported-softwares"></span>
  
- **[BWA 0.7 for GTX.Zip](#bwa)** is the  the most widely used software package for mapping DNA sequences that can input XXX.gtz file directly. It consists of two softwares : bwa 0.7 and bwa-opt 0.7.   
	- bwa-opt 0.7 is the optimized version that is about 30% faster than standard bwa, and its mapping results are completely consistent with those of standard bwa.       
- **[BOWTIE](#bowtie) / [BOWTIE2 for GTX.Zip](#bowtie2)** is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It can input XXX.gtz file directly, and You can use this tool as if you are using the official version.  
	- BOWTIE for GTX.Zip based on BOWTIE 1.2.2 version.  
	- BOWTIE2 for GTX.Zip based on BOWTIE2 2.3.4.3 version. 

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
- **64-bit Linux system (CentOS >= 6.1；Ubuntu >= 12.04， < 18.04)**                                                                                                                            
- To achieve good performance, the computing server with **32-core 64GB** memory is recommended, or that has the same configuration with the **AWS C4.8xlarge** machine)
  
## How to Install？<span id="install"></span>  
- **Way one**
##### Install directly from the command line (recommended installation method)  

If you only want to use it for the current user after installation, perform the 

`curl -SL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sh /tmp/gtz.run && source ~/.bashrc`  

If you want all users to be able to use it after installation, do 

`sudo curl -SL https://gtz.io/gtz_latest.run -o /tmp/gtz.run && sudo sh /tmp/gtz.run`



- **Way two**  
##### Download the software first then install it 

First download the software from [-GTX.Zip Professional-]( https://gtz.io/gtz_latest.run ).

If you only want to use it for the current user after installation, perform the 

`sh gtz_latest.run && source ~/.bashrc`

If you want all users to be able to use it after installation, do 

`sudo sh gtz_latest.run`

- **Verify that the installation was successful**

Running the following command, the corresponding software version information appears, indicates that the installation was successful  

`gtz -v`      
	  
	    
[-Back to Top-](#index)  
  
--------  

## Quick Start <span id="quick-start"></span>	
GTX.Zip Professional needs to be installed on the current machine. If not, please see [-How to Install-](#install) .

**1. Download samples file to be compressed**	  
Sample Download: [-sample.fq-](https://gtz.io/sample.fq)  
>  <font size=1>\* 2GB fastq file, extracted from a real WES data produced by Novaseq</font>

Reference genome Download: [-GCF_000001405.37_GRCh38.p11_genomic.fna.gz-](https://gtz.io/GCF_000001405.37_GRCh38.p11_genomic.fna.gz)
 
**2. Start compression**	  

 `gtz sample.fq --ref GCF_000001405.37_GRCh38.p11_genomic.fna.gz`  
>  <font size=1>\* gtz can also directly compress fastq.gz file</font>

**3、decompress**

`gtz -d sample.fq.gtz`


## How to use:

### Feature description:

<table style="width:100%">
<tr>
	<td>
		<img src="https://i.loli.net/2019/05/07/5cd14cc9ba4cb.png">
	</td>
<tr>
<tr>
<tr>
	<td>
		<img src="https://i.loli.net/2019/05/07/5cd14cc9e6f08.png">
	</td>
<tr>
<tr>
<tr>
	<td>
		<img src="https://i.loli.net/2019/05/07/5cd14cc9dabac.png">
	</td>
</tr>
</table>

### Parameter description:
```  
   --ref <string>
     @ compress : specifies Fasta corresponding to the compressed file,
     which results in a higher compression rate

     @ decompress : if compression uses Fasta and parameter
     --donot-pack-ref is used, the corresponding Fasta needs to be
     specified by this parameter when decompressing

   -z,  --fastq-to-fastq-gz
     @ compress : do not use

     @ decompress : decompress fastq to fastq.gz, it's valid only for
     FASTQ

   --cache-path <string>
     @ compress : when Fasta is specified by --ref, GTZ converts the Fasta
     to the corresponding binary file and then caches it to the default
     path, so that when the same Fasta is specified for compression, GTZ
     can read directly data from cache path, which is relatively fast.
     default cache path is /home/xuxl/.config/gtz, you can use this
     parameter to change it

     @ decompress : same as compress

   --donot-pack-ref
     @ compress : this option is not recommended. By default, when
     compression uses Fasta, GTZ extracts data from the Fasta and then
     compresses it to the GTZ file, so that the resulting GTZ file is no
     longer required Fasta when decompressed. use this option or not, the
     compression rate has a low impact, but if you use this option, you
     need to specify the corresponding Fasta when decompressing

     @ decompress : do not use

   --verify
     @ compress : after data compression, decompress the generated GTZ file
     again to ensure that the generated GTZ file must be decompressed.
     Usually it's not necessary, but if it's used for archiving, you can
     use this parameter.

     @ decompress : do not use

   -l <number>,  --level <number>
     @ compress : [1-5] is fast compress mode, at present, 1-5 compression
     algorithm is same, here is for later expansion. 6 is default. [6-9] is
     best compress level, compression algorithm is also the same, here is
     for later expansion

     @ decompress : do not use

   -r <string>,  --rbin-path <string>
     @ compress : do not use

     @ decompress : use only for version less than 2.0.0, mainly for
     compatibility with older versions. when compression specifies the BIN
     file, You can use this parameter to specify the corresponding RBIN
     file or the directory in which the RBIN file is located to
     decompress.

   -O <string>,  --out-dir <string>
     @ compress : do not use

     @ decompress : specify the save directory of decompression file

   -f,  --force
     @ compress : force overwrite of output file

     @ decompress : same as compress

   -c,  --stdout
     @ compress : do not use

     @ decompress : decompression output to terminal

   -d,  --decompress
     @ compress : do not use

     @ decompress : specify the GTZ file to decompress

   -p <number>,  --parallel <number>
     @ compress : specify parallel number, default is CPU logical cores

     @ decompress : same as compress

   -o <string>,  --out <string>
     @ compress : specify output GTZ file name                 

     @ decompress : do not use

   -e,  --no-keep
     @ compress : don't keep input files                 

     @ decompress : do not use

   --version
     Displays version information and exits.

   -h,  --help
     Displays usage information and exits.

   <file name>
     input file name


   GTX Lab Compressor
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
  


## Ecology Softwares<span id="ecology"></span>  
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


## 1、BWA for GTZ <span id="bwa"></span>  

- **How to Install?**

	##### For installation you can (recommended)  
	  
	`sudo curl -SL https://gtz.io/bwagtz_latest.run -o /tmp/bwagtz.run && sudo sh /tmp/bwagtz.run`    
	  
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
	
## 2、BCL2FASTQ for GTZ <span id="bcl2fastq"></span>

- **How to Install?**
    
    ##### Mode one: Install to the current user, no sudo permissions required
    For installation you can (recommended) 
    
    `curl -SL https://gtz.io/bcl2fastq_gtz_latest.run -o /tmp/bcl2fastqgtz.run && sh /tmp/bcl2fastqgtz.run`  
	
    After the first installation, you need to perform a source ~/.bashrc or exit to log back in, and then you can execute bcl2fastq-gtz in any directory
    
    ###### or
    download installation files：[-GTX.Zip bcl2fastq-gtz-]( https://gtz.io/bcl2fastq_gtz_latest.run )，then install
    
    `sh bcl2fastq_gtz_latest.run`
	
    Similarly, after the first installation, you need to perform a source ~/.bashrc or exit and log back in again
        
    ##### Mode two: Install to all users, need sudo permissions
    For installation you can (recommended)   
    
	`sudo curl -SL https://gtz.io/bcl2fastq_gtz_latest.run -o /tmp/bcl2fastqgtz.run && sudo sh /tmp/bcl2fastqgtz.run`  
	
    ###### or
    download installation files：[-GTX.Zip bcl2fastq-gtz-]( https://gtz.io/bcl2fastq_gtz_latest.run )，then install 
    
	`sudo sh bcl2fastq_gtz_latest.run`
	
	After the installation is complete, you can perform bcl2fastq-gtz in any directory


- **How to Use?**


    Gtx. Zip's support package for bcl2fastq, based on the v2.20.0.422 version of bcl2fastq.

    Default output gtz format, output gz format when command use --no-bgtzf-compression parameter
    
    #### Example 1. by default, the output result file is in gtz format, taking normal compression
	
	`bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`

	#### Example 2. output result file is gtz format, go high compression, specify bin file by --bin_file
	
	`bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* --bin_file Homo_sapiens_bcacac9064331276504f27c6cf40e580.bin >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`
           
    #### Example 3. output result file is gz format, use --no-bgtzf-compression parameter
        
    `bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* --no-bgtzf-compression >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`

- **performance**

	
	#####	Test command

	`bcl2fastq -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`

	`bcl2fastq-gtz -i ./data/BaseCalls -R ./outdir/run --interop-dir ./outdir/interop -o ./outdir/result --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --barcode-mismatches 0 --use-bases-mask y*,i7,i7,y* >./outdir/bcl2fastq.log 2>&1 || touch bcl2fastq.err`


	#####	Testing environment

	Server configuration: 16 core CPU, 64G memory; file size: ./data/BaseCalls total size 40G

	#####	Performance data

	bcl2fastq output destination folder total size 40G，bcl2fastq-gtz output destination folder total size 16G
	
## 3、STAR for GTZ <span id="star"></span> 

  The official website STAR directly supports the GTZ format, after the installation of GTZ and STAR,

- **First step**

	make the index file with STAR

	`STAR --runMode genomeGenerate --genomeDir /path/to/genomeDir --genomeFastaFiles /path/xxx.fasta`

	Detailed reference to the official website documents:

	https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf

- **Second Step**

	perform the mapping operation. an example as follows:

	##### method one

    export GTZ_RBIN_PATH=/path/rbin/
    
    STAR --genomeDir /path/to/genomeDir --readFilesIn read1.fq.gtz read2.fq.gtz --readFilesCommand gtz -c -d

    >  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up GTZ processing. Because when GTZ needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, and the download process will consume time.</font>

	##### method two

    STAR --genomeDir /path/to/genomeDir --readFilesIn read1.fq.gtz read2.fq.gtz --readFilesCommand gtz -r /path/to/gtz_rbin_dir/ -c -d

    >  <font size=1>\* In this example, the directory where the RBIN file is located is specified by -r, it's same as method one.</font>

## 4、BOWTIE for GTZ <span id="bowtie"></span>  

- **How to Install?**

	##### For installation you can (recommended)  
	
	`sudo curl -SL https://gtz.io/bowtiegtz_latest.run -o /tmp/bowtiegtz.run && sudo sh /tmp/bowtiegtz.run`  
	##### or 
	download installation files：[-GTX.Zip bowtie-gtz-]( https://gtz.io/bowtiegtz_latest.run )  
	Run commands in the installation file directory 
	
	`sudo sh bowtiegtz_latest.run`  
	complete installation according to prompt.  
	
- **How to Use?**

    After installation, three executable programs of bowtie-gtz, bowtie-build-gtz and bowtie-inspect-gtz will be generated.
    If y is selected when installing "create a soft link to /usr/bin", the above executable program can be run directly in any directory;
    Otherwise, you need to switch to the installation directory and run with ./bowtie-gtz.
    
	GTX.Zip's support package for bowtie based on 1.2.2 version.
	Bowtie-gtz can directly use the index produced by bowtie on the official website. You can use bowtie-build or bowtie-build-gtz to make the index. 
	Of course, bowtie-inspect-gtz and bowtie-inspect functions are exactly the same.

	#### Use examples


	##### Step one: make index

	`bowtie-build-gtz ref.fa ref_index`

	##### Step two: execution comparison

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bowtie-gtz -S ref_index reads.fq.gtz eg.sam`

	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, it is recommended that you specify it to speed up bowtie-gtz processing. Because when bowtie-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, which will take time to download.。</font>
	

	
- **performance**

	
 	
## 5、BOWTIE2 for GTZ <span id="bowtie2"></span>  

- **How to Install?**

	##### For installation you can (recommended)   
	
	`sudo curl -SL https://gtz.io/bowtie2gtz_latest.run -o /tmp/bowtie2gtz.run && sudo sh /tmp/bowtie2gtz.run`  
	##### or  
	download installation files：[-GTX.Zip bowtie2-gtz-]( https://gtz.io/bowtie2gtz_latest.run )  
	Run commands in the installation file directory  
	
	`sudo sh bowtie2gtz_latest.run`  
	complete installation according to prompt.   
	
- **How to Use?**

    After installation, three executable programs of bowtie2-gtz, bowtie2-build-gtz and bowtie2-inspect-gtz will be generated.
    If y is selected when installing "create a soft link to /usr/bin", the above executable program can be run directly in any directory;
    Otherwise, you need to switch to the installation directory and run with ./bowtie2-gtz.
    
	GTX.Zip's support package for bowtie2 based on 2.3.4.3 version.
	Bowtie2-gtz can directly use the index produced by bowtie2 on the official website. You can use bowtie2-build or bowtie2-build-gtz to make the index. 
	Of course, bowtie2-inspect-gtz and bowtie2-inspect functions are exactly the same.

	#### Use examples


	##### Step one: make index

	`bowtie2-build-gtz ref.fa ref_index`

	##### Step two: execution comparison

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bowtie2-gtz -x ref_index -1 reads_1.fq.gtz -2 reads_2.fq.gtz -S eg2.sam -p 4 --reorder`

	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up bowtie2-gtz processing. Because, when bowtie2-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, and the download process will consume time.。</font>
	

	
- **performance**

	
	#####	Test command
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`bowtie2 -x ref_index -1 reads_1.fq.gz -2 reads_2.fq.gz -S eg2.sam -p 4 --reorder`
	
	`bowtie2-gtz -x ref_index -1 reads_1.fq.gtz -2 reads_2.fq.gtz -S eg2.sam -p 4 --reorder`
	
	#####	Test environment
	
	Server configuration: 16 core CPU, 64G memory; file size: read1.fq.gz(1.55G), read2.fq.gz(1.78G), read1.fq.gtz(0.43G), read2.fq.gtz(0.61G)
	
	#####	performance data
	
	Software  |bowtie2|bowtie2-gtz
	:---:|:---:|:--:
	CPU consumption(average)|400|445
	Memory consumption(average)|0.19G|12.92G
 	Time consumption|63m41.06s|61m56.67s
	
	
## 6、TOPHAT for GTZ <span id="tophat"></span>  

- **How to Install?**

	##### For installation you can (recommended)   
	
	`sudo curl -SL https://gtz.io/tophatgtz_latest.run -o /tmp/tophatgtz.run && sudo sh /tmp/tophatgtz.run`  
	##### or 
	download installation files：[-GTX.Zip tophat-gtz-]( https://gtz.io/tophatgtz_latest.run )  
	Run commands in the installation file directory 
	
	`sudo sh tophatgtz_latest.run`  
	complete installation according to prompt.
	
- **How to Use?**

    After installation, you can run tophat-gtz directly without any other dependencies.（If bowtie/bowtie2 is not installed in the environment, it will be installed automatically when tophat installing.）
    
    If y is selected when installing "create a soft link to /usr/bin", you can run tophat-gtz in any directory; Otherwise, you need to switch to the installation directory and run with ./tophat-gtz.
    
    GTX.Zip's support package for tophat based on 2.1.2 version. Among them: the ability to read GTZ files directly is added, and all functions are completely consistent with the main code function of tophat.

	#### Use examples


	##### Step one: use bowtie/bowtie2 (bowtie2-gtz) to make index.

	`bowtie2-build ref.fa ref_index`
	
	>  <font size=1>\* Note: It is recommended that bowtie 2/bowtie 2-gtz be used to produce index, because for bowtie, tophat can only use bowtie 1.1.2 and previous versions.</font>

	##### Step two: execution comparison

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`tophat-gtz -o report_dir ref_index reads_1.fq.gtz reads_2.fq.gtz`

	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up the processing of tophat-gtz. Because when tophat-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, which will consume time.</font>
	
	
- **performance**

	
	#####	Test command
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`tophat -o report_dir -p 4 ref_index reads_1.fq.gz reads_2.fq.gz`
	
	`tophat-gtz -o report_dir -p 4 ref_index reads_1.fq.gtz reads_2.fq.gtz`
	
	
	#####	Testing environment
	
	Server configuration: 16 core CPU, 64G memory; file size: read1.fq.gz(1.55G), read2.fq.gz(1.78G), read1.fq.gtz(0.43G), read2.fq.gtz(0.61G)
	
	#####	Performance data
	
	Software  |tophat|tophat-gtz
	:---:|:---:|:--:
 	Time consumption|133m12.61s|134m43.02s
	
## 7、HISAT2 for GTZ <span id="hisat2"></span>  
- **How to Install?**
    
    ##### Mode one: Install to the current user, no sudo permissions required
    
    For installation you can (recommended)  
	
    `curl -SL https://gtz.io/hisat2gtz_latest.run -o /tmp/hisat2gtz.run && sh /tmp/hisat2gtz.run`  
		
    After the first installation, you need to perform a source ~/.bashrc or exit to log back in, and then you can execute minimap2-gtz in any directory.
    
    ###### or
    
    download installation files：[-GTX.Zip hisat2-gtz-]( https://gtz.io/hisat2gtz_latest.run ),then install:
    
    `sh hisat2gtz_latest.run` 

    Similarly, after the first installation, you need to perform a source ~/.bashrc or exit and log back in again

    ##### Mode two: Install to all users, need sudo permissions
    
    For installation you can (recommended)  
   
   `sudo curl -SL https://gtz.io/hisat2gtz_latest.run -o /tmp/hisat2gtz.run && sudo sh /tmp/hisat2gtz.run`  

    ###### or
    
    download installation files：[-GTX.Zip hisat2-gtz-]( https://gtz.io/hisat2gtz_latest.run )
    
    `sudo sh hisat2gtz_latest.run` 
    
    After the installation is complete, you can perform hisat2-gtz and hisat2-build in any directory	


- **How to Use?**

    After the installation is complete, the execution program and related scripts will be generated in the installation directory,such as hisat2-gtz,hisat2-build,etc.

    GTX.Zip support package for hisat2, based on hisat2 (2.1.0) version, which: Added direct reading capability for gtz files, all functions are exactly the same as hisat2 main code function.
    
    #### Use examplesgtz
	##### Step one: use hisat2-build to make index.

	`hisat2-build -p 4 ~/GCF_000001405.37_GRCh38.p11_genomic.fna genome`
	
	##### Step two: execution comparison

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`hisat2-gtz -x genome -1　reads_1.fq.gtz -2 reads_2.fq.gtz -S result.sam`

	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up the processing of hisat2-gtz. Because when hisat2-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, which will consume time.</font>
	
- **performance**
	#####	Test command
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`hisat2 -x genome -1 reads_1.fq.gz -2 reads_2.fq.gz -S gz.sam -p 16 --reorder`
	
	`hisat2-gtz -x genome -1 reads_1.fq.gtz -2 reads_2.fq.gtz -S gtz.sam -p 16 --reorder`
	
	
	#####	Testing environment
	
	Server configuration: 16 core CPU, 64G memory; file size: read1.fq.gz(7.3G), read2.fq.gz(7.3G), read1.fq.gtz(1.6G), read2.fq.gtz(1.8G)
	
	#####	Performance data
	
	Software  |hisat2|hisat2-gtz
	:---:|:---:|:--:
 	Time consumption|8m25.845s|10m47.930s
	
	
## 8、MEGAHIT for GTZ <span id="megahit"></span>  

- **How to Install?**

	##### For installation you can (recommended)   
		`sudo curl -SL https://gtz.io/megahitgtz_latest.run -o /tmp/megahitgtz.run && sudo sh /tmp/megahitgtz.run`  
	##### or 
	download installation files：[-GTX.Zip megahit-gtz-]( https://gtz.io/megahitgtz_latest.run )  
	Run commands in the installation file directory 
	`sudo sh megahitgtz_latest.run`  
	complete installation according to prompt.
	
- **How to Use?**

    After installation, megahit-gtz (and megahit_asm_core, megahit_sdbg_build, megahit_toolkit) will be generated.
    
    If y is selected when installing "create a soft link to /usr/bin", you can run megahit-gtz in any directory; Otherwise, you need to switch to the installation directory and run with ./megahit-gtz.
    
    GTX.Zip's support package for megahit based on 1.1.3 version. Among them: the ability to read GTZ files directly is added, and all functions are completely consistent with the main code function of megahit.

	#### Use examples


	##### Example 1: support fq

	`megahit-gtz -1 pe1.fq -2 pe2.fq -o out`
	

	##### Example 2: support gtz

	`export GTZ_RBIN_PATH=/path/rbin/`
    
    `megahit-gtz -1 pe1.fq.gtz -2 pe2.fq.gtz -o out`

	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up the processing of megahit-gtz. Because when megahit-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, which will consume time.</font>
	
	
- **performance**

	
	#####	Test command
	
	`megahit -t 16 -o out -1 pe1.fq.gz -2 pe2.fq.gz`
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`megahit-gtz -t 16 -o out -1 pe1.fq.gtz -2 pe2.fq.gtz`
	
	
	#####	Testing environment
	
	Server configuration: 16 core CPU, 64G memory; file size: read1.fq.gz(1.55G), read2.fq.gz(1.78G), read1.fq.gtz(0.43G), read2.fq.gtz(0.61G)
	
	#####	Performance data
	
	Software  |megahit|megahit-gtz
	:---:|:---:|:--:
 	Time consumption|67m38.381s|66m44.151s
	
## 9、FASTQC for GTZ <span id="fastqc"></span>  
- **How to Install?**

    ##### Mode one: Install to the current user, no sudo permissions required
    For installation you can (recommended)  
    
    `curl -SL https://gtz.io/fastqc_gtz_latest.run -o /tmp/fastqc2gtz.run &&  sh /tmp/fastqc2gtz.run`  

    After the first installation, you need to perform a source ~/.bashrc or exit to log back in, and then you can execute minimap2-gtz in any directory.
    
     ###### or
    download installation files：[-GTX.Zip fastqc-gtz-]( https://gtz.io/fastqc_gtz_latest.run ) ，
    
    then install
    
    `sh fastqc_gtz_latest.run`  
	
    Similarly, after the first installation, you need to perform a source ~/.bashrc or exit and log back in again
        
    ##### Mode two: Install to all users, need sudo permissions
    
    For installation you can (recommended) 
    
    `sudo curl -SL https://gtz.io/fastqc_gtz_latest.run -o /tmp/fastqc2gtz.run && sudo sh /tmp/fastqc2gtz.run`

    ###### or
    
    download installation files： [-GTX.Zip fastqc-gtz-]( https://gtz.io/fastqc_gtz_latest.run ) ，then install  
    
    
    `sudo sh fastqc_gtz_latest.run`  
	
    After the installation is complete, you can perform fastqc-gtz in any directory	

- **How to Use?**

    After the installation is complete, the execution program and related scripts will be generated in the installation directory.
    GTX.Zip support package for fastqc, based on fastqc (0.11.8) version, which: Added direct reading capability for gtz files, all functions are exactly the same as fastqc main code function.
    
    #### Use examples

	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`fastqc-gtz -t 1 reads_1.fq.gtz -o ~/result_directory`

	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up the processing of fastqc-gtz. Because when fastqc-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, which will consume time.</font>
    
  
## 10、FASTP for GTZ <span id="fastp"></span>

- **How to Install?**
    
    ##### Mode one: Install to the current user, no sudo permissions required
    For installation you can (recommended)  
    
    `curl -SL https://gtz.io/fastpgtz_latest.run -o /tmp/fastpgtz.run && sh /tmp/fastpgtz.run`  
	
    After the first installation, you need to perform a source ~/.bashrc or exit to log back in, and then you can execute fastp-gtz in any directory
    
    ###### or
    download installation files：[-GTX.Zip fastp-gtz-]( https://gtz.io/fastpgtz_latest.run )，then install
    
    `sh fastpgtz_latest.run`
	
    Similarly, after the first installation, you need to perform a source ~/.bashrc or exit and log back in again
        
    ##### Mode two: Install to all users, need sudo permissions
    For installation you can (recommended)  
    
	`sudo curl -SL https://gtz.io/fastpgtz_latest.run -o /tmp/fastpgtz.run && sudo sh /tmp/fastpgtz.run`  
	
    ###### or
    download installation files：[-GTX.Zip fastp-gtz-]( https://gtz.io/fastpgtz_latest.run )，then install  
    
	`sudo sh fastpgtz_latest.run`
	
	After the installation is complete, you can perform fastp-gtz in any directory


- **How to Use?**


    Gtx. Zip to fastp in the support package, based on FASTP version 0.19.5.
    Both input and output support GTZ and non-GTZ format files, and when the output file name ends with the .gtz, fastp-gtz compresses the output file GTZ
    
    #### 1. Input is not GTZ format
        
	examples:

	Output GTZ Format:  
	
	`fastp-gtz -i in.fq -o out.fq.gtz --bin_file in.fq.species.bin`

	Output non-GTZ format: 
	
	`fastp-gtz -i in.fq -o out.fq`

	For --bin_file use, refer to the following sections for instructions
    
    #### 2. Input is GTZ format
    
	examples:

	export GTZ_RBIN_PATH=/path/rbin/

	fastp-gtz -i in.R1.fq.gtz -I in.R2.fq.gtz -o out.R1.fq.gtz -O out.R2.fq.gtz --bin_file in.fq.species.bin


	Command Description:

	1) export GTZ_RBIN_PATH=/path/rbin/
	  The environment variable is recommended for setting, but is not required, to specify the search path for the Rbin file when reading the file as a high-magnification compressed GTZ file, with detailed readable working principles

	2) --bin_file
	  This parameter is recommended to specify, but is not required, to specify the two-ended read into the file belongs to the species corresponding to the bin file, specified when the FASTP-GTZ will be high magnification to compress the output result file, detailed readable working principle


  ###### How it works:

	When entered as a GTZ file, FASTP-GTZ can be briefly described as four procedures:
	
	    (A) read into In.gtz-> (B) unzip into In.fq-> (C) processing Data-> (D) compressed into IN.GTZ

	Note
	##### 1) Process B

	   If IN.GTZ in Process A is a high-magnification compressed file, procedure B requires the corresponding Rbin file, and there are two ways to work:
	   Mode one: 
	       You have the Rbin file locally and specify the path of the file with the following environment variables: 
	       
		   export GTZ_RBIN_PATH=/path/rbin
	       Then the program will complete step b using the local Rbin file
	   Mode two:
	       You do not have the Rbin file locally, or you do not specify it through an environment variable, in which case the program automatically downloads the rbin from the network, and of course the process consumes a certain amount of time

	##### 2) Process C

	    fastp-gtz Analysis Data

	##### 3) Process D

	   Mode one: 
	       Bin file not specified through--bin_file
	       The fastp-gtz automatically recognizes in based on the bin and rec files under the ~/.config/gtz/path. Which species R1.fq.gtz and in.R2.fq.gtz each belong to, and then use the bin file of the corresponding species for compression, the automatic identification process will consume a certain amount of time.
	       Of course, if there is no bin and rec under ~/.config/gtz/or no species information is identified, normal compression is used
	   Mode two:
	       The bin file is specified by--bin_file, fastp-gtz the bin file is used to do the high magnification compression directly
           
        
- **performance**

	
	#####	Test command

	`fastp -i in.R1.fq.gz -I in.R2.fq.gz -o out.R1.fq.gz -O out.R2.fq.gz`

	`export GTZ_RBIN_PATH=/path/rbin/`

	`fastp-gtz -i in.R1.fq.gtz -I in.R2.fq.gtz -o out.R1.fq.gtz -O out.R2.fq.gtz --bin_file in.fq.species.bin`


	#####	Testing environment

	Server configuration: 16 core CPU, 64G memory; file size: in.R1.fq.gz(1.55G), in.R2.fq.gz(1.78G), in.R1.fq.gtz(0.43G), in.R2.fq.gtz(0.61G)

	#####	Performance data

	fastp total output file size of R1.fq.gz and out.R2.fq.gz is 3.3G, and the fastp-gtz total output file size of R1.fq.gtz and out.R2.fq.gtz is 1G
	
## 11、MINIMAP2 for GTZ <span id="minimap2"></span>

- **How to Install?**
    
    ##### Mode one: Install to the current user, no sudo permissions required
    For installation you can (recommended)  
    
    `curl -SL https://gtz.io/minimap2_gtz_latest.run -o /tmp/minimap2_gtz_latest.run && sh /tmp/minimap2_gtz_latest.run`  
	
    After the first installation, you need to perform a source ~/.bashrc or exit to log back in, and then you can execute minimap2-gtz in any directory
    
    ###### or
    download installation files：[-GTX.Zip minimap2-gtz-]( https://gtz.io/minimap2_gtz_latest.run )，then install
    
    `sh minimap2_gtz_latest.run`
	
    Similarly, after the first installation, you need to perform a source ~/.bashrc or exit and log back in again
        
    ##### Mode two: Install to all users, need sudo permissions
    For installation you can (recommended)  
    
	`sudo curl -SL https://gtz.io/minimap2_gtz_latest.run -o /tmp/minimap2_gtz_latest.run && sudo sh /tmp/minimap2_gtz_latest.run`  
	
    ###### or
    download installation files：[-GTX.Zip minimap2-gtz-]( https://gtz.io/minimap2_gtz_latest.run )，then install  
    
	`sudo sh minimap2_gtz_latest.run`
	
	After the installation is complete, you can perform minimap2-gtz in any directory	
	
	
   - **How to Use?**

    After installation, minimap2-gtz will be generated.
    
    ### Use examples
	`export GTZ_RBIN_PATH=/path/rbin/`
    
   	`minimap2-gtz -ax asm20 ref.fa pacbio-ccs.fq.gtz > aln.sam`
        
	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up the processing of minimap2-gtz. Because when minimap2-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, which will consume time.</font>
	
	#### Test command
	
	`minimap2 -t 16 -a Arab.mmi Arab_E822-R02-I_good_1.fq.gz > Arab_p.sam`
	
	`export GTZ_RBIN_PATH=/path/rbin/`
	
	`minimap2-gtz -t 16 -a Arab.mmi Arab_E822-R02-I_good_1.fq.gz.gtz > Arab_gtz_p.sam`
		
	#### Testing environment
	
	Server configuration: 16 core CPU, 64G memory; 
	
	#### Performance data
	
	Software  |minimap2|minimap2-gtz
	:---:|:---:|:--:
 	Time consumption|2m57s|3m57.151s
	
	
## 12、WTDBG2 for GTZ <span id="wtdbg2"></span>
- **How to Install?**
    
    ##### Mode one: Install to the current user, no sudo permissions required
    For installation you can (recommended)  
    
    `curl -SL https://gtz.io/wtdbg2_gtz_latest.run -o /tmp/wtdbg2_gtz_latest.run && sh /tmp/wtdbg2_gtz_latest.run`  
	
    After the first installation, you need to perform a source ~/.bashrc or exit to log back in, and then you can execute wtdbg2-gtz in any directory
    
    ###### or
    download installation files：[-GTX.Zip wtdbg2-gtz-]( https://gtz.io/wtdbg2_gtz_latest.run )，then install
    
    `sh wtdbg2_gtz_latest.run`
	
    Similarly, after the first installation, you need to perform a source ~/.bashrc or exit and log back in again
        
    ##### Mode two: Install to all users, need sudo permissions
    For installation you can (recommended)  
    
	`sudo curl -SL https://gtz.io/wtdbg2_gtz_latest.run -o /tmp/wtdbg2_gtz_latest.run && sudo sh /tmp/wtdbg2_gtz_latest.run`  
	
    ###### or
    download installation files：[-GTX.Zip wtdbg2-gtz-]( https://gtz.io/wtdbg2_gtz_latest.run )，then install  
    
	`sudo sh wtdbg2_gtz_latest.run`
	
	After the installation is complete, you can perform wtdbg2-gtz in any directory	
	
	
   - **How to Use?**

    After installation, wtdbg2-gtz will be generated.
    
    ### Use examples
	`export GTZ_RBIN_PATH=/path/rbin/`
    
   	`wtdbg2-gtz -x rs -g 4.6m -t 16 -i wtdbg2_test.fastq.gtz -fo prefix`
	
	`wtpoa-cns -t 16 -i prefix.ctg.lay.gz -fo prefix.ctg.fa`
        
	>  <font size=1>\* In this example, the path of the RBIN file is specified by the environment variable GTZ_RBIN_PATH, where "export GTZ_RBIN_PATH=/path/rbin/" is not necessary, but if you know the path of rbin, you are advised to specify it, which can speed up the processing of wtdbg2-gtz. Because when wtdbg2-gtz needs RBIN file and cannot find the RBIN file under the default path ~/.config/gtz, it will be downloaded through the network, which will consume time.</font>
	
  
[-Back to Top-](#index)  
  
--------  
    
## Change Log  


Current Latest Version：gtz-2.0.0 [2019/05/08]

historical version: [-Change Log-](https://github.com/Genetalks/gtz/blob/master/Changelog.md "Markdown")


    
## FAQ<span id="faq"></span>  
Frequently Asked Questions are intended to help newcomers to understand how we work! [-Click here！-](https://github.com/Genetalks/gtz/blob/master/FAQ_chs.md "Markdown")  

## Contact Us<span id="contact-us"></span> 

If you have any questions, feel free to contact: contact@gtz.io, or  create [a new GitHub issue](https://github.com/Genetalks/gtz/issues/new) .  
  
[-Back to Top-](#index)  
  
--------  
  
## License<span id="license"></span>  

See [LICENSE](https://github.com/Genetalks/gtz/blob/master/License.md) for details.
