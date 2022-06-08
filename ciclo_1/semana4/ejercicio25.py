# libreria numpy y pandas
import numpy as np
import pandas as pd

unidad_datos = np.array(
    [
        [2,5,3,2],
        [4,6,7,2],
        [3,2,4,1]
    ]
)

unidades = pd.DataFrame(unidad_datos)
print(unidades)

unidades = pd.DataFrame(unidad_datos,
                        index=[2015,2016,2017],
                        columns=['Ag','Au','Cu','Pt'])

print(unidades)