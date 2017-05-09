<%--
  Created by IntelliJ IDEA.
  User: happy
  Date: 2016-08-07
  Time: 오후 11:06
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>회원가입</title>

    <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body>
<table align="center" border="0" cellspacing="0" cellpadding="5" >
  <tr> 
    <td align="center" valign="middle" bgcolor="#FFFFCC"> 
      <table border="1" cellspacing="0" cellpadding="2"  align="center">
        <form name="regForm" method="post" action="RegisterProc.jsp">
          <tr align="center" bgcolor="#996600"> 
            <td colspan="3"><font color="#FFFFFF"><b>회원 가입</b></font></td>
          </tr>
          <tr> 
            <td width="16%">아이디</td>
            <td width="57%"> <input type="text" name="id" size="15">
		                     <input type="button" value="ID중복확인" 
                              onClick="idCheck(this.form.id.value)"></td>
            <td width="27%">아이디를 적어 주세요.</td>
          </tr>
          <tr> 
            <td>패스워드</td>
            <td> <input type="password" name="passwd" size="15"> </td>
            <td>패스워드를 적어주세요.</td>
          </tr>
          <tr> 
            <td>패스워드 확인</td>
            <td> <input type="password" name="repasswd" size="15"> </td>
            <td>패스워드를 확인합니다.</td>
          </tr>
          <tr> 
            <td>이름</td>
            <td> <input type="text" name="name" size="15"> </td>
            <td>고객실명을 적어주세요.</td>
          </tr>
		  <tr> 
            <td>주민등록번호</td>
            <td> <input type="text" name="num1" size="6" maxlength="6"
			onKeyUp="if(this.value.length==6)regForm.num2.focus()" >-
			     <input type="text" name="num2" size="7" maxlength="7"
				  onKeyUp="if(this.value.length==7)regForm.email.focus();"></td>
            <td>주민등록번호를 적어주세요.</td>
          </tr>
          <tr> 
            <td>이메일</td>
            <td> <input type="text" name="email" size="27"> </td>
            <td>이메일을 적어주세요.</td>
          </tr>
          <tr>  
            <td>전화번호</td>
            <td> <input type="text" name="phone" size="20"> </td>
            <td>연락처를 적어 주세요.</td>
          </tr>
		  <tr>  
            <td>우편번호</td>
            <td> <input type="text" name="zipcode" size="7">
                 <input type="button" value="우편번호찾기" onClick="zipCheck()"></td>
            <td>우편번호를 검색 하세요.</td>
          </tr>
          <tr>  
            <td>주소1</td>
            <td><input type="text" name="address1" size="70" readonly></td>
            <td>주소1</td>
          </tr>
		  <tr>  
            <td>주소</td>
            <td><input type="text" name="address2" size="70"></td>
            <td>나머지 주소를 적어 주세요.</td>
          </tr>
		  <tr>  
            <td>직업</td>
            <td><select name=job>
 					<option value="0">선택하세요.
 					<option value="회사원">회사원
 					<option value="연구전문직">연구전문직
 					<option value="교수학생">교수학생
 					<option value="일반자영업">일반자영업
 					<option value="공무원">공무원
 					<option value="의료인">의료인
 					<option value="법조인">법조인
 					<option value="종교,언론,에술인">종교.언론/예술인
 					<option value="농,축,수산,광업인">농/축/수산/광업인
 					<option value="주부">주부
 					<option value="무직">무직
 					<option value="기타">기타
				  </select></td>
            <td>직업을 선택 하세요.</td>
          </tr>
          <tr> 
            <td colspan="3" align="center"> 
             <input type="button" value="회원가입"   onclick="inputCheck()"> 
              &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
             <input type="reset" value="다시쓰기"> 
            </td>
          </tr>
        </form>
      </table>
    </td>
  </tr>
</table>

</body>
</html>
