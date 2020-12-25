# djangoチュートリアル #17

レスポンス基礎編〜HTML以外のデータを表示してみよう！〜

今後HTMLだけでなくCSV、JSON、PDF、動画などを扱う上での基礎固めです。

## 事前準備

### サーバー作成

Paizaでdjagoだけにチェックを入れてサーバーを作成して下さい。

### プロジェクト作成

作成

```sh
django-admin startproject pj_response
```

フォルダ移動

```sh
cd pj_response
```

### アプリ作成

作成

```sh
python manage.py startapp sample
```

全体設定の編集

`pj_response/settings.py`

```py
ALLOWED_HOSTS = ['*]
```

```py
INSTALLED_APPS = [
    ...
    'sample',
]
```

### 開発サーバーの起動

```sh
python manage.py runserver
```

## 最も基本的なレスポンス

`sample/views.py`

```py
from django.views.generic import View
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        return HttpResponse("hello")
```

URL設定

`pj_response/urls.py`

```py
from django.contrib import admin
from django.urls import path

from sample.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
]
```

getというのはブラウザからのリクエストのGETを受け取るメソッドです。

他にpost, deleteなどがあります。

これまで使っていたTemplateViewもListViewもDetailViewもすべて内部でこのようにgetで文字列を返しています。

HTMLを表す文字列返せばウェブページとして表示されるということになります。

実際にブラウザから送られる様子を見てみましょう。

## HTMLを表示してみよう

`sample/views.py`を以下のように修正

```py
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
```

ブラウザで確認してみると、HTMLとして表示されます。

このように世の中のウェブサイトはすべてHTMLという文字列をブラウザに渡すことによって表示されています。

どんなに複雑に見えるYouTubeやTwitterなども同様です。

この文字列部分を色々変えてあげると、CSVやPDF、動画などあらゆるデータを表示することが出来ます。

