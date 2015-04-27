var http = require('http');
var xml2js = require('xml2js');

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