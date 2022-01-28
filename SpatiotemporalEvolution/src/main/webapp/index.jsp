<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
	<link rel="icon" href="${pageContext.request.contextPath}/icons/favicon.ico">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/bootstrap/bootstrap.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/mycss/mystyle.css">
    <script src="${pageContext.request.contextPath}/js/jquery/jquery.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/popper.min.js"></script>
    <script src="${pageContext.request.contextPath}/js/bootstrap/bootstrap.min.js"></script>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/toastr.min.css">
    <title>装备事件时空分析</title>
    <style type="text/css">
	    .blog-footer{                                                     
		    padding:2.5rem 1rem;                                          
		    font-size:12px;                                               
		    color:#fff;                                                   
		    text-align:center;                                            
		    position:fixed;                                               
		    bottom:0;                                                     
		    z-index:111;                                                  
		    border-top:0;
		    right:0;
		    left:0;
		    background:transparent;           
		}                                                                 
		.blog-footer a{                                                   
	    	color:#fff;                                                   
		}                                                                
    </style>
    <style>
        label{
            margin:10px;
        }
        .a-radio{
            display: none;
        }
        .b-radio{
            display: inline-block;
            border:1px solid #ccc;
            width:20px;
            height: 20px;
            border-radius:2px;
            vertical-align: middle;
            margin-right: 15px;
            position: relative;
        }
        .b-radio:before{
            content: '';
            font-size: 0;
            width: 20px;
            height: 20px;
            background: gray;
            position: absolute;
            left:50%;
            top:50%;
            margin-left: -9px;
            margin-top: -9px;
            border-radius: 2px;
            display: none;
        }
        .a-radio:checked~.b-radio:before{
            display: block;
        }
		.home-page{
			width: 100%;
			height: 100%;
			margin-top: 75px;
			background:url('${pageContext.request.contextPath}/img/index_world_map-4.jpg') no-repeat;
			background-size: cover;
			position: absolute;
			overflow-x:hidden;
			overflow-y:hidden;
		}
    </style>
</head>
<body class="home-page">
	<!--/ 导航 /-->
	<nav class="navbar navbar-expand-md fixed-top nav-border">
		<div class="container">
			<a class="navbar-brand" href="${pageContext.request.contextPath}/Developer/project">
				<img class=" bodystyle" src="${pageContext.request.contextPath}/icons/favicon.ico" style="width:50px">
                <span class="text-font-beautiful">军事事件时空关联分析系统</span>
			</a>

			<div class="navbar-collapse justify-content-end collapse">
				<ul class="navbar-nav">
					<li><a href="javascript:void(0)" onclick="doRegister()" class="btn btn-success">注册</a></li>
					&nbsp;&nbsp;
					<li><a href="javascript:void(0)" onclick="doLogin()" class="btn btn-success">登录</a></li>
				</ul>
			</div>
		</div>
	</nav>
	<section class="container-main">
		<div class="container-main">
			<div class="container" hidden>
				<div class="carousel" data-ride="carousel" id="slidershow"  data-interval="2000" >
					<!--轮播图片-->
					<div class="carousel-inner" role="listbox">
						<div class="carousel-item active">
							<div style="position:relative;margin-left:0%;top:0;z-index:0;width:auto;height:100%;">
								<img src="${pageContext.request.contextPath}/img/index_world_map-1.jpg" style=" width:auto;height:100%;" alt="">
							</div>
							<div style="position:fixed;margin-left:45%;top:0;z-index:1;width:auto;height:100%;align-items: center;line-height:300px;">
								<p></p>
							</div>
						</div>
						<div class="carousel-item">
							<div style="position:relative;margin-left:0%;top:0;z-index:0;width:auto;height:100%;">
								<img src="${pageContext.request.contextPath}/img/index_world_map-2.jpg"  style=" width:auto;height:100%;" alt="">
							</div>
							<div style="position:fixed;margin-left:45%;top:0;z-index:1;width:auto;height:100%;align-items: center;line-height:300px;">
								<p></p>
							</div>
						</div>
						<div class="carousel-item">
							<div style="position:relative;margin-left:0%;top:0;z-index:0;width:auto;height:100%;">
								<img src="${pageContext.request.contextPath}/img/index_world_map-3.jpg" style=" width:auto;height:100%;" alt="">
							</div>
							<div style="position:fixed;margin-left:45%;top:0;z-index:1;width:auto;height:100%;align-items: center;line-height:300px;">
								<p></p>
							</div>
						</div>
						<div class="carousel-item">
							<div style="position:relative;margin-left:0%;top:0;z-index:0;width:auto;height:100%;">
								<img src="${pageContext.request.contextPath}/img/index_world_map-4.jpg" style=" width:auto;height:100%;" alt="">
							</div>
							<div style="position:fixed;margin-left:45%;top:0;z-index:1;width:auto;height:100%;align-items: center;line-height:300px;">
								<p></p>
							</div>
						</div>
						<div class="carousel-item">
							<div style="position:relative;margin-left:0%;top:0;z-index:0;width:auto;height:100%;">
								<img src="${pageContext.request.contextPath}/img/index_world_map-3.jpg" style=" width:auto;height:100%;" alt="">
							</div>
							<div style="position:fixed;margin-left:45%;top:0;z-index:1;width:auto;height:100%;align-items: center;line-height:300px;">
								<p></p>
							</div>
						</div>
					</div>
					<!--轮播指示器-->
					<ul class="carousel-indicators">
						<li data-slide-to="0" data-target="#slidershow" class="active"></li>
						<li data-slide-to="1" data-target="#slidershow"></li>
						<li data-slide-to="2" data-target="#slidershow"></li>
						<li data-slide-to="3" data-target="#slidershow"></li>
						<li data-slide-to="4" data-target="#slidershow"></li>
					</ul>
				</div>
			</div>
			<div class="blink" style="position: fixed;left:0;right:0;text-align: center;bottom: 150px;">按【Ctrl+shift+C】键，可以切换背景</div>
		</div>
	</section>
	<!--登录  模态框（Modal） -->
	<div class="modal fade" id="logModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h4 class="modal-title" id="myModalLabel">登录框</h4>
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
				</div>
				<div class="modal-body">
					<form class="form-horizontal" id="login_form" name="myform_log">
						<div class="form-group">
							<div class="col-sm-8">
                                <span style="float: left;">账号:</span>
								<input id="acc" placeholder="请输入您的登录账号" type="text" class="form-control" name="account" style="margin-top: 8px;" />
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-8">
                                <span style="float: left;">密码:</span>
								<input id="pw" placeholder="请输入您的密码" type="password" class="form-control" name="pw" style="margin-top: 8px;" />
							</div>
						</div>
                        <div class="form-group">
                            <p style="margin-bottom: 0;">
                                &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                                <label>
                                    <input type="radio" class="a-radio" name="role"  id="user" value="usr" checked="checked"/>
                                    <span class="b-radio"></span>普通用户
                                </label>
								&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                                <label>
                                    <input type="radio" class="a-radio" name="role" id="administrator" value="admin"/>
                                    <span class="b-radio"></span>管理员
                                </label>
                            </p>
                        </div>
					</form>
				</div>

				<div class="modal-footer" >
					<div>
						<div>
							<button id="log_pass" type="button" class="btn btn-success" onclick="dologPass()">确认</button>
<%--							<button id="log_refuse" type="button" class="btn btn-danger col-sm-4" onclick="dologRefuse()">取消</button>--%>
						</div>
					</div>
				</div>
			</div>
			<!-- /.modal-content -->
		</div>
		<!-- /.modal -->
	</div>
	<!--注册  模态框（Modal） -->
	<div class="modal fade" id="regModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h4 class="modal-title" id="myregModalLabel">注册框</h4>
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
				</div>
				<div class="modal-body">
					<form class="form-horizontal" id="reg_form" name="myform_reg">
						<div class="form-group">
							<div class="col-sm-8">
                                <span style="float: left;">用户名:</span>
								<input id="reg_name" placeholder="请输入您的昵称" type="text" class="form-control" name="username" style="margin-top: 8px;" />
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-8">
                                <span style="float: left;">账号:</span>
								<input id="reg_acc" placeholder="请设置您的登录账号" type="text" class="form-control" name="account" style="margin-top: 8px;" onblur="checkAccount()" />
								<span id="acc_info"></span>
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-8">
                                <span style="float: left;">密码:</span>
								<input id="reg_pw" placeholder="请输入您的密码（只能包含字母、数字和‘.’，‘_’，‘@’，‘#’）" type="password" class="form-control" name="pw" style="margin-top: 8px;" onblur="checkPassword()" />
								<span id="pw_info"></span>
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-8">
                                <span style="float: left;">再次输入密码:</span>
								<input id="aga_pw" placeholder="请再次输入密码" type="password" class="form-control" name="pw" style="margin-top: 8px;" onblur="checkPasswordEqual()"/>
								<span id="pw_info_check"></span>
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-8">
                                <p style="margin-bottom: 0;">
                                    <span style="float: left;margin: 10px 20px 10px 0;">性别:</span>
                                    <label>
                                        <input type="radio" class="a-radio" name="sex"  id="man" value="man" checked="checked"/>
                                        <span class="b-radio"></span>男
                                    </label>
                                    <label>
                                        <input type="radio" name="sex" id="woman" class="a-radio" value="wuman"/>
                                        <span class="b-radio"></span>女
                                    </label>
                                </p>
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-8">
                                <span style="float: left;">Email:</span>
								<input id="reg_eml" placeholder="请输入邮箱地址" type="text" class="form-control" name="Email" style="margin-top: 8px;" onblur="checkEmail()"/>
								<span id="eml_info"></span>
							</div>
						</div>
					</form>
				</div>

				<div class="modal-footer" >
					<div style="text-align:center">
						<div>
							<button id="reg_pass" type="button" class="btn btn-success" onclick="doregPass()">确认</button>
						</div>
					</div>
				</div>
			</div>
			<!-- /.modal-content -->
		</div>
		<!-- /.modal -->
	</div>
	<footer class="blog-footer">
		<p>
			<a href="${pageContext.request.contextPath}/Developer/about">关于我们</a>
			<span>|</span>
			<a href="${pageContext.request.contextPath}/Developer/join">加入我们</a>
			<span>|</span>
			<a href="${pageContext.request.contextPath}/Developer/contact">联系我们</a>
		</p>
		<p><span>Copyright © 基于开源军事情报源的时空关联分析 </span><a href="http://beian.miit.gov.cn" target="_blank">晋ICP备 - 2021008544号 </a></p>
	</footer>
    <script src="${pageContext.request.contextPath}/js/toastr.min.js"></script>
	<script>
		toastr.options.positionClass = 'toast-center-center';
		/* 登录 */
		function doLogin(){
			$('#logModal').modal('toggle');
		}
		/* 注册 */
		function doRegister(){
			$('#regModal').modal('toggle');
		}
		/* 登录确认 */
		function dologPass(){
			var urls;
            if(document.myform_log.role.item("users").checked){
                urls="${pageContext.request.contextPath}/Login/user";}
            else {
                urls="${pageContext.request.contextPath}/Login/admin";
            }
			$.post({
				url: urls,
				data:{"Account":$("#acc").val(),"password":$("#pw").val()},
				success: function(data){
					var res=data.result;
					if(res==="ok"){
                        if(data.role==="user"){
                            window.location.href="${pageContext.request.contextPath}/Show/Container";
                        }else if(data.role==="admin"){
                            window.location.href="${pageContext.request.contextPath}/Admin/show";
                        }
					 }else if(res==="password_error") {
						toastr.error("密码不符合要求！");
					}
					else toastr.error("用户名或密码错误！");
				}
			});
		}
		/* 登录取消 */
		function dologRefuse(){
			$('#logModal').modal('hide');
		}
		/* 注册确认 */
		function doregPass(){
			var sex = 0;
			if(document.myform_reg.sex.item("man").checked)sex=1;
			$.post({
				url: "${pageContext.request.contextPath}/Login/Register",
				data:{"username":$("#reg_name").val(),"Account":$("#reg_acc").val(),"sex":sex,"password":$("#reg_pw").val(),
					"Email":$("#reg_eml").val()},
				success: function(data){
					var res=data.result;
					if(res==="ok"){
						toastr.success('注册成功');
						window.location.href="${pageContext.request.contextPath}/Show/Container";
					}else if(res==="had") toastr.error("该账号已存在！");
					else if(res==="password_error") {
						toastr.error("密码不符合要求！");
					}else toastr.error("系统或服务器出错！");
				}
			});
		}
		/* 注册取消 */
		function doregRefuse(){
			$('#regModal').modal('hide');
		}
		var i = 0;
		var HOME_PAGE = $( ".home-page" );
		$(document).ready(function () {
			$(this).keypress(function(event){
				if (event.keyCode === 3){
					console.log(event.keyCode);
					HOME_PAGE.css( "background" ,"url('${pageContext.request.contextPath}/img/index_world_map-"+(i%4+1).toString() + ".jpg') no-repeat");
					HOME_PAGE.css( "background-size" ,"cover");
					HOME_PAGE.css( "position" ,"absolute");
					i+=1;
				}
			})
		});
		function checkAccount(){
			$.post({
				url: "${pageContext.request.contextPath}/Login/Register/check/account",
				data:{"Account":$("#reg_acc").val()},
				success: function(data){
					var res=data.result;
					if(res.toString()==="ok"){
						$("#acc_info").css("color","green");
						$("#acc_info").html("");
					}else {
						$("#acc_info").css("color","red");
						$("#acc_info").html("该账号已经被注册！");
					}
				}
			})
		}
		function checkPassword() {
			var pw1=$("#reg_pw").val();
			var regx = new RegExp("^[a-zA-Z_.@#]{0,}$");
			if (regx.test(pw1)){
				$("#pw_info").css("color","green");
				$("#pw_info").html("");
				$("#pw_info").val("ok");
			}else {
				$("#pw_info").css("color","red");
				$("#pw_info").html("密码不符合要求！");
				$("#pw_info").val("error");
			}
		}
		function checkPasswordEqual(){
			var pw1=$("#reg_pw").val();
			var pw2=$("#aga_pw").val();
			if(pw1==pw2){
				$("#pw_info_check").css("color","green");
				$("#pw_info_check").html("");
				$("#pw_info_check").val("ok");
			}else {
				$("#pw_info_check").css("color","red");
				$("#pw_info_check").html("两次输入的密码不一致！");
				$("#pw_info_check").val("error");
			}
		}
		function checkEmail() {
			var email=$("#reg_eml").val();
			var regx = new RegExp(".*@.*");
			if (regx.test(email)){
				$("#eml_info").css("color","green");
				$("#eml_info").html("");
				$("#eml_info").val("ok");
			}else {
				$("#eml_info").css("color","red");
				$("#eml_info").html("请输入正确的邮箱！");
				$("#eml_info").val("error");
			}
		}
		var BLINK = $(".blink");
		setInterval(function(){ BLINK.fadeIn(2500); }, 5000);
		setTimeout(function(){ setInterval(function(){ BLINK.fadeOut(2500); }, 5000); }, 2500);
	</script>
</body>
</html>