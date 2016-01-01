!function(){

    var texts = document.getElementsByTagName("span");

    for (var i = 0; i < texts.length; i++) {

        texts[i].onclick = function() {

            var index = this.getAttribute("title").split(":");
            console.log(index);
        };
    }
}();
