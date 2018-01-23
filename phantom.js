var page = require('webpage').create();
page.viewportSize = {width: 512, height: 200};
page.open('poem.html', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('poem.png');
  }
  phantom.exit();
});