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
 | ------------- |:-----------:| -----:| ------:| -------:| -------:| -------:| -------:|
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

1. GWAS summary statistics were preprocessed using python [data_prep.py](https://github.com/Kate-Cher/Parkinson-s-disease-and-inflammatory-disorders/blob/main/prep_python_scripts/data_prep.py) sript. 
2. Parkinson's disease summary statistics had only chromosomal coordinates so we used `join` bash command to map it with [RSids](https://drive.google.com/file/d/1XkS8wpTmoBCEjnbm3ksdGT0s-5tIh9ot/view?usp=sharing) of 1000 Genomes project.
3. Prepared GWAS summary statistics were also processed using [munge_sumstats.py](https://github.com/bulik/ldsc/blob/master/munge_sumstats.py) python script from [ldsc](https://github.com/bulik/ldsc) package to make [PLEIO](https://github.com/cuelee/pleio) scripts work with following command: `python munge_sumstats.py --sumstats <file_path> --N <sample_size> --N-cas <N_cases> --N-con <N_controls> --out <output_path> --snp variant_id`
4. Genetic correlation, environmental covariance matrices and merged input for PLEIO were prepared using [ldsc_preprocess](https://github.com/cuelee/pleio/blob/master/ldsc_preprocess) from `PLEIO` 
```bash
python ./pleio --metain path/to/meta_input \ 
  --sg path/to/env_corr_matrix \ 
  --ce path/to/gen_cov_matrix \ 
  --nis 100000 \ 
  --parallel \ 
  --create \ 
  --out output/path
```
5. Results can be found at [output](https://github.com/Kate-Cher/Parkinson-s-disease-and-inflammatory-disorders/blob/main/results/output.txt)
6. Preprocessed data were used to run [MTAG](https://github.com/JonJala/mtag) script as following: 
```bash
python mtag.py --sumstats path/to/input_list \
--use_beta_se \
--out ./path_to_output \ 
--stream_stdout \ 
--force
```
7. [Intersection script](https://github.com/Kate-Cher/Parkinson-s-disease-and-inflammatory-disorders/blob/main/prep_python_scripts/intersect.py) is used to identify differences in found snips from PLEIO and MTAG results. No differences were found.
8. One of the significant coding snips from PLEIO result was rendered using [PleiotropyPlot](https://github.com/cuelee/pleiotropyPlot) package with [pleio_PD_plot.R](https://github.com/Kate-Cher/Parkinson-s-disease-and-inflammatory-disorders/blob/main/pleiotropy_plot/pleio_PD_plot.R) script

## Results

 - 247 pleiotropic loci were Identified using PLEIO
 - 7 coding variants were found using [VEP](https://www.ensembl.org/Homo_sapiens/Tools/VEP)
 - Effect of SNP in SPPCL2C (Intramembrane-cleaving aspartic protease (I-CLiP), which may be capable of cleaving type II membrane signal peptides in the hydrophobic membrane plane) was shown on PleiotropyPlot
 - Inflammatory disorders are much more strongly correlated and their heritability is higher, but there is some correlation with Parkinson's disease as well

## Future plans

 - Expand the PLEIO analysis further by adding new GWAS summary statistics, and to check if this variants are also identified as significant and if we find any other SNPs
 - Compare our approach with others such as Mendelian Randomisation to confirm or deny this variant significance
