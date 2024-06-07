"""
Aplikasi Deteksi Gempa Terkini
"""
import gempaTerkini as gt

if __name__ == '__main__':
    print('Aplikasi utama')

    id_earthquake = gt.GempaTerkini('https://www.bmkg.go.id/')
    id_earthquake.show_description()
    id_earthquake.run()
