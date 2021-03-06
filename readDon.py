#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: UTF-8 -*-

import os
from Person import PersonInfo
from Person import *

fname = "bob@hotmail.com"
p = PersonInfo(fname)

html = '''
	<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Donation Manager</title>

	<!-- Bootstrap -->
	<link rel="stylesheet" href="css/bootstrap.css" type="text/css">
	<link rel="stylesheet" href="css/masterStyles.css" type="text/css">
	<script type="text/javascript" src="https://www.simplify.com/commerce/v1/simplify.js"></script>

	<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
	      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
	      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	    <![endif]-->
	</head>
	<body>
	<div style="position:fixed;width:100%;">
	<nav class="navbar navbar-default navbar-inverse" style="border-radius:0px;">
	  <div class="container-fluid"> 
	    <!-- Brand and toggle get grouped for better mobile display -->
	    <div class="navbar-header">
	      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>
	      <div class="proj-name"><img src="img/mc.png" height="25px"/> Spend to Save</div> 
	    </div>
	    
	    <!-- Collect the nav links, forms, and other content for toggling -->
	    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
	      <ul class="nav navbar-nav navbar-right">
	        <li><a href="http://localhost:8000/PageGen.py?first=bob%40hotmail.com&last=password">Home </a> </li>
	        <li  class="active"><a href="#">Donation Manager <span class="sr-only">(current)</span></a> </li>
	        <li><a href="http://localhost:8000/readCharities.py">Charity Settings </a> </li>
	      </ul>
	      <!--<ul class="nav navbar-nav navbar-right">
	        <li><a href="#profile">Profile</a> </li>
	        <li><a href="#">Logout</a> </li>
	      </ul>-->
	    </div>
	    <!-- /.navbar-collapse --> 
	  </div>
	  <!-- /.container-fluid --> 
	</nav>
	</div>
	
<div id="user-info" class="container-fluid">
  <div class="row">
    <div class="gen-info">
    	<div class="user-pic">
       		<img src="img/gir.jpg" height="150px" id="user-pic"/>
        </div>
	        <div class="user-info"> '''+str(p.firstName)+" "+str(p.lastName)+'''
	        	<br/>''' + str(p.level) + ''' <br/><br/>
	            Donations to next level:<br/>
	            <div class="progress" style="width:90%;margin-left:5%">
	            	<div class="progress-bar progress-bar-striped" 
	                	role="progressbar" aria-valuenow="50"
	                    aria-valuemin="0" aria-valuemax="100" style="width:'''+str(int(float(p.getPercentageToNextLevel())))+'''%">'''+p.getPercentageToNextLevel()+'''% to '''+p.getNameOfNextLevel()+'''
	  				</div>
	  			</div>
	            <br/>'''+str(p.username)+'''<br/><br/>'''+"Card ending in: "+str(p.cardNum)[-4:]+'''
	        </div>
	    </div>
	  </div>
	</div>

	<!--<form id="simplify-payment-form" action="" method="POST">
	    <div>
	        <label>Credit Card Number: </label>
	        <input id="cc-number" type="text" maxlength="20" autocomplete="off" value="" autofocus />
	    </div>
	    <div>
	        <label>CVC: </label>
	        <input id="cc-cvc" type="text" maxlength="4" autocomplete="off" value=""/>
	    </div>
	    <div>
	        <label>Expiry Date: </label>
	        <select id="cc-exp-month">
	            <option value="01">Jan</option>
	            <option value="02">Feb</option>
	            <option value="03">Mar</option>
	            <option value="04">Apr</option>
	            <option value="05">May</option>
	            <option value="06">Jun</option>
	            <option value="07">Jul</option>
	            <option value="08">Aug</option>
	            <option value="09">Sep</option>
	            <option value="10">Oct</option>
	            <option value="11">Nov</option>
	            <option value="12">Dec</option>
	        </select>
	        <select id="cc-exp-year">
	            <option value="13">2013</option>
	            <option value="14">2014</option>
	            <option value="15">2015</option>
	            <option value="16">2016</option>
	            <option value="17">2017</option>
	            <option value="18">2018</option>
	            <option value="19">2019</option>
	            <option value="20">2020</option>
	            <option value="21">2021</option>
	            <option value="22">2022</option>
	        </select>
	    </div>
	    <button id="process-payment-btn" type="submit">Process Payment</button>
	</form>-->
	<div id="donation-info" class="content">
	  	<div class="title">
	    	Edit your Donation Settings
	    </div>
	    <br/>
	  	<div id="amount">
	  		<div class="col-md-5 donation-text">
	        	Donation as percentage of spending:
	        </div>
	        <div class="col-md-3">
	        	<div class="input-group">
	    			<input type="text" class="form-control" value="5.3" style="width:50%;">
	  			</div>
	        </div>
	        <div class="col-md-1 optional">
	        	%
	        </div>
	  	</div>
	    <div id="maximum">
	  		<div class="col-md-5 donation-text">
	        	Maximum donation per cycle:        
	        </div>
	        <div class="col-md-3">
	        	<div class="input-group">
	    			<input type="text" class="form-control" value="$5000" style="width:50%;">
	  			</div>
	        </div>
	        <div class="col-md-1 optional">
	        	(optional)
	        </div>
	  	</div>
	    <div id="minimum">
	  		<div class="col-md-5 donation-text">
	        	Minimum donation per cycle:        
	        </div>
	        <div class="col-md-3">
	        	<div class="input-group">
	    			<input type="text" class="form-control" value="$60" style="width:50%;">
	  			</div>
	        </div>
	        <div class="col-md-1 optional">
	        	(optional)
	        </div>
	  	</div>
	    <div id="cycle">
	  		<div class="col-md-5 donation-text">
	        	Cycle length:
	        </div>
	        <div class="col-md-3">
	        	<div class="input-group">
	    			<input type="text" class="form-control" value="2" style="width:50%;">
	  			</div>
	        </div>
	        <div class="col-md-1 drop">
	        	<div class="dropdown">
	  				<button class="btn dropdown-toggle" type="button" data-toggle="dropdown">week(s)
	  				<span class="caret"></span></button>
	  				<ul class="dropdown-menu">
	    				<li><a href="#">month(s)</a></li>
	    				<li><a href="#">year(s)</a></li>
	  				</ul>
				</div>
	        </div>
	  	</div>
	    <div id="repeat">
	  		<div class="col-md-5 donation-text">
	        	Repeat Until:
	        </div>
	        <div class="col-md-3">
	        	<div class="input-group">
	    			<input type="text" class="form-control" value="01/2017" style="width:50%;">
	  			</div>
	        </div>
	  	</div>
	    <div id="email">
	  		<div class="col-md-5 donation-text">
	        	Email Notification on Donation:
	        </div>
	        <div class="col-md-3 donation-text">
	        	<div class="dropdown">
	  				<button class="btn dropdown-toggle" type="button" data-toggle="dropdown">yes
	  				<span class="caret"></span></button>
	  				<ul class="dropdown-menu">
	    				<li><a href="#">no</a></li>
	  				</ul>
				</div>
	        </div>
	  	</div>
	    <div id="facebook">
	  		<div class="col-md-5 donation-text">
	        	Facebook Auto Post on Donation:
	        </div>
	        <div class="col-md-2 donation-text">
	        	<div class="dropdown">
	  				<button class="btn dropdown-toggle" type="button" data-toggle="dropdown">yes
	  				<span class="caret"></span></button>
	  				<ul class="dropdown-menu">
	    				<li><a href="#">no</a></li>
	  				</ul>
				</div>
	        </div>
	        <div class="col-md-2 optional">
	        	<a href="#">edit auto post</a>
	        </div>
	  	</div>
	    <div id="twitter">
	  		<div class="col-md-5 donation-text">
	        	Twitter Auto Tweet on Donation:
	        </div>
	        <div class="col-md-2 donation-text">
	        	<div class="dropdown">
	  				<button class="btn dropdown-toggle" type="button" data-toggle="dropdown">no
	  				<span class="caret"></span></button>
	  				<ul class="dropdown-menu">
	    				<li><a href="#">yes</a></li>
	  				</ul>
				</div>
	        </div>
	        <div class="col-md-2 optional">
	        	<a href="#">edit auto tweet</a>
	        </div>
	  	</div>
	    <div id="save-cancel" >
	    	<div class="col-md-5 donation-text"> 
	        </div>
	        <div class="col-md-1"  style="margin-top:50px;">
	        	<div class="input-group">
	    			<button type="button" class="btn btn-default btn-md"> Save </button>
	  			</div>
	        </div>
	        <div class="col-md-1"  style="margin-top:50px;">
	        	<button type="button" class="btn btn-default btn-md"> Cancel </button>
	        </div>
	    </div>
	  </div>
	  <br/>
	  <footer class="text-center">
	    <div class="container-fluid">
	        <div class="col-xs-12" style="margin-bottom:10px;">
	        <hr/>
	          <p>Copyright © 2015 BXT SENC. All rights reserved.</p>
	      </div>
	    </div>
	  </footer>
	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) --> 
	<script src="js/jquery-1.11.2.min.js"></script> 
	<!-- Include all compiled plugins (below), or include individual files as needed --> 
	<script src="js/bootstrap.min.js"></script>
	</body>
	</html>
	'''

print html