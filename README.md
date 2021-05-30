# Shared biologic architecture between Parkinson’s disease and inflammatory disorders

## Relevance

Parkinson's disease (PD) is the second most common neurodegenerative disease, pathologically characterized by progressive degeneration of dopaminergic neurons in the compact part of the substantia nigra. 

The disease etiology is associated with a complex interaction between genetic and environmental factors. There is now compelling evidence that inflammation and immunity play an important role in the pathogenesis of Parkinson's disease, and comorbidity between it and autoimmune diseases has been reported. 

But it is not known exactly what led to this association. Therefore, we used various methods to understand the possible cause.

## Project goals and objectives

The aim of this project was to search for a common genetic architecture and specific common markers between diseases, using data from summary statistics of genome-wide association studies.

### Tasks:
 - Сollect  GWAS summary statistics on diseases necessary for analysis
 - Process and filter summary statistics
 - Find pleiotropy loci common in this statistics using PLEIO and MTAG
 - Filter the found loci and leave only significant and new ones
 - Visualize results
 - Evaluate the influence of the found loci on the development of diseases

## System requirements

For running PLEIO and MTAG we used a server with following parameters:
 - Ubuntu 20.04
 - 20 Gb RAM
 - 4 Cores & 8 Thread

Other scripts (python and R) are not demanding on machine resources and can be run on any local computer.

## Data availability 

 Disease | Publication | Year | Journal | N cases | N controls | Sample size | GWAS link
 | ------------- |:-------------:| -----:| --------:| -------:| -------:| -------:| -------:|
 Parkinson's disease | [Article](https://pubmed.ncbi.nlm.nih.gov/31701892/) | 2019 | Lancet | | |  482730 | [zip archive](https://drive.google.com/file/d/1FZ9UL99LAqyWnyNBxxlx6qOUlfAnublN/view)
 Celiac disease  | [Article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2847618/) | 2010 | Nature Genetics | 4 533 | 10 750 | 15 283 | [FTP](ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/DuboisPC_20190752_GCST000612)
 Rheumatoid arthritis | [Article](https://pubmed.ncbi.nlm.nih.gov/23143596/) | 2012 | Nature Genetics | 13 838 | 33 742 | 47 580 | [FTP](ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/DuboisPC_20190752_GCST000612)
 Multiple sclerosis  | [Article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3182531/) | 2013 | Nature Genetics | 14 498 | 24 091 | 38582 | [FTP](ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/BeechamAH_24076602_GCST005531)
 Psoriasis  | [Article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510312/) | 2012 | Nature Genetics | 10 588 | 22 806 | 33 394 | [FTP](ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/TsoiLC_23143594_GCST005527)
 Primary biliary cirrhosis  | [Article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4580981/) | 2015 | Nature Communications | 2 764 | 10 475 | 13 239 | [FTP](ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/CordellHJ_26394269_GCST003129)
Systemic lupus erythematosus | [Article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5977506/) | 2018 | Arthritis Research & Therapy | 4 943 | 8 483 | 16966 | [FTP](ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/JuliaA_29848360_GCST005831/)
Asthma | [Article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7160128/) | 2017 | Nature Genetics | 19 954 | 107 715 | 127 669 | [FTP](ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/ZhuZ_31619474_GCST008916)

All preprocessed data are available at [GoogleDrive](https://drive.google.com/drive/folders/1e9-xojOVwFFCbkxXdi2v6ShzJvlQgtNX?usp=sharing)

## Materials and methods

1. GWAS summary statistics were preprocessed using python [data_prep.py]() sript. 
2. Parkinson's disease summary statistics had only chromosomal coordinates so we used `join` bash command to map it with [RSids]() of 1000 Genomes project.
