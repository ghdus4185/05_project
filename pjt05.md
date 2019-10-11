# project05

## django

#### CRUD 로직으로 영화사이트를 만들어보자!

- 데이터 조작
- Template 제작
- 영화 정보 데이트 관리
- Object Relational Mapping



### 데이터 저장

- models.py에 class 선언을 통해서 데이터를 저장할 공간을 만들어준다.

- 정보를 저장할 칼럼을 만들고 저장할 데이터 타입을 정해준다.

- python manage.py makemigrations 명령어로 자료를 변환해준다.

- python manage.py migrate 명령어로 변환한 자료를 적용시킨다.

- sqlite로 data.csv파일에 들어있는 정보를 저장한다.

  ```
  $ sqlite3 db.sqlite3
  sqlite > .mode csv
  sqlite > .import users.csv users_user
  sqlite > SELECT COUNT(*) FROM users_user;
  ```





### 영화목록

- urls.py에 요청을 받아줄 path('', views.index) 를 만들어준다.
- views.py에 요청이 들어오면 수행할 함수를 선언한다.

- 요청을 보낼 html을 만들기 위해서 base.html과 index.html 을 만들고 base.html block을 열어둔다.


#### Create
- form.html을 만들어 새로 입력할 데이터 수 만큼 input자리를 만들어준다.

- submit버튼 클릭 시 경로를 다시 movies로 보여준다. href = "/movies/create/"

- GET/POST방식 둘 다 사용가능하지만 이번 프로젝트에서는 GET방식을 사용

- ```python
  def create(request):
      title = request.GET.get('title')
      title_en = request.GET.get('title_en')
      audience = request.GET.get('audience')
      open_data = request.GET.get('open_data')
      genre = request.GET.get('genre')
      watch_grade = request.GET.get('watch_grade')
      score = request.GET.get('score')
      poster_url = request.GET.get('poster_url')
      description = request.GET.get('description')
  
      movie = Movie()
      movie.title = title
      movie.title_en = title_en
      movie.audience = audience
      movie.open_data = open_data
      movie.genre = genre
      movie.watch_grade = watch_grade
      movie.score = score
      movie.poster_url = poster_url
      movie.description = description
      movie.save()
  
      return redirect('/movies/')
  ```

  

#### Read
- 제목을 클릭하면 detail.html 로 들어간다. <a href="/movies/{{movie.id}}/detail"></a>

- 수정, 삭제, 목록 버튼을 만든다.

- ```pyhon
  def detail(request, id):
      movie = Movie.objects.get(id=id)
      context = {
          'movie': movie
      }
      return render(request, 'detail.html', context)
  ```

  

#### Update
- 수정 버튼으로 edit.html에 들어간다.

- form.html에서 모든 input 태그에 value="불러올 데이터" 설정해준다.

- ```python
  def edit(request, id):
      movie = Movie.objects.get(id=id)
      context = {
          'movie': movie
      }
      return render(request, 'edit.html', context)
  
  def update(request, id):
      movie = Movie.objects.get(id=id)
  
      title = request.GET.get('title')
      title_en = request.GET.get('title_en')
      audience = request.GET.get('audience')
      open_data = request.GET.get('open_data')
      genre = request.GET.get('genre')
      watch_grade = request.GET.get('watch_grade')
      score = request.GET.get('score')
      poster_url = request.GET.get('poster_url')
      description = request.GET.get('description')
  
      movie.title = title
      movie.title_en = title_en
      movie.audience = audience
      movie.open_data = open_data
      movie.genre = genre
      movie.watch_grade = watch_grade
      movie.score = score
      movie.poster_url = poster_url
      movie.description = description
      movie.save()
  
      return redirect('/movies/')
  ```

  

#### Delete
- id를 요청으로 받아서 해당 id를 movie에 저장하고 .delete()함수로 삭제해준다.

  ```python
  def delete(request, id):
      movie = Movie.objects.get(id=id)
      movie.delete()
      return redirect('/movies/')
  ```

  
