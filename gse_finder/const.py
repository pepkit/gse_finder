RETMAX = 10000000 # once it should be increased

# gds = geo DataSets
ETOOLS_GEO_BASE = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds'
ETOOLS_GEO_GSE_BASE = f'{ETOOLS_GEO_BASE}&term=GSE[ETYP]'

ETOOLS_ENDING = '&retmax={retmax}&usehistory=y'

TODAY_DATE = '3000'

DATE_FILTER = '+AND+("{start_date}"[Publication%20Date]%20:%20"{end_date}"[Publication%20Date])'
THREE_MONTH_FILTER = '+AND+"published+last+3+months"[Filter]'
