$(document)
  .ready(function() {
    var
      changeSides = function() {
        $('.ui.shape')
          .eq(0)
            .shape('flip over')
            .end()
          .eq(1)
            .shape('flip over')
            .end()
          .eq(2)
            .shape('flip over')
            .end()
          .eq(3)
            .shape('flip over')
            .end()
          .eq(4)
            .shape('flip over')
            .end()
          .eq(5)
            .shape('flip over')
            .end()
          .eq(6)
            .shape('flip over')
            .end()
			
        ;
      },
      validationRules = {
        firstName: {
          identifier  : 'email',
          rules: [
            {
              type   : 'empty',
              prompt : 'Please enter an e-mail'
            },
            {
              type   : 'email',
              prompt : 'Please enter a valid e-mail'
            }
          ]
        }
      }
    ;

    $('.ui.dropdown')
      .dropdown({
        on: 'hover'
      })
    ;

    $('.ui.form')
      .form(validationRules, {
        on: 'blur'
      })
    ;

    $('.masthead .information')
      .transition('scale in')
    ;

    setInterval(changeSides, 3000);
	
	$('.flexslider').flexslider({
		directionNav: true,
		pauseOnAction: false
	});
	
});