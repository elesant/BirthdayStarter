$(document).ready(function() {
  // Events for clicking

  $('.birthday-picture').on('hover', function(event) {
    
  });

  var $container = $('#birthday-container');

  var monthMap = {
    0: 'January',
    1: 'February',
    2: 'March',
    3: 'April',
    4: 'May',
    5: 'June',
    6: 'July',
    7: 'August',
    8: 'September',
    9: 'October',
    10: 'November',
    11: 'December'
  };

  $.get('/api/friend/list', function(data) {
    var friendsList = data['friend_list'];

    // Remove friends with no birthday
    friendsList = friendsList.filter(function(element, index, array) {
      return element.birthday !== undefined;
    });

    // Normalize the year to sort correctly
    var currentDate = new Date();
    friendsList.forEach(function(element, index, array) {
      var date = new Date(element['birthday']);

      var normalizedCurrentDate = new Date(currentDate);
      normalizedCurrentDate.setFullYear(0);

      var normalizedDate = new Date(date);
      normalizedDate.setFullYear(0);

      if (normalizedDate > normalizedCurrentDate) {
        date.setYear(currentDate.getFullYear());
      } else {
        date.setYear(currentDate.getFullYear() + 1);
      }

      element['birthday'] = date;
    });

    console.log(friendsList);

    friendsList.sort(function(a, b) {
      return a['birthday'] - b['birthday'];
    });

    console.log(friendsList);

    photoUrls = friendsList.map(function(element, index, array) {
      return 'https://graph.facebook.com/' + element['id'] + '/picture?type=large&width=205&height=205';
    });

    monthDayPairs = friendsList.map(function(element, index, array) {
      var date = new Date(Date.parse(element['birthday']));
      var month = date.getMonth();
      var day = date.getDate();
      return [month, day];
    });

    dateStrings = monthDayPairs.map(function(element, index, array) {
      return monthMap[element[0]] + ' ' + (element[1]);
    });

    // render templates
    var birthdayBoxTemplateCode = $("#birthday-box-template").html();
    var birthdayBoxTemplate = Handlebars.compile(birthdayBoxTemplateCode);
    friendsList.forEach(function(element, index, array) {
      var context = {
        'name': element['name'],
        'birthday': dateStrings[index],
        'id': element['id'],
        'profile_url': 'https://facebook.com/' + element['id'],
        'picture_url': photoUrls[index],
        'birthday_url': '/birthday?facebook_id=' + element['id'] + '&datestr=' + element['birthday'].toString()
      };
      var html = birthdayBoxTemplate(context);
      $container.append(html);
    });

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