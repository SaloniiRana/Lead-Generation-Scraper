import pandas as pd
from scraper import fetch_page_html, extract_business_info

def run_lead_generation_pipeline():
    print("🚀 Initializing Lead Generation Public Data Scraper...")
    
    # A list of public URLs to target (Replace these with your target public business URLs)
    target_urls = [
        "https://example.com",  # Sample test URL 1
    ]
    
    leads_dataset = []

    for index, url in enumerate(target_urls, start=1):
        print(f"🔍 [{index}/{len(target_urls)}] Scraping target: {url}")
        
        html_data = fetch_page_html(url)
        business_details = extract_business_info(html_data)
        
        if business_details:
            business_details["Source URL"] = url
            leads_dataset.append(business_details)
        else:
            print(f"⚠️ Failed to extract data from: {url}")

    # Convert the scraped data into a structured table
    df = pd.DataFrame(leads_dataset)
    
    # Save the data to a CSV file
    output_file = "generated_leads.csv"
    df.to_csv(output_file, index=False)
    
    print(f"\n✅ Data scraping complete! Leads successfully saved to: {output_file}")

if __name__ == "__main__":
    run_lead_generation_pipeline()
