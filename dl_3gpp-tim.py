import os
import requests

def download_ts(ts_number):
    url = f"https://www.etsi.org/deliver/etsi_ts/1{ts_number[:3]}00_{ts_number[:3]}199/{ts_spec_number}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        pdf_url = None
        for line in response.text.splitlines():
            if "pdf" in line:
                pdf_url = line.split('"')[1]
                break
        
        if pdf_url:
            pdf_response = requests.get(pdf_url)
            if pdf_response.status_code == 200:
                with open(f"{ts_spec}.pdf", "wb") as f:
                    f.write(pdf_response.content)
                print(f"Downloaded {ts_number}.pdf successfully!")
            else:
                print(f"Failed to download {ts_number}.pdf. Status code: {pdf_response.status_code}")
        else:
            print(f"No PDF file found for {ts_number}.")
    else:
        print(f"Failed to retrieve {ts_number}. Status code: {response.status_code}")

def main():
    while True:
        try:
            ts_number = input("Enter the 3GPP Technical Specification number (e.g., 122.135): ")
            #ts_spec_number = input("Enter the intended number")
            download_ts(ts_number)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != "y":
            break

if __name__ == "__main__":
    main()