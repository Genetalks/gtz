### gtz-3.0.0 [2020/12/15]

1. Support high-ratio compression of three generations of gene data (PacBio/Nanopore)

2. Fixed a known issue

### gtz-2.1.4 [2020/07/02]

Important fixes:

sometimes, it maybe takes multiple times to succeed decompress a gtz packet to FASTQ.gz format, but it work normally when decompress to FASTQ format

### gtz-2.1.3 [2020/03/16]

Optimised some features.

### gtz-2.1.2 [2019/11/13]

Fix issue:

1. Cannot compress the fastq.gz files with very special format

2. Cannot run on a server for a specific cpu type

### gtz-2.1.1 [2019/09/16]

1. fix a known issue

### gtz-2.1.0 [2019/08/21]

1. Support for bam compression

2. When compressing fastq.gz files, performance is more than doubled

3. Fixes previous version feedback some issues that fasta can't handle

4. When you unzip the gtz of the fastq format into gz format, you can modify the compression level of the gz format by -l/-level

### gtz-2.0.1 [2019/05/23]

fix: an abnormal problem of GTZ decompression in very special cases

### gtz-2.0.0 [2019/05/08]
1. No longer need to make bin, direct use --ref designated species Fasta (fast)

2. By default, after the pressurized use of the reference genome, decompression is no longer required unless --donot-pack-ref is used

3. Parameters with speed and compression level added (-l 0~9)

### gtz-1.2.3 [2019/01/24]

The main changes are as follows:
1. Improved performance of compressed gz file and decompression into gz file

2. fix: gtz can not run on some specific CPU models
3. fix: progress bar displays more than 100% when compressing a gz format file

4. add: -s parameter for automatic species recognition when compressed. which invalidates when -b specifies a bin file
5. add: --bin-path parameter, use to specify the directory in which the bin file resides when automatic species recognition is turned on. If the bin default path (~/.CONFIG/GTZ) is not modified, you can not specify



### gtz-1.2.2 [2018/11/09]

Mainly optimize the loading speed of index files, the compression speed will be significantly improved



### gtz-1.2.1 [2018/10/30]

1. fix: gtz will be slow in some cases when verify data after the compression is completed

2. fix: -e not working when decompression is done with -c



### gtz-1.2 [2018/10/25]

1. fix gtz sometimes loads slowly

2. fix gtz sometimes cannot be exited when input ctrl+c



### gtz-1.1 [2018/10/16]

Add Features:

1. -c/--stdout, decompress to Terminal

2. -z/--fastq-to-fastq-gz, decompress fastq to gz format, which is valid only for fastq



### gtz-1.0 [2018/10/11]

Basic revisions
