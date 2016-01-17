!function(root) { "use strict";

    var hash, texts;

    root.mark = function(element, color) {
        element.style.background = color;
        return element;
    };

    root.show = function(element) {
        console.log(element.title + ':\n' + element.innerText);
        return element;
    };

    root.find = function(surah, verse) {

        var element = document.getElementById(
            verse == undefined ? "s" + surah : "s" + surah + "v" + verse
        );

        if (!element) throw RangeError(
            "Can not go to Surah " + surah + (verse ? ", Verse " + verse : "")
        );

        return element;
    };

    root.goto = function (surah, verse) {

        var element, offset;

        element = find(surah, verse);
        offset = (verse == undefined ? 20 : 10)

        window.scrollBy(0, element.getBoundingClientRect().top - offset);
        mark(element, "rgba(0, 255, 67, 0.35)");
        setTimeout(mark, 1000, element, "");

        return element;
    };

    if (hash = location.hash.slice(1)) goto.apply(this, hash.split(":"));

    texts = document.getElementsByTagName("span");

    Array.prototype.slice.call(texts, 0).forEach(
        text => { text.addEventListener("click", function(){ show(this) }) }
    );

}(window || global);
