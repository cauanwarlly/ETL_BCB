import pandas as pd
from src.extractTransform import requestApiBCB
from src.load import salvarCsv

"SALVA O BANCO DE DADOS EM CSV"

dadosBcb = requestApiBCB('20191')
salvarCsv(dadosBcb, "src/datasets/MeiosdePagamentosTri.csv",",",".")