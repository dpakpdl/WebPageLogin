import requests

# Fill in your details here to be posted to the login form.
payload = {
    'dnn$ctr811$Login$Login_DNN$txtUsername': 'test@t.com',  # change email here
    'dnn$ctr811$Login$Login_DNN$txtPassword': 'test@t',  # change password here
    'ScriptManager': 'dnn$ctr811$dnn$ctr811$Login_UPPanel|dnn$ctr811$Login$Login_DNN$cmdLogin',
    'StylesheetManager_TSSM': ';Telerik.Web.UI, Version=2015.3.1006.45, Culture=neutral, PublicKeyToken=121fae78165ba3d4:en-GB:4939a17e-195b-45a5-a29e-e53207862f06:45085116:27c5704c',
    'ScriptManager_TSM': ';;System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35:en:b7585254-495e-4311-9545-1f910247aca5:ea597d4b:b25378d2;Telerik.Web.UI, Version=2015.3.1006.45, Culture=neutral, PublicKeyToken=121fae78165ba3d4:en:4939a17e-195b-45a5-a29e-e53207862f06:16e4e7cd:f7645509:ed16cbdc:88144a7a',
    'RadAJAXControlID': 'dnn_ctr811_Login_UP',
    '__EVENTTARGET': 'dnn$ctr811$Login$Login_DNN$cmdLogin',
    '__VIEWSTATE': 'gOrlRvc3y1s7OZyRTLp9uXPapdGuEFzumHORNCncUXHpHFmkkJkNBYHY8qn/ujr4pUsEpUfoNpSo7TKJXsyjjvIgjpEiRGs2IycQgDdYfOVm2dEM8jp76tAJpTWVGlJUrWusLh3ViWLoO71XmVX4BzpZw6LpnIj69hI2kVovPhrcP0D0bDf/517gT/j5VAISsFDo8jtxGXqE+E4EpdU4azzQuu0xyr0jjdmoMapuy90mFAHNWtIuo19tQuCsC6U8DfslyLmO+YwMeNnat/u80OtYHFqHDuKwDZzDGkhboM25Yt/UW1jcsCU1g0hjdJ0DJO6wY+/NHsX/PecqtAr69rr6WOLm7pNEqHNe483TCgnIYKKKzwAyQLxNNLpEUJsMewWjvmwzdhpkie0cNDkS7/9E2PR+KJjtH1/sqzhG8Qy82x75HFQw3IFawYLFLaDq2D3Qopo1PqtK04kv1377sb9if6do8cZvhd9KQmayM9obIU6PlynyV0hdIKc5z+kmqDFdCuY5ddSwStENCIDcN0Iw9dGaVomVGrSnlXuPhoB71onOv23NJGOQFJIOUJAySf1TOQ==',
    '__VIEWSTATEGENERATOR': 'CA0B0334',
    '__VIEWSTATEENCRYPTED':'',
    '__EVENTVALIDATION': '6vbX+MBmxzy1A3xmJCYsJtCnt7gracFY1z/DuhlbtV6G6HGLVd6jrQT2rucELJxisEshVOaLBuZTcRWL2c5HrtddvAbQYA9HeYVvzIu99OJM5E3epfCmqWftfExijNfwqUqvYN/ythsPl/IlrpbElQTubh37wbp8rw5CusbRl2QBndobn0jnLFSSWuVLauwNOa/j0A==',
    'ScrollTop': '104',
    '__dnnVariable': '{`__scdoff`:`1`,`sf_siteRoot`:`/`,`sf_tabId`:`167`}',
    '__RequestVerificationToken': 'mgeX9ZdFqfYldrV9ve6UarTCOLy57sDFXeI-Cl0kWhlFfc2iSmeyK159ZpGM2I4fEr8_pw2',
    '__ASYNCPOST': 'true'
}

LOGIN_URL = 'https://www.trickybet.net/TrickyBet-Login'
# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(LOGIN_URL, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    URL = 'https://www.trickybet.net/Each-Way-Catcher'
    data = s.get(URL)
    print (data.text)
