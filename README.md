# verisign<br>
> Purpose is to export list of domains from Verisign<br>
<br>
Purpose of <b>get-verisign-zones.py</b> script is to export domains from Verisign<br>
<br>

You can see the documentation here, [Verisign REST API Swagger](https://mdns.verisign.com/rest/rest-doc/index.html)

This script exports all domains.  Before using it, you'll need to edit the <b><i>apikey</b></i> and <b><i>account_id</b></i> variables.  See detailed information below in the <b>Usage Example</b> section.<br>
<br>
I suggest that you use a read-only API user as a best practice.<br>
<br>

## Installation & Dependencies

Python 3.6 installed<br>
<br>
The following modules installed:<br>
1.  json<br>
2.  requests<br>
<br>

## Usage example

To run this from command line:<br>
<br>
```sh
./get-verisign-zones.py
```
<br>
These are configurable items in the script:
<br>
<b>1.  Proxy Information:</b><br>
<br>
<br>
The script assumes you don't need to go through a proxy.  If you have a proxy setup at work, then edit the variables section of the script and put in the correct proxy for <b><i>http_proxy</i></b> & <b><i>https_proxy</i></b>.<br>
<br>
You will also need to change three lines of the script from:<br>
```sh
verify=False
```
to<br>
```sh
proxies=proxyDict, verify=False
```

## Release History

* 0.0.1
    * Initial version

## Meta

Brian Bullard – [@BrianBullard94](https://twitter.com/BrianBullard94) – dns.dhcp.ipam@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/ddiguy/verisign](https://github.com/ddiguy)

## Contributing

1. Fork it (<https://github.com/ddiguy/verisign/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
