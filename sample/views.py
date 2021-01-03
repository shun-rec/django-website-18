from django.views.generic import View
from django.http import HttpResponse



body = """
<h1>Hello</h1>
<ol>
  <li>りんご</li>
  <li>ばなな</li>
  <li>いちご</li>
</ol>
"""

class IndexView(View):
    def get(self, request):
        return HttpResponse(body)


import csv


header = ['ID', '名前', '年齢']

people = [
    ('1', 'Hoge', 10),
    ('2', 'Fuga', 18),
    ('3', 'Foo', 23),
]


class CSVView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mycsv.csv"'

        writer = csv.writer(response)
        writer.writerow(header)
        writer.writerows(people)
        return response
        

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

class PDFView(View):
    def get(self, request):
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        
        # この部分を変えると内容が変わる
        p.drawString(50, 800, "Hello PDF!")
        
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
        
        
from django.http import JsonResponse

class PeopleAPIView(View):
    def get(self, request):
        people_ret = []
        for p in people:
            people_ret.append({
                'id': p[0],
                'name': p[1],
                'age': p[2],
            })
        data = {
            "people": people_ret
        }
        return JsonResponse(data=data)