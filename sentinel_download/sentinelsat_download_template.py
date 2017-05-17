# Please install python packages pycurl, homora and sentinelsat
# The download from Scihub will fail if the server certificate cannot be verified because no default CA bundle is defined, as on Windows, or when the CA bundle is outdated. In most cases the easiest solution is to install or update `certifi <https: pypi.python.org="" pypi="" certifi="">`_: for example with 'pip install -U certifi'


from datetime import datetime, date
from sentinelsat.sentinel import SentinelAPI, get_coordinates
import pdb

def get_area(latmin, latmax, lonmin, lonmax):
    """Change input coordinates for the query of Sentinel products"""
    assert latmin <= latmax, 'ERROR: invalid lat'
    assert lonmin <= lonmax, 'ERROR: invalid lon'
    return '%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f' % (lonmin, latmin, lonmax, latmin, lonmax, latmax, lonmin, latmax, lonmin, latmin)


"""
user : username of Copernicus Open Access Hub account
password : password of Copernicus Open Access Hub account
area : area(s) of interest
    input with coordinates (e.g. get_area('latmin, latmax, lonmin, lonmax') ) or
    input with file for one or more areas (e.g. get_coordinates('coordinates.geojson') )
api_url: url of Sentinel Scientific Data Hub
path: path where to store the data

Possible keywords of query
------------------------------------
inital_date: (e.g.  '20160101'; datetime(2016, 1, 1, 12, 5); date(2016,1,1))
end_date: (e.g. '20160102'; datetime(2016, 1, 2, 12, 5); date(2016,1,2)) (default setting: end_date=datetime.now())
platformname: (e.g. 'Sentinel-1'; 'Sentinel-2'; 'Sentinel-1 OR Sentinel-2')
polarisationmode: (e.g. 'HH'; 'VV'; 'HV'; 'VH'; 'HH HV'; 'VV VH'; 'HH OR VV VH'; ...)
producttype: (e.g. 'SLC'; 'GRD'; 'OCN'; 'RAW'; 'SLC OR GRD'; ... )
sensoroperationalmode ( e.g. 'SM'; 'IW'; 'EW'; 'SM OR IW'; ...)
orbitnumber
lastorbitnumber
orbitdirection (e.g. 'ascending'; 'decending')
relativeorbitnumber
swathidentifer
cloudcoverpercentage (e.g. '[0 TO 40]')

for possible values and probably more parameters please visit
https://scihub.copernicus.eu/twiki/do/view/SciHubUserGuide/3FullTextSearch#Search_Keywords
"""
print(datetime.now())

### login information Copernicus Open Access Hub (https://scihub.copernicus.eu/dhus/#/home)
api = SentinelAPI('user', 'password', api_url='https://scihub.copernicus.eu/apihub/')

### Sentinel data search
# products = api.query(area=get_coordinates('/media/tweiss/Work/coordinates_wallerfing.geojson'), initial_date='20151219', end_date=datetime(2015, 12, 24), platformname='Sentinel-1', producttype='GRD')
products = api.query(get_area(48.68, 48.70, 12.89 ,12.999), '20151219', datetime(2015, 12, 29), platformname='Sentinel-1')
print(api._last_query)
print('%s product results for your query. The products need %s Gb disk space') % (len(products), api.get_products_size(products))

### convert to Pandas DataFrame
products_df = api.to_dataframe(products)
print(products_df.index.values)

### download all query products
path = '/media/tweiss/Daten'
result = api.download_all(products, directory_path=path, max_attempts=10, checksum=True, check_existing=True, show_progress=False)
print('Downloaded files:')
print(result.viewkeys())


"""
Change and/or sort query results
"""
# ### sort and limit to first 5 sorted products
# products_df_sorted = products_df.sort_values(['ingestiondate', 'producttype'], ascending=[True, True])
# products_df_sorted = products_df_sorted.head(1)

# ### download (sorted and reduced) products in order
# path = '/media/tweiss/Daten'
# result={}
# for product_id in products_df_sorted["id"]:
#   path, product_info = api.download(product_id, directory_path=path, max_attempts=10, checksum=True, check_existing=True, show_progress=False)
#   result[path] = product_info
# print('Downloaded files:')
# print(result.viewkeys())

print(datetime.now())




