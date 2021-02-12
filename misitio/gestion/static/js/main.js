$(document).ready(function(){
    var imgItems = $('.slider li').length;
    var imgPos = 1;

    $('.slider li').hide();
    $('.slider li:first').show();
    $('.pagination li:first').css({'color':'#ffffff'})

    $('.pagination li').click(pagination);
    $('.right span').click(nextSlider);
    $('.left span').click(prevSlider);

    setInterval(function(){
        nextSlider();
    }, 10000)

    function pagination(){
        var paginationPos = $(this).index() + 1;

        $('.slider li').hide();
        $('.slider li:nth-child('+ paginationPos +')').fadeIn();

        $('.pagination li').css({'color':'#9B9B9B'})
        $(this).css({'color':'#ffffff'})

        imgPos = paginationPos;
    }

    function nextSlider(){
        if(imgPos >= imgItems){
            imgPos = 1
        }
        else{
            imgPos++;
        }
        $('.pagination li').css({'color':'#9B9B9B'})
        $('.pagination li:nth-child('+ imgPos +')').css({'color':'#ffffff'})

        $('.slider li').hide();
        $('.slider li:nth-child('+ imgPos +')').fadeIn();
    }

    function prevSlider(){
        if(imgPos <= 1){imgPos = imgItems;}
        else{imgPos--;}
        $('.pagination li').css({'color':'#9B9B9B'})
        $('.pagination li:nth-child('+ imgPos +')').css({'color':'#ffffff'})

        $('.slider li').hide();
        $('.slider li:nth-child('+ imgPos +')').fadeIn();
    }

    $('#perro1').click(function(e){
        var alt = e.target.alt;
        var modal = '<div class="modal" id="galeriazoom"><img src="static/gestion/img/perro1.jpg" alt="'+alt+'" class="modal_img"><div id="descripcion1"><br><br><p>Nombre: Luna.</p><p>Le gusta dormir y comer todo el dia, es jugueton.</p></div><div id="cross" class="far fa-times-circle"></div></div>'
        $('body').append(modal);
        $('#cross').click(function(){
            $('#galeriazoom').remove();
        })
    })

    $('#perro2').click(function(e){
        var alt = e.target.alt;
        var modal = '<div class="modal" id="galeriazoom"><img src="static/gestion/img/perro2.jpg" alt="'+alt+'" class="modal_img"><div id="descripcion2"><br><br><p>Nombre: Squirlax</p><p>Duerme todo el dia y juega con su pelota favorita sin parar.<div id="cross" class="far fa-times-circle"></div></div>'
        $('body').append(modal);
        $('#cross').click(function(){
            $('#galeriazoom').remove();
        })
    })

    $('#perro3').click(function(e){
        var alt = e.target.alt;
        var modal = '<div class="modal" id="galeriazoom"><img src="static/gestion/img/perro3.jpg" alt="'+alt+'" class="modal_img"><div id="descripcion3"><br><br><p>Nombre: Chocolate.</p><p>Le gusta salir a correr y jugar todo el dia con otros perros.<div id="cross" class="far fa-times-circle"></div></div>'
        $('body').append(modal);
        $('#cross').click(function(){
            $('#galeriazoom').remove();
        })
    })

    $('#perro4').click(function(e){
        var alt = e.target.alt;
        var modal = '<div class="modal" id="galeriazoom"><img src="static/gestion/img/perro4.jpg" alt="'+alt+'" class="modal_img"><div id="descripcion4"><br><br><p>Nombre: Michael.</p><p>No le gusta salir fuera de la casa y pelea con otros perros.<div id="cross" class="far fa-times-circle"></div></div>'
        $('body').append(modal);
        $('#cross').click(function(){
            $('#galeriazoom').remove();
        })
    })

    $('#perro5').click(function(e){
        var alt = e.target.alt;
        var modal = '<div class="modal" id="galeriazoom"><img src="static/gestion/img/perro5.png" alt="'+alt+'" class="modal_img"><div id="descripcion5"><br><br><p>Nombre: Balto.</p><p>Es un perro timido acorde a su apariencia y es cuidadoso con las personas.<div id="cross" class="far fa-times-circle"></div></div>'
        $('body').append(modal);
        $('#cross').click(function(){
            $('#galeriazoom').remove();
        })
    })

    $('#perro6').click(function(e){
        var alt = e.target.alt;
        var modal = '<div class="modal" id="galeriazoom"><img src="static/gestion/img/perro6.jpg" alt="'+alt+'" class="modal_img"><div id="descripcion6"><br><br><p>Nombre: Michael.</p><p>Es un perro guardian y no deja que nadie se acerque a su lugar.<div id="cross" class="far fa-times-circle"></div></div>'
        $('body').append(modal);
        $('#cross').click(function(){
            $('#galeriazoom').remove();
        })
    })
    
})


