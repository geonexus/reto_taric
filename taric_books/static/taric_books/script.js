window.onload = function () {
    if (document.search_form != null) {
        document.search_form.search_value.focus();
        document.search_form.addEventListener('submit', verifySearch);
    }
    if (document.page_form != null) {
        document.page_form.id_page_value.focus();
        document.page_form.addEventListener('submit', verifyPage);
    }
}

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
function verifyEmptyForm(form) {
    for (var i=0; i<form.length; i++) {
        if(form[i].type =='text') {
            if (form[i].value == null || form[i].value.length == 0 || /^\s*$/.test(form[i].value)) {
                alert('Please, insert some text before...');
                return false;
            }
        }
    }
    return true
}

function verifySearch(evObject) {
    evObject.preventDefault();
    var form = document.search_form;
    if (verifyEmptyForm(form) == true) {
        form.submit();
    }
}

function isNormalInteger(str, max) {
    //Source http://stackoverflow.com/users/157247/t-j-crowder
    var n = ~~Number(str);
    return String(n) === str && n > 0 && n <= max;
}

function verifyPage(evObject) {
    evObject.preventDefault();
    var form = document.page_form;
    if (verifyEmptyForm(form) == true) {
        if (isNaN(form.id_page_value.value) == true || isNormalInteger(form.id_page_value.value, form.max_page.value) == false ){
            alert('Page number inserted is not valid number');
        }
        else {
            form.submit();
        }
    }
}
