# proj_pqc_sca_FALCON_GAUSS_KeyGen
Side channel attack on FALCON's discrete Gaussian sampling process with Key generation (Attacking Software implementation). 

Procedure to replicate the experimental results: 
  1. Call the Trasfer.py to transfer the .trs files to .csv raw data.
  2. Correlation power analysis takes the correlation between the power traces and a fixed value set over time:
     First call write_LABLs.py to generate the fixed value set.
     Then call Correlation.py to calculate the correlation over time.
  4. At the point of interest, call AVG_Trace_twocase.py to draw the average trace comparison.
  5. Call Univariate_Gauss.py to view the theoretical model analysis results.
  6. OPTIONAL and NOT included in the paper: call PCA-Test to view the clustering results between the two cases.

NOTE: There are two attack points, so steps 2-6 need to be applied at both attack points. 
-------
Update 04212025: Resubmit to ICCAD 2025. No code change, paper updated
