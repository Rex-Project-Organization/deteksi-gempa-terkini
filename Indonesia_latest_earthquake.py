"""
Aplikasi Deteksi Gempa Terkini
"""
import gempaTerkini as gT

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gT.data_extract()
    gT.show_data(result)
