from django.shortcuts import render,redirect,HttpResponse
from . models import *
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import re
import requests.exceptions
from collections import Counter
# Create your views here.

def index(request):
    context = {}
    if request.method=="POST":
        url = request.POST['url']
        try:
            reqs = requests.get(url)
            ssl_enabled = reqs.status_code
            soup = BeautifulSoup(reqs.text, 'html.parser')

            # displaying the title
            meta_title = ''
            for title in soup.find_all('title'):
                meta_title = title.get_text()
            meta_title_without_space = len(meta_title) - meta_title.count(" ")

            # displaying the description
            soup_meta_desc = BeautifulSoup(reqs.content, 'html.parser')
            meta_tag = soup_meta_desc.findAll('meta')
            meta_tag_content = ''
            meta_tag_name = ''
            for x in meta_tag:
                if 'name' in x.attrs.keys() and x.attrs['name'].strip().lower() in ['description', 'keywords']:
                    meta_tag_name = x.attrs['name']
                    meta_tag_content = x.attrs['content']
            meta_desc_without_space = len(meta_tag_content) - meta_tag_content.count(" ")

            # displaying the alt tag
            with_alt_tag = []
            without_alt_tag = []
            without_desc = []
            meta_tagg = soup_meta_desc.findAll('img')
            for x in meta_tagg:
                    if 'alt' in x.attrs.keys():
                        if len(x.attrs.get('alt'))>0:
                            pass
                        else:
                            without_alt_tag.append(x.attrs.get('alt'))
                    else:
                        without_alt_tag.append(x.attrs.get('alt'))


            #display top most frequent ten words
            listed = ['them', 'the', 'and', 'not', 'but', 'that', 'these', 'were', 'being', 'been', 'have', 'having',
                      'does', 'are', 'was', 'has', 'had', 'did', 'will', 'their', 'thier', 'these', 'which', 'what', 'why',
                      'whose', 'whom', 'those', 'where', 'when', 'how', 'who','for','can','you','our','with','your','there','either','whatever','ever'
                      ,'myself','yourself','himself','herself','itself','oneself','ourselves','yourselves','themselves']
            wordlist = []
            source_code = requests.get(url).text
            soup = BeautifulSoup(source_code, 'html.parser')
            souped = str(soup)
            elm = 'style="'
            inlinestyle_used = 0
            if elm in souped:
                inlinestyle_used = souped.count(elm)
            elm1 = "schema.org"
            schema_used = 0
            if elm1 in souped:
                schema_used = souped.count(elm1)
            for each_text in soup.findAll(['h1','h2','h3','h4','h5','h6','p','strong','a','i','b','u','table']):
                content = each_text.text
                words = content.lower().split()
                for each_word in words:
                    if each_word not in listed and len(each_word) >= 5:
                        wordlist.append(each_word)
            clean_list = []
            for word in wordlist:
                symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

                for i in range(len(symbols)):
                    word = word.replace(symbols[i], '')
                if len(word) > 0:
                    clean_list.append(word)
            word_count = {}
            for word in clean_list:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            c = Counter(word_count)
            top_frequent = c.most_common(10)
            top_frequent_words = top_frequent



            #display top two togather ten words
            wordlist_two = []
            source_code_two = requests.get(url).text
            soup_two = BeautifulSoup(source_code_two, 'html.parser')
            for each_text_two in soup_two.findAll(['h1','h2','h3','h4','h5','h6','p','strong','a','i','b','u','table']):
                content_two = each_text_two.text
                result = content_two.lower().split()
                new_result = []
                for res in result:
                    if res not in listed and len(res) >= 4:
                        new_result.append(res)
                words_two = [' '.join(pair) for pair in zip(new_result, new_result[1:])]
                for each_word_two in words_two:
                    wordlist_two.append(each_word_two)

            clean_list_two = []
            for word_two in wordlist_two:
                symbols_two = "!@#$%^&*()_-+={[}]|\;:\"<>?/.,£0123456789×"

                for i_two in range(len(symbols_two)):
                    word_two = word_two.replace(symbols_two[i_two], '')
                if len(word_two) > 0:
                    clean_list_two.append(word_two)
            word_count_two = {}
            for word_two in clean_list_two:
                if word_two in word_count_two:
                    word_count_two[word_two] += 1
                else:
                    word_count_two[word_two] = 1
            c_two = Counter(word_count_two)
            top_two_togather_words = c_two.most_common(10)





            #display top three togather ten words
            wordlist_three = []
            source_code_three = requests.get(url).text
            soup_three = BeautifulSoup(source_code_three, 'html.parser')
            for each_text_three in soup_three.findAll(['h1','h2','h3','h4','h5','h6','p','strong','a','i','b','u','table']):
                content_three = each_text_three.text
                result = content_three.lower().split()
                new_result = []
                for res in result:
                    if res not in listed and len(res) >= 4:
                        new_result.append(res)
                words_three = [' '.join(pair) for pair in zip(new_result, new_result[1:],new_result[2:])]
                for each_word_three in words_three:
                        wordlist_three.append(each_word_three)
            clean_list_three = []
            for word_three in wordlist_three:
                symbols_three = "!@#$%^*()_-+={[}]|\;:\"<>?/.,0123456789£×"
                for i_three in range(len(symbols_three)):
                    word_three = word_three.replace(symbols_three[i_three], '')
                if len(word_three) > 0:
                    clean_list_three.append(word_three)
            word_count_three = {}
            for word_three in clean_list_three:
                if word_three in word_count_three:
                    word_count_three[word_three] += 1
                else:
                    word_count_three[word_three] = 1
            c_three = Counter(word_count_three)
            top_three_togather_words = c_three.most_common(10)

            #display number of headings h1,h2,.....,h6
            h1_tag = soup_meta_desc.findAll('h1')
            h2_tag = soup_meta_desc.findAll('h2')
            h3_tag = soup_meta_desc.findAll('h3')
            h4_tag = soup_meta_desc.findAll('h4')
            h5_tag = soup_meta_desc.findAll('h5')
            h6_tag = soup_meta_desc.findAll('h6')

            #Amount of content
            words_length = 0
            for each_text in soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'strong','i', 'b', 'u', 'table','span','a']):
                content = each_text.text
                words = content.lower().split()
                words_length = words_length + len(words)


            #noindex and unfollow
            tag_exists = 'nothing'
            for x in meta_tag:
                if 'name' in x.attrs.keys() and x.attrs['name'].strip().lower() in ['robots', 'keywords']:
                    meta_tag_index_name = x.attrs['name']
                    meta_tag_index_content = x.attrs['content'].lower()
                    if 'noindex' in meta_tag_index_content and 'nofollow' in meta_tag_index_content:
                        tag_exists = "both"
                    elif 'noindex' in meta_tag_index_content:
                        tag_exists = "noindex"
                    elif 'nofollow' in meta_tag_index_content:
                        tag_exists = "nofollow"
                    else:
                        tag_exists = "doesnot"
            favicon = soup_meta_desc.findAll('link')
            has_favicon = False
            for icon in favicon:
                if 'href' in icon.attrs.keys():
                    meta_link = icon.attrs['href']
                    if 'favicon'.lower() in meta_link:
                        has_favicon = True


            #extract emails
            to = []
            EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            session = HTMLSession()
            r = session.get(url)
            for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
                if re_match.group() not in to:
                    to.append(re_match.group())

            #Check social links
            facebook = "https://www.facebook.com"
            twitter = "https://twitter.com"
            instagram = "https://www.instagram.com"
            linkedin = "https://www.linkedin.com"
            sn_links = soup_meta_desc.findAll('a')
            facebook_link = False
            twitter_link = False
            instagram_link = False
            linkedin_link = False
            for link in sn_links:
                if 'href' in link.attrs.keys():
                    if facebook in link.attrs['href']:
                        facebook_link = True
            for link in sn_links:
                if 'href' in link.attrs.keys():
                    if twitter in link.attrs['href']:
                        twitter_link = True
            for link in sn_links:
                if 'href' in link.attrs.keys():
                    if instagram in link.attrs['href']:
                        instagram_link = True
            for link in sn_links:
                if 'href' in link.attrs.keys():
                    if linkedin in link.attrs['href']:
                        linkedin_link = True

            #twitter card
            twitter_cards = False
            for x in meta_tag:
                if 'name' in x.attrs.keys() and x.attrs['name'].lower() in ['twitter:card', 'keywords']:
                    twitter_cards = True

            #open graph facebook
            open_graph = False
            o_g = 'og:'
            for x in meta_tag:
                if 'property' in x.attrs.keys():
                    if o_g in x.attrs['property']:
                        open_graph = True

            # robot file
            if url[-1] == '/':
                url_slash = url
            else:
                url_slash = url + '/'
            exists_robot_file = False
            new_url_robot = requests.get(url_slash + 'robots.txt')
            if new_url_robot.status_code == 200:
                exists_robot_file = True


            # xml file
            new_url_xml = requests.get(url_slash + 'sitemap.xml')
            exists_xml_file = False
            if new_url_xml.status_code == 200:
                exists_xml_file = True



            #context here
            context['meta_title'] = meta_title
            context['meta_title_char'] = meta_title_without_space
            context['meta_tag_content'] = meta_tag_content
            context['meta_tag_name'] = meta_tag_name
            context['meta_desc_without_space'] = meta_desc_without_space
            context['total_img'] = meta_tagg
            context['with_alt_tag'] = with_alt_tag
            context['without_desc'] = without_desc
            context['without_alt_tag'] = without_alt_tag
            context['h1_tag'] = h1_tag
            context['h2_tag'] = h2_tag
            context['h3_tag'] = h3_tag
            context['h4_tag'] = h4_tag
            context['h5_tag'] = h5_tag
            context['h6_tag'] = h6_tag
            context['top_frequent_words'] = top_frequent_words
            context['top_two_togather_words'] = top_two_togather_words
            context['top_three_togather_words'] = top_three_togather_words
            context['words_length'] = words_length
            context['tag_exists'] = tag_exists
            context['has_favicon'] = has_favicon
            context['ssl_enabled'] = ssl_enabled
            context['emails'] = to
            context['inlinestyle_used'] = inlinestyle_used
            context['facebook_link'] = facebook_link
            context['twitter_link'] = twitter_link
            context['instagram_link'] = instagram_link
            context['linkedin_link'] = linkedin_link
            context['open_graph'] = open_graph
            context['exists_robot_file'] = exists_robot_file
            context['exists_xml_file'] = exists_xml_file
            context['schema_used'] = schema_used
            context['twitter_cards'] = twitter_cards
            context['url'] = url
        except:
            context["raise_error"] = "ERROR Occurred or Something went wrong: Please Enter Valid URL"
        return render(request,"index.html", context)
    return render(request,"index.html", context)

def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        content = Subscribe(email=email)
        content.save()
        messages.success(request,"Successfully Subscribed: Check your Email")
        try:
            send_mail(f'From (No Name)', f'Hi, someone Successfully subscribed using this email {email}',email, ['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        try:
            send_mail(f'From Admin', f'Hi you successfully subscribed using {email} email', 'talhasarwar289@gmail.com',[email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('index')
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        website = request.POST['website']
        message = request.POST['message']
        if len(phone) < 10 or len(phone) > 20:
            messages.error(request,"Invalid Number: Phone Number Length must be minimum to 10 and maximum to 20")
            return redirect('index')
        content = Signup(name=name,email=email,phone=phone,website=website,message=message)
        content.save()
        messages.success(request, "You have Successfully Signup")
        return redirect('index')
    return render(request,"index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        website = request.POST['website']
        company = request.POST['company']
        message = request.POST['message']
        budget = request.POST['budget']
        if len(phone) < 10 or len(phone) > 20:
            messages.error(request,"Invalid Number: Phone Number Length must be minimum to 10 and maximum to 20")
            return redirect('index')
        content = Contact(name=name,email=email,phone=phone,website=website,company=company,budget=budget,message=message)
        content.save()
        try:
            send_mail(f'From {name}', f'Hi, {name} wants to contact with you, \nMore Details are mentioned below: '
                                      f' \nEmail: "{email}",\nMessage: "{message}",\nWebsite: "{website}",\nPhone: "{phone}",\nCompany: "{company}",'
                                      f'\nBudget: "{budget}"',email, ['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        try:
            send_mail(f'From Admin', f'Hi {name}, Your Email has been successfully recieved to admin. we will contact with you soon. your details are mentioned below:'
                                      f' \nEmail: "{email}",\nMessage: "{message}",\nWebsite: "{website}",\nPhone: "{phone}",\nCompany: "{company}",'
                                      f'\nBudget: "{budget}"', 'talhasarwar289@gmail.com',[email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, "Your email successfully recieved to admin! Check your email too")
        return redirect('index')
    return render(request,"index.html")

def businessale(request):
    return render(request,"BusinesSale/index.html")

def businessrapid(request):
    return render(request,"BusinessRapid/index.html")

def businessuccess(request):
    return render(request,"BusinesSuccess/index.html")

def chelseadentalclinic(request):
    return render(request,"Dental/index.html")
def team(request):
    return render(request,"Dental/meet-the-team.html")

def electric_mr(request):
    return render(request,"Electrition/index.html")

def ratedpeople(request):
    return render(request,"RatedPeople/index.html")