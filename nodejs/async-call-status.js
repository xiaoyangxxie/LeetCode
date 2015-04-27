var http = require('http');
var xml2js = require('xml2js');


var no_answer = 0;
var line_busy = 0;
var timeout_max_waittime = 0;
var timeout_before_allowed_schedule = 0;
var timeout_after_allowed_schedule = 0;
var answered_by_human = 0;
var answered_by_fax = 0;
var answered_by_voicemail = 0;
var cancelled = 0;
var failed = 0;
var failed_internal_connection = 0;
var failed_external_connection = 0;
var blocked = 0;


http.createServer(function (req, res) {
	  console.log("received request to: " + req.url);
	  // buffer the body data
	  var body = '';
	  var outboundcallstatus ='';
	  req.on('data', function(chunk) {
	    body += chunk.toString();
	    console.log(body);
	    var parser = new xml2js.Parser();
	    parser.on('end',function(result){
	    	
	    	if(result){
	    		console.log('>>> validateOutboundCallStatus ');
	    		var phoneLineRequestID='';
	    		 var number ='';
	    		 var code = '';
	    		 var callEndTime ='';
	    		 var callStartTime = '';
	    			if(result['outboundCallStatus']['requestDetails']){
	    				if(result['outboundCallStatus']['requestDetails'][0]['$']['phoneLineRequestID']){
	    					phoneLineRequestID = result['outboundCallStatus']['requestDetails'][0]['$']['phoneLineRequestID'];
	    				}
	    				if(result['outboundCallStatus']['requestDetails'][0]['$']['number']){
	    					number = result['outboundCallStatus']['requestDetails'][0]['$']['number'];
	    				}
	    			}
	    			if(result['outboundCallStatus']['attempt']){
	    				if(result['outboundCallStatus']['attempt'][0]['$']['code']){
	    					code = result['outboundCallStatus']['attempt'][0]['$']['code'];
	    					if(code ==  'failed_external_connection'){
	    						failed_external_connection = failed_external_connection +1;
	    					}else if(code == 'no_answer'){
	    						no_answer = no_answer+1;
	    					}else if(code == 'line_busy'){
	    						line_busy = line_busy+1;
	    					}else if(code == 'timeout_max_waittime'){
	    						timeout_max_waittime = timeout_max_waittime+1;
	    					}else if(code == 'timeout_before_allowed_schedule'){
	    						timeout_before_allowed_schedule = timeout_before_allowed_schedule+1;
	    					}else if(code == 'timeout_after_allowed_schedule'){
	    						timeout_after_allowed_schedule = timeout_after_allowed_schedule+1;
	    					}else if(code == 'answered_by_human' ){
	    						answered_by_human = answered_by_human +1;
	    					}else if(code == 'answered_by_fax'){
	    						answered_by_fax = answered_by_fax+1;
	    					}else if(code == 'answered_by_voicemail'){
	    						answered_by_voicemail = answered_by_voicemail+1;
	    					}else if(code == 'cancelled'){
	    						cancelled = cancelled + 1;
	    					}else if(code == 'failed'){
	    						failed = failed+1;
	    					}else if(code == 'failed_internal_connection'){
	    						failed_internal_connection =failed_internal_connection+1;
	    					}else if(code == 'blocked'){
	    						blocked = blocked+1;
	    					}
	    				}
	    				if(result['outboundCallStatus']['attempt'][0]['$']['callStartTime']){
	    					callStartTime = result['outboundCallStatus']['attempt'][0]['$']['callStartTime'];
	    				}
	    				if(result['outboundCallStatus']['attempt'][0]['$']['callEndTime']){
	    					callEndTime = result['outboundCallStatus']['attempt'][0]['$']['callEndTime'];
	    				}
	    			}
	    		console.log('phoneLineRequestID:'+ phoneLineRequestID+
	    					' number:'+ number+
	    					' code:'+ code+
	    					' callStartTime:'+ callStartTime+
	    					' callEndTime:'+ callEndTime);

	    		console.log('<<< validateOutboundCallStatus ');
	    		console.log('============================================================================================');
	    		console.log('============================================================================================');
	    		console.log('Total Result: ');
	    		console.log('failed_external_connection:'+failed_external_connection);
	    		console.log('failed_internal_connection:'+failed_internal_connection);
	    		console.log('no_answer:'+no_answer);
	    		console.log('line_busy:'+line_busy);
	    		console.log('timeout_max_waittime:'+timeout_max_waittime);
	    		console.log('timeout_before_allowed_schedule:'+timeout_before_allowed_schedule);
	    		console.log('timeout_after_allowed_schedule:'+timeout_after_allowed_schedule);
	    		console.log('answered_by_human:'+answered_by_human);
	    		console.log('answered_by_fax:'+answered_by_fax);
	    		console.log('answered_by_voicemail:'+answered_by_voicemail);
	    		console.log('cancelled:'+cancelled);
	    		console.log('failed:'+failed);
	    		console.log('cancelled:'+cancelled);
	    		console.log('============================================================================================');
	    		console.log('============================================================================================');
	    		
	    	}
	    });
	    parser.parseString(body);
	  });

	  req.on('end', function() {
	    res.writeHead(200, {'Content-Type': 'text/plain'});
	    res.write("success!");
	  	res.end(); 
	  }); 
}).listen(9999);
console.log('Server running at :9999');
