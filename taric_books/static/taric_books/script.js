function collapse_post(id) {
    subject = document.getElementById(id);
    divs = subject.getElementsByTagName("div");
    var i;
    var subject_name;
    var subject_list;
    for (i=0; i<divs.length; i++) {
        if (divs[i].className == "subject_name") {
            subject_name = divs[i];
        } else if (divs[i].className == "subject_list") {
            subject_list = divs[i];
        }
    }
    if (subject.className.match(".*collapsed.*")) {
        subject.className = "subject";
    }else {
        subject.className = "collapsed";
    }
}