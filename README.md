# djangoチュートリアル #18

レスポンス基礎編〜HTML以外のデータを表示してみよう！〜

今後HTMLだけでなくCSV、JSON、PDF、動画などを扱う上での基礎固めです。

## 事前準備

### サーバー作成

Paizaでdjagoだけにチェックを入れてサーバーを作成して下さい。

### 前回のプロジェクトのダウンロード

```sh
git clone https://github.com/shun-rec/django-website-17.git
```

フォルダ移動

```sh
cd django-website-17
```

### 開発サーバーの起動

```sh
python manage.py runserver
```

## CSVファイルをダウンロードしてみよう

### Viewの作成

`sample/views.py`に以下を追記。

```py
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
```

### URL設定

`pj_response/urls.py`の以下の部分を以下のように修正して下さい。

```py
from sample import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('csv/', views.CSVView.as_view()),
]
```

### 動かしてみよう

/csv/にアクセスして、mycsv.csvというファイルがダウンロードされたらOKです。

## PDFをダウンロードしてみよう

### PDFライブラリのインストール

コンソールを開いて、PDFを生成するための`reportlab`というPythonライブラリをインストールします。

```sh
pip install reportlab
```

### Viewの作成

`sample/views.py`に以下を追記します。

```py
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
```

### URL設定

`pj_response/urls.py`の`urlpatterns`に以下を追記します。

```py
    path('pdf/', views.PDFView.as_view()),
```

### 動かしてみよう

/pdf/にアクセスして、`Hello PDF!`と書かれたPDFファイルがダウンロードされたらOKです。

## JSONをダウンロードしてみよう

JSONというフォーマットはWebページやアプリと通信するために最もよく使われるデータです。

Webページから実際に取得する様子を観てみましょう。

### Viewの作成

`sample/views.py`に以下を追記します。

```py
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
```

### URL設定

`pj_response/urls.py`の`urlpatterns`に以下を追記します。

```py
    path('api/people/', views.PeopleAPIView.as_view()),
```

### 動かしてみよう

ブラウザでトップページ（`/`）を開いて下さい。

開発者用ツールを立ち上げて、コンソールから以下のJavascriptを実行してみましょう。

```js
fetch("/api/people/").then((res) => res.json()).then(console.log)
```
