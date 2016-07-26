!function(root) { "use strict";

    var main, texts, section, sections, element;

    main = document.getElementsByTagName("main")[0];
    sections = document.getElementsByTagName("section");
    sections = Array.prototype.slice.call(sections, 0);
    section = sections[0];

    var tan = "rgb(200, 180, 160)";

    root.mark = function(element, color) {
        element.style.background = color || tan;
        return element;
    };

    root.unmark = function(element) {
        element.style.background = "rgba(0, 0, 0, 0)";
        return element;
    };

    root.puts = function(element) {
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

    root.show = function(surah, verse) {
        setTimeout(unmark, 1000, mark(goto(find(surah, verse))));
    };

    root.goto = function (element) {
        window.scrollBy(0, element.getBoundingClientRect().top - 20);
        return element;
    };

    texts = document.getElementsByTagName("span");

    Array.prototype.slice.call(texts, 0).forEach(
        text => { text.addEventListener("click", function(){ puts(this) }) }
    );

    root.onresize = function() {
        main.style.fontSize = section.offsetWidth / 30 + "px";
    };

    root.onresize();
    main.style.color = "#4C4C4C";

}(window || global);
