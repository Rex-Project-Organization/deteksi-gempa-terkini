import hamiltoncurrentweather as hct

if __name__ == '__main__':
    print('main app')

    result = hct.data_extract()
    hct.show_data(result)
