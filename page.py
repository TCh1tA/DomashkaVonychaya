from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<img src="static/Slave.jpg" alt="Ой)">'


@app.route('/d1')
def Mizha():
    return '''
<!doctype html>
<html class="no-js" lang="ru">
<head><meta name='csrf-token-name' content='csrftoken'/>
<meta name='csrf-token-value' content='17c89d611b2b7f693b4f5ab1695c1016cbc6bc7ca28b9f1fe6a7f0a715ce084f23041cb4ef632fbd'/>
<meta name='hmac-token-name' content='Ajax-Token'/>

	<meta charset="utf-8">
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	<title>
                        Российская электронная школа      	</title>
	<meta name="description" content="">
	<link rel="stylesheet" href="/static/styles/main.css?">
   	   <link rel="stylesheet" href="/custom/css/vendor/sumoselect.min.css?">
   	<script charset="utf-8" src="/6320453817ce74fac41f234b.js?1707117847475"></script>
<script src="/bundles/fosjsrouting/js/router.min.js?"></script>
	<script src="/js/routing?callback=fos.Router.setData"></script>
	<style>
		.quiz-btn {
			padding: 16px 0 0 12px;
		}
		.quiz-btn a {
			display: block;
			background: #FB5E3A;
			border-radius: 38px;
			color: #fff;
			font-size: 15px;
			line-height: 18px;
			font-weight: 500;
			text-decoration: none;
			width: 100%;
			padding: 10px 0 10px 12px;
			text-transform: uppercase;
		}
		.quiz-btn a i {
			width: 45px;
			height: 32px;
			background: url('/img/quiz-icon.svg') no-repeat left top;
			display: block;
			position: absolute;
		}
		.quiz-btn a span {
			padding-left: 56px;
			display: block;
		}

		.banner__quiz-btn-big {
			position: absolute;
			top: -20px;
			left: 810px;
		}
		.banner__quiz-btn-big a {
			width: 393px;
			height: 77px;
			padding: 0px 0 0px 25px;
			font-size: 25px;
			line-height: 80px;
			font-weight: 500;
		}
		.banner__quiz-btn-big a i {
			width: 72px;
			height: 50px;
			background-size: 100%;
			margin-top: 12px;
		}
		.banner__quiz-btn-big a span {
			padding-left: 90px;
		}
		.banner__quiz-btn-small {
			position: absolute;
			top: 100px;
			left: 996px;
		}
		.banner__quiz-btn-small a {
			font-size: 16px;
			line-height: 20px;
			color: #fff;
			text-transform: uppercase;
			text-decoration: none;
			background: rgba(6, 23, 61, 0.4);
			border-radius: 60px;
			padding: 20px 32px;
			display: block;
			width: 214px;
		}


		.carousel-text__line-quiz-big {
			font-size: 70px;
			line-height: 75px;
			color: #fff;
			margin: 0px;
		}
		.carousel-text__line-quiz-big span {
			display: block;
			font-size: 20px;
			line-height: 20px;
			color: #fff;
			position: absolute;
			left: 438px;
			top: 80px;
		}
		.carousel-text__line-quiz {
			font-size: 16px;
			line-height: 19px;
			width: 430px;
			height: 35px;
			border-radius: 4px;
			padding-left: 18px;
			font-weight: 500;
			padding-top: 8px;
			color: #fff;
			padding-right: 0px;
			margin-top: 0px;
			margin-bottom: 6px;
		}
	</style>
</head>
	<body><noscript><img src="/394c592328cf062b522a24a5ed1e86f1.gif" width="0" height="0" alt="" /></noscript>

	<!--[if lte IE 8]>
	<style>
		.browserupgrade {
			text-align: center;
			border: 2px solid #b4b472;
			font-size: 20px;
			padding: 20px;
			position: fixed;
			background: #333;
			color: #c1bea2;
			width: 400px;
			left: 50%;
			margin-left: -200px;
			z-index: 999999;
		}

		.browserupgrade a {
			color: #fff;
		}

		.browserupgrade a:hover {
			color: #e0c1ff;
			text-decoration: none;
		}
	</style>
	<p class="browserupgrade">Вы используете <strong>устаревший</strong> браузер. Пожалуйста<br/> <a
			href="http://browsehappy.com/">обновите ваш браузер или установите альтернативный</a><br/> для корректного
		отображения содержимого сайта.</p>
	<![endif]-->

	<div class="outer-sf">
		<div class="wrapper-sf">
         				<header class="header">
					<div class="wrapper-main">
						<div class="header__top lk-header__top d-t">
							<div class="d-tc header-top__logo-cell">
								<a href="/" class="logo">
									<img src="/img/svg/logo.svg?" alt="Логотип РЭШ">

									<p class="logo__name">Российская электронная школа</p>
								</a>
							</div>

                         <div class="d-tc header-top__search-cell">

        <form name="resh_search_widget" method="get" class="collection-search" action="/search/">
            <span class="collection-search-close search-close_hide">✕</span>
                        <div class="collection-search__input">
        <span class="search-input__clear-btn"><i class="icon icon_delete-cross"></i></span>
        <input type="text" value="" name="resh_search_widget[search]" id="search" required  placeholder="Поиск" class="menu-slide__input-text ">
        <button type="submit">
            <i class="icon icon_search-glass"></i>
        </button>
    </div>


        

        <input type="hidden" id="resh_search_widget__token" name="resh_search_widget[_token]" class="form-control" value="RxZCH_Q4lFtBFVcV4IPA5FVpuHCwJQpUK3JUapgzq9Y" /></form>

    </div>

                     

    <a href="/office/" class="d-tc header-top__user">
        <div class="user-image">
            <div class="top-user-avatar" style="background: url(/custom/img/default_profile.jpg); background-size: cover"></div>
        </div>
            <span class="user-name">
               Щербаков М.
            </span>
    </a>

    <div class="d-tc header-top__logout-cell">
                    <a href="/logout">
                <div class="header__login">
                    выход
                </div>
            </a>
            </div>



						</div>
					</div>

               <nav class="header__menu ">

    <div class="wrapper-main">

        <div class="d-t header__menu__wrapper">
            <div class="d-tc header__submenu__cell">
                <div class="header__submenu _clickable d-tc" data-target="hmbrg-menu" data-timer="700">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            <a href="/subject/" class="header__menu-link d-tc">Предметы</a>
            <a href="/class/1/" class="header__menu-link d-tc">Классы</a>
            <a href="/for-pupil" class="header__menu-link d-tc">Ученику</a>
            <a href="/for-teacher" class="header__menu-link d-tc">Учителю</a>
            <a href="/for-parent" class="header__menu-link d-tc">Родителю</a>
            <a href="/for-school" class="header__menu-link d-tc">Школе</a>
            <div class="d-tc nav-icon-cell">
                <a class="nav-mail" href="/feedback" style="top: -5px;">
                    <img src="/img/mail.png" alt="">
                    <span style="font: 17px robotoregular, sans-serif; line-height: 17px; display: inline-block; position: relative; top: 4px; text-align: left; text-transform: none; padding-left: 8px;">написать<br>в техподдержку</span>
                </a>
            </div>
        </div>
    </div>
</nav>
				</header>
         
			<main class="main ">

                <div class="lk-wrapper">

        <div class="wrapper-content">
            <div class="block-shadow">

                    <nav class="lk-top-nav d-t">
        <a href="/office/user/timetable" class="d-tc ">Расписания</a>
        <a href="/office/user/myteachers/" class="d-tc ">Учителя</a>
        <a href="/office/user/myhomeworks/" class="d-tc ">Задания</a>
        <a href="/office/user/diary/" class="d-tc active-title">Дневник</a>
        <a href="/office/user/journal" class="d-tc ">Достижения</a>
        <a href="/office/user/notification/" class="d-tc ">Уведомления</a>
        <a href="/office/user/favorite/" class="d-tc ">Избранное</a>
        <a href="/office/user/notes/" class="d-tc ">Заметки</a>
    </nav>

                <div class="lk-cols-wrap d-t">
                    <div class="d-tc lk-col-1">
                        <div class="lk-small-block lk-user-block">
    <div class="lk-user-block__name-wrap">
        Щербаков
        Михаил
    </div>
</div>
<div style="height:auto;" class="lk-small-block lk-user-details">
            <p></p>
        <p>МАОУ &quot;ГИМНАЗИЯ &quot;ГАРМОНИЯ&quot;</p>
        <p>Ученик</p>
    <p></p>
            
        <p>
                15 октября 2006
    </p>
        <div style="position: static; margin-top: 10px;" class="lk-user-details__links-block">
        <a href="/office/user/profile/">Редактировать профиль</a>
        <a href="/office/user/setting/">Настройки</a>
        <a href="/logout">Выйти</a>
    </div>
</div>


                                                                                    <div class="lk-right-block lk-activity block_js">
    <h2 class="lk-right-block-title">Активность</h2>
    <div class="lk-activity__content">
                      <div class="lk-activity__item">
            <p>
                                    Осуществлена регистрация на портале РЭШ
                            </p>
            <p class="lk-activity__time">
                                    3 февраля 2023
                            </p>
        </div>
      
    </div>
    <div class="lk-block-opts">
        <a href="/office/user/setting/"><i class="icon icon_edit"></i></a>
        <i class="icon icon_delete-cross" data-type="activity" data-href="/office/user/hide-widget"></i>
    </div>
</div>                                                    </div>
                        <div class="d-tc lk-col-2">
                            

    <h2>Дневник: Щербаков Михаил Андреевич</h2>
    <div class="lk-subject-choice">
        <span>Предмет</span>
        <div class="lk-select">
            <select class="chosen-select chosen-select-diary" data-type="subject">
                <option value="0">Все</option>
                                  <option value="16" >Алгебра</option>
                                  <option value="51" >Алгебра и начала математического анализа</option>
                                  <option value="11" >Английский язык</option>
                                  <option value="5" >Биология</option>
                                  <option value="54" >Всероссийский открытый урок</option>
                                  <option value="4" >География</option>
                                  <option value="17" >Геометрия</option>
                                  <option value="33" >Естествознание</option>
                                  <option value="7" >Изобразительное искусство</option>
                                  <option value="19" >Информатика</option>
                                  <option value="2" >Испанский язык</option>
                                  <option value="3" >История</option>
                                  <option value="55" >Китайский язык</option>
                                  <option value="14" >Литература</option>
                                  <option value="32" >Литературное чтение</option>
                                  <option value="12" >Математика</option>
                                  <option value="6" >Музыка</option>
                                  <option value="10" >Немецкий язык</option>
                                  <option value="24" >Обществознание</option>
                                  <option value="43" >Окружающий мир</option>
                                  <option value="23" >Основы безопасности жизнедеятельности</option>
                                  <option value="41" >Право</option>
                                  <option value="42" >Россия в мире</option>
                                  <option value="13" >Русский язык</option>
                                  <option value="8" >Технология</option>
                                  <option value="50" >Технология (девочки)</option>
                                  <option value="48" >Технология (мальчики)</option>
                                  <option value="28" >Физика</option>
                                  <option value="9" >Физическая культура</option>
                                  <option value="1" >Французский язык</option>
                                  <option value="29" >Химия</option>
                                  <option value="40" >Экология</option>
                                  <option value="38" >Экономика</option>
                           </select>
        </div>
    </div>

    <div class="lk-date">
        <span>Выберите период</span>

        <div class="lk-date__item">
            <span>c</span>
            <div class="input-outer">
                <input type="text" value="15.04.2024" data-type="start" class="diary-datepicker-diary diary-datepicker-old">
            </div>
        </div>

        <div class="lk-date__item">
            <span>по</span>
            <div class="input-outer">
                <input type="text" value="22.04.2024" data-type="finish" class="diary-datepicker-diary diary-datepicker-new">
            </div>
        </div>
    </div>

    <div class="lk-subjects-table">
                  <table>
               <thead>
               <tr class="table-diary">
                   <th>Класс</th>
                   <th>Предмет</th>
                   <th>Тема урока</th>
                   <th>Тип задания</th>
                   <th>Результат</th>
                   <th>Время</th>
               </tr>
               </thead>
               <tbody>
                                                                                <tr>
                       <td class="table-date-row" colspan="6"><span class="table-date">21 апреля 2024</span></td>
                    </tr>
                                                                    <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/4971/">
                                                                            <p>Урок 34. Индивидуальные, групповые и командные действия в защите</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>2:41</p>
                                                                    <p>2:39</p>
                                                                    <p>2:36</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/5511/">
                                                                            <p>Урок 31. Техники перемещений и владения мячом</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>2:34</p>
                                                                    <p>2:32</p>
                                                                    <p>2:30</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3901/">
                                                                            <p>Урок 32. Тактика игры – командное нападение</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>2:27</p>
                                                                    <p>2:25</p>
                                                                    <p>2:24</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/5419/">
                                                                            <p>Урок 30. Защитное действие накрывание</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>2:21</p>
                                                                    <p>2:22</p>
                                                                    <p>2:17</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3879/">
                                                                            <p>Урок 28. Защитные действия: вырывание и выбивание</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>2:15</p>
                                                                    <p>2:11</p>
                                                                    <p>2:10</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3844/">
                                                                            <p>Урок 29. Защитное действие перехват</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>2:06</p>
                                                                    <p>2:04</p>
                                                                    <p>2:03</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/4969/">
                                                                            <p>Урок 27. Штрафной бросок</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>2:03</p>
                                                                    <p>2:00</p>
                                                                    <p>1:58</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/4639/">
                                                                            <p>Урок 24. Бросок одной и двумя руками в прыжке</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>1:53</p>
                                                                    <p>1:51</p>
                                                                    <p>1:50</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/6104/">
                                                                            <p>Урок 25. Броски мяча после двух шагов и в прыжке с близкого и среднего расстояния</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>1:50</p>
                                                                    <p>1:47</p>
                                                                    <p>1:44</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3854/">
                                                                            <p>Урок 26. Броски мяча в корзину со средних и дальних дистанций</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>1:41</p>
                                                                    <p>1:39</p>
                                                                    <p>1:38</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/6105/">
                                                                            <p>Урок 20. Техника ловли и передачи мяча одной рукой сбоку</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>1:35</p>
                                                                    <p>1:34</p>
                                                                    <p>1:30</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/6106/">
                                                                            <p>Урок 19. Техника ловли и передачи мяча одной рукой снизу</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>1:25</p>
                                                                    <p>1:28</p>
                                                                    <p>1:24</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3807/">
                                                                            <p>Урок 18. Техника передвижений с изменением направления движения нападающего и защитника</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>1:20</p>
                                                                    <p>1:21</p>
                                                                    <p>1:18</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3819/">
                                                                            <p>Урок 17. Техника безопасности на занятиях баскетболом. Правила игры в баскетбол</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                3
            
                                                                            </p>
                                                                    <p>
                                                                4
            
                                                                            </p>
                                                                    <p>
                                                                5
            
                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>1:15</p>
                                                                    <p>1:16</p>
                                                                    <p>1:12</p>
                                                            </td>
                        </tr>
                                                                          </tbody>
           </table>
           </div>
    <div class="lk-pages">
        
    </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    <div class="banner-contain block-shadow wrapper-content">
</div>

			</main>

		</div>
               <footer class="footer _hideable">

    <div class="partners">
        <div class="wrapper-content">
            <h1>НАШИ ПАРТНЁРЫ</h1>
            <div class="partners__wrap">
                    <a class="partners__link" target="_blank" href="https://edu.gov.ru/">
        <img src="/uploads/partner/60d04e5927df4.png" alt="Минпросвещения России">
    </a>
    <a class="partners__link" target="_blank" href="http://edu.ru">
        <img src="/uploads/partner/57c4385d27ab7.jpg" alt="Российское образование">
    </a>
    <a class="partners__link" target="_blank" href="http://obrnadzor.gov.ru">
        <img src="/uploads/partner/57f02217139a4.png" alt="Рособрнадзор">
    </a>
    <a class="partners__link" target="_blank" href="https://www.rgo.ru/">
        <img src="/uploads/partner/585b7c0268b15.jpg" alt="Русское географическое общество">
    </a>
    <a class="partners__link" target="_blank" href="https://rvio.histrf.ru/">
        <img src="/uploads/partner/57f0225b5205b.png" alt="Российское военно-историческое общество">
    </a>
    <a class="partners__link" target="_blank" href="https://www.prlib.ru/">
        <img src="/uploads/partner/580e011b1018a.png" alt="Президентская бибилиотека">
    </a>

            </div>
        </div>
    </div>

    <div class="wrapper-content">
        <nav class="footer__menu">
            <ul class="footer__menu-list">
                <li class="footer__menu-item">
                    <a href="/subject/" class="footer__menu-link">Предметы</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/class/1/" class="footer__menu-link">Классы</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-pupil" class="footer__menu-link">Ученику</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-teacher" class="footer__menu-link">Учителю</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-parent" class="footer__menu-link">Родителю</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-school" class="footer__menu-link">Школе</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-partner" class="footer__menu-link">Партнёрам</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/feedback" class="footer__menu-link">Техническая поддержка</a>
                </li>
            </ul>
        </nav>
        <div class="row">
            <div class="footer__social col-1">
                <a class="soc-links soc-links_grey"
                   target="_blank"
                   href="https://vk.com/resh_edu">
                    <i class="icon icon_soc-vk"></i>
                </a>
                            </div>
            
            <div class="footer__copyright col-10 text-right">
                © Государственная образовательная платформа «Российская электронная школа»
            </div>
        </div>
            </div>
</footer>      
	</div>

	<div class="mask invis"></div>

	
	<div class="fs-menu hmbrg-menu">
    <div class="bg-color-wrapper">
        <div class="fs-wrapper">

            <section class="fs-sujects _tabs">
                <div class="fs-title-row">
                    <h2 class="fs-section-title">Предметы</h2>
                    <span class="fs-sort _tabs__tab">По алфавиту</span>
                    <span class="fs-sort _tabs__tab _tab-active">По предметным областям</span>
                </div>
                <div class="fs-subj _tabs__content">

                    <div class="fs-subjects-abc__box">
                        <ul class="fs-subjects-abc__list">
                                                                                                <li>
                                        <a href="/subject/16/">АЛГЕБРА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/51/">АЛГЕБРА И НАЧАЛА МАТЕМАТИЧЕСКОГО АНАЛИЗА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/11/">АНГЛИЙСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/5/">БИОЛОГИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/54/">ВСЕРОССИЙСКИЙ ОТКРЫТЫЙ УРОК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/4/">ГЕОГРАФИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/17/">ГЕОМЕТРИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/33/">ЕСТЕСТВОЗНАНИЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/7/">ИЗОБРАЗИТЕЛЬНОЕ ИСКУССТВО</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/19/">ИНФОРМАТИКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/2/">ИСПАНСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/3/">ИСТОРИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/55/">КИТАЙСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/14/">ЛИТЕРАТУРА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/32/">ЛИТЕРАТУРНОЕ ЧТЕНИЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/12/">МАТЕМАТИКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/6/">МУЗЫКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/10/">НЕМЕЦКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/24/">ОБЩЕСТВОЗНАНИЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/43/">ОКРУЖАЮЩИЙ МИР</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/23/">ОСНОВЫ БЕЗОПАСНОСТИ ЖИЗНЕДЕЯТЕЛЬНОСТИ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/41/">ПРАВО</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/42/">РОССИЯ В МИРЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/13/">РУССКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/8/">ТЕХНОЛОГИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/50/">ТЕХНОЛОГИЯ (ДЕВОЧКИ)</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/48/">ТЕХНОЛОГИЯ (МАЛЬЧИКИ)</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/28/">ФИЗИКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/9/">ФИЗИЧЕСКАЯ КУЛЬТУРА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/1/">ФРАНЦУЗСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/29/">ХИМИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/40/">ЭКОЛОГИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/38/">ЭКОНОМИКА</a>
                                    </li>
                                                                                    </ul>
                    </div>

                </div>
                <div class="fs-subj _tabs__content _tab-cont-visible">
                    <div class="fs-subj__row">
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__technology"></i>
                                                                        <h3 class="fs-subtitle">Технология</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/54/">Всероссийский открытый урок</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/48/">Технология (мальчики)</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/8/">Технология</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/50/">Технология (девочки)</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__art"></i>
                                                                        <h3 class="fs-subtitle">Искусство</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/7/">Изобразительное искусство</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/6/">Музыка</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__math-Informatics"></i>
                                                                        <h3 class="fs-subtitle">Математика и информатика</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/19/">Информатика</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/12/">Математика</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/16/">Алгебра</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/17/">Геометрия</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/51/">Алгебра и начала математического анализа</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__philology"></i>
                                                                        <h3 class="fs-subtitle">Иностранный язык</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/2/">Испанский язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/11/">Английский язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/10/">Немецкий язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/1/">Французский язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/55/">Китайский язык</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__physical-culture"></i>
                                                                        <h3 class="fs-subtitle">Физическая культура и основы безопасности жизнедеятельности</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/23/">Основы безопасности жизнедеятельности</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/9/">Физическая культура</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__social-science"></i>
                                                                        <h3 class="fs-subtitle">Общественно-научные предметы</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/4/">География</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/24/">Обществознание</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/40/">Экология</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/3/">История</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/42/">Россия в мире</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/41/">Право</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/43/">Окружающий мир</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/38/">Экономика</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__philology"></i>
                                                                        <h3 class="fs-subtitle">Русский язык и литература</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/14/">Литература</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/32/">Литературное чтение</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/13/">Русский язык</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__natural-science"></i>
                                                                        <h3 class="fs-subtitle">Естественнонаучные предметы</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/28/">Физика</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/29/">Химия</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/5/">Биология</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/33/">Естествознание</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                            </div>
                </div>
            </section>
            <section class="fs-classes">
                <div class="fs-title-row">
                    <h2 class="fs-section-title">Классы</h2>
                </div>
                <div class="fs-classes__list">
                                            <a href="/class/1/" class="fs-classes__link">1</a>
                                            <a href="/class/2/" class="fs-classes__link">2</a>
                                            <a href="/class/3/" class="fs-classes__link">3</a>
                                            <a href="/class/4/" class="fs-classes__link">4</a>
                                            <a href="/class/5/" class="fs-classes__link">5</a>
                                            <a href="/class/6/" class="fs-classes__link">6</a>
                                            <a href="/class/7/" class="fs-classes__link">7</a>
                                            <a href="/class/8/" class="fs-classes__link">8</a>
                                            <a href="/class/9/" class="fs-classes__link">9</a>
                                            <a href="/class/10/" class="fs-classes__link">10</a>
                                            <a href="/class/11/" class="fs-classes__link">11</a>
                                    </div>
            </section>

            <footer class="fs-footer">
                <div class="fs-footer__grid fs-footer__grid-1">

                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/about">О проекте</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/guide">Гид по «Российской Электронной
                            Школе»
                        </a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/news/">Новости проекта</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/for-school">Школе</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/feedback">Задать вопрос</a>
                    </div>

                </div>
                <div class="fs-footer__grid fs-footer__grid-2">
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/for-parent">Родителям</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/for-teacher">Учителям</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/for-partner">Партнерам</a>
                    </div>
                </div>

                <div class="fs-footer__grid fs-footer__grid-3">
                    <div class="fs-footer__item-row">
                        <span class="fs-footer__item-large">Мы в социальных сетях</span>
                    </div>
                    <div class="footer__social">
                        <a class="soc-links" href="https://vk.com/resh_edu">
                            <i class="icon icon_soc-vk"></i>
                        </a>
                                            </div>
                    <div class="fs-footer__item-row">
                        <br>

                    </div>
                    <div class="fs-footer__item-row fs-mobile-links">
                        <div class="fs-mobile-links__wrapper">
                            <span class="fs-menu-gp fs-mobile-links__logo"></span>
                            <div class="mobile-item__pending">в разработке</div>
                        </div>
                        <div class="fs-mobile-links__wrapper">
                            <span class="fs-menu-app-store fs-mobile-links__logo"></span>
                            <div class="mobile-item__pending">в разработке</div>
                        </div>
                    </div>
                </div>


            </footer>

            <div class="fs-menu-close _win-close">✕</div>
        </div>
    </div>
</div>

    
                		<script>window.jQuery || document.write('<script src="/js/vendor/jquery-1.12.0.min.js"><\/script>');</script>
		<script src="/js/vendor/jquery.iframetracker.min1.1.0.js?"></script>
        
		<script src="/custom/js/vendor/jquery.sumoselect.js?"></script>

		<script src="/assets/js/bundle.js?"></script>
		<script src="/custom/js/scripts/login_popup.js?"></script>
		<script src="/js/vendor/sweetalert.js?"></script>
		<script src="/custom/js/func.js?"></script>

		
		<!-- Yandex.Metrika counter -->
		<script>
            (function (d, w, c) {
                (w[c] = w[c] || []).push(function () {
                    try {
                        w.yaCounter39997495 = new Ya.Metrika({
                            id: 39997495,
                            clickmap: true,
                            trackLinks: true,
                            accurateTrackBounce: true,
                            webvisor: true
                        });
                        w.yaCounter43464019 = new Ya.Metrika({
                            id: 43464019,
                            clickmap: true,
                            trackLinks: true,
                            accurateTrackBounce: true,
                            webvisor: true
                        });
                    } catch (e) {
                    }
                });

                var n = d.getElementsByTagName("script")[0],
                    s = d.createElement("script"),
                    f = function () {
                        n.parentNode.insertBefore(s, n);
                    };
                s.type = "text/javascript";
                s.async = true;
                s.src = "https://mc.yandex.ru/metrika/watch.js";

                if (w.opera == "[object Opera]") {
                    d.addEventListener("DOMContentLoaded", f, false);
                } else {
                    f();
                }
            })(document, window, "yandex_metrika_callbacks");
		</script>
		<noscript>
			<div><img src="https://mc.yandex.ru/watch/39997495" style="position:absolute; left:-9999px;" alt=""/></div>
		</noscript>
		<!-- /Yandex.Metrika counter -->

		    
    <script>
        $(function() {
            $('.teacher_message_icon').on('click', function () {
                var jThis = $(this),
                    message = jThis.attr('data-message');
                Swal.fire({
                    'text': message,
                    showCloseButton: true,
                    showConfirmButton: false
                });
            });
        });
    </script>

	<div class="show-password-change" data-period=""></div>
	</body>
</html>'''


@app.route('/d2')
def Stesha():
    return '''
<!doctype html>
<html class="no-js" lang="ru">
<head><meta name='csrf-token-name' content='csrftoken'/>
<meta name='csrf-token-value' content='17c89d611b2b7f693b4f5ab1695c1016cbc6bc7ca28b9f1fe6a7f0a715ce084f23041cb4ef632fbd'/>
<meta name='hmac-token-name' content='Ajax-Token'/>

	<meta charset="utf-8">
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	<title>
                        Российская электронная школа      	</title>
	<meta name="description" content="">
	<link rel="stylesheet" href="/static/styles/main.css?">
   	   <link rel="stylesheet" href="/custom/css/vendor/sumoselect.min.css?">
   	<script charset="utf-8" src="/6320453817ce74fac41f234b.js?1707117847475"></script>
<script src="/bundles/fosjsrouting/js/router.min.js?"></script>
	<script src="/js/routing?callback=fos.Router.setData"></script>
	<style>
		.quiz-btn {
			padding: 16px 0 0 12px;
		}
		.quiz-btn a {
			display: block;
			background: #FB5E3A;
			border-radius: 38px;
			color: #fff;
			font-size: 15px;
			line-height: 18px;
			font-weight: 500;
			text-decoration: none;
			width: 100%;
			padding: 10px 0 10px 12px;
			text-transform: uppercase;
		}
		.quiz-btn a i {
			width: 45px;
			height: 32px;
			background: url('/img/quiz-icon.svg') no-repeat left top;
			display: block;
			position: absolute;
		}
		.quiz-btn a span {
			padding-left: 56px;
			display: block;
		}

		.banner__quiz-btn-big {
			position: absolute;
			top: -20px;
			left: 810px;
		}
		.banner__quiz-btn-big a {
			width: 393px;
			height: 77px;
			padding: 0px 0 0px 25px;
			font-size: 25px;
			line-height: 80px;
			font-weight: 500;
		}
		.banner__quiz-btn-big a i {
			width: 72px;
			height: 50px;
			background-size: 100%;
			margin-top: 12px;
		}
		.banner__quiz-btn-big a span {
			padding-left: 90px;
		}
		.banner__quiz-btn-small {
			position: absolute;
			top: 100px;
			left: 996px;
		}
		.banner__quiz-btn-small a {
			font-size: 16px;
			line-height: 20px;
			color: #fff;
			text-transform: uppercase;
			text-decoration: none;
			background: rgba(6, 23, 61, 0.4);
			border-radius: 60px;
			padding: 20px 32px;
			display: block;
			width: 214px;
		}


		.carousel-text__line-quiz-big {
			font-size: 70px;
			line-height: 75px;
			color: #fff;
			margin: 0px;
		}
		.carousel-text__line-quiz-big span {
			display: block;
			font-size: 20px;
			line-height: 20px;
			color: #fff;
			position: absolute;
			left: 438px;
			top: 80px;
		}
		.carousel-text__line-quiz {
			font-size: 16px;
			line-height: 19px;
			width: 430px;
			height: 35px;
			border-radius: 4px;
			padding-left: 18px;
			font-weight: 500;
			padding-top: 8px;
			color: #fff;
			padding-right: 0px;
			margin-top: 0px;
			margin-bottom: 6px;
		}
	</style>
</head>
	<body><noscript><img src="/394c592328cf062b522a24a5ed1e86f1.gif" width="0" height="0" alt="" /></noscript>

	<!--[if lte IE 8]>
	<style>
		.browserupgrade {
			text-align: center;
			border: 2px solid #b4b472;
			font-size: 20px;
			padding: 20px;
			position: fixed;
			background: #333;
			color: #c1bea2;
			width: 400px;
			left: 50%;
			margin-left: -200px;
			z-index: 999999;
		}

		.browserupgrade a {
			color: #fff;
		}

		.browserupgrade a:hover {
			color: #e0c1ff;
			text-decoration: none;
		}
	</style>
	<p class="browserupgrade">Вы используете <strong>устаревший</strong> браузер. Пожалуйста<br/> <a
			href="http://browsehappy.com/">обновите ваш браузер или установите альтернативный</a><br/> для корректного
		отображения содержимого сайта.</p>
	<![endif]-->

	<div class="outer-sf">
		<div class="wrapper-sf">
         				<header class="header">
					<div class="wrapper-main">
						<div class="header__top lk-header__top d-t">
							<div class="d-tc header-top__logo-cell">
								<a href="/" class="logo">
									<img src="/img/svg/logo.svg?" alt="Логотип РЭШ">

									<p class="logo__name">Российская электронная школа</p>
								</a>
							</div>

                         <div class="d-tc header-top__search-cell">

        <form name="resh_search_widget" method="get" class="collection-search" action="/search/">
            <span class="collection-search-close search-close_hide">✕</span>
                        <div class="collection-search__input">
        <span class="search-input__clear-btn"><i class="icon icon_delete-cross"></i></span>
        <input type="text" value="" name="resh_search_widget[search]" id="search" required  placeholder="Поиск" class="menu-slide__input-text ">
        <button type="submit">
            <i class="icon icon_search-glass"></i>
        </button>
    </div>




        <input type="hidden" id="resh_search_widget__token" name="resh_search_widget[_token]" class="form-control" value="RxZCH_Q4lFtBFVcV4IPA5FVpuHCwJQpUK3JUapgzq9Y" /></form>

    </div>



    <a href="/office/" class="d-tc header-top__user">
        <div class="user-image">
            <div class="top-user-avatar" style="background: url(/custom/img/default_profile.jpg); background-size: cover"></div>
        </div>
            <span class="user-name">
               Жолондевская С.
            </span>
    </a>

    <div class="d-tc header-top__logout-cell">
                    <a href="/logout">
                <div class="header__login">
                    выход
                </div>
            </a>
            </div>



						</div>
					</div>

               <nav class="header__menu ">

    <div class="wrapper-main">

        <div class="d-t header__menu__wrapper">
            <div class="d-tc header__submenu__cell">
                <div class="header__submenu _clickable d-tc" data-target="hmbrg-menu" data-timer="700">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            <a href="/subject/" class="header__menu-link d-tc">Предметы</a>
            <a href="/class/1/" class="header__menu-link d-tc">Классы</a>
            <a href="/for-pupil" class="header__menu-link d-tc">Ученику</a>
            <a href="/for-teacher" class="header__menu-link d-tc">Учителю</a>
            <a href="/for-parent" class="header__menu-link d-tc">Родителю</a>
            <a href="/for-school" class="header__menu-link d-tc">Школе</a>
            <div class="d-tc nav-icon-cell">
                <a class="nav-mail" href="/feedback" style="top: -5px;">
                    <img src="/img/mail.png" alt="">
                    <span style="font: 17px robotoregular, sans-serif; line-height: 17px; display: inline-block; position: relative; top: 4px; text-align: left; text-transform: none; padding-left: 8px;">написать<br>в техподдержку</span>
                </a>
            </div>
        </div>
    </div>
</nav>
				</header>

			<main class="main ">

                <div class="lk-wrapper">

        <div class="wrapper-content">
            <div class="block-shadow">

                    <nav class="lk-top-nav d-t">
        <a href="/office/user/timetable" class="d-tc ">Расписания</a>
        <a href="/office/user/myteachers/" class="d-tc ">Учителя</a>
        <a href="/office/user/myhomeworks/" class="d-tc ">Задания</a>
        <a href="/office/user/diary/" class="d-tc active-title">Дневник</a>
        <a href="/office/user/journal" class="d-tc ">Достижения</a>
        <a href="/office/user/notification/" class="d-tc ">Уведомления</a>
        <a href="/office/user/favorite/" class="d-tc ">Избранное</a>
        <a href="/office/user/notes/" class="d-tc ">Заметки</a>
    </nav>

                <div class="lk-cols-wrap d-t">
                    <div class="d-tc lk-col-1">
                        <div class="lk-small-block lk-user-block">
    <div class="lk-user-block__name-wrap">
        Жолондевская
        Стефания
    </div>
</div>
<div style="height:auto;" class="lk-small-block lk-user-details">
            <p></p>
        <p>МАОУ &quot;ГИМНАЗИЯ &quot;ГАРМОНИЯ&quot;</p>
        <p>Ученик</p>
    <p></p>

        <p>
                8 июня 2006
    </p>
        <div style="position: static; margin-top: 10px;" class="lk-user-details__links-block">
        <a href="/office/user/profile/">Редактировать профиль</a>
        <a href="/office/user/setting/">Настройки</a>
        <a href="/logout">Выйти</a>
    </div>
</div>


                                                                                    <div class="lk-right-block lk-activity block_js">
    <h2 class="lk-right-block-title">Активность</h2>
    <div class="lk-activity__content">
                      <div class="lk-activity__item">
            <p>
                                    Осуществлена регистрация на портале РЭШ
                            </p>
            <p class="lk-activity__time">
                                    14 апреля 2022
                            </p>
        </div>

    </div>
    <div class="lk-block-opts">
        <a href="/office/user/setting/"><i class="icon icon_edit"></i></a>
        <i class="icon icon_delete-cross" data-type="activity" data-href="/office/user/hide-widget"></i>
    </div>
</div>                                                    </div>
                        <div class="d-tc lk-col-2">


    <h2>Дневник: Жолондевская Стефания Александровна</h2>
    <div class="lk-subject-choice">
        <span>Предмет</span>
        <div class="lk-select">
            <select class="chosen-select chosen-select-diary" data-type="subject">
                <option value="0">Все</option>
                                  <option value="16" >Алгебра</option>
                                  <option value="51" >Алгебра и начала математического анализа</option>
                                  <option value="11" >Английский язык</option>
                                  <option value="5" >Биология</option>
                                  <option value="54" >Всероссийский открытый урок</option>
                                  <option value="4" >География</option>
                                  <option value="17" >Геометрия</option>
                                  <option value="33" >Естествознание</option>
                                  <option value="7" >Изобразительное искусство</option>
                                  <option value="19" >Информатика</option>
                                  <option value="2" >Испанский язык</option>
                                  <option value="3" >История</option>
                                  <option value="55" >Китайский язык</option>
                                  <option value="14" >Литература</option>
                                  <option value="32" >Литературное чтение</option>
                                  <option value="12" >Математика</option>
                                  <option value="6" >Музыка</option>
                                  <option value="10" >Немецкий язык</option>
                                  <option value="24" >Обществознание</option>
                                  <option value="43" >Окружающий мир</option>
                                  <option value="23" >Основы безопасности жизнедеятельности</option>
                                  <option value="41" >Право</option>
                                  <option value="42" >Россия в мире</option>
                                  <option value="13" >Русский язык</option>
                                  <option value="8" >Технология</option>
                                  <option value="50" >Технология (девочки)</option>
                                  <option value="48" >Технология (мальчики)</option>
                                  <option value="28" >Физика</option>
                                  <option value="9" >Физическая культура</option>
                                  <option value="1" >Французский язык</option>
                                  <option value="29" >Химия</option>
                                  <option value="40" >Экология</option>
                                  <option value="38" >Экономика</option>
                           </select>
        </div>
    </div>

    <div class="lk-date">
        <span>Выберите период</span>

        <div class="lk-date__item">
            <span>c</span>
            <div class="input-outer">
                <input type="text" value="15.04.2024" data-type="start" class="diary-datepicker-diary diary-datepicker-old">
            </div>
        </div>

        <div class="lk-date__item">
            <span>по</span>
            <div class="input-outer">
                <input type="text" value="22.04.2024" data-type="finish" class="diary-datepicker-diary diary-datepicker-new">
            </div>
        </div>
    </div>

    <div class="lk-subjects-table">
                  <table>
               <thead>
               <tr class="table-diary">
                   <th>Класс</th>
                   <th>Предмет</th>
                   <th>Тема урока</th>
                   <th>Тип задания</th>
                   <th>Результат</th>
                   <th>Время</th>
               </tr>
               </thead>
               <tbody>
                                                                                <tr>
                       <td class="table-date-row" colspan="6"><span class="table-date">20 апреля 2024</span></td>
                    </tr>
                                                                    <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/4971/">
                                                                            <p>Урок 34. Индивидуальные, групповые и командные действия в защите</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>12:41</p>
                                                                    <p>12:39</p>
                                                                    <p>12:36</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/5511/">
                                                                            <p>Урок 31. Техники перемещений и владения мячом</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                3

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>12:34</p>
                                                                    <p>12:32</p>
                                                                    <p>12:30</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3901/">
                                                                            <p>Урок 32. Тактика игры – командное нападение</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>12:27</p>
                                                                    <p>12:25</p>
                                                                    <p>12:24</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/5419/">
                                                                            <p>Урок 30. Защитное действие накрывание</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>12:21</p>
                                                                    <p>12:22</p>
                                                                    <p>12:17</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3879/">
                                                                            <p>Урок 28. Защитные действия: вырывание и выбивание</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>12:15</p>
                                                                    <p>12:11</p>
                                                                    <p>12:10</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3844/">
                                                                            <p>Урок 29. Защитное действие перехват</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>12:06</p>
                                                                    <p>12:04</p>
                                                                    <p>12:03</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/4969/">
                                                                            <p>Урок 27. Штрафной бросок</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>12:03</p>
                                                                    <p>12:00</p>
                                                                    <p>11:58</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/4639/">
                                                                            <p>Урок 24. Бросок одной и двумя руками в прыжке</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>11:53</p>
                                                                    <p>11:51</p>
                                                                    <p>11:50</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/6104/">
                                                                            <p>Урок 25. Броски мяча после двух шагов и в прыжке с близкого и среднего расстояния</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>11:50</p>
                                                                    <p>11:47</p>
                                                                    <p>11:44</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3854/">
                                                                            <p>Урок 26. Броски мяча в корзину со средних и дальних дистанций</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>11:41</p>
                                                                    <p>11:39</p>
                                                                    <p>11:38</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/6105/">
                                                                            <p>Урок 20. Техника ловли и передачи мяча одной рукой сбоку</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>11:35</p>
                                                                    <p>11:34</p>
                                                                    <p>11:30</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/6106/">
                                                                            <p>Урок 19. Техника ловли и передачи мяча одной рукой снизу</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                3

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>11:25</p>
                                                                    <p>11:28</p>
                                                                    <p>11:24</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3807/">
                                                                            <p>Урок 18. Техника передвижений с изменением направления движения нападающего и защитника</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>11:20</p>
                                                                    <p>11:21</p>
                                                                    <p>11:18</p>
                                                            </td>
                        </tr>
                                                                                            <tr>
                            <td><p>11</p></td>
                            <td><p>Физическая культура</p></td>
                            <td>
                                <a href="/subject/lesson/3819/">
                                                                            <p>Урок 17. Техника безопасности на занятиях баскетболом. Правила игры в баскетбол</p>
                                                                    </a>
                            </td>
                            <td>
                                                                    <p>        Контрольные задания В1
    </p>
                                                                    <p>        Контрольные задания В2
    </p>
                                                                    <p>        Задания тренировочного модуля
    </p>
                                                            </td>
                            <td>
                                                                    <p>
                                                                5

                                                                            </p>
                                                                    <p>
                                                                4

                                                                            </p>
                                                                    <p>
                                                                5

                                                                            </p>
                                                            </td>
                            <td>
                                                                    <p>11:15</p>
                                                                    <p>11:16</p>
                                                                    <p>11:12</p>
                                                            </td>
                        </tr>
                                                                          </tbody>
           </table>
           </div>
    <div class="lk-pages">

    </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    <div class="banner-contain block-shadow wrapper-content">
</div>

			</main>

		</div>
               <footer class="footer _hideable">

    <div class="partners">
        <div class="wrapper-content">
            <h1>НАШИ ПАРТНЁРЫ</h1>
            <div class="partners__wrap">
                    <a class="partners__link" target="_blank" href="https://edu.gov.ru/">
        <img src="/uploads/partner/60d04e5927df4.png" alt="Минпросвещения России">
    </a>
    <a class="partners__link" target="_blank" href="http://edu.ru">
        <img src="/uploads/partner/57c4385d27ab7.jpg" alt="Российское образование">
    </a>
    <a class="partners__link" target="_blank" href="http://obrnadzor.gov.ru">
        <img src="/uploads/partner/57f02217139a4.png" alt="Рособрнадзор">
    </a>
    <a class="partners__link" target="_blank" href="https://www.rgo.ru/">
        <img src="/uploads/partner/585b7c0268b15.jpg" alt="Русское географическое общество">
    </a>
    <a class="partners__link" target="_blank" href="https://rvio.histrf.ru/">
        <img src="/uploads/partner/57f0225b5205b.png" alt="Российское военно-историческое общество">
    </a>
    <a class="partners__link" target="_blank" href="https://www.prlib.ru/">
        <img src="/uploads/partner/580e011b1018a.png" alt="Президентская бибилиотека">
    </a>

            </div>
        </div>
    </div>

    <div class="wrapper-content">
        <nav class="footer__menu">
            <ul class="footer__menu-list">
                <li class="footer__menu-item">
                    <a href="/subject/" class="footer__menu-link">Предметы</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/class/1/" class="footer__menu-link">Классы</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-pupil" class="footer__menu-link">Ученику</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-teacher" class="footer__menu-link">Учителю</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-parent" class="footer__menu-link">Родителю</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-school" class="footer__menu-link">Школе</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/for-partner" class="footer__menu-link">Партнёрам</a>
                </li>
                <li class="footer__menu-item">
                    <a href="/feedback" class="footer__menu-link">Техническая поддержка</a>
                </li>
            </ul>
        </nav>
        <div class="row">
            <div class="footer__social col-1">
                <a class="soc-links soc-links_grey"
                   target="_blank"
                   href="https://vk.com/resh_edu">
                    <i class="icon icon_soc-vk"></i>
                </a>
                            </div>

            <div class="footer__copyright col-10 text-right">
                © Государственная образовательная платформа «Российская электронная школа»
            </div>
        </div>
            </div>
</footer>      
	</div>

	<div class="mask invis"></div>


	<div class="fs-menu hmbrg-menu">
    <div class="bg-color-wrapper">
        <div class="fs-wrapper">

            <section class="fs-sujects _tabs">
                <div class="fs-title-row">
                    <h2 class="fs-section-title">Предметы</h2>
                    <span class="fs-sort _tabs__tab">По алфавиту</span>
                    <span class="fs-sort _tabs__tab _tab-active">По предметным областям</span>
                </div>
                <div class="fs-subj _tabs__content">

                    <div class="fs-subjects-abc__box">
                        <ul class="fs-subjects-abc__list">
                                                                                                <li>
                                        <a href="/subject/16/">АЛГЕБРА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/51/">АЛГЕБРА И НАЧАЛА МАТЕМАТИЧЕСКОГО АНАЛИЗА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/11/">АНГЛИЙСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/5/">БИОЛОГИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/54/">ВСЕРОССИЙСКИЙ ОТКРЫТЫЙ УРОК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/4/">ГЕОГРАФИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/17/">ГЕОМЕТРИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/33/">ЕСТЕСТВОЗНАНИЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/7/">ИЗОБРАЗИТЕЛЬНОЕ ИСКУССТВО</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/19/">ИНФОРМАТИКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/2/">ИСПАНСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/3/">ИСТОРИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/55/">КИТАЙСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/14/">ЛИТЕРАТУРА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/32/">ЛИТЕРАТУРНОЕ ЧТЕНИЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/12/">МАТЕМАТИКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/6/">МУЗЫКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/10/">НЕМЕЦКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/24/">ОБЩЕСТВОЗНАНИЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/43/">ОКРУЖАЮЩИЙ МИР</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/23/">ОСНОВЫ БЕЗОПАСНОСТИ ЖИЗНЕДЕЯТЕЛЬНОСТИ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/41/">ПРАВО</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/42/">РОССИЯ В МИРЕ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/13/">РУССКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/8/">ТЕХНОЛОГИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/50/">ТЕХНОЛОГИЯ (ДЕВОЧКИ)</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/48/">ТЕХНОЛОГИЯ (МАЛЬЧИКИ)</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/28/">ФИЗИКА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/9/">ФИЗИЧЕСКАЯ КУЛЬТУРА</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/1/">ФРАНЦУЗСКИЙ ЯЗЫК</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/29/">ХИМИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/40/">ЭКОЛОГИЯ</a>
                                    </li>
                                                                                                                                <li>
                                        <a href="/subject/38/">ЭКОНОМИКА</a>
                                    </li>
                                                                                    </ul>
                    </div>

                </div>
                <div class="fs-subj _tabs__content _tab-cont-visible">
                    <div class="fs-subj__row">
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__technology"></i>
                                                                        <h3 class="fs-subtitle">Технология</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/54/">Всероссийский открытый урок</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/48/">Технология (мальчики)</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/8/">Технология</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/50/">Технология (девочки)</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__art"></i>
                                                                        <h3 class="fs-subtitle">Искусство</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/7/">Изобразительное искусство</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/6/">Музыка</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__math-Informatics"></i>
                                                                        <h3 class="fs-subtitle">Математика и информатика</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/19/">Информатика</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/12/">Математика</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/16/">Алгебра</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/17/">Геометрия</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/51/">Алгебра и начала математического анализа</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__philology"></i>
                                                                        <h3 class="fs-subtitle">Иностранный язык</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/2/">Испанский язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/11/">Английский язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/10/">Немецкий язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/1/">Французский язык</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/55/">Китайский язык</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__physical-culture"></i>
                                                                        <h3 class="fs-subtitle">Физическая культура и основы безопасности жизнедеятельности</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/23/">Основы безопасности жизнедеятельности</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/9/">Физическая культура</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__social-science"></i>
                                                                        <h3 class="fs-subtitle">Общественно-научные предметы</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/4/">География</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/24/">Обществознание</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/40/">Экология</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/3/">История</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/42/">Россия в мире</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/41/">Право</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/43/">Окружающий мир</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/38/">Экономика</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__philology"></i>
                                                                        <h3 class="fs-subtitle">Русский язык и литература</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/14/">Литература</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/32/">Литературное чтение</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/13/">Русский язык</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                                    <div class="fs-subj__grid">
                                <div class="fs-subj__title-link">
                                                                            <i class="icon icon icon_b-menu__natural-science"></i>
                                                                        <h3 class="fs-subtitle">Естественнонаучные предметы</h3>
                                </div>
                                <ul class="fs-subj__list">
                                                                                                                        <li>
                                                <a href="/subject/28/">Физика</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/29/">Химия</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/5/">Биология</a>
                                            </li>
                                                                                                                                                                <li>
                                                <a href="/subject/33/">Естествознание</a>
                                            </li>
                                                                                                            </ul>
                            </div>
                                            </div>
                </div>
            </section>
            <section class="fs-classes">
                <div class="fs-title-row">
                    <h2 class="fs-section-title">Классы</h2>
                </div>
                <div class="fs-classes__list">
                                            <a href="/class/1/" class="fs-classes__link">1</a>
                                            <a href="/class/2/" class="fs-classes__link">2</a>
                                            <a href="/class/3/" class="fs-classes__link">3</a>
                                            <a href="/class/4/" class="fs-classes__link">4</a>
                                            <a href="/class/5/" class="fs-classes__link">5</a>
                                            <a href="/class/6/" class="fs-classes__link">6</a>
                                            <a href="/class/7/" class="fs-classes__link">7</a>
                                            <a href="/class/8/" class="fs-classes__link">8</a>
                                            <a href="/class/9/" class="fs-classes__link">9</a>
                                            <a href="/class/10/" class="fs-classes__link">10</a>
                                            <a href="/class/11/" class="fs-classes__link">11</a>
                                    </div>
            </section>

            <footer class="fs-footer">
                <div class="fs-footer__grid fs-footer__grid-1">

                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/about">О проекте</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/guide">Гид по «Российской Электронной
                            Школе»
                        </a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/news/">Новости проекта</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/for-school">Школе</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item" href="/feedback">Задать вопрос</a>
                    </div>

                </div>
                <div class="fs-footer__grid fs-footer__grid-2">
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/for-parent">Родителям</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/for-teacher">Учителям</a>
                    </div>
                    <div class="fs-footer__item-row">
                        <a class="fs-footer__item-large" href="/for-partner">Партнерам</a>
                    </div>
                </div>

                <div class="fs-footer__grid fs-footer__grid-3">
                    <div class="fs-footer__item-row">
                        <span class="fs-footer__item-large">Мы в социальных сетях</span>
                    </div>
                    <div class="footer__social">
                        <a class="soc-links" href="https://vk.com/resh_edu">
                            <i class="icon icon_soc-vk"></i>
                        </a>
                                            </div>
                    <div class="fs-footer__item-row">
                        <br>

                    </div>
                    <div class="fs-footer__item-row fs-mobile-links">
                        <div class="fs-mobile-links__wrapper">
                            <span class="fs-menu-gp fs-mobile-links__logo"></span>
                            <div class="mobile-item__pending">в разработке</div>
                        </div>
                        <div class="fs-mobile-links__wrapper">
                            <span class="fs-menu-app-store fs-mobile-links__logo"></span>
                            <div class="mobile-item__pending">в разработке</div>
                        </div>
                    </div>
                </div>


            </footer>

            <div class="fs-menu-close _win-close">✕</div>
        </div>
    </div>
</div>


                		<script>window.jQuery || document.write('<script src="/js/vendor/jquery-1.12.0.min.js"><\/script>');</script>
		<script src="/js/vendor/jquery.iframetracker.min1.1.0.js?"></script>

		<script src="/custom/js/vendor/jquery.sumoselect.js?"></script>

		<script src="/assets/js/bundle.js?"></script>
		<script src="/custom/js/scripts/login_popup.js?"></script>
		<script src="/js/vendor/sweetalert.js?"></script>
		<script src="/custom/js/func.js?"></script>


		<!-- Yandex.Metrika counter -->
		<script>
            (function (d, w, c) {
                (w[c] = w[c] || []).push(function () {
                    try {
                        w.yaCounter39997495 = new Ya.Metrika({
                            id: 39997495,
                            clickmap: true,
                            trackLinks: true,
                            accurateTrackBounce: true,
                            webvisor: true
                        });
                        w.yaCounter43464019 = new Ya.Metrika({
                            id: 43464019,
                            clickmap: true,
                            trackLinks: true,
                            accurateTrackBounce: true,
                            webvisor: true
                        });
                    } catch (e) {
                    }
                });

                var n = d.getElementsByTagName("script")[0],
                    s = d.createElement("script"),
                    f = function () {
                        n.parentNode.insertBefore(s, n);
                    };
                s.type = "text/javascript";
                s.async = true;
                s.src = "https://mc.yandex.ru/metrika/watch.js";

                if (w.opera == "[object Opera]") {
                    d.addEventListener("DOMContentLoaded", f, false);
                } else {
                    f();
                }
            })(document, window, "yandex_metrika_callbacks");
		</script>
		<noscript>
			<div><img src="https://mc.yandex.ru/watch/39997495" style="position:absolute; left:-9999px;" alt=""/></div>
		</noscript>
		<!-- /Yandex.Metrika counter -->


    <script>
        $(function() {
            $('.teacher_message_icon').on('click', function () {
                var jThis = $(this),
                    message = jThis.attr('data-message');
                Swal.fire({
                    'text': message,
                    showCloseButton: true,
                    showConfirmButton: false
                });
            });
        });
    </script>

	<div class="show-password-change" data-period=""></div>
	</body>
</html>'''

if __name__ == "__main__":
    app.run('127.0.0.1', port=8080)
