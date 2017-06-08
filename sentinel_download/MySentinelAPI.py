
from sentinelsat.sentinel import SentinelAPI, get_coordinates
from datetime import datetime

class MySentinelAPI(SentinelAPI):
    def __init__(self, *args, **kwargs):
        super(MySentinelAPI, self).__init__(*args, **kwargs)

    def get_area(self, latmin, latmax, lonmin, lonmax):
        assert latmin <= latmax, 'ERROR: invalid lat'
        assert lonmin <= lonmax, 'ERROR: invalid lon'
        return '%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f' % (lonmin, latmin, lonmax, latmin, lonmax, latmax, lonmin, latmax, lonmin, latmin)


def all_in_one(user, password, area, api_url='https://scihub.copernicus.eu/apihub/', path='./', download='no', initial_date=None, end_date=datetime.now(),  **keywords):

    ### login information Copernicus Open Access Hub (https://scihub.copernicus.eu/dhus/#/home)
    api=MySentinelAPI(user, password, api_url)

    ### read area information
    try:
        geojson=get_coordinates(area)
    except IOError:
        area=area.split(',')
        area=api.get_area(float(area[0]),float(area[1]),float(area[2]),float(area[3]))
        geojson=area

    ### Sentinel data search
    products = api.query(geojson, initial_date, end_date, **keywords)
    # products_df = api.to_dataframe(products)
    print(api._last_query)
    print('%s product results for your query. The products need %s Gb disk space') % (len(products), api.get_products_size(products))
    print([i['title'] for i in products if 'title' in i])

    ### download all query products
    if download == 'yes':
        result = api.download_all(products, directory_path=path, max_attempts=10, checksum=True, check_existing=True, show_progress=False)
        # print('Downloaded files:')
        # print(result.viewkeys())

        return result
    # print(products_df.index.values)
    # return products_df
    # print([i['title'] for i in products if 'title' in i])
    return products





