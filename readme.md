# sentinel_download #
Template to download Sentinel data from the Copernicus Open Access Hub with python package sentinelsat version 0.9.1 (https://github.com/ibamacsr/sentinelsat)

### Getting started ###
* install python packages sentinelsat, pycurl and homora
* sign up at Copernicus Open Access Hub (https://scihub.copernicus.eu/dhus/#/home) 
* change log in information
```python
### login information Copernicus Open Access Hub (https://scihub.copernicus.eu/dhus/#/home)
api = SentinelAPI('user', 'password', api_url='https://scihub.copernicus.eu/apihub/')
```
* change Sentinel data query
```python
### Sentinel data search
products = api.query(area=get_coordinates('/media/tweiss/Work/coordinates_wallerfing.geojson'), initial_date='20151219', end_date=datetime(2015, 12, 24), platformname='Sentinel-1', producttype='GRD')
```
* change storage path
```python
### download all query products
path = '/media/tweiss/Daten'
```