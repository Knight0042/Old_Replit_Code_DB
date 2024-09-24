# < !DOCTYPE
# html >
# < html >
# < head >
# < meta
# charset = "utf-8" >
# < meta
# name = "viewport"
# content = "width=device-width" >
# < title > repl.it < / title >
# < link
# href = "style.css"
# rel = "stylesheet"
# type = "text/css" / >
# < / head >
# < body >
# < t > Hello < / t >
# < a
# href = "https://google.com" > Hi < / a >
# < br >
# < p > Output: < / p >
# < pre
# id = 'output' >
# < / pre >
#
# < script
# src = './script.js' > < / script >
# < / body >
# < / html >
#
#
#
#
#
#
# // alert(1)
#
# const log = (text) => {
#     document.getElementById('output').innerText += text + '\n';
# }
#
# for (let i = 4; i>0; i--) {
#     log(i);
#     let test = 'hey'
# }
# log(test)