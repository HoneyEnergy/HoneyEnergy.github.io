function getOS() {
    var userAgent = window.navigator.userAgent,
        platform = window.navigator.platform,
        macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'],
        windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'],
        iosPlatforms = ['iPhone', 'iPad', 'iPod'],
        os = null;
  
    if (macosPlatforms.indexOf(platform) !== -1) {
      os = 'Mac OS';
    } else if (iosPlatforms.indexOf(platform) !== -1) {
      os = 'iOS';
      alert("Auf IOS geht diese site villeicht nicht wir emphelen diese das die es auf en pc versuchen")
    } else if (windowsPlatforms.indexOf(platform) !== -1) {
      os = 'Windows';
    } else if (/Android/.test(userAgent)) {
      os = 'Android';
      alert("Auf Android geht diese site villeicht nicht wir emphelen diese das die es auf en pc versuchen")
    } else if (!os && /Linux/.test(platform)) {
      os = 'Linux';
    }
  
    return os;
  }
getOS()

if (getOS() == 'Android') {
    alert("its better if you vist this website from a pc")
}
if (getOS() == 'iOS') {
    alert("its better if you vist this website from a pc")
}
