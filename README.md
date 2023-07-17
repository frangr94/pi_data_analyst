# PI DATA ANALYST OPS

El creciente uso de internet por parte de los seres humanos ha constituido uno de los principales factores explicativos de los cambios experimentados por las sociedades modernas a lo largo del SXXI, por lo que el análisis de las tendencias relativas a este se ha vuelto una práctica imperativa en nuestros días para todas las organizaciones que constituyen el cuerpo social.

Este proyecto tiene el objetivo de generar información sobre el mercado del internet en Argentina en el año 2022 con el fin de otorgar lineamientos para la inversión en dicho mercado en el ciclo económico subsiguiente.

Para ello se ingestaron datos de diversas fuentes (API ENACOM, ENCC 2017 y 2019, Censo Nacional de Población, Hogares y Viviendas del año 2022) en una base de datos MYSQL (previamente adecuados con Libre Office Calc) que fueron luego leídos (PyMYSQL), explorados, transformados y analizados/visualizados con Python (pandas, plotly, streamlit y otras librerías).
Se puede clonar el repositorio ejecutando:

    $ git clone https://github.com/frangr94/pi_data_analyst


Las visualizaciones fueron creadas con Streamlit y se pueden ejecutar localmente con el comando:

    $ streamlit run home.py

#### Nota: es necesario tener instaladas las librerías que utiliza el script.

Esto abrirá la siguiente pantalla en su navegador por defecto:

![alt text](src/dash_home.png "Home preview")

Ahora puedes navegar en la app como lo desees.

En estadísticas nacionales se pueden ver datos sobre las conexiones a nivel nacional:

![alt text](src/dash_1.png "P1")

En acceso a internet se pueden ver datos sobre el acceso a internet y los ingresos de los argentinos:

![alt text](src/dash_2.png "P2")

En conexiones lentas se pueden ver las localidades demandantes de internet:

![alt text](src/dash_3.png "P3")

En norte argentino se pueden ver datos sobre consumos digitales en el norte del país:

![alt text](src/dash_4.png "P4")


El repositorio cuenta además con otros archivos pertinentes:

* En el archivo EDA.ipynb se puede apreciar el análisis exploratorio realizado sobre los datos: fue un paso importante para la lectura de los mismos ya que presentaban algunos problemas que era necesario resolver para generar un correcto análisis.

* El archivo ingesta_pandas.ipynb contiene la lectura de los datos desde MYSQL y las transformaciones que fue necesario hacer para el correcto funcionamiento del repositorio.

* En los directorios datasets y datasets_ordenados se encuentran los archivos (.csv) necesarios para la ejecución del script.




