import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

contratos = [
  {'no':'1',  'arrendatario':'AT&T Comunicaciones Digitales S.A. de C.V.',
              'hotel':'HOO.TEL\n(Nuevo Laredo)',
              'sitio':'Azotea 88.20 m²\nAv. Reforma 5102, Nuevo Laredo, Tamps.',
              'plazo':'6 años forz.\n25-oct-2023 a 25-oct-2029',
              'renta':'$51,142.99 MN/mes + IVA',
              'incremento':'Anual INPC\n(1° mes c/año)',
              'deposito':'No especificado',
              'penalizacion':'Rentas faltantes\npor vencer + daños'},
  {'no':'2',  'arrendatario':'ZELIKS S.A.P.I. de C.V.\n(carpeta: Nuviax)',
              'hotel':'Fracc. Resid. "El Tapatío"\n(Tlaquepaque, Jal.)',
              'sitio':'Azotea 46 m²\nTlaquepaque, Jalisco',
              'plazo':'10 años forz.\n01-jul-2019 a 01-jul-2029',
              'renta':'$18,000 MN/mes + IVA',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'Rentas faltantes\npor vencer'},
  {'no':'3',  'arrendatario':'MXT Capital Partners S.A.P.I. de C.V.',
              'hotel':'Hotel Real Inn Morelia',
              'sitio':'Azotea ~55 m²\nEjido Jesús del Monte, Morelia, Mich.',
              'plazo':'10 años forz.\n01-dic-2017 a 01-dic-2027',
              'renta':'$20,000 MN/mes + IVA',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'2 meses renta + IVA\n(con 60 días aviso)'},
  {'no':'4',  'arrendatario':'MXT Capital Partners S.A.P.I. de C.V.',
              'hotel':'AC Marriott Juriquilla\n(Querétaro)',
              'sitio':'Azotea 101.82 m²\nAntea, Juriquilla, Querétaro',
              'plazo':'10 años forz.\n02-ago-2017 a 02-ago-2027',
              'renta':'$20,000 MN/mes + IVA\n(inicio: oct-2017)',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'2 meses renta + IVA\n(con 60 días aviso)'},
  {'no':'5',  'arrendatario':'Intelli Site Solutions S.A.P.I. de C.V.',
              'hotel':'Fiesta Inn Hermosillo',
              'sitio':'Azotea 9.68 m²\nBlvd. Eusebio Kino 369, Hermosillo, Son.',
              'plazo':'10 años forz.\n01-sep-2019 a 01-sep-2029',
              'renta':'$22,000 MN/mes + IVA\n(+ $3,500 mant. energía)',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'Rentas faltantes\npor vencer'},
  {'no':'6',  'arrendatario':'Intelli Site Solutions S.A.P.I. de C.V.',
              'hotel':'Fiesta Inn Chihuahua',
              'sitio':'Azotea 40.99 m²\nBlvd. A. Ortiz Mena 2801, Chihuahua',
              'plazo':'10 años forz.\n01-sep-2019 a 01-sep-2029',
              'renta':'$22,000 MN/mes + IVA',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'Rentas faltantes\npor vencer'},
  {'no':'7',  'arrendatario':'Megacable Comunicaciones de México\nS.A. de C.V.',
              'hotel':'Hotel One Monterrey\nAeropuerto (Apodaca, N.L.)',
              'sitio':'Polígono I\nBlvd. Aeropuerto, Parque Ind. Milenium',
              'plazo':'5 años forz.\n01-abr-2020 a 01-abr-2025',
              'renta':'$364,044.83 MN/año ant. + IVA',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'3 meses renta\n(con 90 días aviso)'},
  {'no':'8',  'arrendatario':'Megacable Comunicaciones de México\nS.A. de C.V. (subarrendatario)',
              'hotel':'Fiesta Inn Periférico Sur\n(CDMX)',
              'sitio':'Azotea 31.27 m²\nPeriférico Sur 5530, Pedregal de Carrasco',
              'plazo':'5 años forz. desde 01-ene-2015\n(convenio modificatorio)',
              'renta':'$300,000 MN/año ant. + IVA\n(50% Arrendador + 50% Posadas)',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'Rentas faltantes\npor vencer'},
  {'no':'9',  'arrendatario':'Mexico Tower Partners S.A.P.I. de C.V.',
              'hotel':'Live Aqua\nSan Miguel de Allende',
              'sitio':'Línea de instalación\nCalzada de la Presa 85, San Miguel, Gto.',
              'plazo':'10 años forz. F/1596 desde 31-jul-2019\n(MTP puede term. c/30 días aviso)',
              'renta':'$5,000/mes (1-2 oper.) ó\n$12,500/mes (3+ oper.) + IVA',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'Contraprestaciones\nfaltantes por vencer'},
  {'no':'10', 'arrendatario':'Mexico Tower Partners S.A.P.I. de C.V.\n(convenio mod.)',
              'hotel':'Fiesta Inn Perinorte\n(Tultitlán, Edomex)',
              'sitio':'Área ~16 m²\nCarretera México-Cuautitlán Lote 1',
              'plazo':'5 años desde feb-2025 (conv.)\n+ 5 años prórroga automática',
              'renta':'$39,556.26 MN/mes + IVA\n(desde feb-2025)',
              'incremento':'Anual INPC',
              'deposito':'No especificado',
              'penalizacion':'12 meses de renta'},
  {'no':'11', 'arrendatario':'Canalizaciones y Accesos Profesionales\nS. de R.L. de C.V. (CAPSA) — convenio',
              'hotel':'Fiesta Inn Oaxaca',
              'sitio':'Azotea 29.55 m²\nAv. Universidad 140, Oaxaca, Oax.',
              'plazo':'Extendido a 31-jul-2028\n(5 años forz. desde jul-2023)',
              'renta':'No especificado en convenio\n(rige contrato orig. 31-jul-2018)',
              'incremento':'No especificado\nen convenio',
              'deposito':'No especificado',
              'penalizacion':'No especificado\nen convenio'},
  {'no':'12', 'arrendatario':'Canalizaciones y Accesos Profesionales\nS. de R.L. de C.V. (CAPSA) — convenio',
              'hotel':'Fiesta Inn Guadalajara',
              'sitio':'Azotea (sup. no espec. en conv.)\nAv. Mariano Otero 1550, Guadalajara, Jal.',
              'plazo':'Extendido a 31-ene-2028\n(5 años forz. desde ene-2023)',
              'renta':'No especificado en convenio\n(rige contrato orig. 01-feb-2018)',
              'incremento':'No especificado\nen convenio',
              'deposito':'No especificado',
              'penalizacion':'No especificado\nen convenio'},
  {'no':'13', 'arrendatario':'Canalizaciones y Accesos Profesionales\nS. de R.L. de C.V. (CAPSA) — convenio 2025',
              'hotel':'FA Condesa Cancún\n(Torre Mar + Torre Luna)',
              'sitio':'23 m² Torre Mar + 3 m² Torre Luna\nBlvd. Kukulkán Km. 16.5, Cancún, Q.Roo',
              'plazo':'10 años 01-nov-2025 a 31-oct-2035\n(conv. mod. contrato 01-nov-2010)',
              'renta':'$347,557.98 MN/año + IVA',
              'incremento':'Anual INPC\n(en septiembre)',
              'deposito':'No especificado\nen el convenio',
              'penalizacion':'Per contrato original'},
  {'no':'14', 'arrendatario':'Canalizaciones y Accesos Profesionales\nS. de R.L. de C.V. (CAPSA)',
              'hotel':'FA Condesa Cancún\n(contrato mensual)',
              'sitio':'Azotea\nBlvd. Kukulkán Km. 16.5, Cancún, Q.Roo',
              'plazo':'10 años forz.\n15-ago-2019 a 15-ago-2029',
              'renta':'$20,000 MN/mes + IVA',
              'incremento':'Anual INPC\n(1° y 12° mes)',
              'deposito':'2 meses\n= $40,000 MN',
              'penalizacion':'Rentas faltantes\npor vencer'},
  {'no':'15', 'arrendatario':'Canalizaciones y Accesos Profesionales\nS. de R.L. de C.V. (CAPSA) — convenio',
              'hotel':'Fiesta Inn Durango',
              'sitio':'Azotea 30 m²\nBlvd. Felipe Pescador 1401, Durango, Dgo.',
              'plazo':'Extendido a 12-feb-2030\n(5 años forz. desde feb-2025)',
              'renta':'$378,048.58 MN/año + IVA\n(vigente al convenio)',
              'incremento':'Anual INPC\n(en septiembre)',
              'deposito':'No especificado',
              'penalizacion':'Rentas faltantes\npor vencer'},
  {'no':'16', 'arrendatario':'Canalizaciones y Accesos Profesionales\nS. de R.L. de C.V. (CAPSA)',
              'hotel':'Fiesta Inn Cuautitlán\n(Edomex)',
              'sitio':'Azotea 85.52 m²\nAv. Chalma s/n esq. Méx-Qro Lote 8, Cuautitlán Izcalli',
              'plazo':'5 años forz.\n01-ago-2024 a 01-ago-2029',
              'renta':'$385,583.66 MN/año ant. + IVA',
              'incremento':'Anual INPC\n(+5% al renovar)',
              'deposito':'No especificado',
              'penalizacion':'Renta vigente × meses\nfaltantes + IVA'},
  {'no':'17', 'arrendatario':'Canalizaciones y Accesos Profesionales\nS. de R.L. de C.V. (CAPSA)',
              'hotel':'Camino Real Puebla',
              'sitio':'Azotea 36 m²\nBlvd. Atlixcayotl Km 5, Fracc. La Vista, Puebla',
              'plazo':'5 años forz.\n01-feb-2024 a 01-feb-2029',
              'renta':'$437,668.81 MN/año ant. + IVA',
              'incremento':'Anual INPC\n(+5% al renovar)',
              'deposito':'No especificado',
              'penalizacion':'Renta vigente × meses\nfaltantes + IVA'},
]

col_labels = [
    '#',
    'ARRENDATARIO',
    'HOTEL',
    'SITIO / SUPERFICIE\nY UBICACIÓN',
    'PLAZO / VIGENCIA',
    'RENTA',
    'FECHA / CRITERIO\nDE INCREMENTO',
    'DEPÓSITO EN\nGARANTÍA',
    'PENALIZACIÓN POR\nRESCISIÓN ANTICIP.',
]
keys = ['no','arrendatario','hotel','sitio','plazo','renta','incremento','deposito','penalizacion']
col_widths = [0.5, 5.8, 3.5, 5.5, 4.2, 4.5, 2.8, 2.8, 4.4]

n_rows = len(contratos)
n_cols = len(col_labels)
row_height = 1.25

fig_w = sum(col_widths) + 0.5   # ~34.5"
fig_h = n_rows * row_height + 2.6
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.axis('off')

fig.suptitle(
    'FIBRA HOTELERA (FIHO) — Cuadro Comparativo de Contratos de Arrendamiento de Antenas (17 contratos)',
    fontsize=15, fontweight='bold', y=0.997, x=0.5, ha='center'
)

header_color = '#1a3a5c'
row_colors = ['#f0f4f8', '#dce8f3']

cell_text, cell_colors = [], []
for i, c in enumerate(contratos):
    cell_text.append([c[k] for k in keys])
    cell_colors.append([row_colors[i % 2]] * n_cols)

table = ax.table(
    cellText=cell_text,
    colLabels=col_labels,
    cellColours=cell_colors,
    colWidths=[w / fig_w for w in col_widths],
    loc='center',
    cellLoc='center',
)
table.auto_set_font_size(False)
table.set_fontsize(9.5)

for j in range(n_cols):
    cell = table[0, j]
    cell.set_facecolor(header_color)
    cell.set_text_props(color='white', fontweight='bold', fontsize=10.0)
    cell.set_height(0.05)

for i in range(1, n_rows + 1):
    for j in range(n_cols):
        cell = table[i, j]
        cell.set_height(row_height / fig_h)
        cell.PAD = 0.022

plt.tight_layout(rect=[0, 0, 1, 0.993])
out = '/home/user/Contratos-Arrendamiento/cuadro_antenas.png'
plt.savefig(out, dpi=120, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"Guardado: {out}")
