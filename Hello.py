from docxtpl import DocxTemplate
import datetime
s = datetime.datetime.now()
d=s.date()
y=d.strftime('%d/%m/%y')


doc = DocxTemplate("invoice1.docx")
# l= [[84, 85,86,87,89],[77,88,99,44,55],[66,77,99,785,99]]
k= [1, 2, 3, 4, 5]

doc.render({"name":"Ravi Gupta",
            "address":"Crossing Republik Ghaziabad",
            "phone":"+91-1234567890",
            "gst": "09AAACY8927H1ZU",
            "date": y,
             "k": k,
            "invoice_list": k,
            "subtotal": 601,
            "cgst": 500,
            "sgst": 400,
            "igst": 300,
            "shipping": 0,
            "total": 51200, })

doc.save("new_invoice.docx")

