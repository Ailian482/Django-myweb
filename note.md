- 项目目录结构
    - myweb 项目
        - django-admin startproject myweb
    - myapp 应用
        - python3 manage.py startapp myapp
    - db.sqlite3 数据库
    - manage.py 函数入口
    
- 创建视图
    - 1. 打开myapp/views.py并放入Python代码
    - 2. 在当前应用目录下(myapp)创建我们自己的路由(urls.py)
        - 文件内容
        - from django.urls import path
          from . import views
          urlpatterns = [
            path('', views.index, name='index'),
          ]
        - 代码释义
            - 写一个请求的路径，访问的是 views.index 方法
    - 3. 把我们自己定义的路由加到项目的主路由里面去-- myweb/urls.py
        - 使用include() 方法把我们自己定义的路由加进来
            - 导入 include模块 from django.urls import path, include
            - 把 path("myapp/", include('myapp.urls')) 加到 urlpatterns
    