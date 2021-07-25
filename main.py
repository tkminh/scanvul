import sandbox.xss as xss

urls = ['http://holicoffee.com/', 'https://xss-game.appspot.com/level1/frame']

xss.scan_xss(urls[1])
