var page = require('webpage').create();
page.viewportSize = {width: 512, height: 200};
page.open('index.html', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('example.png');
  }
  phantom.exit();
});