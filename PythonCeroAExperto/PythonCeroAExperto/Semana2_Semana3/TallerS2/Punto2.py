"""Logica proposicional

Mediante operaciones con tablas de verdad. 
    - Realizarán manualmente estas operaciones para predecir resultados. 
    - Implementarán las operaciones en código, utilizando un lenguaje de
      programación python, para confirmar los resultados
    - Interpreta los resultados


|   P   |   Q    |not P |not Q |P and Q|P or Q|P and not Q|not P or Q|P or (notP and Q)|Q and (P and notQ)|not(P and Q)|
|-------|--------|------|------|-------|------|-----------|----------|-----------------|------------------|------------|
| False | True   | True | False| False | True |  False    | True     |  True           | False            | True       |
| True  | False  | False| True | False | True |  True     | False    |  True           | False            | True       |
| False | False  | True | True | False | False|  False    | True     |  False          | False            | True       |
| True  | True   | False| False| True  | True |  False    | True     |  True           | False            | False      |

"""