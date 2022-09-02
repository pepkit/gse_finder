RETMAX = 10000000 #one day it should be increased

# gds = geo DataSets
ETOOLS_GEO_BASE = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds'

ETOOLS_GEO_GSE_BASE = f'{ETOOLS_GEO_BASE}&term=GSE[ETYP]'
ETOOLS_ENDING = f'&retmax={RETMAX}&usehistory=y'

ETOOLS_GEO_GSE_GET_ALL = ETOOLS_GEO_GSE_BASE

ETOOLS_GEO_GSE_GET_LAST_3_MONTH = f'{ETOOLS_GEO_GSE_BASE}&+AND+"published+last+3+months"{ETOOLS_ENDING}'

TODAY_DATE = '3000'

DATE_FILTER = '+AND+("{start_date}"[Publication%20Date]%20:%20"{end_date}"[Publication%20Date])'
ETOOLS_GEO_GSE_GET_BY_DATE = f'{ETOOLS_GEO_GSE_BASE}{DATE_FILTER}{ETOOLS_ENDING}'


ADDITIONAL_FILTERS = {
    'bed': '+AND+(bed)+AND+'
}