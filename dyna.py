from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import pymongo

def print2html(statlist,dynalist, file):
    html = "<html>\n<head></head>\n<style>p{margin:0 !important;} h1{text-align: center; font-family:Courier New;} table, th, td {border: 1px solid; text-align:center;} table{ margin-left:auto; margin-right:auto; background-color: #f6f6f6;}</style> \n <body> \n"

    title = "Dynamic Link Validation"

    html += '\n<h1>' + title + '</h1>\n ' + '<br>' + '<br>\n'

    headin0= "Static ID"
    headin1 = "Dynamic ID"
    headin2 = "Status "
    headin3 = " Reason/ Error Code "
    headin4 ="Ticket"

    html += '<table>' + '<tr>' + '<th>' + headin0 + '</th>' + '<th>' + headin1 + '</th>' + '<th>' + headin2 + '</th>' + '<th>' + headin3 + '</th>' + '<th>' + headin4 + '</th>'+ '</tr>'

    for a,i,s,r,g in zip(statlist,dynalist,status,reason,tick):
        html += '<tr>' + '\n<td>' + a + '</td> ' + '<td>' + i + '</td>' +  '<td>' + s + '</td>' + '<td>' + str(r) + '</td>\n'
        if g =="\t":
            html+= '<td>' + g + '</td>\n'
        else:
            html+= '<td>' + '<a href ="https://www.google.com">' + g + '</a>' + '</td>\n'

    with open(file, 'w') as f:
        f.write(html + "</tr> </table>\n</body>\n</html>")

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["link_2"]
mycollection = db["validation2app_link"]

statlist=[]
dynalist=[]

item_details = mycollection.find()
for a in item_details:
    statlist.append(a['Static_ID'])
print(statlist)

item_details = mycollection.find()
for i in item_details:
    dynalist.append(i['Dynamic_ID'])
print(dynalist)

full_link_list=[]
for a, i in zip(statlist,dynalist):
    var = a+i
    full_link_list.append(var)
print(full_link_list)

status=[]
reason=[]
append_str="https:"
for i in full_link_list:
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
for g in status:
    if g=="success":
        tick.append("\t")
    else:
        tick.append("Raise Ticket")

print2html(statlist,dynalist,'dyna.html')