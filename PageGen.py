#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: UTF-8 -*-

from Person import PersonInfo
from Person import *
import os,sys
import cgi
 
### Retrieve CGI Values ###
form = cgi.FieldStorage()
val1 = form.getvalue('first')
val2 = form.getvalue('last')
###########################


### Method Definitions ###
# Validate account
def isValidUP(username,password):
	accFile = open(os.path.join(datapath,accountsFile),"r").readlines()
	for pair in accFile:
		u,p = pair.strip().split(",")
		if u==username and p==password: return True
	return False

#


#####################
# CGI Generate Page #
#####################

### Authentication Failed ###
if not isValidUP(val1,val2):
	print "Content-type: text/html"
	print
	print "<title>Test CGI</title>"
	print """ Invalid U+P: %s %s
	</body></html>""" % (val1, val2)

### Authentication Worked ###
else:
	p = PersonInfo(val1)
	print '''
	<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Profile</title>

	<!-- Bootstrap -->
	<link rel="stylesheet" href="css/bootstrap.css" type="text/css">
	<link rel="stylesheet" href="css/masterStyles.css" type="text/css">
	<script src="js/masterscript.js"></script>

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
        <li class="active"><a href="#">Home <span class="sr-only">(current)</span></a> </li>
        <li><a href="http://localhost:8000/readDon.py">Donation Manager </a> </li>
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

	<div id="donation-info" class="content">
	  	<div class="title">
	    		Welcome '''+('Mr. ' if p.gender=='M' else 'Ms. ')+p.lastName+'''
	    </div>
	    <br/>
	  	<div id="total">
	  		<div class="col-md-4 donation-text" style="z-index:-100;">
	        	Total Donations To Date:
	        </div>
	        <div class="col-md-3 donation-text" style="z-index:-100;">
	        	<div class="">
	    			$'''+str(p.getTotalDonations())+'''0 CAD
	    			
	  			</div>
	        </div>
	  	</div>
	    <div id="charities-helped">
	  		<div class="col-md-5 donation-text">
	        	Charities Donated to:      
	        </div>
	  	</div>
	    <br/>
	    <div class="table-responsive" style="width:80%;margin-left:10%;">
	    	<table class="table table-striped table-hover">
	    <thead>
	      <tr>
	        <th>Charity</th>
	        <th>Date Last Donated</th>
	        <th>Last Donation</th>
	        <th>Lifetime Total</th>
	      </tr>
	    </thead>

	    <tbody> '''+p.generateDonationTable()+'''</tbody>

	  </table>

		<div style="margin-left:-100px;">
	  		<div class="col-md-4 donation-text">
	        	Upcoming Donation:
	        </div>
	        <div class="col-md-3 donation-text">
	        	<div class="">
	    			$'''+str(p.genUpcomingDonation())+'''0 CAD
	    			
	  			</div>
	        </div>
	  	</div>
		<br/>
	    <div id="bank-trans" style="margin-left:-100px;">
	  		<div class="col-md-5 donation-text">
	        	Card Transactions:     
	        </div>
	  	</div>

		<div class="table-responsive" style="width:100%;">
	    	<table class="table table-striped table-hover">
	    <thead>
	      <tr>
	        <th>Merchant Name</th>
	        <th>Purchase Date</th>
	        <th>Purchase Amount</th>
	        <th>Resulting Donation</th>
	      </tr>
	    </thead>

	    <tbody> '''+p.genBankTransTable()+'''</tbody>

	  </table>

	    </div>
	    <br/>
	    <br/>
		<img src="img/facebook.png" height="25px"/>
		Link your Facebook

		<br/>
		<br/>
		<img src="img/Twitter-icon.png.png" height="25px"/>
		Link your Twitter
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
