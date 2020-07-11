import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)

  # HTML 전체 로드
  soup = BeautifulSoup(result.text, "html.parser")

  # 페이지 번호 element 추출
  pagination = soup.find("div", {"class": "pagination"})

  # 페이지 번호 내의 anchor로 구성된 element 추출
  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]: # 마지막 요소 제외
  # span 내의 페이지 번호만 추출
    pages.append(int(link.string))

  max_page = pages[-1] 

  # 총 페이지 개수 리턴
  return max_page

# 직무명, 회사, 위치, 회사 링크 추출
def extract_job(html):
  # 직무명 추출
  title = html.find("h2", {"class":"title"}).find("a")["title"]

  # 회사명 추출
  company = html.find("span", {"class":"company"})
  # 회사에 링크가 있는지 없는지 체크 (있으면 anchor 저장, 없으면 span 저장)
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = company_anchor.string
  else:
    company = company.string
  company = company.strip() # 공백 모두 제거 : strip()

  # 위치 추출
  # 아래 구문은 원하는 div를 찾은 다음, 그 div의 속성을 [""]로 접근하는 동작을 함
  location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
  
  # 회사 링크 추출
  job_id = html["data-jk"]
  apply_link = f"https://www.indeed.com/viewjob?jk={job_id}"

  # 직무명, 회사, 위치, 회사 링크로 이루어진 딕셔너리 리턴
  return {'title':title, 'company': company, 'location':location, 'apply_link': apply_link
  }

# 구인 정보 추출
def extract_jobs(last_pages):
  jobs = [] # 빈 리스트 생성
  for page in range(last_pages): # 페이지 처음부터 끝까지 스크래핑
    print(f"Scrapping Indeed {page}")

    #html 문서에서 구인 정보 엘리먼트 추출
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    
    # 각 엘리먼트마다 직무, 회사명, 위치, 회사 링크 등 정보 추출
    for result in results:
      job = extract_job(result)
      jobs.append(job)

  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs