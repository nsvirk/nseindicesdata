import os
from urllib.parse import urljoin

# Base URL for NSE Indices
NSE_INDICES_BASE_URL = "https://niftyindices.com/IndexConstituent/"

# Dictionary mapping index names to file names
NSE_INDICES_FILE_MAP = {
    "NSE:NIFTY 50": "ind_nifty50list.csv",
    "NSE:NIFTY NEXT 50": "ind_niftynext50list.csv",
    "NSE:NIFTY 100": "ind_nifty100list.csv",
    "NSE:NIFTY 200": "ind_nifty200list.csv",
    "NSE:NIFTY TOTAL MARKET": "ind_niftytotalmarket_list.csv",
    "NSE:NIFTY 500": "ind_nifty500list.csv",
    "NSE:NIFTY MIDCAP 50": "ind_niftymidcap50list.csv",
    "NSE:NIFTY MIDCAP 100": "ind_niftymidcap100list.csv",
    "NSE:NIFTY SMALLCAP 100": "ind_niftysmallcap100list.csv",
    "NSE:NIFTY AUTO": "ind_niftyautolist.csv",
    "NSE:NIFTY BANK": "ind_niftybanklist.csv",
    "NSE:NIFTY FINANCIAL SERVICES": "ind_niftyfinancelist.csv",
    "NSE:NIFTY HEALTHCARE": "ind_niftyhealthcarelist.csv",
    "NSE:NIFTY IT": "ind_niftyitlist.csv",
    "NSE:NIFTY FMCG": "ind_niftyfmcglist.csv",
    "NSE:NIFTY METAL": "ind_niftymetallist.csv",
    "NSE:NIFTY PHARMA": "ind_niftypharmalist.csv",
    "NSE:NIFTY REALTY": "ind_niftyrealtylist.csv",
    "NSE:NIFTY CONSUMER DURABLES": "ind_niftyconsumerdurableslist.csv",
    "NSE:NIFTY OIL GAS": "ind_niftyoilgaslist.csv",
}


def main():
    # Create the 'csvfiles' directory if it doesn't exist
    os.makedirs("csvfiles", exist_ok=True)

    # Download each CSV file
    for index_name, file_name in NSE_INDICES_FILE_MAP.items():
        url = urljoin(NSE_INDICES_BASE_URL, file_name)
        file_path = os.path.join("csvfiles", file_name)
        print(url)


if __name__ == "__main__":
    main()
