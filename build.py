import json, html as htmlmod

with open('../BlackHole ESAJ - 20260324.204042/data_export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

movs_js = {}
for proc, items in data['movimentacoes'].items():
    movs_js[proc] = []
    for m in items:
        movs_js[proc].append({
            'data': m['data'],
            'titulo': m['titulo'],
            'desc': m['detalhe'].replace('\n', ' ').replace('\r', '') if m['detalhe'] else ''
        })

capas_js = {}
for proc, c in data['capas'].items():
    capas_js[proc] = {
        'classe': c.get('CLASSE',''),
        'assunto': c.get('ASSUNTO',''),
        'foro': c.get('FORO','').replace('Foro de ',''),
        'vara': c.get('VARA',''),
        'juiz': c.get('JUIZ',''),
        'distribuicao': c.get('DISTRIBUICAO',''),
        'area': c.get('AREA',''),
        'valor': c.get('VALOR_ACAO',''),
        'tags': c.get('TAGS',''),
        'parte_ativa': c.get('PARTE_ATIVA',''),
        'adv_ativa': c.get('ADV_ATIVA',''),
        'parte_passiva': c.get('PARTE_PASSIVA',''),
        'adv_passiva': c.get('ADV_PASSIVA',''),
        'outros': c.get('OUTROS_PARTES',''),
    }

print(json.dumps({'movimentacoes': movs_js, 'capas': capas_js}, ensure_ascii=False, indent=1)[:500])
print(f"\nTotal movs exported: {sum(len(v) for v in movs_js.values())}")

with open('data_movs.js', 'w', encoding='utf-8') as f:
    f.write('const MOVIMENTACOES_ESAJ = ')
    json.dump(movs_js, f, ensure_ascii=False)
    f.write(';\n')
    f.write('const CAPAS_ESAJ = ')
    json.dump(capas_js, f, ensure_ascii=False)
    f.write(';\n')

print("Written data_movs.js")
