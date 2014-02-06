$('.art li').mouseover(function(e) {
	var li = $(e.target).parents('li');
	li.find('.caption').addClass('in');
	li.find('.description').fadeIn(100)
}).mouseleave(function(e) {
	var li = $(e.target).parents('li');
	li.find('.caption').removeClass('in');
	li.find('.description').fadeOut(100)
});