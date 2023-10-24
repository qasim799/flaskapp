# Flask Application

Author: Kyungrae Kim

----

## Turn On a Wake-on-LAN enabled Computer

This is a simple RESTful API built using Flask. The application turns on a Wake-on-LAN enabled computer with the following:

* Accepts a POST request to the route "/wol", which accepts one argument "mac_address"
* Returns a JSON object with the key "message" and broadcasts a magic packet to the subnet

This README contains extra steps to use Google Assistant to communicate with the endpoint running on a local server.

This is a continued effort to complete a personal project started from the following repositories:

* <https://github.com/jeremymaya/google-home-wol>
* <https://github.com/jeremymaya/google-home-netlify>

----

### Example

If you POST

```json
{"mac_address": "XX:XX:XX:XX:XX:XX"}
```

It will return the following and turn on the computer:

```json
{"message": "Starting the computer"}
```

### Enable Wake-on-LAN (WoL)

Before trying out the endpoint, enable Wake-on-LAN (WoL) feature on the target computer by following a post similar to [Lifewire - How to Set Up and Use Wake-on-LAN](https://www.lifewire.com/wake-on-lan-4149800).

### Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/jeremymaya/raspberry-pi-os.git
```

Install the dependencies:

```bash
pip3 install -r requirements.txt
```

#### Development Mode

Start the application in development mode with the following command:

```bash
FLASK_ENV=development flask run
```

Test the functionality of the endpoint running at ```localhost:5000``` with the following command:

```bash
curl -X POST http://127.0.0.1:5000/api/v1/wol --data '{"mac_address": "XX:XX:XX:XX:XX:XX"}' -H 'Content-Type: application/json'
```

The expected output upn suceess of the above command is:

```json
{
    "message": "Turning on the computer"
}
```

Alternatively, test the functionality of the endpoint running at <http://127.0.0.1:5000/api/docs/> by clicking the ```Try it out``` button.

![Open API](https://github.com/jeremymaya/raspberry-pi-os/blob/master/assets/open_api.png?raw=true)

#### Production

Run the application in production using uWSGI with the following command:

```bash
uwsgi --ini app.ini --need-app
```

----

### Turn On the Computer with Google Assistant

Now that the computer can be turned on with a POST request, let's integrate Google Assistant and Webhooks so it can be turned on remotely.

#### Expose the Local Server with ngrok

For Google Assistant to communicate with the endpoint running on the local server, the server nseeds to be exposed with a public URL.

There are different ways to achieve this. This example uses [ngrok](https://ngrok.com/) to expose the local server.

After following the [Setup & Installation](https://dashboard.ngrok.com/get-started/setup) steps, enter the following command for the application running in production:

```bash
./ngrok http 8600
```

The above command should output the following which indicates a public URL of the local server.

```bash
Session Status                online
Account                       Kyungrae Kim (Plan: Free)
Version                       2.3.35
Region                        United States (us)
Web Interface                 http://127.0.0.1:XXXX
Forwarding                    http://XXXX.ngrok.io -> http://localhost:8600
Forwarding                    https://XXXX.ngrok.io -> http://localhost:8600

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00  
```

#### Send a POST request with Google Assistant with IFTTT

HTTP request can be sent using Google Assistant by pairing with Webhook on [If This Than This (IFTTT)](https://ifttt.com/).

Create a new applet following [Integrating Google Home And IFTTT Webhooks](https://www.francoisdelport.com/2018/04/23/integrating-google-home-and-ifttt-webhooks/).

For this example,

1. Select "Say a simple phrase" as trigger
2. Select "Webhooks" as action
3. Select "POST" as method for the Webhooks
4. Use `{"mac_address": "XX:XX:XX:XX:XX:XX"}` as Body for the Webhooks
5. Use the ngrok URL + /api/v1/wol as URL for the Webhooks
6. Select "application/json" as Content Type for the Webhooks

![IFTTT Applet](https://github.com/jeremymaya/raspberry-pi-os/blob/master/assets/ifttt.png?raw=true)

----

## Credits

* [Lifewire - How to Set Up and Use Wake-on-LAN](https://www.lifewire.com/wake-on-lan-4149800)
* [Data Science Blog - REST API Development with Flask](https://www.datascienceblog.net/post/programming/flask-api-development/)
* [Integrating Google Home And IFTTT Webhooks](https://www.francoisdelport.com/2018/04/23/integrating-google-home-and-ifttt-webhooks/)
* [Reddit - [GUIDE] Switch your PC from anywhere in the world with an OK Google command (using a RaspberryPi and wake on LAN)](https://www.reddit.com/r/googlehome/comments/didz91/guide_switch_your_pc_from_anywhere_in_the_world/)
* [How to Host a Raspberry Pi Web Server on the Internet with ngrok](https://thisdavej.com/how-to-host-a-raspberry-pi-web-server-on-the-internet-with-ngrok/)
* [intrinsic - Why should I use a Reverse Proxy if Node.js is Production-Ready?](https://medium.com/intrinsic/why-should-i-use-a-reverse-proxy-if-node-js-is-production-ready-5a079408b2ca)
* [How to Build a Raspberry Pi Server for Development](https://www.toptal.com/raspberry-pi/how-to-turn-your-raspberry-pi-into-a-development-server)
* [How do you set up a local testing server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server)
* [Python's http.server library “basic security checks”](https://security.stackexchange.com/questions/226095/pythons-http-server-library-basic-security-checks)
* [Wake On LAN Python Script](https://dev.to/kevinmel2000/wake-on-lan-python-scrip-pf1)
* [WAKE ON LAN (PYTHON RECIPE)](http://code.activestate.com/recipes/358449-wake-on-lan/)
* [https://andreashessblog.wordpress.com/2016/12/10/python-script-wake-on-lan/](https://andreashessblog.wordpress.com/2016/12/10/python-script-wake-on-lan/)
* [Github - Python Wake on LAN](https://gist.github.com/rschuetzler/8854764)

----

## Change Log

* */wol v1 Completed* - 17 September 2020
