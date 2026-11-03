# proj_pqc_sca_FALCON_GAUSS_KeyGen
A complete side-channel attack pipeline on FALCON's disreate gaussian sampling process in KeyGen. This sampling process samples small polynomial coefficients for lattice base components f and g. The attack exploits intermediate values using simple power analysis. Then use these intermedaite variables to deduce the full key. This attack provides practical, detailed, and replicable tasks starting from raw power measurements.  Procedure to replicate the experimental results are: 
  1. Trace preprocessing: transfer the .trs raw trace to .csv data values
  2. Points of interest(POIs) identification: We use a correlation power analysis based method to identify the POIs. We start with 
  4. At the point of interest, call AVG_Trace_twocase.py to draw the average trace comparison.
  5. Call Univariate_Gauss.py to view the theoretical model analysis results.
  6. OPTIONAL and NOT included in the paper: call PCA-Test to view the clustering results between the two cases.

NOTE: There are two attack points, so steps 2-6 need to be applied at both attack points. 
-------
Update 04212025: Resubmit to ICCAD 2025. No code change, paper updated
