import pandas as pd
from src.extractTransform import requestApiBCB
from src.load import salvarCsv, salvarSqlite, salavarMySQL


dadosBcb = requestApiBCB("20191")

# SALVA O BANCO DE DADOS EM CSV
# salvarCsv(dadosBcb, "src/datasets/MeiosdePagamentosTri.csv",",",".")

# SALVA O BANCO DE DADOS EM SQL
# salvarSqlite (dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

# salva e jogando no banco MySQL
salavarMySQL(dadosBcb, "root", "root", "localhost", "etlbcb", "meios_pagamentos_tri")
