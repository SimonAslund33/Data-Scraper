from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# URL of the LinkedIn jobs page (replace with the actual URL)
url = "https://www.linkedin.com/jobs/search?keywords=Programutveckling&location=Stockholms%20kommun%2C%20Stockholms%20l%C3%A4n%2C%20Sverige&geoId=100907646&trk=public_jobs_jobs-search-bar_search-submit&original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3DProgramutveckling%26location%3DSverige%26geoId%3D105117694%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26position%3D1%26pageNum%3D0&position=1&pageNum=0"

# Open the URL
driver.get(url)

# Wait for the job section to load
wait = WebDriverWait(driver, 10)
job_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section[2]/ul')))

# Find all job entries
job_entries = driver.find_elements(By.XPATH, '//*[@id="main-content"]/section[2]/ul/li')

# Initialize lists to hold job titles and addresses
#job_titles = []
#job_addresses = []
#print(job_entries)
# Iterate over job entries to extract job titles and addresses

for job in job_entries:
    # Extract job title
   
    job_title_element = job.find_element(By.CLASS_NAME, 'base-search-card__title')
    print(job_title_element.text)
    job_location_element = job.find_element(By.CLASS_NAME, 'job-search-card__location')
    print(job_location_element.text)
    job_company_element = job.find_element(By.CLASS_NAME, 'base-search-card__subtitle')
    print(job_company_element.text)
    #job_titles.append(job_title_element.text)
    print("-" * 50)
    job.click

    details_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="details-pane__content details-pane__content--show"]/section[1]')))

    apply_button = driver.find_element(By.XPATH, '//button[@data-tracking-control-name=public_jobs_apply-link-offsite_sign-up-modal]')
    #apply_button = driver.find_element(by=By.CSS_SELECTOR, value="sign-up-modal__outlet top-card-layout__cta mt-2 ml-1.5 h-auto babybear:flex-auto top-card-layout__cta--primary btn-md btn-primary")
    apply_button.click()
    # Wait for the job details pane to load
    #details_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="details-pane__content details-pane__content--show"]/section[1]')))

    # Find the apply button with the specified class name and click it
    #apply_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sign-up-modal__outlet top-card-layout__cta mt-2 ml-1.5 h-auto babybear:flex-auto top-card-layout__cta--primary btn-md btn-primary')))
    #apply_button.click()
    #wait = WebDriverWait(driver, 10)
    #details_section = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="details-pane__content details-pane__content--show"]/section[1]')))
    
    # Extract job address
    #job_address_element = job.find_element(By.XPATH, '//div[@class="base-search-card__metadata"]')
    #job_addresses.append(job_address_element.text)

# Print the job titles and addresses
#for title, address in zip(job_titles, job_addresses):
    #print(f"Job Title: {title}")
    #print(f"Address: {address}\n")
#for i in job_titles:
    #print(i)
    #print("-" * 50)

# Close the WebDriver
#driver.quit()

#//*[@id="main-content"]/section[2]/ul/li
#//*[@class="details-pane__content details-pane__content--show"]/section[1]