// based on https://stackoverflow.com/a/18614545
document.addEventListener('DOMContentLoaded', () => {
    var scrolled = false;
    function updateScroll(){
        if(!scrolled){
            var element = document.getElementByClassName("scroll_box");
            element.scrollTop = element.scrollHeight;
        }
    }

    $(".scroll_box").on('scroll', function(){
        scrolled=true;
    });
});