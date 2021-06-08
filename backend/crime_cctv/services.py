from crime_cctv.models import cctvDto
import pandas as pd
from common.services import CommonService
import xlwings as xw


class CrimeService(CommonService):
    dto = cctvDto()

    # DF 생성하기
    def new_model_csv(self, payload):

        this = self.dto
        this.context = './data/'
        this.fname = payload
        df = pd.read_csv(this.context + this.fname + '.csv')
        return df

    def new_model_xls(self, payload):

        this = self.dto
        this.context = './data/'
        this.fname = payload
        df = pd.read_excel(this.context + this.fname + '.xls')
        return df

