$(function() {
  $('<img/>').attr('src', 'http://images2.alphacoders.com/546/546183.jpg').load(function() {
    $('.bg-img').append($(this));
    // simulate loading
    setTimeout(function() { 
     $('.container').addClass('loaded'); 
    }, 1500)
   //$(this).remove(); // prevent memory leaks as @benweet suggested
  });
  $('.form-toggle').on('click', function() {
    $('.container').toggleClass('show-register')
  })
})