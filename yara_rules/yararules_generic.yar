// common generic patterns and regular expressions 

rule http_request_header{
        meta:    	
                author="@matonis"
		description="HTTP header fields"
	strings:
		//methods
		$method0 = "OPTIONS"
		$method1 = "GET"
		$method2 = "HEAD"
		$method3 = "POST"
		$method4 = "PUT"
		$method5 = "DELETE"
		$method6 = "TRACE"
		$method7 = "CONNECT"

		//http version
		$version0 = "HTTP/1.1"
		$version1 = "HTTP/1.0"

		//headers
		$header0 = "Host: "
		$header1 = "User-Agent: "
		$header2 = "Content-Encoding: "
		$header3 = "Last-Modified: "
		$header4 = "Expires: "
		$header5 = "Connection: "
		$header6 = "Accept-Language: "
		$header7 = "Accept-Encoding: "
		$header8 = "Accet-Charset: "
		$header9 = "Cookie: "
		$header10 = "Content-Length: "
		$header11 = "Accept: "
	condition:
		(1 of ($method*)) and (1 of ($version*)) and (2 of ($header*))
}

rule http_response_header{
	meta:		
                author="@matonis"
		description="HTTP Response headers"
	strings:
		//Response Codes
		$response0 = "200 OK"
		$response1 = "201 Created"
		$response2 = "202 Accepted"
		$response3 = "203 Non-Authoritative Information"
		$response4 = "204 No Content"
		$response5 = "205 Reset Content"
		$response6 = "206 Partial Content"
		$response7 = "300 Multiple Choices"
		$response8 = "301 Moved Permanently"
		$response9 = "302 Found"
		$response10 = "303 See Other"
		$response11 = "304 Not Modified"
		$response12 = "305 Use Proxy"
		$response13 = "307 Temporary Redirect"
		$response14 = "400 Bad REQUEST"
		$response15 = "401 Unauthorized"
		$response16 = "403 Forbidden"
		$response17 = "404 Not Found"
		$response18 = "405 Method Not Allowed"
		$response19 = "406 Not Acceptable"
		$response20 = "407 Proxy Authentication Require"
		$response21 = "408 Request Timeout"
		$response22 = "409 Conflict"
		$response23 = "410 Gone"
		$response24 = "411 Length Required"
		$response25 = "412 Precondition Failed"
		$response26 = "413 Request Entity Too Large"
		$response27 = "414 Request-URI Too Long"
		$response28 = "415 Unsupported Media Type"
		$response29 = "416 Requested Range Not Satisfiable"
		$response30 = "417 Expectation Failed"
		$response31 = "500 Internal Server Error"
		$response32 = "501 Not Implemented"
		$response33 = "502 Bad Gateway"
		$response34 = "503 Service Unavailable"
		$response35 = "504 Gateway Timeout"
		$response36 = "505 HTTP Version Not Supported"

		//HTTP Versions
		$version0 = "HTTP/1.1"
		$version1 = "HTTP/1.0"

		//headers
		$field0 = "Set-Cookie:"
		$field1 = "Content-Type:"
		$field2 = "X-Powered-By:"
		$field3 = "Vary:"
		$field4 = "Transfer-Encoding:"
		$field5 = "Etag:"
		$field6 = "Date:"
		$field7 = "Server:"
		$field8 = "Cache-Control:"
		$field9 = "Connection:"
		$field10 = "Last-Modified:"
	condition:
		(1 of ($response*)) and (1 of ($version*)) and (2 of ($field*))
}

rule webartifact_html{
	meta:		
                author="@matonis"
		description="HTML identifiers"
	strings:
		//sepcific tags
		$html0 = "DOCTYPE"
		$html1 = "head>"
		$html2 = "body>"
		$html3 = "title>"
		$html4 = "body>"
		$html5 = "html>"
		$html6 = "</html>"
		$html7 = "<!--"
		$html8 = "-->"
		$html9 = "br>"
		$html10 = "script>"

	condition:
		2 of them
}

rule webartifact_javascript{
	meta:		
                author="@matonis"
		description="Javascript signature"
	strings:
		$java0 = "document.write" nocase
		$java1 = "createElement" nocase
		$java2 = "getElementsByTagName" nocase
		$java3 = "appendChild" nocase
		$java4 = "eval" nocase
		$java5 = "document.cookie" nocase
		$java6 = "p,a,c,k,e,d" nocase
		$java7 = ".substring"
	condition:
		3 of them
}

rule webartifact_gmail{
	meta:		
                author="@matonis"
		description="Gmail artifacts"
	strings:
		$s1 = "[\"ms\","
		$s2 = "[\"ce\"]"
		$s3 = "[\"e\""
	condition:
		2 of them
}


rule url_address{
        meta:
            author="@aung"
            description="regex for url address"
        strings:
                $reg = /(www|http).+\.(com|net|org|gov|edu|mil)/ nocase wide ascii
        condition:
                any of them
}


rule email_address{
        meta:
            author="@aung"
            description="regex for email address"
        strings:
                $reg2 = /\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b/ nocase wide ascii
        condition:
                any of them
}

rule ip_address{
        meta:
            author="@aung"
            description="ip address"
        strings:
                $reg3 = /([0-9]{1,3}\.){3}[0-9]{1,3}\x00/ nocase wide ascii
        condition:
                any of them
}
