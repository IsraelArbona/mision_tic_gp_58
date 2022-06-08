# libreria pandas

import pandas as pd

elementos = {
    'Numero atómico': [1,6,47,88],
    'Masa atómica': [1.008,12.011,107.87,226],
    'Familia': ['No metal','No metal','Metal','Metal']
}

tablaPeriodica = pd.DataFrame(elementos, 
                                index=['H','C','Ag','Ra'],
                                columns=['Familia','Masa atómica','Numero atómico'])

print(tablaPeriodica)