import json
import requests

def ambil_data_hari_ini():
    url = 'https://covid19.ngodingpython.com/hari-ini/'
    r = requests.get(url)
    data = json.loads(r.text)
    data_hari_ini = {'tanggal':data['data']['tanggal'],
                     'positif':data['data']['total_kasus'],
                     'perawatan':data['data']['total_perawatan'],
                     'sembuh':data['data']['total_sembuh'],
                     'meninggal':data['data']['total_meninggal'],
                     'positif_harian':data['data']['kasus_harian'],
                     'perawatan_harian':data['data']['perawatan_harian'],
                     'sembuh_harian':data['data']['sembuh_harian'],
                     'meninggal_harian':data['data']['meninggal_harian']}
    return data_hari_ini

def rekapitulasi():
    url = 'https://covid19.ngodingpython.com/kumulatif/'
    r = requests.get(url)
    data = json.loads(r.text)
    indexer = None
    data_rekap = {'label':[],
                  'positif':[],
                  'perawatan':[],
                  'sembuh':[],
                  'meninggal':[]}
    if data['data'][-1]['total_kasus'] is None:
        indexer = -1
    for item in data['data'][:indexer]:
        data_rekap['label'].append(item['tanggal'])
        data_rekap['positif'].append(item['total_kasus'])
        data_rekap['perawatan'].append(item['total_perawatan'])
        data_rekap['sembuh'].append(item['total_sembuh'])
        data_rekap['meninggal'].append(item['total_meninggal'])
    return data_rekap

def rekapitulasi_tabel():
    url = 'https://covid19.ngodingpython.com/kumulatif/'
    r = requests.get(url)
    data = json.loads(r.text)
    indexer = None
    data_rekap = []
    if data['data'][-1]['total_kasus'] is None:
        indexer = -1
    for item in data['data'][:indexer]:
        data_rekap.append(item)
    return data_rekap


def get_daerah(text):
    url = f'https://covid19.ngodingpython.com/daerah?lok={text}'
    r = requests.get(url)
    data = json.loads(r.text)
    return data['provinsi'], data['data']
