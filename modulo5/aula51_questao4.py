from datetime import date
from datetime import datetime
data = date.today()

data_texto = data.strftime('%d/%m/%Y')
print(f"O dia atual é: {data}")
print(f"O dia atual é: {data_texto}")

horas= datetime.now()
horas_texto = horas.strftime('%H:%M')
print(f"As horas são: {horas}")
print(f"As horas são: {horas_texto}")