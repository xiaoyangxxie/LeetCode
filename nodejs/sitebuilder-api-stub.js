var http = require('http');
var querystring = require('querystring');
var fs = require('fs');

// evaluate the configuration file
eval(fs.readFileSync('sitebuilder-config.js', encoding="UTF-8"));

// not ripped off, see node.js documentation for more info
http.createServer(function (req, res) {

    // buffer the body data
    var body = '';
    req.on('data', function(chunk) {
    });

    // received the entire request, time to respond
    req.on('end', function() {

        var parsedReq = require('url').parse(req.url, true);

        // split up the path stack
        // stack[0]:
        // stack[1]: sb-api
        // stack[2]: accounts
        // stack[3]: 123456789
        // stack[4]: voicesites
        var pathStack = parsedReq.pathname.split('/');
        var accountId = pathStack[3];

        console.log("%s received request %s",new Date(),req.url);

        res.writeHead(200, {
            'Content-Type': 'application/json'
        });

        var json;
        if ( req.url.indexOf('/voicesites') > -1 ) {
            // voicesite summaries
            if ( settings.voicesiteSummaries[accountId] == null ) {
                json = JSON.stringify([],null,4);
            }
            else {
                var summaries = settings.voicesiteSummaries[accountId];
                json = JSON.stringify(summaries,null,4);
            }
        }
        else if ( req.url.indexOf('/accounts') > -1 ) {
            // account
            if ( settings.accounts[accountId] == null ) {
                json = JSON.stringify({},null,4);
            }
            else {
                var account = settings.accounts[accountId];
                json = JSON.stringify(account,null,4);
            }
        }

        // send XML response
        res.write(json);
        res.end();
    });

}).listen(9999);
console.log('Server running at :9999');