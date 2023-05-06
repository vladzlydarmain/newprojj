$(document).ready(function(){
    $(".buy").click(function(event){
        event.preventDefault();
        $.ajax({
            url:$("#url").val(),
            type:"post",
            data:{
                csrfmiddlewaretoken: $("#csrf").val(),
                'article':$(this.closest(".product").querySelector('.article')).val(),
                'amount':$(this.closest(".down").querySelector(".value")).val(),
            },
            success: function(response){
                let modalWrapper = document.querySelector(".modal-wrapper");
                let closeButton = document.querySelector(".stay");
                
                modalWrapper.setAttribute("hidden","1");

                function modalAppear(){
                    modalWrapper.removeAttribute("hidden");
                }

                function modalDisappear(){
                    modalWrapper.setAttribute("hidden","1");
                }
                modalAppear();
                closeButton.addEventListener("click",modalDisappear);
            }
        });
    });
});

