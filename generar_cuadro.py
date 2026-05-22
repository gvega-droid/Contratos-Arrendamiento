import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

contratos = [
  {'no':'1',  'arrendatario':'AGRO-PARTES PUEBLA S.A. DE C.V.',              'sup':'179 m²',           'ciudad':'Cuautlancingo, Pue.',        'vigencia':'15-abr-2023 a 15-abr-2028\n(1 año forz. + 4 vol.)',            'renta':'$15,000 MN/mes',                                           'incr':'INPC anual (15 abr)',     'deposito':'2 meses\n= $30,000 MN',           'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Arrendador prorratea $/m³',         'luz':'Arrendatario\ndirecto CFE'},
  {'no':'2',  'arrendatario':'COMERCIAL AUTOMOTRIZ DE LOS ALTOS S.A. DE C.V.','sup':'252 m²',           'ciudad':'Aguascalientes, Ags.',        'vigencia':'01-dic-2024 a 01-dic-2029\n(2 años forz. Arrend. / 3 Arrdor.)', 'renta':'$37,809 MN/mes',                                           'incr':'INPC anual (01 dic)',     'deposito':'2 meses\n= $75,618 MN',           'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Arrendatario\npaga directo',        'luz':'Arrendatario\ndirecto CFE'},
  {'no':'3',  'arrendatario':'BANCO SANTANDER MÉXICO S.A. IBM GFSM',          'sup':'432 m²',           'ciudad':'Cuautitlán Izcalli, Edomex',  'vigencia':'01-sep-2023 a 01-sep-2030\n(5 años forz.; conv. mod.)',         'renta':'$201,691.51 MN/mes\n(desde sep-2024)',                     'incr':'INPC anual (01 sep)',     'deposito':'No espec.\n(convenio mod.)',      'penalizacion':'No espec.\n(convenio mod.)',             'agua':'No espec.\n(convenio mod.)',        'luz':'No espec.\n(convenio mod.)'},
  {'no':'4',  'arrendatario':"WALDO'S DÓLAR MART DE MÉXICO S. DE R.L. DE C.V.",'sup':'853 m²',          'ciudad':'Cuautitlán Izcalli, Edomex',  'vigencia':'02-mar-2024 a 01-mar-2026\n(2 años forz.)',                     'renta':'$117,524 MN/mes',                                          'incr':'INPC anual (abr)',        'deposito':'No especificado',                'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Directo o\nprorrateado $/m³',       'luz':'Arrendatario\ndirecto CFE'},
  {'no':'5',  'arrendatario':'TV AZTECA S.A.B. DE C.V.',                      'sup':'379 m²',           'ciudad':'Acapulco, Guerrero',          'vigencia':'04-jul-2025 a 04-jul-2028\n(3 años forz.)',                     'renta':'$76,717.12 MN/mes\n+ IVA',                                'incr':'INPC + 2 pp anual',      'deposito':'2 meses\n= $204,466.66 MN',      'penalizacion':'No espec.\nrescisión anticip.',        'agua':'Arrendatario\npaga exclusivo',      'luz':'Arrendatario\npaga exclusivo'},
  {'no':'6',  'arrendatario':'TRAIGO TODO S.A.P.I. DE C.V. ("Sonora Grill")', 'sup':'725 m²\n+245 terr.','ciudad':'Hermosillo, Sonora',          'vigencia':'10 años forz.\ndesde Fecha Apertura',                          'renta':'Mayor: $200,000 MN mín.\nó 50% utilidad mensual',         'incr':'INPC anual\n(renta mínima)',     'deposito':'No especificado',                'penalizacion':'Años 1-5: 50%×(prom.×meses)\nAño 6+: renta×meses falt.',   'agua':'Arrendatario\ndirecto/prorrateado',  'luz':'Arrendatario\ndirecto CFE'},
  {'no':'7',  'arrendatario':'SERVICIOS INMOBILIARIOS ALSEA S.A. DE C.V.',    'sup':'450 m²',           'ciudad':'Apodaca, N.L.',               'vigencia':'5 años forz. + 5 vol. + 5 prórroga\n(desde abr-2016)',          'renta':'Mayor: $45,000 MN fija\nó 6% ventas netas',               'incr':'INPC anual\n(renta fija)',      'deposito':'No especificado',                'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Directo o\nprorrateado $/m³',       'luz':'Arrendatario\ndirecto CFE'},
  {'no':'8',  'arrendatario':'OPERADORA HOTELERA INHOUSE S.A.P.I. DE C.V.\n(Hotel completo — León)',    'sup':'12,834 m²',        'ciudad':'León, Guanajuato',           'vigencia':'01-ene-2024 a 31-dic-2028\n(5 años forz.)',                     'renta':'Escalonada: $100k–$450k/mes\nó 20% ingresos (mayor)',     'incr':'No aplica\n(tabla escalonada)', 'deposito':'No especificado',                'penalizacion':'No espec.\n(causales rescisión)',       'agua':'Arrendataria paga\ntodos los servicios',    'luz':'Arrendataria paga\ntodos los servicios'},
  {'no':'9',  'arrendatario':'JULIO CESAR TORRES ROJO (persona física)',       'sup':'103.55 m²',        'ciudad':'Tijuana, B.C.',               'vigencia':'2 años forz.\ndesde Fecha Apertura',                            'renta':'USD $1,800/mes',                                           'incr':'INPC anual',             'deposito':'1 mes\n= USD $1,800',             'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Directo o\nprorrateado $/m³',       'luz':'Arrendatario\ndirecto CFE'},
  {'no':'10', 'arrendatario':'ZAPATA S.A. DE C.V.',                            'sup':'81 m²',            'ciudad':'Cuautitlán Izcalli, Edomex',  'vigencia':'28-oct-2025 a ~oct-2030\n(5 años forz.)',                       'renta':'$32,400 MN/mes',                                           'incr':'INPC anual',             'deposito':'1 mes\n= $32,400 MN',             'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Arrendatario\npaga directo',        'luz':'Arrendatario\ndirecto CFE'},
  {'no':'11', 'arrendatario':'GRUPO POSADAS S.A.B. DE C.V.\n(Hotel completo — Cancún)',                 'sup':'41,413 m²\n(lote)', 'ciudad':'Cancún, Q. Roo',             'vigencia':'Hasta 31-dic-2032\n(cond. suspensiva)',                         'renta':'USD $791,666.65/mes mín.\n+ renta variable',              'incr':'CPI EE.UU. anual',       'deposito':'No especificado',                'penalizacion':'No especificado',                       'agua':'Arrendataria paga\ntodos los servicios',    'luz':'Arrendataria paga\ntodos los servicios'},
  {'no':'12', 'arrendatario':'DIVOL NORTE S.A.P.I. DE C.V.',                  'sup':'1,710 m²',         'ciudad':'Cuautitlán Izcalli, Edomex',  'vigencia':'01-nov-2025 a 31-oct-2045\n(20 años forz.)',                    'renta':'$240,963.27 MN/mes\n($257,706.73 con acceso adic.) + IVA','incr':'INPC anual (ago)',        'deposito':'1 mes\n= $240,963.27 MN',         'penalizacion':'Todas las rentas\nhasta fin del plazo',        'agua':'Arrendatario\npaga exclusivo',      'luz':'Arrendatario\npaga exclusivo'},
  {'no':'13', 'arrendatario':'TIENDAS EXTRA S.A. DE C.V. (Circle K)',          'sup':'200 m²',           'ciudad':'Acapulco, Guerrero',          'vigencia':'15 años desde apertura\n(5 forz. + 10 vol.)',                  'renta':'Mayor: $38,000 MN mín.\nó 8% ventas netas',               'incr':'INPC anual',             'deposito':'1 mes de renta\nvigente',         'penalizacion':'Prom. 12 meses × meses\nfalt. + IVA (exhib. única)',  'agua':'Arrendatario\npaga exclusivo',      'luz':'Arrendatario\npaga exclusivo'},
  {'no':'14', 'arrendatario':'AERO CHARTER DE MÉXICO S.A. DE C.V. (Primeflight)','sup':'123.09 m²',      'ciudad':'Apodaca, N.L.',               'vigencia':'06-nov-2023 a 06-nov-2026\n(3 años forz.)',                     'renta':'$27,537.93 MN/mes',                                        'incr':'INPC anual',             'deposito':'2 meses\n(monto no especif.)',    'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Arrendatario\ncuota consumo',       'luz':'Arrendatario\ndirecto CFE'},
  {'no':'15', 'arrendatario':'T.I. EXPERIENCIAS EN GRUPOS Y CONV. S.A. DE C.V.','sup':'21 m²',           'ciudad':'Cancún, Q. Roo',              'vigencia':'03-feb-2025 a 03-feb-2028\n(3 años forz.)',                     'renta':'USD $3,000/mes + IVA',                                     'incr':'INPC anual',             'deposito':'1 mes\n= USD $3,000',             'penalizacion':'Rentas faltantes\n× plazo forz. + IVA',        'agua':'Arrendatario paga\ny entrega recibos',   'luz':'Arrendatario paga\ny entrega recibos'},
  {'no':'16', 'arrendatario':'QUATTRALIA HOLDING S.A. DE C.V.',                'sup':'750 m²',           'ciudad':'Naucalpan, Edomex',           'vigencia':'17-jun-2025 a 17-jun-2026\n(1 año forz.; conv. mod.)',          'renta':'$1,365,000 MN/año\nen 2 pagos semestral + IVA',         'incr':'No espec.\n(conv. mod.)',  'deposito':'No espec.\n(conv. mod.)',        'penalizacion':'Rentas faltantes\nhasta fin plazo',            'agua':'No espec.\n(conv. mod.)',           'luz':'No espec.\n(conv. mod.)'},
  {'no':'17', 'arrendatario':'DAVID VALDEZ ROMO (persona física)',             'sup':'252 m²',           'ciudad':'Aguascalientes, Ags.',        'vigencia':'04-dic-2025 a 03-dic-2031\n(6 años; conv. mod.)',               'renta':'$21,157.49/mes (oct-mar)\n+ $505,000/mes (abr-may) + IVA','incr':'INPC anual\n(ambos montos)', 'deposito':'No espec.\n(conv. mod.)',       'penalizacion':'No espec.\n(conv. mod.)',                'agua':'No espec.\n(conv. mod.)',           'luz':'No espec.\n(conv. mod.)'},
  {'no':'18', 'arrendatario':'CORPORATIVO EMPRESARIAL SOLAR S.A. DE C.V.',    'sup':'41 m²',            'ciudad':'Monterrey, N.L.',             'vigencia':'01-feb-2024 a 31-ene-2027\n(3 años forz.)',                     'renta':'$10,291 MN/mes',                                           'incr':'INPC anual',             'deposito':'2 meses\n= $20,582 MN',           'penalizacion':'No espec.\n(hoja condiciones)',         'agua':'Cuota recuperación\nenergéticos (desde ene-2025)', 'luz':'Cuota recuperación\nenergéticos (desde ene-2025)'},
  {'no':'19', 'arrendatario':'OPERADORA HOTELERA INHOUSE S.A.P.I. DE C.V.\n(Hotel completo — Cd. Carmen)','sup':'No especificada', 'ciudad':'Cd. del Carmen, Camp.',      'vigencia':'Hasta 30-abr-2029\n(~3 años forz.)',                            'renta':'Escalonada: $100k–$200k/mes\nó 20% ingresos (mayor)',     'incr':'No aplica\n(tabla escalonada)', 'deposito':'No especificado',                'penalizacion':'No espec.\n(causales rescisión)',       'agua':'Arrendataria paga\ntodos los servicios',    'luz':'Arrendataria paga\ntodos los servicios'},
  {'no':'20', 'arrendatario':'ARRENDATARIO CD. OBREGÓN\n(nombre no disponible)','sup':'No disponible',   'ciudad':'Cd. Obregón, Sonora',         'vigencia':'No disponible',                                                 'renta':'No disponible',                                            'incr':'No disponible',          'deposito':'No disponible',                  'penalizacion':'No disponible',                         'agua':'No disponible',             'luz':'No disponible'},
]

col_labels = [
    '#',
    'ARRENDATARIO',
    'SUPER-\nFICIE',
    'CIUDAD / ESTADO',
    'VIGENCIA / PLAZO',
    'RENTA MENSUAL',
    'INCREMENTO\nDE RENTA',
    'DEPÓSITO\nEN GARANTÍA',
    'PENALIZACIÓN POR\nRESCISIÓN ANTICIP.',
]
keys = ['no','arrendatario','sup','ciudad','vigencia','renta','incr','deposito','penalizacion']
# Landscape sin columnas de agua y luz
col_widths = [0.6, 5.5, 1.8, 3.2, 4.8, 4.5, 2.5, 3.5, 5.0]

n_rows = len(contratos)
n_cols = len(col_labels)
row_height = 1.1

fig_w = sum(col_widths) + 0.5   # ≈ 34.1"
fig_h = n_rows * row_height + 2.4  # ≈ 24.4"
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.axis('off')

fig.suptitle(
    'FIBRA HOTELERA (FIHO) — Cuadro Comparativo de Contratos de Arrendamiento (20 contratos)',
    fontsize=14, fontweight='bold', y=0.995, x=0.5, ha='center'
)

header_color = '#1a3a5c'
row_colors = ['#f0f4f8', '#dce8f3']

cell_text, cell_colors = [], []
for i, c in enumerate(contratos):
    cell_text.append([c[k] for k in keys])
    bg = '#ffe0e0' if c['no'] == '20' else row_colors[i % 2]
    cell_colors.append([bg] * n_cols)

table = ax.table(
    cellText=cell_text,
    colLabels=col_labels,
    cellColours=cell_colors,
    colWidths=[w / fig_w for w in col_widths],
    loc='center',
    cellLoc='center',
)
table.auto_set_font_size(False)
table.set_fontsize(9.0)

for j in range(n_cols):
    cell = table[0, j]
    cell.set_facecolor(header_color)
    cell.set_text_props(color='white', fontweight='bold', fontsize=9.5)
    cell.set_height(0.05)

for i in range(1, n_rows + 1):
    for j in range(n_cols):
        cell = table[i, j]
        cell.set_height(row_height / fig_h)
        cell.PAD = 0.022

plt.tight_layout(rect=[0, 0, 1, 0.993])
out = '/home/user/Contratos-Arrendamiento/cuadro_contratos.png'
plt.savefig(out, dpi=120, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"Guardado: {out}")
