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
            
- path()函数介绍
    - Django path()函数可以接收四个参数，分别是两个必选参数：route、view和两个可选参数：kwargs、name
        - route
            - 包含URL模式的字符串，在处理请求，Django从第一个模式开始，urlpatterns然后沿列表向下移动，将请求的URL与每个模式进行比较，直到找到匹配的URL
        - view
            - 用于执行与正则表达式匹配的URL请求，就是匹配我们写的代码方法
        - kwargs
            - 试图使用的字典类型的参数
        - name
            - 用来反向获取URL
        
- 项目的模型
    - 是数据库操作
    - 1. 连接mysql数据库设置
        - 默认情况下配置 sqlite 数据库 ，若不使用sqlite数据库，则需要额外的设置，例如 USER、PASSWORD、HOST必须加入
        - 其中 ENGINE 设置为后端数据库使用，内置数据库后端有：
            "django.db.backends.postgresql"
            "django.db.backends.mysql"
            "django.db.backends.sqlite3"
            "django.db.backends.oracle"
        - 在myweb/settings.py文件中，通过DATABASES项进行数据库设置，要确保这个数据库存在
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'tmc_services',
                    'USER': 'root',
                    'PASSWORD': '',
                    'HOST': 'tyx-nonproduction-mysql.teyixing.com',
                    'PORT': '3314',
                }
            }
        - 注意：Django使用mysql数据库需要加载MySQLdb模块，需要安装 mysqlclient，若已经安装请略过
          Django2.2版本之前我们安装的是pymysql模块，不过现在使用的是 mysqlclient
        