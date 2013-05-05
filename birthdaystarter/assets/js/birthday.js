$(document).ready(function() {
  // Events for clicking

  var $container = $('#birthday-container');
    $container.imagesLoaded(function(){
      $container.masonry({
        itemSelector : '.birthday-box',
        gutterWidth: 10,
        isResizable: false,
        isFitWidth: true
      });
    });
  });
});