$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
});

// Model ADD ADDRESS
var modelId = document.getElementById('modelId');
  
    modelId.addEventListener('show.bs.modal', function (event) {
        // Button that triggered the modal
        let button = event.relatedTarget;
        // Extract info from data-bs-* attributes
        let recipient = button.getAttribute('data-bs-whatever');
  
      // Use above variables to manipulate the DOM
    });


// 

$(document).ready(function(){
    alert('ok')
    $('.plus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        // var elm = this.parentNode.children[2]
        console.log('id', id)
        // $.ajax({
    //     type: 'GET',
    //     url: "/pluscart",
    //     data: {
    //         product_id: id
    //     },
    //     success: function(data){
    //         console.log(data)
    //     }
    // })
    })
});

function inc_dty_pro(id) {
    var qty = document.getElementById('quantity')
    $.ajax({
        type: 'GET',
        url: "/pluscart",
        data: {
            product_id: id
        },
        success: function(data){
            qty.innerText = data.quantity
            console.log(qty.innerText)
        }
    })
}