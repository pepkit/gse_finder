from const import *
import requests
import xmltodict
import re
import logmuse
import coloredlogs
from datetime import datetime
from datetime import timedelta

UID_REGEX = re.compile(r'[1-9]+0+([1-9]+[0-9]*)')

_LOGGER = logmuse.init_logger("pepannot")
coloredlogs.install(
    logger=_LOGGER,
    datefmt="%H:%M:%S",
    fmt="[%(levelname)s] [%(asctime)s] %(message)s",
)


class Generator:

    def get_gse_all(self) -> list:
        """

        :return:
        """
        return self.get_gse_id_by_query(url=ETOOLS_GEO_GSE_GET_ALL)

    def get_gse_last_3_month(self) -> list:
        """

        :return:
        """
        return self.get_gse_id_by_query(url=ETOOLS_GEO_GSE_GET_LAST_3_MONTH)

    def get_gse_last_week(self) -> list:
        """

        :return:
        """
        return self.get_gse_by_day_count(7)

    def get_gse_by_day_count(self, n_days: int = 1) -> list:
        """

        :param n_days:
        :return:
        """
        today = datetime.today()
        start_date = today - timedelta(days=n_days)
        start_date_str = start_date.strftime("%Y/%m/%d")
        return self.get_gse_by_date(start_date_str)

    def get_gse_by_date(self, start_date: str, end_date: str = None) -> list:
        """
        Search gse accessions by providing start date and end date. By default, the last date is today.
        :param start_date: the oldest date of update (from YYYY/MM/DD to now) [input format: 'YYYY/MM/DD']
        :param end_date: the nearest date of update (from __ to YYYY/MM/DD) [input format: 'YYYY/MM/DD']
        :return: list of gse accessions
        """
        if end_date is None:
            end_date = TODAY_DATE
        new_url = ETOOLS_GEO_GSE_GET_BY_DATE
        new_url = new_url.format(start_date=start_date, end_date=end_date)
        return self.get_gse_id_by_query(url=new_url)


    def get_gse_id_by_query(self, url: str) -> list:
        """
        Use esearch query to find uids and then convert them to gse ids
        :param url: url of the query
        :return: list of gse ids
        """
        uids_list = self.run_search_query(url)
        gse_id_list = [self.uid_to_gse(d) for d in uids_list]

        return gse_id_list

    def run_search_query(self, url: str) -> list:
        """
        Run get request and return list of uids found
        :param url: url of the query
        :return: list of UIDs
        """
        x = requests.get(url)
        if x.status_code != 200:
            _LOGGER.error(f"Request status != 200. Error. Check your request")
            return []
        try:
            x_result = x.text
            return xmltodict.parse(x_result)["eSearchResult"]["IdList"]["Id"]
        except Exception:
            return []


    def uid_to_gse(self, uid: str) -> str:
        """
        UID to GES accession converter
        :param uid: uid string
        :return: GSE id string
        """
        return 'GSE' + UID_REGEX.match(uid).group(1)


# Generator().get_gse_by_date('2022/08/01','2022/09/01')
fff = Generator().get_gse_by_day_count(1)
fff