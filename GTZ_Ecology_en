# GTX.Zip 生态圈    
- [1、BWA Support](#1)  
 
-----------------------------------------
**1、BWA Support**<span id="1"></span>  
## bwa support<span id="bwa-support"></span>

- **How to Install?**

	##### For installation you can (recommended)  
	  
	`sudo curl -sSL https://gtz.io/bwagtz_latest.run -o /tmp/bwagtz.run && sudo sh /tmp/bwagtz.run`    
	  
	##### or 
	download installation files：[-GTX.Zip bwa-gtz-]( https://gtz.io/bwagtz_latest.run )  
	Run commands in the installation file directory   
	  
	`sudo sh bwagtz_lastest.run`  
	  
	complete installation according to prompt. 
	
- **How to Use?**

	bwa-gtz is based on the modification of version 0.7.17 of bwa official website. It supports GTZ format data on the  basis of bwa. At the same time, its performance is 1/3 times higher than that of BWA official website.
	bwa-gtz other functions and modes of use are exactly the same as those of official website bwa. Examples are as follows:
	
	official network bwa  
	  
	`bwa mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq nova_wes_2.fq -t 4 -o nova_wes.sam`  

	bwa-gtz  
	   
	`bwa-gtz mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq nova_wes_2.fq -t 4 -o nova_wes.sam`  
	`bwa-gtz mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq.gtz nova_wes_2.fq.gtz -t 4 -o nova_wes.sam`   
	  
	
	
	>\*1) When bwa-gtz processes data in GTZ format, we recommend that you specify the path of the RBIN file 
	>through the following environment variables, because when bwa-gtz processes data in GTZ format，If you 
	>need RBIN files,It only searches the corresponding RBIN files from ～/.config/gtz， In the case of not 
	>found, then drag the corresponding RBIN from the network, download will take a certain amount of time.  
	>**How to set environment variables:**  
	>    `export GTZ_RBIN_PATH=/path/rbin`  
	>    
	>\*2) When using bwa-gtz, all index must be remade, and index can not be directly used by official website BWA.
	
	
- **performance**

	In the case of sufficient server resources, the performance of bwa-gtz will be 1/3 better than that of official bwa. Here is a set of test data in the same environment (the number of specified threads is 4):
	
	official website bwa, takes 50 minutes.

	`bwa mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq nova_wes_2.fq -t 4 -o nova_wes.sam`

	bwa-gtz，takes 34 minutes.

	`bwa-gtz mem GCF_000001405.37_GRCh38.p11_genomic.fna nova_wes_1.fq.gtz nova_wes_2.fq.gtz -t 4 -o nova_wes.sam`
	
	
- **Best practice**  


