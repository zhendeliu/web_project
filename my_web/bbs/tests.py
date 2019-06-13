from django.test import TestCase

# Create your tests here.


<div class="container">
    <div class="row mt-2">

        {% for post in posts_list %}
        <!-- 文章内容 -->
        <div class="col-4 mb-4">
        <!-- 卡片容器 -->
            <div class="card h-100">
                <!-- 标题 -->
                <h4 class="card-header">{{ post.title }}</h4>
                <!-- 摘要 -->
                <div class="card-body">
                    <p class="card-text">{{ post.body|slice:'100' }}</p>
                </div>
                <!-- 注脚 -->
                <div class="card-footer">
                    <a href="#" class="btn btn-primary">
                        read more</a>
                    <span>
                        <small class="col align-self-end" style="color: gray;">
                            浏览：100
                        </small>
                    </span>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>




<div class='container'>
    <div class="list" id="threadlist" style="position: relative;">
    <script src="/static/css/forum_moderate.js" type="text/javascript"></script>
    <form method="post" autocomplete="off" name="moderate" id="moderate" action="">
    <input type="hidden" name="formhash" value="31213a3e">
    <input type="hidden" name="listextra" value="">
        {% if posts_list %}
        {% for post in posts_list %}
            <table width="100%">
        <tbody><tr id="post">
            <td width="10%" class="avatar" valign="middle">
		    <a href="{{ post.get_absolute_url }}" title="">
			<!--img src="#">-->
		    </a>
            </td>
            <td width="auto" valign="middle" class="mainbox">
                <div class="title">
                <a class="title" href="{{ post.get_absolute_url }}" rel="bookmark" title="">{{ post.title }}</a>
                </div>
                <div class="status">
                    <div class="cate"><a href="{{ post.column.get_absolute_url }}" target="_blank">{{ post.column }}</a></div>
                    <span>•</span>
                    <div class="date"><span title="">发表于{{ post.created_time|date:"Y-m-d H:i:s" }}</span></div>
                    <span>•</span>
                    <div class="author">{{ post.author }}</div>
                </div>
            </td>
            <td width="11%" align="right" valign="middle" class="reply">
            	<a href="" target="_blank">浏览：100</a>
            </td>
        </tr>
    </tbody></table>
        {% endfor %}
    {% endif %}
    </div>
</div>