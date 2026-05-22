import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import textwrap
import numpy as np

# ─────────────────────────────────────────────
# DATOS COMPLETOS DE LOS 20 CONTRATOS
# ─────────────────────────────────────────────
contratos = [
  # 0
  {
    'no': '1',
    'arrendatario': 'AGRO-PARTES PUEBLA\nS.A. DE C.V.\n(Rep. Laura Fabiola\nTorres Pérez)',
    'local_clave': 'No especificado',
    'superficie': '179 m²',
    'ubicacion': 'Lateral Sur, Autopista\nMéxico-Puebla 55,\nCuautlancingo, 72710\nPuebla, Puebla',
    'fecha_firma': '13-Mar-2023',
    'vigencia': '15-Abr-2023 al\n15-Abr-2028\n(1 año forzoso +\n4 voluntarios)',
    'renta': '$15,000.00 MN/mes',
    'incremento': 'Cada 12 meses\n(15 abr), 100%\nINPC General',
    'deposito': '2 meses de renta\n= $30,000.00 MN\n(se actualiza c/incr.)',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Arrendador divide costo\ntotal ÷ m³ consumidos;\nArrendatario paga por\nmeses vencidos dentro\nde 3 días naturales\nde notificación escrita',
    'luz': 'Arrendatario contrata y\npaga directamente,\nmedidor propio.\nEntrega copia recibo\nal Arrendador en 48 hrs',
    'fuente': 'Contrato firmado\n13-Mar-2023\n(local repo)',
  },
  # 1
  {
    'no': '2',
    'arrendatario': 'COMERCIAL AUTOMOTRIZ\nDE LOS ALTOS S.A. DE C.V.\n(Rep. J. Guadalupe\nPonce Ríos)',
    'local_clave': 'L-01 / L-02 / L-03',
    'superficie': '252.06 m²',
    'ubicacion': 'Blvd. José María Chávez\n2010, Cd Industrial,\nC.P. 20290\nAguascalientes, Ags.',
    'fecha_firma': '01-Dic-2024',
    'vigencia': '01-Dic-2024 al\n01-Dic-2029\n(2 años forzosos\nArrendatario;\n3 años forzosos\nArrendador)',
    'renta': '$37,809.00 MN/mes',
    'incremento': 'Cada 12 meses\n(01 dic), 100%\nINPC General',
    'deposito': '2 meses de renta\n= $75,618.00 MN\n(se actualiza c/incr.)',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Arrendatario paga por\nsu exclusiva cuenta:\ngastos de consumo de\nagua, incluyendo el\ncosto de la póliza\nque contrate',
    'luz': 'Arrendatario contrata y\npaga directamente,\nmedidor propio.\nEntrega copia recibo\nal Arrendador en 48 hrs',
    'fuente': 'Contrato firmado\n01-Dic-2024\n(local repo)',
  },
  # 2
  {
    'no': '3',
    'arrendatario': 'BANCO SANTANDER\nMÉXICO S.A. IBM\nGFSM\n(Rep. Arq. Edmundo\nPérez Toledo y\nC.P. José L. Álvarez)',
    'local_clave': 'F-02A',
    'superficie': '432 m²',
    'ubicacion': 'Paseo de Las Hdas. s/n\nLote 4 Norte, Jardines\nde la Hacienda, 54720\nCuautitlán Izcalli,\nEstado de México',
    'fecha_firma': '01-Sep-2023 (orig.)\nConvenio: 26-May-2025',
    'vigencia': '01-Sep-2023 al\n01-Sep-2030\n(5 años forzosos\npara ambas partes;\nmod. por convenio)',
    'renta': '$201,691.51 MN/mes\n(vigente desde\n05-Sep-2024)',
    'incremento': 'Anual el 01 de\nseptiembre de\ncada año, INPC',
    'deposito': 'No especificado\nen el convenio\nmodificatorio',
    'penalizacion': 'No especificado\nen el convenio\nmodificatorio',
    'agua': 'No especificado\nen el convenio\nmodificatorio',
    'luz': 'No especificado\nen el convenio\nmodificatorio',
    'fuente': 'Convenio Mod.\n26-May-2025\n(local repo)',
  },
  # 3
  {
    'no': '4',
    'arrendatario': 'WALDO\'S DÓLAR MART\nDE MÉXICO S. DE R.L.\nDE C.V.\n(Rep. Ma. Cristina\nHernández Castillo y\nJ.M. Altamirano V.)',
    'local_clave': '01 y 02',
    'superficie': '853.00 m²',
    'ubicacion': 'Plaza Comercial San\nMarcos Power Center,\nCuautitlán Izcalli,\nEstado de México',
    'fecha_firma': '12-Feb-2024',
    'vigencia': '02-Mar-2024 al\n01-Mar-2026\n(2 años forzosos\npara ambas partes)',
    'renta': '$117,524.00 MN/mes\n(base inicial para\nincrementos)',
    'incremento': 'Cada 12 meses\n(a partir abr-2024),\n100% INPC General',
    'deposito': 'No especificado\nen el contrato',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Si hay toma individual:\npaga directo a\nautoridad. Si no:\nArrendador divide $/m³;\npago x meses vencidos\nen 3 días de notif.',
    'luz': 'Arrendatario tramita\nSS y contrata\ndirectamente, medidor\npropio',
    'fuente': 'Contrato firmado\n12-Feb-2024\n(Google Drive)',
  },
  # 4
  {
    'no': '5',
    'arrendatario': 'TV AZTECA S.A.B. DE C.V.\n(Rep. Denisse Andrea\nRivas Rodriguez)',
    'local_clave': 'Local 4\n(oficinas admin.)',
    'superficie': '379 m²',
    'ubicacion': 'Hotel One Acapulco\ny C. Comercial,\nAv. Costera Miguel\nAlemán 16, Fracc.\nCosta Azul, 39850\nAcapulco, Guerrero',
    'fecha_firma': '13-Ene-2026',
    'vigencia': '04-Jul-2025 al\n04-Jul-2028\n(3 años forzosos\npara ambas partes)',
    'renta': '$76,717.12 MN/mes\n+ IVA',
    'incremento': 'Anual; INPC +\n2 puntos porc.\nPrimer incr. a los\n12 meses de inicio',
    'deposito': '$204,466.66 MN\n(equiv. 2 meses\nde renta mensual)\nSe actualiza\nanualmente',
    'penalizacion': 'No especificada\nrescisión anticipada\npor Arrendatario.\nSi no desocupa al\ntérmino: pena conv.\n= 1 mes renta/mes\n+ renta y mant.',
    'agua': 'Por cuenta exclusiva\ndel Arrendatario\n(contratación y\ngastos de consumo)',
    'luz': 'Por cuenta exclusiva\ndel Arrendatario.\nSi opera en horarios\ndistintos al hotel:\npaga sobrecostos\nde operación',
    'fuente': 'Contrato firmado\n13-Ene-2026\n(Google Drive)',
  },
  # 5
  {
    'no': '6',
    'arrendatario': 'TRAIGO TODO S.A.P.I.\nDE C.V.\n(Rep. Ricardo Añorve\nMartínez y José A.\nSánchez Ruiz)',
    'local_clave': '"Sonora Grill"\n(restaurante)',
    'superficie': '725 m² techados\n+ 245 m² terraza',
    'ubicacion': 'Eusebio Kino No. 369\nCol. Lomas Pitic,\n83010 Hermosillo,\nSonora',
    'fecha_firma': '15-Oct-2021',
    'vigencia': '10 años forzosos\ndesde Fecha de\nApertura (fecha no\nespecificada en\nel contrato)',
    'renta': 'Mayor entre:\n• Renta Mínima:\n  $200,000 MN/mes\n• Renta Variable:\n  50% de Utilidad\n  Mensual',
    'incremento': 'Renta Mínima cada\n12 meses desde\nFecha de Apertura,\n100% INPC General',
    'deposito': 'No especificado\nen el contrato',
    'penalizacion': 'Años 1-5: 50% ×\n(prom. Renta 12 meses\n× meses por vencer)\nAño 6 en adelante:\nRenta Mínima ×\nmeses por vencer\n(una sola exhibición)',
    'agua': 'Arrendatario contrata\ny paga directamente.\nSi medidor individual:\ndirecto a autoridad.\nSi no: Arrendador\nprorratea por m³',
    'luz': 'Arrendatario contrata\ncon CFE directamente,\nmedidor propio\n(S.S. a cargo del\nArrendatario)',
    'fuente': 'Contrato firmado\n15-Oct-2021\n(Google Drive)',
  },
  # 6
  {
    'no': '7',
    'arrendatario': 'SERVICIOS INMOBILIARIOS\nALSEA S.A. DE C.V.\n(Rep. Armando\nTorrado Martínez)\nObl. Solidario:\nALSEA S.A.B. DE C.V.',
    'local_clave': 'PAD01',
    'superficie': '450 m²',
    'ubicacion': 'Hotel One Monterrey,\nBlvd. Aeropuerto\nMza. 12 Lte. 12,\nZona Hot. Parque\nInd. Milenium,\nApodaca, N.L.',
    'fecha_firma': '20-Abr-2016',
    'vigencia': 'Desde firma:\n5 años forzosos\n+ 5 años volunt.\n+ prórroga opc.\nde 5 años\n(hasta ~2031)',
    'renta': 'Mayor entre:\n• Renta Fija:\n  $45,000 MN/mes\n• Renta Variable:\n  6% Ventas Netas',
    'incremento': 'Renta Fija cada\n12 meses desde\nFecha Inicio Renta,\n100% INPC General',
    'deposito': 'No especificado\nen el contrato\n(posiblemente en\ncontrato original)',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Si hay toma individual:\npaga directo a\nautoridad. Si no:\nArrendador prorratea\npor m³ consumidos',
    'luz': 'Arrendatario tramita\nSS y contrata\ndirectamente, medidor\npropio',
    'fuente': 'Contrato firmado\n20-Abr-2016\n(Google Drive)',
  },
  # 7
  {
    'no': '8',
    'arrendatario': 'OPERADORA HOTELERA\nINHOUSE S.A.P.I. DE C.V.\n(Rep. Alejandro\nCarbajal Ascencio\ny Luis E. Sierra\nRobles) — LEÓN',
    'local_clave': 'Hotel completo',
    'superficie': '12,834 m²\n(superficie total\ndel hotel)',
    'ubicacion': 'Blvd. Aeropuerto\nNúm. 1452 (antes 1120)\nCol. El Alto,\nLeón, Guanajuato',
    'fecha_firma': '11-Dic-2023',
    'vigencia': '01-Ene-2024 al\n31-Dic-2028\n(5 años forzosos\npara ambas partes)',
    'renta': 'Mayor entre Renta\nMensual Fija y Renta\nVariable (20% Ingr.\nTotales desde mes 7)\nFija Año 1: $100k-$300k\nFija Año 2: $350,000\nFija Año 3: $400,000\nFija Años 4-5: $450,000',
    'incremento': 'No aplica:\nrenta fija por\ntabla escalonada;\nvariable = 20%\nde ingresos',
    'deposito': 'No especificado\nen el contrato',
    'penalizacion': 'Causales de rescisión\ndefinidas; no se\nespecificó penalización\nfinanciera por\nrescisión anticipada\nen el contrato',
    'agua': 'Arrendataria paga\ntodos los servicios\npúblicos del hotel\n(agua, electricidad,\ngas, teléfono)',
    'luz': 'Arrendataria paga\ntodos los servicios\npúblicos del hotel\n(agua, electricidad,\ngas, teléfono)',
    'fuente': 'Contrato firmado\n11-Dic-2023\n(Google Drive)',
  },
  # 8
  {
    'no': '9',
    'arrendatario': 'JULIO CESAR\nTORRES ROJO\n(Persona física)',
    'local_clave': 'No. 17226\n(local comercial)',
    'superficie': '103.55 m²',
    'ubicacion': 'Col. Otay\nConstituyentes,\nTijuana, Baja\nCalifornia Norte',
    'fecha_firma': '05-Jun-2023',
    'vigencia': '2 años forzosos\npara ambas partes\ndesde Fecha de\nApertura (no\nespecificada)',
    'renta': 'USD $1,800.00/mes\n(mil ochocientos\ndólares)',
    'incremento': 'Cada 12 meses\ndesde Fecha Inicio\nde Renta, conforme\na la Inflación\n(INPC)',
    'deposito': '1 mes de renta\n= USD $1,800.00\n(documentado por\nrecibo del Arrend.)',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Si hay toma individual:\npaga directo a\nautoridad. Si no:\nArrendador prorratea\npor m³; pago por\nmeses vencidos en\n3 días de notif.',
    'luz': 'Arrendatario tramita\nSS y contrata\ndirectamente, medidor\npropio',
    'fuente': 'Contrato firmado\n05-Jun-2023\n(Google Drive)',
  },
  # 9
  {
    'no': '10',
    'arrendatario': 'ZAPATA S.A. DE C.V.\n(Rep. Montserrat\nBeltrán Ramos)',
    'local_clave': 'No especificado\nen el contrato',
    'superficie': '81 m²',
    'ubicacion': 'Paseo de Las Hdas.\ns/n Lote 4 Norte,\nJardines de la\nHacienda, 54720\nCuautitlán Izcalli,\nEstado de México',
    'fecha_firma': '26-May-2025',
    'vigencia': 'Desde 28-Oct-2025\n(Fecha Inicio Renta)\n5 años forzosos\npara ambas partes\n(hasta ~Oct-2030)',
    'renta': '$32,400.00 MN/mes\n(a partir del\n28-Oct-2025)',
    'incremento': 'Cada 12 meses\ndesde Fecha de\nApertura, 100%\nINPC General',
    'deposito': '1 mes de renta\n= $32,400.00 MN\n(entregado a la\nfirma del contrato)',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Arrendatario paga\ndirectamente a la\nautoridad u organismo\noperador municipal\ncompetente',
    'luz': 'Arrendatario tramita\nSS y contrata\ndirectamente, medidor\npropio',
    'fuente': 'Contrato firmado\n26-May-2025\n(Google Drive)',
  },
  # 10
  {
    'no': '11',
    'arrendatario': 'GRUPO POSADAS\nS.A.B. DE C.V.\n(Rep. Ing. José Carlos\nAzcárraga Andrade y\nJorge Carvallo\nCouttolenc)',
    'local_clave': 'Hotel completo\n(Fiesta Americana)',
    'superficie': 'Lote de 41,413 m²\n(Zona Hotelera\nCancún)',
    'ubicacion': 'Zona Hotelera,\nLote 44, Sección A,\n2a Etapa, Cancún,\nMpio. Benito Juárez,\nQuintana Roo',
    'fecha_firma': '14-Feb-2018\n(instrumento\nnotarial 19,338)',
    'vigencia': 'Forzoso para\nambas partes\nhasta el\n31-Dic-2032\n(sujeto a\ncondición suspensiva)',
    'renta': 'Renta Mínima\nMensual:\nUSD $791,666.65/mes\n+ Renta Variable\nadicional',
    'incremento': 'Anual por CPI\n(Consumer Price\nIndex) de EE.UU.\ndesde el 2do Año\nde Renta',
    'deposito': 'No especificado\nen el contrato\ndisponible',
    'penalizacion': 'No especificado\nen el contrato\ndisponible',
    'agua': 'Arrendataria paga\ntodos los servicios\ndel hotel (es la\noperadora del\ninmueble completo)',
    'luz': 'Arrendataria paga\ntodos los servicios\ndel hotel (es la\noperadora del\ninmueble completo)',
    'fuente': 'Contrato firmado\n14-Feb-2018\n(Google Drive)',
  },
  # 11
  {
    'no': '12',
    'arrendatario': 'DIVOL NORTE\nS.A.P.I. DE C.V.\n(Rep. Rodrigo Huerta\nMartínez y Rodolfo\nHuerta...)',
    'local_clave': 'Local industrial\n(Lote 1)',
    'superficie': '1,710 m²',
    'ubicacion': 'Carretera México-\nCuautitlán, Lote 1,\nCuautitlán Izcalli,\nEstado de México',
    'fecha_firma': '01-Oct-2025',
    'vigencia': '01-Nov-2025 al\n31-Oct-2045\n(20 años forzosos\npara ambas partes)',
    'renta': '$240,963.27 MN/mes\n(desde oct-2025);\n$257,706.73 MN/mes\n(con acceso\nadicional) + IVA',
    'incremento': 'Cada 12 meses;\nprimer incr.\n01-Ago-2026,\nINPC (comparando\njulio ant. vs\njulio año previo)',
    'deposito': '$150,416.67 (cedido\nde DIVOL S.A.) +\n$90,546.60 (nuevo)\n= $240,963.27 total\n(equiv. 1 mes renta)',
    'penalizacion': 'La parte que termine\nanticipadamente paga\ntodas las rentas\npendientes hasta\nconcluir el plazo\nforzoso completo',
    'agua': 'Arrendatario paga\npor su exclusiva\ncuenta el servicio\nde consumo de agua\nde la localidad\narrendada',
    'luz': 'Arrendatario paga\npor su cuenta en\ntérminos de los\ncontratos con los\nproveedores\ncorrespondientes',
    'fuente': 'Contrato firmado\n01-Oct-2025\n(Google Drive)',
  },
  # 12
  {
    'no': '13',
    'arrendatario': 'TIENDAS EXTRA S.A.\nDE C.V. (Circle K)\n(Rep. Mario González\nPadilla y Eduardo\nJosé Cervera Gamboa)',
    'local_clave': 'Local B',
    'superficie': '200 m²',
    'ubicacion': 'Hotel One Acapulco,\nAv. Costera Miguel\nAlemán 16, Col.\nCosta Azul, 39850\nAcapulco, Guerrero',
    'fecha_firma': '25-Feb-2026',
    'vigencia': '15 años desde Fecha\nde Apertura;\n5 años forzosos\npara ambas partes;\n10 años voluntarios\n(aviso 6 meses ant.)',
    'renta': 'Mayor entre:\n• Renta Mínima:\n  $38,000 MN/mes\n• Renta Variable:\n  8% Ventas Netas\n  Mensuales',
    'incremento': 'Cada 12 meses\ndesde Fecha Inicio\nde Pago de Renta,\n100% INPC General',
    'deposito': 'Equivalente a\n1 mes de Renta\n(monto según renta\nvigente a la firma)',
    'penalizacion': 'Promedio Renta\nMensual últimos\n12 meses × meses\nfaltantes al plazo\nforzoso + IVA,\nen una exhibición.\nSi no desocupa:\nrenta +100%',
    'agua': 'Arrendatario paga\npor su cuenta el\nservicio de consumo\nde agua de la\nlocalidad arrendada',
    'luz': 'Arrendatario paga\npor su cuenta en\ntérminos de los\ncontratos con los\nproveedores\ncorrespondientes',
    'fuente': 'Contrato firmado\n25-Feb-2026\n(Google Drive)',
  },
  # 13
  {
    'no': '14',
    'arrendatario': 'AERO CHARTER DE\nMÉXICO S.A. DE C.V.\n(Primeflight)\n(Rep. Luis Ricardo\nRamos Cabrero)',
    'local_clave': 'Local en Plaza\nOne Monterrey',
    'superficie': '123.09 m²',
    'ubicacion': 'Plaza One Monterrey,\nBlvd. Aeropuerto\nMza. 12 Lte. 12,\nZona Hot. Parque\nInd. Milenium,\nApodaca, N.L.',
    'fecha_firma': '06-Nov-2023',
    'vigencia': '06-Nov-2023 al\n06-Nov-2026\n(3 años forzosos\npara ambas partes)',
    'renta': '$27,537.93 MN/mes\n(cantidad inicial)',
    'incremento': 'Cada 12 meses\ndesde Fecha Inicio\nde Renta, 100%\nINPC General',
    'deposito': 'Equivalente a\n2 meses de Renta\nVigente (monto\nno especificado\nen el contrato\npara el 1er año)',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Arrendatario paga\nconsumo de agua\nde la localidad.\nCuota de mant.\ncubre áreas comunes\n(incl. agua común)',
    'luz': 'Arrendatario tramita\nSS y contrata\ndirectamente, medidor\npropio (cargo\na cargo del\nArrendatario)',
    'fuente': 'Contrato firmado\n06-Nov-2023\n(Google Drive)',
  },
  # 14
  {
    'no': '15',
    'arrendatario': 'T.I. EXPERIENCIAS EN\nGRUPOS Y CONVENCIONES\nS.A. DE C.V.\n(Rep. Arturo Aguirre\nEscalante)',
    'local_clave': '"Escritorio de\nVentas de Tours"\n(a lado de recepción)',
    'superficie': '21 m²',
    'ubicacion': 'Cancún,\nQuintana Roo\n(Hotel en zona\nhotelera)',
    'fecha_firma': '21-Abr-2025\n(efect. retroact.\nal 03-Feb-2025)',
    'vigencia': '03-Feb-2025 al\n03-Feb-2028\n(3 años forzosos\npara ambas partes)',
    'renta': 'USD $3,000.00/mes\n+ IVA aplicable',
    'incremento': 'Cada 12 meses\ndesde Fecha de\nApertura, conforme\na la Inflación\n(INPC General)',
    'deposito': '1 mes de renta\n= USD $3,000.00\n(entregado a la\nfirma del contrato)',
    'penalizacion': 'Renta vigente × meses\nfaltantes al plazo\nforzoso + IVA, en una\nexhibición. Si no\ndesocupa: última renta\n+100% hasta desocup.',
    'agua': 'Arrendatario paga\nderechos de servicio\nde agua cuando\nle corresponda;\nentrega recibos\nal Arrendador',
    'luz': 'Arrendatario paga\nenergía eléctrica;\nentrega recibos\nde pago al\nArrendador cuando\nse solicite',
    'fuente': 'Contrato firmado\n21-Abr-2025\n(Google Drive)',
  },
  # 15
  {
    'no': '16',
    'arrendatario': 'QUATTRALIA HOLDING\nS.A. DE C.V.\n(Rep. Jorge Patricio\nPérez Aristig\nCastellano)',
    'local_clave': 'Local comercial\n(aprox. 750 m²)',
    'superficie': '750 m²',
    'ubicacion': 'Periférico Blvd.\nManuel Ávila\nCamacho No. 150,\nFragcionamiento\n"El Parque",\nNaucalpan, Edo. Méx.',
    'fecha_firma': 'Contrato: 17-Jun-2024\nConvenio Mod.:\n28-May-2025',
    'vigencia': '17-Jun-2025 al\n17-Jun-2026\n(1 año forzoso para\nambas partes;\nconvenio modif.)',
    'renta': '$1,365,000 MN\ntotal anual, pagado:\n• $682,500 el\n  01-Jun-2025\n• $682,500 el\n  01-Dic-2025\n(+ IVA cada pago)',
    'incremento': 'No especificado\nen el convenio\nmodificatorio\n(rige contrato orig.)',
    'deposito': 'No especificado\nen el convenio\n(rige contrato\noriginal)',
    'penalizacion': 'El Arrendatario paga\nlas rentas que\nfaltaren por vencer\nhasta concluir\nel plazo forzoso',
    'agua': 'No especificado\nen el convenio\n(rigen cláusulas\ndel contrato\noriginal)',
    'luz': 'No especificado\nen el convenio\n(rigen cláusulas\ndel contrato\noriginal)',
    'fuente': 'Convenio Mod.\n28-May-2025\n(Google Drive)',
  },
  # 16
  {
    'no': '17',
    'arrendatario': 'DAVID VALDEZ ROMO\n(Persona física)',
    'local_clave': 'Local comercial\n(restaurante)',
    'superficie': '252 m²',
    'ubicacion': 'Calles Los Laureles\ns/n, Col. Las Flores,\nC.P. 20290,\nAguascalientes\n(Fiesta Americana\nAguascalientes)',
    'fecha_firma': 'Contrato: 04-Dic-2019\nConvenio Mod.:\n21-Ene-2026\n(efect. 04-Dic-2025)',
    'vigencia': '04-Dic-2025 al\n03-Dic-2031\n(6 años adicionales\nconvenio modif.)',
    'renta': '• Jun–Mar (10 meses):\n  $21,157.49 MN/mes\n• Abr y May\n  (2 meses):\n  $505,000 MN\n+ IVA en ambos\ncasos',
    'incremento': 'Aumenta anualmente\nconforme al INPC\n(ambos montos)',
    'deposito': 'No especificado\nen el convenio\n(rige contrato\noriginal de 2019)',
    'penalizacion': 'No especificado\nen el convenio\n(rigen cláusulas\ndel contrato\noriginal de 2019)',
    'agua': 'No especificado\nen el convenio\n(rigen cláusulas\ndel contrato\noriginal de 2019)',
    'luz': 'No especificado\nen el convenio\n(rigen cláusulas\ndel contrato\noriginal de 2019)',
    'fuente': 'Convenio Mod.\n21-Ene-2026\n(Google Drive)',
  },
  # 17
  {
    'no': '18',
    'arrendatario': 'CORPORATIVO\nEMPRESARIAL SOLAR\nS.A. DE C.V.\n(Rep. Erwin Eduardo\nRomero Ávila)',
    'local_clave': 'Local 2 Carranza',
    'superficie': '41 m²',
    'ubicacion': 'Sheraton Ambassador,\nMonterrey, N.L.\n(Av. Hidalgo 306,\nMonterrey)',
    'fecha_firma': '20-Feb-2024\n(fecha condiciones)',
    'vigencia': '01-Feb-2024 al\n31-Ene-2027\n(3 años forzosos\npara ambas partes)',
    'renta': '$10,291.00 MN/mes\nsin IVA\n($251 MN/m²)',
    'incremento': 'Anual conforme\nal INPC publicado\npor INEGI',
    'deposito': '2 meses de renta\n= $20,582.00 MN',
    'penalizacion': 'No especificado\nen hoja de\ncondiciones (rigen\ncláusulas del\ncontrato estándar)',
    'agua': 'A partir del\n01-Ene-2025 se\nfactura cuota de\nrecuperación de\nenergéticos\n(incluye agua)',
    'luz': 'A partir del\n01-Ene-2025 se\nfactura cuota de\nrecuperación de\nenergéticos\n(incluye luz)',
    'fuente': 'Hoja condiciones\n20-Feb-2024\n(Google Drive)',
  },
  # 18
  {
    'no': '19',
    'arrendatario': 'OPERADORA HOTELERA\nINHOUSE S.A.P.I. DE C.V.\n(Rep. Alejandro\nCarbajal Ascencio\ny Luis E. Sierra\nRobles) — CD. CARMEN',
    'local_clave': 'Hotel completo\n(Torre E)',
    'superficie': 'No especificada\nen el contrato',
    'ubicacion': 'Av. 10 de Julio\nNúm. 1, Ciudad del\nCarmen, Estado de\nCampeche',
    'fecha_firma': '04-Mar-2026',
    'vigencia': 'Hasta 30-Abr-2029\n(3 años y ~2 meses\nforzosos para\nambas partes;\nperiodo de gracia\nhasta 31-May-2026)',
    'renta': 'Mayor entre Renta\nMensual Fija y 20%\nde Ingresos Totales\n(si supera $2.5M):\n• Jun-2026-May-2027:\n  $100,000 MN/mes\n• Jun-2027-May-2028:\n  $150,000 MN/mes\n• Jun-2028-Abr-2029:\n  $200,000 MN/mes',
    'incremento': 'No aplica:\nrenta fija por\ntabla escalonada;\nvariable = 20%\nde ingresos si\n> $2,500,000 MN',
    'deposito': 'No especificado\nen el contrato',
    'penalizacion': 'Causales de rescisión\ndefinidas; no se\nespecificó penalización\nfinanciera por\nrescisión anticipada\nen el contrato',
    'agua': 'Arrendataria paga\ntodos los servicios\npúblicos del hotel\n(agua, electricidad,\ngas, teléfono)',
    'luz': 'Arrendataria paga\ntodos los servicios\npúblicos del hotel\n(agua, electricidad,\ngas, teléfono)',
    'fuente': 'Contrato firmado\n04-Mar-2026\n(Google Drive)',
  },
  # 19
  {
    'no': '20',
    'arrendatario': 'ARRENDATARIO\nCIUDAD OBREGÓN\n(Nombre no disponible)',
    'local_clave': 'No disponible',
    'superficie': 'No disponible',
    'ubicacion': 'Ciudad Obregón\n(Estado de Sonora)\n— según nombre\nde subcarpeta',
    'fecha_firma': 'No disponible',
    'vigencia': 'No disponible',
    'renta': 'No disponible',
    'incremento': 'No disponible',
    'deposito': 'No disponible',
    'penalizacion': 'No disponible',
    'agua': 'No disponible',
    'luz': 'No disponible',
    'fuente': 'PDF escaneado\n— no legible\n(Google Drive)',
  },
]

# ─────────────────────────────────────────────
# IMAGEN 1: IDENTIFICACIÓN Y PLAZO
# ─────────────────────────────────────────────
def make_table_img(title, col_labels, col_data_keys, col_widths, filename, row_height=1.0):
    n_rows = len(contratos)
    n_cols = len(col_labels)

    fig_w = sum(col_widths) + 0.5
    fig_h = n_rows * row_height + 2.0
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.axis('off')

    # Title
    fig.suptitle(title, fontsize=13, fontweight='bold', y=0.99, x=0.5, ha='center')

    # Build cell text and colors
    cell_text = []
    cell_colors = []

    header_color = '#1a3a5c'
    row_colors = ['#f0f4f8', '#dce8f3']

    for i, c in enumerate(contratos):
        row = [c[k] for k in col_data_keys]
        cell_text.append(row)
        bg = row_colors[i % 2]
        if c['no'] == '20':  # unreadable
            bg = '#ffe0e0'
        cell_colors.append([bg] * n_cols)

    table = ax.table(
        cellText=cell_text,
        colLabels=col_labels,
        cellColours=cell_colors,
        colWidths=[w / fig_w for w in col_widths],
        loc='center',
        cellLoc='left',
    )
    table.auto_set_font_size(False)
    table.set_fontsize(6.5)

    # Style header
    for j in range(n_cols):
        cell = table[0, j]
        cell.set_facecolor(header_color)
        cell.set_text_props(color='white', fontweight='bold', fontsize=7)
        cell.set_height(0.06)

    # Row heights
    for i in range(1, n_rows + 1):
        for j in range(n_cols):
            cell = table[i, j]
            cell.set_height(row_height / fig_h)
            cell.PAD = 0.02

    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.savefig(filename, dpi=130, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Guardado: {filename}")


# ─── IMAGEN 1 ────────────────────────────────
make_table_img(
    title='CONTRATOS DE ARRENDAMIENTO FIHO — Cuadro Comparativo (Parte 1/2): Identificación y Vigencia',
    col_labels=['#', 'ARRENDATARIO', 'LOCAL\n/ CLAVE', 'SUPERFICIE', 'UBICACIÓN', 'FECHA\nFIRMA', 'VIGENCIA / PLAZO', 'RENTA MENSUAL\n(sin IVA)', 'INCREMENTO\nDE RENTA'],
    col_data_keys=['no', 'arrendatario', 'local_clave', 'superficie', 'ubicacion', 'fecha_firma', 'vigencia', 'renta', 'incremento'],
    col_widths=[0.4, 2.6, 1.6, 1.2, 2.4, 1.4, 2.6, 2.4, 2.0],
    filename='/home/user/Contratos-Arrendamiento/cuadro_contratos_parte1.png',
    row_height=1.8,
)

# ─── IMAGEN 2 ────────────────────────────────
make_table_img(
    title='CONTRATOS DE ARRENDAMIENTO FIHO — Cuadro Comparativo (Parte 2/2): Condiciones Económicas y Servicios',
    col_labels=['#', 'ARRENDATARIO', 'DEPÓSITO\nEN GARANTÍA', 'PENALIZACIÓN POR\nRESCISIÓN ANTICIPADA', 'COBRO DE AGUA', 'COBRO DE\nENERGÍA ELÉCTRICA', 'FUENTE\nDOCUMENTO'],
    col_data_keys=['no', 'arrendatario', 'deposito', 'penalizacion', 'agua', 'luz', 'fuente'],
    col_widths=[0.4, 2.6, 2.2, 3.2, 2.8, 2.8, 1.8],
    filename='/home/user/Contratos-Arrendamiento/cuadro_contratos_parte2.png',
    row_height=1.8,
)

print("¡Listo!")
