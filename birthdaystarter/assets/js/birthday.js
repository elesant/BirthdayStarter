$(document).ready(function() {
  // Events for clicking

  var $container = $('#birthday-gift-ideas');
    $container.imagesLoaded(function(){
      $container.masonry({
        itemSelector : '.birthday-box',
        gutterWidth: 10,
        isResizable: false,
        isFitWidth: true
    });
  });
});
