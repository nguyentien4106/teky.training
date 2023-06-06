$(document).ready(function() {
    console.log('a')
    $("#searchBar").on("click", function() {
        $(".menu-item").toggle("slow", "swing", function(){
            $(".search").toggleClass("hide", $( this ).next().is(":visible"))
        })
    })
});