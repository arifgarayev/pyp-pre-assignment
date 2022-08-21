import json
import pandas as pd
from decimal import *




class HTMLGenerator():
    """
    >>> print(HTMLGenerator().generate_htmlI(list_of_tuples= [('Amarilla', Decimal('155315.00'), Decimal('19037279.50'), Decimal('1290163.44'), Decimal('2814104.06')), ('Carretera', Decimal('146846.00'), Decimal('14937520.50'), Decimal('1122212.62'), Decimal('1826804.89')), ('Montana', Decimal('154198.00'), Decimal('16549834.50'), Decimal('1159032.62'), Decimal('2114754.88')), ('Velo', Decimal('162424.50'), Decimal('19826768.50'), Decimal('1576709.04'), Decimal('2305992.47')), ('Paseo', Decimal('338239.50'), Decimal('35611662.00'), Decimal('2600518.05'), Decimal('4797437.95')), ('VTT', Decimal('168783.00'), Decimal('21968533.50'), Decimal('1456612.48'), Decimal('3034608.02'))]))
    """

    def __init__(self):
        self.data_for_df = {}

    def generate_df(self, list_of_tuples):
        for tup in list_of_tuples:
            for i in range(len(tup)):
                if i == 0:
                    self.data_for_df[tup[i]] = []
                else:
                    self.data_for_df[tup[0]].append(str(tup[i]))

        return pd.DataFrame(data=self.data_for_df)

    def generate_html(self, list_of_tuples):
        df: pd.DataFrame = self.generate_df(list_of_tuples=list_of_tuples)

        df = df.to_html(index=False)

        return df





