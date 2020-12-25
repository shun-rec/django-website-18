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
