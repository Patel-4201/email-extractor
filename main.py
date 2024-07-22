import requests

# urls = ["https://shantanuuchak.tech","https://quastech.in",
#        "https://innovaccer.com/contact-us",
#        "https://www.infogain.com/about/contact-us/"
#        ]
# res = requests.get('https://shantanuuchak.tech')

# func to split on 
def split_quote(text):
  return text.split('"')

# remove malto
def remove_malto(text):
  return text.replace("mailto:","")
  
# func to find email in a list 
def find_emails(data_list):
  email_list = []
  for el in data_list:
    if "@" in el and "." in el and "/" not in el:
      email_list.append(remove_malto(el))
  return email_list


# func to request to url
def fetch(url):
  res = requests.get(url)
  if res.status_code ==200:
    return res.text
  print(f"failed with error code {res.status_code}")
  return ""
x = fetch(urls[0])
print(x)

# performing reqeust 
if res.status_code == 200:
  data_list = split_quote(res.text)
  emails = find_emails(data_list)
  print(data_list)
else :
  print(f"request failed. try again {res.status_code}")

# itrating over urls

emails = []

for url in urls:
  data = fetch(url)
  data_list = split_quote(data)
  email_list = find_emails(data_list)
  emails.extend(email_list)
  print(emails)

# unique 
unique_emails = []
for email in emails:
  if email not in unique_emails:
    unique_emails.append(email)

# print(unique_emails)
    
# sets 
email = set(emails)
print(email)

# talking input
urls = []
while True:
  user_input = input("enter your URL or N to exit: ")
  if user_input == "N":
    print("URL list Ready!")
    break

  if "://" not in user_input :
    print("enter invalid URL!")
  else:
    urls.append(user_input)

  emails = []
  
# create emails file
f = open('emails.text','w')
f.write(str(emails))
f.close()