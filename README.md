<p align="center"> :warning: This code works on the most recent version of ReCaptcha v2. Only use on sites you control for educational purposes. :warning:</p>

Created in April 2017, [unCaptcha](https://github.com/ecthros/uncaptcha) achieved 85% accuracy defeating Google's ReCaptcha. After the release of this work, Google released an update to ReCaptcha with the following major changes:
* Better browser automation detection
* Spoken phrases rather than digits

These changes were initially successful in protecting against the original unCaptcha attack. However, as of June 2018, these challenges have been solved. We have been in contact with the ReCaptcha team for over six months and they are fully aware of this attack. The team has allowed us to release the code, despite its current success.

# Introducing unCaptcha2

Thanks to the changes to the audio challenge, passing ReCaptcha is easier than ever before. The code now only needs to make a single request to a free, publicly available speech to text API to achieve around *90% accuracy* over all captchas.

Since the changes to ReCaptcha prevent Selenium, a browser automation engine, unCaptcha2 uses a screen clicker to move to certain pixels on the screen and move around the page like a human. There is certainly work to be done here - the coordinates need to be updated for each new user and is not the most robust.

# The Approach

unCaptcha2's approach is very simple:
1. Navigate to Google's ReCaptcha Demo site
2. Navigate to audio challenge for ReCaptcha
3. Download audio challenge
4. Submit audio challenge to Speech To Text
5. Parse response and type answer
6. Press submit and check if successful

# Demo

![vid](https://user-images.githubusercontent.com/14065974/45004579-df021180-afbb-11e8-8598-177159ed09b4.gif)

# How To Use

Since unCaptcha2 has to go to specific coordinates on the screen, you'll need to update the coordinates based on your setup. These coordinates are located at the top of run.py. On Linux, using the command `xdotool getmouselocation --shell` to find the coordinates of your mouse may be helpful.

You'll also need to set your credentials for whichever speech-to-text API you choose. Since Google's, Microsoft's, and IBM's speech-to-text systems seem to work the best, those are already included in queryAPI.py. You'll have to set the username and password as required; for Google's API, you'll have to set an environment variable (GOOGLE_APPLICATION_CREDENTIALS) with a file containing your Google application credentials.

Finally, install the dependencies, using `pip install -r dependencies.txt`.

# Responsible Disclosure

We contacted the Recaptcha team in June 2018 to alert them that the updates to the Recaptcha system made it less secure, and a formal issue was opened on June 27th, 2018. We demonstrated a fully functional version of this attack soon thereafter. We chose to wait 6 months after the initial disclosure to give the Recaptcha team time to address the underlying architectural issues in the Recaptcha system. The Recaptcha team is aware of this attack vector, and have confirmed they are okay with us releasing this code, despite its current success rate.

This attack vector was deemed out of scope for the bug bounty program.

# Disclaimer

unCaptcha2, like the original version, is meant to be a proof of concept. As Google updates its service, this repository will *not* be updated. As a result, it is not expected to work in the future, and is likely to break at any time.

Unfortunately, due to Google's work in browser automation detection, this version of unCaptcha does not use Selenium. As a result, the code has to navigate to specific parts of the screen. To see unCaptcha working for yourself, you will need to change the coordinates for your screen resolution.

While unCaptcha2 is tuned for Google's Demo site, it can be changed to work for any such site - the logic for defeating ReCaptcha will be the same.

Additionally, we have removed our API keys from all the necessary queries. If you are looking to recreate some of the work or are doing your own research in this area, you will need to acquire API keys from each of the six services used. These keys are delineated in our files by a long string of the character 'X'. It's worth noting that the only protection against creating multiple API keys is ReCaptcha - therefore, unCaptcha could be made self sufficient by solving captchas to sign up for new API keys.

As always, thanks to everyone who puts up with me, including,

[Kkevsterrr](https://github.com/Kkevsterrr)

[Dave Levin](https://cs.umd.edu/~dml)

[dpatel19](https://github.com/dpatel19)

