"""
Aplikasi Deteksi Gempa Terkini
"""


def data_extract():
    """
    dateTime: date: 31 Mei 2024, time: 05:54:38 WIB
    magnitude: 5.4
    kedalaman: 88 km
    location: LS: 1.48, BT: 134.01
    pusat: 139 km BaratLaut PULAUKARATUNG-SULUT
    keterangan: tidak berpotensi TSUNAMI
    :return:
    """
    data_result = {
        'dateTime': {'date': '31 Mei 2024', 'time': '05:54:38 WIB'},
        'magnitude': 5.4,
        'kedalaman': '88 km',
        'location': {'LU': 1.48, 'BT': 134.01},
        'pusat': '139 km BaratLaut PULAUKARATUNG-SULUT',
        'keterangan': 'tidak berpotensi TSUNAMI',
    }
    return data_result


def show_data(datas):
    print(f'DateTime = {datas['dateTime']['date']}, {datas['dateTime']['time']}')
    print(f'Magnitude = {datas['magnitude']}')
    print(f'kedalaman = {datas['kedalaman']}')
    print(f'location = {datas['location']['LU']}LU - {datas['location']['BT']}BT')
    print(f'pusat = {datas['pusat']}')
    print(f'keterangan = {datas['keterangan']}')


if __name__ == '__main__':
    print('Aplikasi utama')
    result = data_extract()
    show_data(result)
