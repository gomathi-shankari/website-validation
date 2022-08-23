from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import pymongo

import http.client as httplib

def printtohtml(alist, status, file):

    html ="<html>\n<head></head>\n<style>p{margin:0 !important;} h1{text-align: center; font-family:Courier New;} table, th, td {border: 1px solid; text-align:center;} table{ margin-left:auto; margin-right:auto; background-color: #f6f6f6;}</style> \n <body> \n"

    title = "Website Validation"

    html +='\n<h1>' + title + '</h1>\n ' + '<br>' + '<br>\n'

    headin1 = "Links"
    headin2 = "Status "
    headin3 =" Reason/ Error Code "
    headin4 ="Ticket"

    html += '<table>' + '<tr>' + '<th>' + headin1 + '</th>' + '<th>' + headin2 + '</th>' + '<th>' + headin3 + '</th>' + '<th>' + headin4 + '</th>'+ '</tr>'


    for i,a,x,s in zip(alist, status, reason,tick):
        html+= '<tr>' + '\n<td>' + i + '</td> ' + '<td>' + a + '</td>' + '<td>' + str(x) + '</td>\n'
        if s =="\t":
            html+= '<td>' + s + '</td>\n'
        else:
            html+= '<td>' + '<a href ="https://www.google.com">' + s + '</a>' + '</td>\n'

    with open(file ,'w') as f:
        f.write(html + "</tr> </table>\n</body>\n</html>")


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["link"]
mycollection = db["validapp_link"]


alist=[]
item_details = mycollection.find()
for i in item_details:
    alist.append(i['link'])
print(alist)

append_str = "https://"
status=[]
reason=[]
for i in alist:
    if "https" in i:
        req = Request(i)
        try:
            response = urlopen(req)

        except HTTPError as e:
            status.append('fail')
            reason.append(e.code)
            print('Error code: ', e.code, i)

        except URLError as e:
            status.append('fail')
            reason.append(e.reason)
            print('Reason: ', e.reason, i)


        else:
            status.append('success')
            reason.append("ok")

    else:
        pre_res = append_str + i
        req1 = Request(pre_res)
        try:
            response = urlopen(req1)
        except HTTPError as e:
            status.append('fail')
            reason.append(e.code)
            print('Error code: ', e.code, i)
        except URLError as e:
            status.append('fail')
            reason.append(e.reason)
            print('Reason: ', e.reason, i)

        else:
            status.append('success')
            reason.append("ok")

tick =[]
for s in status:
    if s=="success":
        tick.append("\t")
    else:
        tick.append("Raise Ticket")

# dictionary = dict(zip(alist,status))
# value = {i for i in dictionary if dictionary[i]=="fail"}
# print("key by value:",value)

    # else:
    #     conn = httplib.HTTPConnection(i)
    #     conn.request("HEAD", "/")
    #     r1 = conn.getresponse()
    #
    #     if r1.status==200:
    #         status.append('success')
    #     else:
    #         status.append("fail")

printtohtml(alist, status, 'webpage.html')