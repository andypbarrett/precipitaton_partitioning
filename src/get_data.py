import zipfile
from hda import Client, Configuration

DATASET_ID = "EO:ECMWF:DAT:REANALYSIS_ERA5_SINGLE_LEVELS_MONTHLY_MEANS"

YEAR_BEGIN = 1979
YEAR_END = 2023

query = {
    "dataset_id": DATASET_ID,
    "product_type": [
        "monthly_averaged_reanalysis"
        ],
    "variable": [
        "Total Precipitation" ,
        "Snowfall" ,
        "2m_temperature"
        ],
    "year": [str(yr) for yr in range(YEAR_BEGIN, YEAR_END+1)],
    "month": [f"{mo:02d}" for mo in range(1,13)],
    "time": [
        "00:00",
        "06:00",
        "12:00",
        "18:00"
        ],
    "bbox": [
        -180,
        90,
        180,
        60
        ],
    "format": "netcdf",
    "itemsPerPage": 200,
    "startIndex": 0
    }


def main():
    c = Client(max_workers=8, progress=True)

#    query = {
#        'dataset_id': 'EO:EUM:DAT:SENTINEL-3:OL_1_EFR___',
#        'dtstart': '2023-07-03T13:59:00.000Z',
#        'dtend': '2023-07-03T14:03:00.000Z',
#        }
    matches = c.search(query)

    if len(matches.results) > 0:
        print('Downloading...')
        matches.download(download_dir="data")
    else:
        print(f"No matches found for query")

    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

if __name__ == "__main__":
    main()
